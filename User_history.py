import os
from datetime import datetime
import slack
from slackbot.slackclient import SlackClient
from slack import WebClient

slack_token = 'xoxp-'
channel_name = 'general'
date_from = '2019-09-10'
date_to = '2019-09-23'

oldest = (datetime.strptime(date_from, "%Y-%m-%d") - datetime(1970, 1, 1)).total_seconds()
latest = (datetime.strptime(date_to, "%Y-%m-%d") - datetime(1970, 1, 1)).total_seconds()

sc = WebClient(slack_token)

users_list = sc.api_call("users.list")
users = {}
for user in users_list['members']:
    users[user['id']] = user['profile']['real_name'] 

channels = sc.api_call("channels.list")
channel_id = None
for channel in channels['channels']:
    if channel['name'] == channel_name:
        channel_id = channel['id']
if channel_id == None:
    raise Exception("cannot find channel " + channel_name)
	
history = sc.channels_history(channel = channel_id)
#history = sc.api_call("channels.history", channel=channel_id, oldest=oldest, latest=latest)
posts_by_user = {}
print(history)
for message in history['messages']:
    if message['text'] in posts_by_user:
        posts_by_user[users[message['text']]] += 1
    #else:
     #   posts_by_user[users[message['text']]] = 1    

for user, count in posts_by_user.items():
	
	print(user, 'posted', count, 'messages')





