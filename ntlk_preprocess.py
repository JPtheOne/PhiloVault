#Libraries and downloads
import nltk
#nltk.download("wordnet")
#nltk.download('punkt')
#nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer

#PARAGRAPH DECLARATION
paragraph = "played, John, ran, forgot, actually, ONU, forgot"
paragraph2 = "Je m’appelle Jessica. Je suis une fille, je suis française et j’ai treize ans. Je vais à l’école à Nice, mais j’habite à Cagnes-Sur-Mer. J’ai deux frères."


tokenizer = word_tokenize(paragraph)
print("TOKENIZED PARAGRAPH: ",(tokenizer))

#Now that is tokenized, let's get rid of stop words
stopwords= set(stopwords.words("english"))
filtered_paragraph = []

for word in tokenizer:
    if word.casefold() not in stopwords and word.isalnum():
        filtered_paragraph.append(word)

print("WITHOUT STOPWORDS AND MARKS: ", filtered_paragraph)

#Stemmer functions weirdly... lets try with lemmatizers hehe
'''
stemmer = SnowballStemmer("french")
stemmed_list = []

for word in filtered_paragraph:
    stemmed_word = stemmer.stem(word)
    stemmed_list.append(stemmed_word)

print("Without stopwords, punctuation marks and stemmed: ", stemmed_list)
'''

lemmatizer = WordNetLemmatizer()
lemmatized_list = []

for word in filtered_paragraph:
    lemmatized_word = lemmatizer.lemmatize(word)
    lemmatized_list.append(lemmatized_word)
print("LEMMATIZED LIST WITHOUT STOP WORDS NOR MARKS: ", lemmatized_list)