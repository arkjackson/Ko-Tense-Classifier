# Korean Article Tense Classifier

This project is a tool that analyzes the tenses of article sentences written in Korean and classifies them into future, past, and present tense. It analyzes the verbs, adjectives, and time expressions of a sentence by using the NLP libraries 'SentenceTransformer', 'Santa', and 'GLiNER'.

## 주요 기능

- **Preprocessing**: Remove unnecessary elements such as e-mails, hashtags, links, copyright statements, etc
- **Sentence analysis**: Extract verbs and adjectives from sentences and use them as the basis for determining the tense
- **Test classification**: Classify future, past and present tense based on keyword and time entity

## How to Install

1. **Repository clone**
   ```bash
   git clone https://github.com/[your-username]/korean-tense-classifier.git
   cd korean-tense-classifier
   ```
   
2. **Dependency installation**
   ```bash
   pip install -r requirements.txt
   ```

   `requirements.txt` 예시:
   ```
   sentence-transformers==2.2.2
   stanza==1.5.0
   gliner==0.0.6
   torch==2.0.0  # GPU 지원 시 적절한 버전 설치 필요
   ```

3. **Download Model**
  - 'Sentence Transformer' and 'GLiNER' are automatically downloaded when the code is executed.
  - The 'Sanza' Korean model is downloaded via 'stanza.download('ko')' within the code.

## Instructions

### 1. Code execution
Below is a basic usage example.

```python
from tense_classifier import preprocess_text, classify_tense

# Sample Data
article_date = "2025-03-16"
sample_text = [
    "올해 3분기 매출이 증가할 전망이다.",
    "지난해 매출은 감소했다.",
    "이날 주가는 상승 중이다."
]

# Preprocessing
processed_text = preprocess_text(sample_text)

# Classify Tense
future, past, current = classify_tense(processed_text, article_date)

print("미래 시제:", future)
print("과거 시제:", past)
print("현재 시제:", current)
```

### Sample Output
```
미래 시제: ['올해 3분기 매출이 증가할 전망이다.']
과거 시제: ['지난해 매출은 감소했다.']
현재 시제: ['이날 주가는 상승 중이다.']
```

## Restrictions

- When using GPU, 'torch' and CUDA settings are required.
- Time entity recognition relies on the accuracy of the 'GLNER' model.
- There is a possibility of misclassification in complex sentence structures or non-standard Korean expressions.
  
## License

[MIT License](LICENSE)

## Contact

Email: mihy1968@gmail.com
