import random, urllib2
from nltk.corpus import stopwords

url = "http://open.live.bbc.co.uk/weather/feeds/en/2640194/3dayforecast.rss"
f = urllib2.urlopen(url).read()

data = f.split('<title>')
data = data[4]
data = data.split('</title>')

cachedStopWords = stopwords.words("english")
weather = data[0]
greetings = ['Hey', 'Hello', 'Hi']
random_greeting = random.choice(greetings)
questions = ['How has your day been so far?','Whats your day been like?']
random_question = random.choice(questions)
sad = ['bad', 'crap', 'shitty', 'boring', 'poor', 'shit']
mixed = ['okay', 'alright', 'so so', 'not bad']
happy = ['brilliant', 'good', 'exciting', 'excellent']
yes = ['yes', 'yeah', 'why not', 'y', 'sure', 'alright']
no = ['no', 'nah', 'im good', 'your alright', 'nope', 'rather not']
good = ['sun', 'sunny', 'clear', 'dry', 'good']
bad = ['rain', 'bad', 'cloudy', 'overcast', 'fog', 'shit']

filtered_words = [word for word in word_list if word not in stopwords.words('english')]

response_name = raw_input(random_greeting + " I'm Chatbot, " + "What is your name?")
print(random_greeting + " " + response_name)

response_question = raw_input(random_question)
userInput_question = response_question
if userInput_question in sad:
        print("Sorry to hear that.")
if userInput_question in mixed:
        print("Good, at least it wasn't a bad day.")
if userInput_question in happy:
        print("Brilliant, thats nice to hear.")

response_weather = raw_input("How is the weather today?")
userInput_weather = response_weather
if userInput_weather in good:
    print("Good.")
if userInput_weather in bad:
    print("Oh wellim sure it will improve.")

response_weather = raw_input("Can I tell you about the weather near you tomorrow?")
userInput_weather = response_weather
if userInput_weather in yes:
    print("Okay, the weather in Plymouth on " + weather)
    if userInput_weather in no:
        print("Oh, okay then.")
