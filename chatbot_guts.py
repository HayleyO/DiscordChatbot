import string
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def read_in_corpus():
    f=open('corpus\joker.txt','r',errors = 'ignore')
    raw=f.read()
    raw = raw.lower()
    #Install words while we're here
    nltk.download('punkt') 
    nltk.download('wordnet')
    return raw

raw = read_in_corpus()
sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
lemmer = WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

#Cosine similarity
def generate_response(user_input):
    sent_tokens.append(user_input.lower())
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        return "Don't get it"
    else:
        return sent_tokens[idx]


if __name__ == '__main__':
    while(True):
        user_input = str(input())
        response = generate_response(user_input)
        print(response)