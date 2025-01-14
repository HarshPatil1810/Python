import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


nltk.download('punkt')
nltk.download('stopwords')

input_string = "This is an example of text that we will tokenize and remove stop words from."

tokens = word_tokenize(input_string)

stop_words = set(stopwords.words('english'))

filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

print("With Stop words ",tokens)
print("After remove stop word ",filtered_tokens)
