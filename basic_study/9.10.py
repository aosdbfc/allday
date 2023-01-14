import wikipedia
from wordcloud import WordCloud
import matplotlib.pyplot as plt


wiki1 = wikipedia.page('South Korea')
wiki2 = wikipedia.page('Japan')

text = wiki1.content + wiki2.content

wordcloud = WordCloud(width = 2000, height = 1500).generate(text)

plt.figure()
plt.imshow(text)
plt.show(text) 
