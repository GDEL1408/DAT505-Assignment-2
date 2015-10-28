import random


greetings = ['Hey', 'Hello', 'Hi']
random_greeting = random.choice(greetings)

questions = ['How has your day been so far?','Whats your day been like?']
random_question = random.choice(questions)

sad = ['bad', 'crap', 'shitty', 'boring', 'poor']
mixed = ['okay', 'alright', 'so so', 'not bad']
happy = ['brilliant', 'good', 'exciting', 'excellent']

response = raw_input(random_greeting + " I'm Chatbot, " + "What is your name?")
print(random_greeting + " " + response)

response = raw_input(random_question)

while True:
    userInput = raw_input()
    if userInput in sad:
        print("Sorry to hear that")
    