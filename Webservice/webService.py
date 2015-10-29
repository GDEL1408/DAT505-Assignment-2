import twitter, datetime

file = open("C:\Users\George\Documents\Uni Work\Year 2\DAT505\Assignment 2\Webservice\TwitterCredentials.txt", 'r')
creds = file.readline().strip().split(',')

api = twitter.Api(creds[0],creds[1],creds[2],creds[3])

timestamp = datetime.datetime.utcnow()

response = api.PostUpdate("Tweeted at " + str(timestamp))

file = open("C:\Users\George\Library\")

print("Status updated to: " + response.text)
