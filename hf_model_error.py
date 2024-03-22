from transformers import AutoTokenizer, TFAutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased"
model = TFAutoModelForSequenceClassification.from_pretrained("bert-base-uncased)
