#Libraries and downloads
import nltk
#nltk.download('punkt')
#nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.snowball import SnowballStemmer

#PARAGRAPH DECLARATION
paragraph = "The kid plays with the ball and the girl runs outside."
paragraph2 = "Je m’appelle Jessica. Je suis une fille, je suis française et j’ai treize ans. Je vais à l’école à Nice, mais j’habite à Cagnes-Sur-Mer. J’ai deux frères."


tokenizer = word_tokenize(paragraph2)
print("TOKENIZED PARAGRAPH: ",(tokenizer))

#Now that is tokenized, let's get rid of stop words
stopwords= set(stopwords.words("french"))
filtered_paragraph = []

for word in tokenizer:
    if word.casefold() not in stopwords and word.isalnum():
        filtered_paragraph.append(word)

print("Without stop words nor punctuation marks: ", filtered_paragraph)

stemmer = SnowballStemmer("french")
stemmed_list = []

for word in filtered_paragraph:
    stemmed_word = stemmer.stem(word)
    stemmed_list.append(stemmed_word)

print("Without stopwords, punctuation marks and stemmed: ", stemmed_list)