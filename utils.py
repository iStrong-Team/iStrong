import os
	
def wav_to_mp3(wf, mf):
	cmd = 'lame -b 32k %s %s' %(wf, mf)
	os.system(cmd)
	print 'done.'

def mp3_to_wav(mf, wf):
	cmd = 'lame --decode %s %s' %(mf, wf)
	os.system(cmd)
	print 'done.'


def wav_to_flac(wf, ff):
	cmd = 'flac %s %s' %(wf, ff)	
	os.system(cmd)
	print 'done.'

def flac_to_wav(ff, wf):
	cmd = 'flac -d %s -o %s ' %(ff, wf)
	os.system(cmd)
	print 'done.'

