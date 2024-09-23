import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import csv
import numpy as np

class CleanupCSVData:

    def __init__(self):
        pass

    def ReadCSVFile(self,filename,Textcolumname):  
        df = pd.read_csv(filename, na_values=[''])
        df[Textcolumname] = df[Textcolumname].str.lower()
        return df
    
    def LowerCaseTextColumnDataframe(self,df,Textcolumname):
        df[Textcolumname] = df[Textcolumname].str.lower()
        return df
    
    
    def RemovePunctuation(self,df,Textcolumname):
        df[Textcolumname] = df[Textcolumname].apply(lambda x: re.sub(r'[^\w\s]', '', x))
        # return df[Textcolumname]
        return df
    
    def RemoveNumbers(self,df,Textcolumname):
        df[Textcolumname] = df[Textcolumname].apply(lambda x: re.sub(r'\d+', '', x))
        # df[Textcolumname]
        return df


    def RemoveWhitespace(self,df,Textcolumname):
        df[Textcolumname] = df[Textcolumname].apply(lambda x: x.strip())
        # return df[Textcolumname]
        return df

    
    def RemoveStopwords(self,df,Textcolumname):
        stop_words = set(stopwords.words('english'))
        df[Textcolumname] = df[Textcolumname].apply(lambda x: ' '.join([word for word in x.split() if word not in stop_words]))
        # return df[Textcolumname] 
        return df
    
    def TokenizeText(self,df,Textcolumname):
        print(len(df))
        print(Textcolumname)
        df['text_tokenized'] = df[Textcolumname].apply(lambda x: x.split())
        print(len(df))
        # return df['text_tokenized']
        return df
    
    def Stemming_Lemmatization(self,df,Textcolumname):
        ps = PorterStemmer()
        df['text_stemmed'] = df[Textcolumname].apply(lambda x: ' '.join([ps.stem(word) for word in x.split()]))
        # return df['text_stemmed']
        return df
    

     # Method to clean text data
    def CleanupCSVData(self,filename,Textcolumname):
        df=self.ReadCSVFile(filename,Textcolumname)
        df=self.LowerCaseTextColumnDataframe(df,Textcolumname)
        df=self.RemovePunctuation(df,Textcolumname)
       
        df=self.RemoveNumbers(df,Textcolumname)
        df=self.RemoveWhitespace(df,Textcolumname)
        df=self.RemoveStopwords(df,Textcolumname)
        # print('TokenizeText')
        df=self.TokenizeText(df,Textcolumname)
        df=self.Stemming_Lemmatization(df,Textcolumname)
        # df=self.StemParagraph(df,Textcolumname)
        # df=self.LemmatizeParagraph(df,Textcolumname)
        return df;