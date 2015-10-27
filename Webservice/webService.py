import twitter, datetime

user = #put in my user ID



api = twitter.Api(creds[0], creds[1], creds[2], creds[3],)

statuses = api.GetUserTimeline(user)

print(statuses[0].text)