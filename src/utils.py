import re
import spacy
import en_core_web_sm
from collections import defaultdict
from math import log10
nlp = spacy.load("en_core_web_sm")

# defining a function to preprocess the text 
def processed_df(text):
    text = re.sub(r'[^a-zA-Z0-9]+', ' ', text)
    text = text.lower()
    tokens=[]
    doc = nlp(text)
    for token in doc:
        if token.is_stop or token.is_punct or token.is_space or token.like_num or token.like_url or token.like_email:
            continue
        tokens.append(token.lemma_)
    return ' '.join(tokens)

# defined a function to preprocess both documents and query
def preprocess_query(text):
    text = re.sub(r'[^a-zA-Z0-9]+', ' ', text)
    doc = nlp(text)
    tokens = []
    for token in doc:
        if not token.is_stop and not token.is_punct and not token.is_space and not token.like_num and not token.like_url:
            tokens.append(token.lemma_.lower())
    return tokens

# defining a function that returns dictionary word and relevant postings list.
def inverted_index(docs):
    inverted_index = defaultdict(list)
    for doc_id, doc in enumerate(docs):
        for token in preprocess_query(doc):
            inverted_index[token].append(doc_id)
    return inverted_index

# defined a function for document scoring using TF-IDF
def rank_docs(query, inverted_index, docs):
    scores = defaultdict(float)
    query_terms = set(query)
    N = len(docs)
    max_score = 0

    for term in query_terms:
        df = len(inverted_index.get(term, []))  # Handle terms not in the index
        idf = log10((N / (df + 1)))  # Calculate IDF once per term
        for doc_id in inverted_index.get(term, []):
            tf = docs[doc_id].count(term)
            scores[doc_id] += tf * idf
            if scores[doc_id] > max_score:
                max_score = scores[doc_id]

    # Normalize scores
    if max_score > 0:
        for doc_id in scores:
            scores[doc_id] /= max_score

    # Rank documents by score
    ranked_docs = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return ranked_docs

def fix_incomplete_sentence(text):

    if not re.search(r'[.!?]$', text.strip()):
        # Split text into sentences
        sentences = re.split(r'(?<=[.!?])\s+', text)
        if len(sentences) > 1:
            # Remove the last incomplete sentence
            text = ' '.join(sentences[:-1])
    return text

'''
Filename: e:\projects\CORD19-SummaryGenerator\src\utils.py
Path: e:\projects\CORD19-SummaryGenerator\src
Created Date: Friday, March 7th 2025, 5:25:48 pm
Author: Devang Vamja

Copyright (c) 2025 Your Company
'''
