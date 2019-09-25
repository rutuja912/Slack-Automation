import os
import slack
from slack import WebClient
from slackbot.slackclient import SlackClient


slack_token = "xoxp-"
client = slack.WebClient(token=slack_token)
'''slack_c = SlackClient(slack_token)
with open('./wt.pdf', 'rb') as f:
   slack_c.api_call(
       "files.upload",
       channels='CXXXXXXX',
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
sc = SlackClient("UNEXXXXXX")
sc.api_call(
  'files.upload', 
  channels='#general', 
  as_user=True, 
  filename='wt.pdf', 
  file=open('wt.pdf', 'rb'),
)'''
