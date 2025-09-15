# Senti 0_0


<div>
  <a href=https://github.com/04AR/Senti target="_blank"><img src=https://img.shields.io/badge/Code-black.svg?logo=github height=22px></a>
  <a href=https://huggingface.co/AR04/Senti target="_blank"><img src=https://img.shields.io/badge/%F0%9F%A4%97%20Models-d96902.svg height=22px></a>
  <a href=https://github.com/04AR/Senti/blob/main/Senti.ipynb target="_blank"><img src="https://img.shields.io/badge/Training%20Code-%20jupyter-orange"></a>
  
</div>

**Senti** is a lightweight emotion classification model fine-tuned on the [Google GoEmotions](https://github.com/google-research/google-research/tree/master/goemotions) dataset.  
It uses **MobileBERT**, making it small and efficient enough to run on **low-powered devices** such as smartphones, Raspberry Pi, or edge AI systems.

This repo contains **Training Jupyter notebook** and **infer.py** for simple inference.

## 🏷️ Emotion Labels

| ID  | Emotion         | ID  | Emotion         | ID  | Emotion         | ID  | Emotion     |
|-----|----------------|-----|----------------|-----|----------------|-----|----------------|
| 0   | admiration     | 1   | amusement      | 2   | anger          | 3   | annoyance      |
| 4   | approval       | 5   | caring         | 6   | confusion      | 7   | curiosity      |
| 8   | desire         | 9   | disappointment | 10  | disapproval    | 11  | disgust        |
| 12  | embarrassment  | 13  | excitement     | 14  | fear           | 15  | gratitude      |
| 16  | grief          | 17  | joy            | 18  | love           | 19  | nervousness    |
| 20  | optimism       | 21  | pride          | 22  | realization    | 23  | relief         |
| 24  | remorse        | 25  | sadness        | 26  | surprise       | 27  | neutral        |

---

## ✨ Features

- 📦 **Compact** — based on MobileBERT (optimized for efficiency and speed).
- 💬 **Emotion-rich** — trained on **27 emotion labels + neutral** from the GoEmotions dataset.
- ⚡ **Low-resource friendly** — designed to work on edge devices and mobile apps.
- 🔌 **Plug-and-play** — easy integration with Hugging Face `transformers`.

---

## 🧪 Evaluation

Here are the evaluation results of **Senti** on the GoEmotions validation set:

| Metric       | Value |
|--------------|-------|
| Loss         | 0.085 |
| F1-score     | 0.586 |
| ROC AUC      | 0.752 |
| Accuracy     | 0.460 |

---

## 📊 Dataset

- **Source:** [Google GoEmotions](https://github.com/google-research/google-research/tree/master/goemotions)  
- **Classes:** 27 emotions + neutral  
- **Task type:** Single-label classification (best label per input text)

---

## 🚀 Quickstart

#### Inference

There are multiple ways to use this model in Huggingface Transformers. Possibly the simplest is using a pipeline:

### 1. Install dependencies

```bash
pip install torch transformers
```


```python
from transformers import pipeline
classifier = pipeline(task="text-classification", model="AR04/Senti", top_k=None)
sentences = ["hi! you  are looking beautiful today dear"]
model_outputs = classifier(sentences)
print(model_outputs[0])
# produces a list of dicts for each of the labels
```
Output:
```bash
[{'label': 'admiration', 'score': 0.9517803192138672}, {'label': 'love', 'score': 0.18317067623138428}, {'label': 'joy', 'score': 0.03131399303674698}, {'label': 'neutral', 'score': 0.01567094214260578}, {'label': 'surprise', 'score': 0.009232419542968273}, {'label': 'approval', 'score': 0.007308646105229855}, {'label': 'excitement', 'score': 0.006345656234771013}, {'label': 'pride', 'score': 0.004945244640111923}, {'label': 'caring', 'score': 0.0038624939043074846}, {'label': 'realization', 'score': 0.0023580112028867006}, {'label': 'desire', 'score': 0.0017759536858648062}, {'label': 'optimism', 'score': 0.0013220690889284015}, {'label': 'sadness', 'score': 0.001188945840112865}, {'label': 'disappointment', 'score': 0.0009136834414675832}, {'label': 'gratitude', 'score': 0.0008250900427810848}, {'label': 'relief', 'score': 0.0005154621903784573}, {'label': 'amusement', 'score': 0.0004376845608931035}, {'label': 'fear', 'score': 0.00038696840056218207}, {'label': 'embarrassment', 'score': 0.0003084330528508872}, {'label': 'grief', 'score': 0.00019462488126009703}, {'label': 'confusion', 'score': 0.00018893269589170814}, {'label': 'annoyance', 'score': 0.0001587819424457848}, {'label': 'curiosity', 'score': 0.0001355114800389856}, {'label': 'remorse', 'score': 0.00011744408402591944}, {'label': 'anger', 'score': 0.00010586195276118815}, {'label': 'disgust', 'score': 9.386352030560374e-05}, {'label': 'nervousness', 'score': 7.547048153355718e-05}, {'label': 'disapproval', 'score': 3.7117086321813986e-05}]
```


