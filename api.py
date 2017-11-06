import os
import utils
import subprocess
import json
from watson_developer_cloud import ConversationV1


def t2s(text, aud_name, username='ba84f60f-e001-4b9c-9af6-e7213506a026', passwd='ymb5n7i3gNCG'):
	print '===================================== begin text to speech ======================================\n' 
	cmd = 'curl -X POST -u %s:%s --header \"Content-Type: application/json\"  --header \"Accept: audio/wav\" --data "{\\\"text\\\":\\\"%s \\\"}\" --output %s \"https://stream.watsonplatform.net/text-to-speech/api/v1/synthesize?voice=en-US_AllisonVoice\"'%(username, passwd, text, aud_name)
	#print(cmd)
	os.system(cmd)


def play_audio_file(aud_file):
	cmd = 'play %s' % aud_file
	os.system(cmd)


def s2t(audio, username='d2d15743-8af0-4ee8-918e-eeb07a66fb37', passwd='0ymqxsRqhhxE'):
	print '===================================== begin speech to text ======================================\n' 
	cmd = 'curl -X POST -u %s:%s --header \"Content-Type: audio/wav\"  --header \"Transfer-Encoding:chunked\" --data-binary @%s "https://stream.watsonplatform.net/speech-to-text/api/v1/recognize\"'%(username, passwd, audio)
	#print(cmd)
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
	(output, err) = p.communicate()
	p_status = p.wait()
	output = output.replace('true', 'True').replace('false','False')
	output = dict(eval(output))
	j = json.dumps(output)
	d = json.loads(j)
	#print '===================================== speech to text result:======================================\n',d 
	if len(d[u'results']) < 1:
		return 'none'
	transcript = d[u'results'][0][u'alternatives'][0][u'transcript']
	
	return transcript


def chat(input):
	conversation = ConversationV1(
	    username='98884adb-0346-4501-b6c3-98d132c36fb6',
	    password='AJz4qCghyxDc',
	    version='2017-04-21')
	
	# replace with your own workspace_id
	workspace_id = '9bdc4eda-e512-4e27-9994-1bc2343ce8d1'
	
	response = conversation.message(workspace_id=workspace_id, message_input={
	    'text': input})
	output = json.dumps(response, indent=7)
	#print output# = json.dumps(response, indent=7)
	output = json.loads(output)
	if len(output['intents']) < 1:
		intent = 'not recognized'
	else:		
		intent = output['intents'][0]['intent']
	reply = output['output']['text'][0]
	print 'intent:', intent
	if intent == 'wake' or intent == 'start' or intent == 'bye':
		sign = intent
	else:
		sign = 'talk'
	return reply, sign


def ibm_api(send_voice, response_voice, sent_sign):
	send_words = s2t(send_voice)
	print '===================================== speech to text result:======================================\n',send_words 
	if send_words == 'none':
		respone_words = 'Sorry I didn\'t understand. Can you repeat again?'
		sign = 'none'
	else:
		respone_words, sign = chat(send_words)
	print '===================================== respone from AI:======================================\n', respone_words
	t2s(respone_words, response_voice)
	play_audio_file(response_voice)
	return sign
