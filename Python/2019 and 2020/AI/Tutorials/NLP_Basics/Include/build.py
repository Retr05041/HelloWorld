# ---<{ NLP Basics }>---
# ---<{ Following this tutroial -> https://towardsdatascience.com/gentle-start-to-natural-language-processing-using-python-6e46c07addf3 }>---
# ---<{ April 22, 2021  }>---

# pip install nltk
# pip install beautifulsoup4
# pip install matplotlib

# IMPORTS
import nltk # Imports the NLP library we are going to use
nltk.download('stopwords')
from nltk.corpus import stopwords # Count word Frequency, nltk offers a function FreqDist() which will do the job for us. Also, we will remove stop words (a, at, the, for etc) from our web page as we don't need them to hamper our word frequency count.

# nltk.download() | This will show the NLTK downloader to choose what packages need to be installed.
import urllib # helps us crawl webpages
# We will use Beautiful Soup which is a Python library for pulling data out of HTML and XML files. We will use beautiful soup to clean our webpage text of HTML tags.
from bs4 import BeautifulSoup

# MAIN
# We use urllib here to get the html from the website
response =  urllib.request.urlopen('https://en.wikipedia.org/wiki/SpaceX')
html = response.read()

# We then use soup to make a long text line with all the words on the page
soup = BeautifulSoup(html,'html.parser')
text = soup.get_text(strip = True)

# then convert the text into a list with each entity being a word
tokens = [t for t in text.split()]

# counts the words
sr = stopwords.words('english')
clean_tokens = tokens[:]
for token in tokens:
    
    if token in stopwords.words('english'):
        clean_tokens.remove(token)
        
freq = nltk.FreqDist(clean_tokens)
for key,val in freq.items():
    print(str(key) + ':' + str(val))
# We need matplotlib
freq.plot(20, cumulative=False) # From this we can make the assumption this site is about spaceX