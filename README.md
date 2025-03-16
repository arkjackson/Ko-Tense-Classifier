# Korean Article Tense Classifier

This project is a tool that analyzes the tenses of article sentences written in Korean and classifies them into future, past, and present tense. It analyzes the verbs, adjectives, and time expressions of a sentence by using the NLP libraries 'SentenceTransformer', 'Santa', and 'GLiNER'.

## Features

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
    "LG엔솔이 곧 완공될 랜싱 공장에서 설비 설치를 시작할 수 있을 것으로 예상했다",
    "애플의 지난해 중국 시장 점유율은 15%로, 연간 기준으로 17% 감소했다.",
    "업계에 따르면 국내 배터리 3사(LG에너지솔루션, 삼성SDI, SK온) 직원들의 현대차 이직이 계속 되고 있다."
]

# Preprocessing
processed_text = preprocess_text(sample_text)

# Classify Tense
future, past, current = classify_tense(processed_text, article_date)

# Output
print("미래 시제:", future)
print("과거 시제:", past)
print("현재 시제:", current)
```

### Sample Output
```
미래 시제: ['LG엔솔이 곧 완공될 랜싱 공장에서 설비 설치를 시작할 수 있을 것으로 예상했다']
과거 시제: ['애플의 지난해 중국 시장 점유율은 15%로, 연간 기준으로 17% 감소했다.']
현재 시제: ['업계에 따르면 국내 배터리 3사(LG에너지솔루션, 삼성SDI, SK온) 직원들의 현대차 이직이 계속 되고 있다.']
```

## Restrictions

- When using GPU, 'torch' and CUDA settings are required.
- Time entity recognition relies on the accuracy of the 'GLiNER' model.
- There is a possibility of misclassification in complex sentence structures or non-standard Korean expressions.
  
## License

[MIT License](LICENSE)

## Contact

Email: mihy1968@gmail.com
