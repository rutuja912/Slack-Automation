import os
import slack
from slack import WebClient
from slackbot.slackclient import SlackClient

#slack_token = os.environ["xoxp-754552798980-755017691632-757262358374-c0070416328b44d0269c7ab089ac007a"]

slack_token = "xoxp-754552798980-755017691632-757262358374-c0070416328b44d0269c7ab089ac007a"
client = slack.WebClient(token=slack_token)
'''slack_c = SlackClient(slack_token)
with open('./wt.pdf', 'rb') as f:
   slack_c.api_call(
       "files.upload",
       channels='CMVG8MWLT',
        filename='wt.pdf',
        title='sampletitle',
        initial_comment='sampletext',
        file=io.BytesIO(f.read())
    )
	'''
client.files_upload(
 channels="CMVG8MWLT",
 file="wt.pdf",
title="Test upload")
'''
#from slackclient import SlackClient
sc = SlackClient("UNEU07DQQ")
sc.api_call(
  'files.upload', 
  channels='#general', 
  as_user=True, 
  filename='wt.pdf', 
  file=open('wt.pdf', 'rb'),
)'''