import random


greetings = ['Hey', 'Hello', 'Hi']
random_greeting = random.choice(greetings)
questions = ['How has your day been so far?','Whats your day been like?']
random_question = random.choice(questions)
sad = ['bad', 'crap', 'shitty', 'boring', 'poor']
mixed = ['okay', 'alright', 'so so', 'not bad']
happy = ['brilliant', 'good', 'exciting', 'excellent']
yes = ['yes', 'yeah', 'why not', 'y', 'sure', 'alright']
no = ['no', 'nah', 'im good', 'your alright', 'nope', 'rather not']
good = []
bad = []

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
else print("Im not sure what you mean, sorry.")

response_weather = raw_input("How is the weather today?")

response_weather = raw_input("Can I tell you about the weather near you tomorrow?")
userInput_weather = response_weather
if userInput_weather in yes:
        print("Okay, the weather in Plymouth tomorrow is" + put weather here + " and the Tempurature will be a high of " + maxtemp + ", low of " + mintemp)
        #put in line of text to say if they should enjoy the day whilst it lasts or tell them it will get better


