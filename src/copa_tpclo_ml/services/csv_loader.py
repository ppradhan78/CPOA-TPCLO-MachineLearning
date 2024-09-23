# import pandas as pd
# import os
# import time
# import nltk
# from nltk.corpus import stopwords
# import re
# import string
# from src.ComplaintClassification.config.JsonConfigurationManager import JsonConfigurationManager
# from src.ComplaintClassification.utils.helper import Helper

# class CSVLoader:
#     def __init__(self):
#         filepath=os.path.join(os.getcwd(),'config\\config.json')
#         self.jsonConfigurationManager=JsonConfigurationManager(filepath)

#     def extract_data(self ):
#         path=self.jsonConfigurationManager.get('data_ingestion').get('source_dir')
#         filepath=os.path.join(os.getcwd(),path)
#         archive_dir=self.jsonConfigurationManager.get('data_ingestion').get('archive_dir')
#         archive_path=os.path.join(archive_dir,Helper.GetUniquefileName(Helper.GetfileName(filepath)))

#         data = pd.read_csv(filepath)
#         data.columns = data.columns.str.replace(' ', '') 
        
#         data.to_csv(archive_path)
#         data.dropna()

#         def clean(text):
#             # nltk.download('stopwords')
#             stemmer = nltk.SnowballStemmer("english")
#             stopword=set(stopwords.words('english'))
#             text = str(text).lower()
#             text = re.sub('\[.*?\]', '', text)
#             text = re.sub('https?://\S+|www\.\S+', '', text)
#             text = re.sub('<.*?>+', '', text)
#             text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
#             text = re.sub('\n', '', text)
#             text = re.sub('\w*\d\w*', '', text)
#             text = [word for word in text.split(' ') if word not in stopword]
#             text=" ".join(text)
#             text = [stemmer.stem(word) for word in text.split(' ')]
#             text=" ".join(text)
#             return text
#         data["Consumercomplaintnarrative"] = data["Consumercomplaintnarrative"].apply(clean)
#         return data  