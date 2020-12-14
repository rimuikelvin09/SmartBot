# import libraries
from newspaper import Article
import random
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings

warnings.filterwarnings('ignore')

# download the punkt package
nltk.download('punkt', quiet=True)

# Get the article
article = Article(
    'https://www.tomshardware.com/reviews/how-to-build-a-pc,5867.html')
article.download()
article.parse()
article.nlp()
corpus = article.text

# print articles text
# print(corpus)

# tokenization
text = corpus
sentence_list = nltk.sent_tokenize(text)  # a list of sentences

# print list of sentences
# print(sentence_list)

# Function to return a random greeing response


def greeting_response(text):
    text = text.lower()

    # bot greeting response
    bot_greetings = ['Hey', 'Hi', 'Niaje', 'hello', 'Habari yako']
    # users greeting patterns
    user_greetings = ['hi', 'hey', 'hello', 'niaje', 'bro', 'wassup']

    for word in text.split():
        if word in user_greetings:
            return random.choice(bot_greetings)

# Creating bots response


def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0, length))

    x = list_var
    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                # Swap
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp

    return list_index


def bot_response(user_input):
    user_input = user_input.lower()
    sentence_list.append(user_input)
    bot_response = ''
    cm = CountVectorizer().fit_transform(sentence_list)
    similarity_scores = cosine_similarity(cm[-1], cm)
    similarity_scores_list = similarity_scores.flatten()
    index = index_sort(similarity_scores_list)
    index = index[1:]
    response_flag = 0

    j = 0
    for i in range(len(index)):
        if similarity_scores_list[index[i]] > 0.0:
            bot_response = bot_response+' '+sentence_list[index[i]]
            response_flag = 1
            j = j+1
        if j > 2:
            break

    if response_flag == 0:
        bot_response = bot_response + ' ' + \
            "I am sorry, cant find what you are asking, Kindly pc me @rimui09 on instagram "

    sentence_list.remove(user_input)

    return bot_response


# Start Chatting
print('RimBot: Hi i am Your assistant . I will answer your questions about PC building.To close me  type exit.')

exit_list = ['exit', 'bye', 'quit']

while(True):
    user_input = input()
    if user_input.lower() in exit_list:
        print('RimBot: Wagwan :) catchya later!')
        break
    else:
        if greeting_response(user_input) != None:
            print('RimBot: '+greeting_response(user_input))
        else:
            print('RimBot: '+bot_response(user_input))
