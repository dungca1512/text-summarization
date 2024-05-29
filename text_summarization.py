from transformers import pipeline

summarizer = pipeline("summarization", model="Falconsai/text_summarization")

ARTICLE = input("Enter article: ")
print(summarizer(ARTICLE, max_length=1000, min_length=30, do_sample=False))

