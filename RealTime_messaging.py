import os
import slack

@slack.RTMClient.run_on(event='message')
def say_hello(**payload):
	data = payload['data']
	web_client = payload['web_client']
	rtm_client = payload['rtm_client']
	if 'Hello' in data['text']:
		channel_id = data['channel']
		thread_ts = data['ts']
		user = data['user']

		web_client.chat_postMessage(
			channel=channel_id,
			text=f"Hi <@{user}>!",
			thread_ts=thread_ts
		)
	else:
		channel_id = data['channel']
		thread_ts = data['ts']
		user = data['user']

		web_client.chat_postMessage(
			channel=channel_id,
			text=f"Greet me first <@{user}>!",
			thread_ts=thread_ts
		
		)
slack_token = 'xoxp-'
rtm_client = slack.RTMClient(token=slack_token)
rtm_client.start()
