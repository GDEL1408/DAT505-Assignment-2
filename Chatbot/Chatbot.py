import random


greetings = ['Hey', 'Hello', 'Hi']
random_greeting = random.choice(greetings)

yes = ['yes', 'yeah', 'sure', 'yep', 'y']
no = ['no', 'nope', 'nah', 'n']

response = raw_input(random_greeting + " I'm Chatbot, " + "What is your name?")
print(random_greeting + " " + response)

response = raw_input("Would you like to know about the weather near you today?")
if response in yes:
        responce = raw_input("Where abouts do you live then?")
        
else response in no
        responce = raw_input("Okay then, whats your favourite football team?")
    