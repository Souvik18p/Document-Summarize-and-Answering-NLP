import spacy
from transformers import pipeline

nlp = spacy.load("en_core_web_sm")

# Define function to summarize a document
def summarize_document(text):
    doc = nlp(text)
    summary = ""
    for sent in doc.sents:
        summary += sent.text + " "
    return summary

# Define function to answer a question based on a document
def answer_question(document, question):
    summarizer = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad", tokenizer="distilbert-base-uncased-distilled-squad")
    answer = summarizer(question=question, context=document)
    return answer['answer']

# Example document and question
document = """
Natural Language Processing (NLP) is a subfield of artificial intelligence (AI) that focuses on the interaction between computers and humans through natural language. It aims to enable computers to understand, interpret, and generate human language in a way that is both meaningful and useful.

NLP techniques are used in a variety of applications, including machine translation, sentiment analysis, text summarization, and question answering. For example, NLP can be used to automatically summarize long documents or answer questions based on a given text.

One popular library for NLP tasks in Python is SpaCy, which provides easy-to-use tools for processing and analyzing text data. Another widely used resource is the Hugging Face Transformers library, which offers pre-trained models for various NLP tasks, such as question answering and text generation.

Overall, NLP plays a crucial role in enabling computers to understand and interact with human language, opening up new possibilities for applications ranging from virtual assistants to automated content analysis.
"""

question = "What are some examples of applications of NLP?"

# Summarize the document
summary = summarize_document(document)
print("Document Summary:")
print(summary)

# Answer the question based on the document
answer = answer_question(document, question)
print("\nAnswer to the question:", answer)
