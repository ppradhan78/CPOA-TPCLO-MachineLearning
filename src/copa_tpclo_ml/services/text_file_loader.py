# import pandas as pd
# import os
# import time
# import nltk
# from nltk.corpus import stopwords
# import re
# import string
# from src.ComplaintClassification.config.JsonConfigurationManager import JsonConfigurationManager
# from src.ComplaintClassification.utils.helper import Helper

# class TextFileLoader:
#     def __init__(self):
#         filepath=os.path.join(os.getcwd(),'config\\config.json')
#         self.jsonConfigurationManager=JsonConfigurationManager(filepath)

#     def read_textfile_data(self):
#         path=self.jsonConfigurationManager.get('data_ingestion').get('source_dir')
#         f = open(path, encoding="utf8")
#         return f.read()    