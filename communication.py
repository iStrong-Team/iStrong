# -*- coding: utf-8 -*-
"""
Created on Sat Nov 04 14:22:51 2017

@author: liuka
"""
import os
import sys
import cv2 
import numpy as np
import video_test as vt
from api import ibm_api


def send_respond(audio, send_voice, respond_voice, sign):
    """
    send message and recognize it,then get the respond
    """
    #record wake voice 
    flag = 0
    while flag == 0:
        key_val = raw_input("Press any key to start record: ")
        audio.record_voice(send_voice,3)
        #IBM　ＡＰＩ
        respond_sign = ibm_api(send_voice, respond_voice, sign)
        if respond_sign == 'bye':
			sys.exit(1)
        elif respond_sign == sign:
            flag = 1
            print "get voice sucess!"
#            audio.play_voice(respond_voice)
        else:
            "Please say it again!"
        
    #return respond_sign
    

if __name__ == "__main__":
    wav_dir = 'voice_data'
    audio = vt.Audio()
    #send wake voice 
    send_voice = os.path.join(wav_dir,'wake_voice.wav')
    respond_voice = os.path.join(wav_dir, 'wake_res_voice.wav')
    sign_wake = 'wake'
    send_respond(audio, send_voice, respond_voice, sign_wake)
    #send start voice 
    send_voice = os.path.join(wav_dir,'start_voice.wav')
    respond_voice = os.path.join(wav_dir, 'start_res_voice.wav')
    sign_wake = 'start'
    send_respond(audio, send_voice, respond_voice, sign_wake)
