import re
import stanza
from gliner import GLiNER
from datetime import datetime
from sentence_transformers import SentenceTransformer

# 모델 초기화
model_ST = SentenceTransformer('paraphrase-MiniLM-L6-v2')
stanza.download('ko')
nlp = stanza.Pipeline('ko', use_gpu=True)
model_gliner = GLiNER.from_pretrained("urchade/gliner_medium-v2.1")
labels = ["Time", "Date"]

# 전처리 통합 함수
def preprocess_text(context):
    patterns = [
        r'[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',  # 이메일
        r'#\S+',  # 해시태그
        r'https?://\S+|www\.\S+',  # 링크
        r'\<저작권자(\(c\)|©|(\(C\))).+?\>|(Copyrights)|(\(c\))|(\(C\))|©|(C)|',
        r'\[사진=[^\]]*\]|사진.*?\.|\[.*?\]|\d{4}\.\d{1,2}\.\d{1,2}\.|\(.*?\)|\{.*?\}'
    ]
    return [re.sub('|'.join(patterns), '', text).strip() for text in context if re.sub('|'.join(patterns), '', text).strip()]

# 문장 분석 함수
def get_predicates(sentence):
    doc = nlp(sentence)
    return [word.text for sent in doc.sentences for word in sent.words if word.upos in ("VERB", "ADJ")]

def check_l_suffix(word):
    doc = nlp(word)
    for sent in doc.sentences:
        for w in sent.words:
            lemma, xpos = w.lemma.split('+'), w.xpos.split('+')
            return lemma[-1] == 'ㄹ' and xpos[-1] == 'ef' if lemma and xpos else False
    return False

# 시제 분류 함수
def classify_tense(sentences, article_date):
    future_sentences, past_sentences, current_sentences = [], [], []
    future_keywords = ["전망", "예정", "계획", "예측", "예상", "가능"]
    past_keywords = ["지난분기", "지난 분기", "작년", "지난 달", "지난달", "전분기", "전 분기", "지난해", "지난 해"]
    current_keywords = ["이날", "이 날"]
    current_predicates = ["이다"]
    compare_keywords = ["비교", "비해"]
    time_pattern = r"(지난해)|(내년|올해|지난해|다음해|이달) (\d분기|\d월|\d주|\d일|상반기|하반기)|(이날|이 날)"
    past_year = f"{datetime.strptime(article_date, '%Y-%m-%d').year - 1}년"

    for sentence in sentences:
        predicates = get_predicates(sentence)

        # 미래 시제
        if any(check_l_suffix(p) or "할" in p or any(fk in p for fk in future_keywords) for p in predicates):
            future_sentences.append(sentence)
            continue

        # 시간 엔터티 추출
        entities = [e['text'] for e in model_gliner.predict_entities(sentence, labels, threshold=0.5)]
        time_entities = entities + [match.group() for match in re.finditer(time_pattern, sentence)]

        # 현재 시제
        if any(ck in time_entities for ck in current_keywords):
            current_sentences.append(sentence)
            continue

        # 과거 시제
        if past_year in sentence or any(pk in time_entities for pk in past_keywords):
            if not (any(ck in sentence for ck in compare_keywords) and any(cp in predicates for cp in current_predicates)):
                past_sentences.append(sentence)
                continue

        current_sentences.append(sentence)

    return future_sentences, past_sentences, current_sentences