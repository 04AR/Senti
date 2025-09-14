# Senti 0_0


<div>
  <a href=https://github.com/04AR/Senti target="_blank"><img src=https://img.shields.io/badge/Code-black.svg?logo=github height=22px></a>
  <a href=https://huggingface.co/AR04/Senti target="_blank"><img src=https://img.shields.io/badge/%F0%9F%A4%97%20Models-d96902.svg height=22px></a>
</div>

**Senti** is a lightweight emotion classification model fine-tuned on the [Google GoEmotions](https://github.com/google-research/google-research/tree/master/goemotions) dataset.  
It uses **MobileBERT**, making it small and efficient enough to run on **low-powered devices** such as smartphones, Raspberry Pi, or edge AI systems.

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

### 1. Install dependencies
```bash
pip install torch transformers

