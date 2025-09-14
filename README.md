# Senti 0_0

**Senti** is a lightweight emotion classification model fine-tuned on the [Google GoEmotions](https://github.com/google-research/google-research/tree/master/goemotions) dataset.  
It uses **MobileBERT**, making it small and efficient enough to run on **low-powered devices** such as smartphones, Raspberry Pi, or edge AI systems.

---

## ✨ Features

- 📦 **Compact** — based on MobileBERT (optimized for efficiency and speed).
- 💬 **Emotion-rich** — trained on **27 emotion labels + neutral** from the GoEmotions dataset.
- ⚡ **Low-resource friendly** — designed to work on edge devices and mobile apps.
- 🔌 **Plug-and-play** — easy integration with Hugging Face `transformers`.

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

