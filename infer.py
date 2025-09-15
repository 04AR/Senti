from transformers import pipeline

classifier = pipeline(task="text-classification", model="AR04/Senti", top_k=None)

sentences = ["hi! u r looking beautiful today dear"]

model_outputs = classifier(sentences)
print(model_outputs[0])
