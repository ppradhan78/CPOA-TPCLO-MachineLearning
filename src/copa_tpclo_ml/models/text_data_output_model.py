
import base64
from pydantic import BaseModel


class TextDataOutputModel(BaseModel):

    word_tokens:list[str]= None 
    sentence_tokens:list[str]= None 
    most_frequentWords_plot:bytes  =b''
    analyze_sentiment_plot:bytes  =b''
    generate_ngrams_plot:bytes =b''  
