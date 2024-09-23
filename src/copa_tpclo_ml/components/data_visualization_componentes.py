# import matplotlib.pyplot as plt
# from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# class DataVisualizationComponentes:
#     def __init__(self):
#         pass
#     def draw_bar_plot(data):
#         fig = plt.figure(figsize=(8,6))
#         data.groupby('Product').Consumercomplaintnarrative.count().plot.bar()
#         plt.show()


#     def draw_word_cloud(data):
#         text = " ".join(i for i in data['Consumercomplaintnarrative'])
#         ## text = " ".join(i for i in data.Issue )
#         # Consumer complaint narrative
#         stopwords = set(STOPWORDS)
#         wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
#         plt.figure( figsize=(15,10))
#         plt.imshow(wordcloud, interpolation='bilinear')
#         plt.axis("off")
#         plt.show() 