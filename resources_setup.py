import os
import sys
import nltk


nltk_data_path=sys.prefix+"\\nltk_data"
print(nltk_data_path)
os.makedirs(nltk_data_path, exist_ok=True)

# Download NLTK resources

# nltk.download('punkt', download_dir=nltk_data_path)
nltk.download('wordnet', download_dir=nltk_data_path)
# nltk.download('punkt_tab', download_dir=nltk_data_path)
nltk.download('omw-1.4', download_dir=nltk_data_path)
nltk.download('stopwords', download_dir=nltk_data_path)
nltk.download()


# class ResourcesSetup:
#     def __init__(self):
#         pass;

#     def DownloadResources(self):
#         # Download NLTK resources
#         nltk.download('punkt')
#         nltk.download('stopwords')
#         nltk.download('wordnet')
#         nltk.download('omw-1.4')