# NLP Task with SpaCy and Hugging Face Transformers

This project demonstrates basic natural language processing (NLP) tasks using SpaCy for text summarization and Hugging Face Transformers for question answering.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Functionality](#functionality)
  
## Introduction

Natural Language Processing (NLP) is a subfield of artificial intelligence (AI) focused on enabling computers to understand and interact with human language. This project utilizes two popular libraries:

- **SpaCy:** A Python library for advanced NLP tasks such as tokenization, part-of-speech tagging, named entity recognition, and text summarization.
- **Hugging Face Transformers:** A library providing pre-trained models and pipelines for various NLP tasks, including question answering.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/nlp-with-spacy-transformers.git
   cd nlp-with-spacy-transformers
pip install spacy transformers
python -m spacy download en_core_web_sm
## Usage
Summarize a Document:

Use SpaCy to summarize a document into coherent sentences.
Answer Questions Based on a Document:

Utilize Hugging Face Transformers to extract answers from a document given a specific question.

##Functionality
Functions Provided:
summarize_document(text): Uses SpaCy to summarize a given document.
answer_question(document, question): Uses Hugging Face Transformers for question answering based on a provided document
