import base64
import io
import string
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
import matplotlib.pyplot as plt
from collections import Counter
from copa_tpclo_ml.models.text_data_output_model import TextDataOutputModel
from textblob import TextBlob
import matplotlib
matplotlib.use('agg')

class ProcessingTextData :
    def __init__(self):
        pass

# ---------- cleanup text file data ----------
    def read_textfile(self,filename):
        with open(filename, encoding="utf8") as file:
            contents = file.read()
            
        return contents    

    def remove_punctuation(self,text):
            return text.translate(str.maketrans('', '', string.punctuation))
    
    def remove_numbers(self,text):
         return ''.join([char for char in text if not char.isdigit()])

    def remove_whitespace(self,text):
         return text.replace("\t", "").replace("\n", "")
    
    def remove_stopwords(self,text):
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(text)
        filtered_sentence = [word for word in word_tokens if word.lower() not in stop_words]
        return ' '.join(filtered_sentence)
    
    def stem_paragraph(self,text):
        ps = PorterStemmer()
        word_tokens = word_tokenize(text)
        stemmed_words = [ps.stem(word) for word in word_tokens]
        return ' '.join(stemmed_words)

    def lemmatize_paragraph(self,text):
        lemmatizer = WordNetLemmatizer()
        word_tokens = word_tokenize(text)
        lemmatized_words = [lemmatizer.lemmatize(word) for word in word_tokens]
        return ' '.join(lemmatized_words)
    
    def tokenize_text(self,text)-> TextDataOutputModel:
          textDataOutputModel=TextDataOutputModel()
          # Tokenize into words
          textDataOutputModel.word_tokens = word_tokenize(text)
          # Tokenize into sentences
          textDataOutputModel.sentence_tokens = sent_tokenize(text)
          return textDataOutputModel

    # Method to clean text data
    def cleanup_textdata(self,filename)-> TextDataOutputModel:
    # def CleanupTextData(self,filename,ngrams=0):
        text=self.read_textfile(filename)
        text=self.remove_punctuation(text)
        text=self.remove_numbers(text)
        text=self.remove_whitespace(text)
        text=self.remove_stopwords(text)
        text=self.stem_paragraph(text)
        text=self.lemmatize_paragraph(text)
        text=self.tokenize_text(text)
        return text
    
# ---------- Generate plot from text file data ----------
    # def MostFrequentWords(self,tokens):
    def frequent_words(self,tokens):
         word_freq = Counter(tokens)
         print("Most common words:", word_freq.most_common(10))
         most_common_words = word_freq.most_common(10)
         words, counts = zip(*most_common_words)
         plt.figure(figsize=(10,6))
         plt.bar(words, counts, color='blue')
         plt.title('Top 10 Most Frequent Words')
         plt.xlabel('Words')
         plt.ylabel('Frequency')

         plot_location = "plot/most_frequency_word_plot.png"
         plt.savefig(plot_location)
         plt.close()
         return plot_location
        #  plt.show()

    def most_frequent_words(self,filename):
        output=self.cleanup_textdata(filename)
        output=self.frequent_words(output.word_tokens)
        return output


    def get_ngrams(self,tokens,ngrams):
            ngrams = list(nltk.ngrams(tokens, ngrams))
            bigram_freq = Counter(ngrams)
            most_common_bigrams = bigram_freq.most_common(10)
            bigrams_words, bigrams_counts = zip(*most_common_bigrams)
            bigrams_labels = [' '.join(gram) for gram in bigrams_words]

            plt.figure(figsize=(10,6))
            plt.bar(bigrams_labels, bigrams_counts, color='green')
            plt.title('Top 10 Most Frequent ngrams')
            plt.xlabel('ngrams')
            plt.ylabel('Frequency')
            plt.xticks(rotation=45)

            # Save the plot to a BytesIO object
            img_buffer = io.BytesIO()
            plt.savefig(img_buffer, format='png')
            img_buffer.seek(0)
            img_str = base64.b64encode(img_buffer.getvalue()).decode('utf-8')
            plot_location = "plot/generate_ngrams.png"
            #  plt.savefig(plot_location)
            #  plt.close()
            return plot_location
            #  plt.show()
    def generate_ngrams(self,filename,ngrams):
         output=self.cleanup_textdata(filename)
         output=self.get_ngrams(output.word_tokens,ngrams)
         return output
         
    def get_sentiment(self,text):
            blob = TextBlob(text)
            # Get polarity score (ranges from -1 to 1)
            polarity = blob.sentiment.polarity
            # Classify the sentiment based on polarity score
            if polarity > 0:
                return 'Positive'
            elif polarity < 0:
                return 'Negative'
            else:
                return 'Neutral'
            
    def get_analyze_sentiment(self,text):
         # Analyze sentiment for each sentence in the text
         sentences = text.split("\n")
         sentiments = [self.get_sentiment(sentence) for sentence in sentences if sentence]

         # Display the results
         for sentence, sentiment in zip(sentences, sentiments):
            print(f"Sentence: {sentence.strip()}")
            print(f"Sentiment: {sentiment}\n")

        # Count the occurrences of each sentiment
         sentiment_counts = {
            'Positive': sentiments.count('Positive'),
            'Negative': sentiments.count('Negative'),
            'Neutral': sentiments.count('Neutral')
         }
        # Visualization: Pie chart of sentiment distribution
         plt.figure(figsize=(7,7))
         plt.pie(sentiment_counts.values(), labels=sentiment_counts.keys(), autopct='%1.1f%%', startangle=90, colors=['green', 'red', 'gray'])
         plt.title('Sentiment Distribution')
         plot_location = "plot/analyze_sentiment_plot.png"
         plt.savefig(plot_location)
         plt.close()
         return plot_location
        #  plt.show()
    def analyze_sentiment(self,filename):
         text=self.read_textfile(filename)
         text=self.remove_punctuation(text)
         text=self.remove_numbers(text)
         text=self.remove_whitespace(text)
         text=self.remove_stopwords(text)
         text=self.stem_paragraph(text)
         text=self.lemmatize_paragraph(text)
         text=self.get_analyze_sentiment(text)
         return text


    