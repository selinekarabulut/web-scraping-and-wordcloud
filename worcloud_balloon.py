#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 19:34:53 2023

@author: selin
"""

import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import PIL.Image
import numpy as np

# Set the keyword to search for
keyword = "balloon"

# Create the URL for the Google News search
url = f"https://news.google.com/search?q={keyword}&hl=en-US&gl=US&ceid=US%3Aen"

# Send a request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, "html.parser")

# Find all of the articles on the page
articles = soup.find_all("article")

# Create a string to store the contents of the articles
text = ""

# Loop through each article
for article in articles:
    # Get the text of the article
    article_text = article.text

    # Add the article text to the string
    text += article_text
    
python_mask = np.array(PIL.Image.open('balloon.jpg'))

# Create a word cloud
wordcloud = WordCloud(stopwords=STOPWORDS,
                     mask=python_mask,
                     background_color='white',
                     contour_color='black',
                     contour_width=3,
                     min_font_size=3,
                     max_words=50).generate(text)

# Display the word cloud
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()