import time
import slack
from slack import WebClient

ts1 = time.time()
print (ts1)
slack_token ='xoxp-754552798980-755017691632-767089405015-d47cfdc1e038b8bffb5ba45f25886cf8'
sc = WebClient(slack_token)
channel_name = 'general'

channels = sc.api_call("channels.list")
channel_id = None
for channel in channels['channels']:
    if channel['name'] == channel_name:
        channel_id = channel['id']
if channel_id == None:
    raise Exception("cannot find channel " + channel_name)
history = sc.channels_history(channel = channel_id)
print(history)
t_s = history['thread_ts']
print(t_s)
t =history['ts']
print(t)
#for t_s in history['thread_ts']:
#	print(t_s['string'])

'''for t_s in history['thread_ts']:		
		
	if t_s['string'] < ts1:
		slack_client.api_call(
                'chat.delete',
                channel=channel_id,
                thread_tsts=t_s['string'],
                as_user=True
            )
			'''