import pandas as pd
import torch
from src.components.preprocess import Preprocessor
from src.utils import preprocess_query, rank_docs, fix_incomplete_sentence

class QueryProcessor:
    def __init__(self):
        self.data_preprocessor = Preprocessor()
        self.data_preprocessor.load_data()
        self.document_list,self.inverted_index = self.data_preprocessor.preprocess_data()
    
    def process_query(self,query):
        self.processed_query = preprocess_query(query)
        self.ranked_docs = rank_docs(self.processed_query, self.inverted_index, self.document_list)
        self.abstracts = []
        if len(self.ranked_docs) == 0:
            return "There are no similar documents found."
        else:
            for i,j in zip(self.ranked_docs,range(5)):
                if i[1] >= 0.5:
                    self.abstracts.append(self.data_preprocessor.data.abstract[i[0]])

            self.abstract = " ".join(self.abstracts)
            with open('model.pkl', 'rb') as f:
                model = torch.load(f, weights_only=False)
                response = model.predict([self.abstract])
                print("Response Generated")
                return fix_incomplete_sentence(response[0])
            
            
    
    
'''
Filename: e:\projects\CORD19-SummaryGenerator\src\components\queryProcessing.py
Path: e:\projects\CORD19-SummaryGenerator\src\components
Created Date: Friday, March 7th 2025, 5:44:36 pm
Author: Devang Vamja

Copyright (c) 2025 Your Company
'''
