# -*- coding: utf-8 -*-
"""
Created on Sat Nov 04 10:16:17 2017

@author: liuka
"""
import cv2
import numpy as np
import os
import time 
import pdb 
import pyaudio
import wave
import utils
from array import array 

class Audio(object):
    def __init__(self):
        None
        #self._cap = cv2.VideoCapture(2)    
    
    def record_voice(self, wav_file, record_seconds):
        chunk = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        RECORD_SECONDS = record_seconds
        
        threshold = 10
        max_value = 0
        
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, output=True, frames_per_buffer=chunk)
        print '* recording'
        frames = []
        for i in range( 0, 44100/chunk * RECORD_SECONDS):
        	  data = stream.read(chunk)
        	  as_ints = array('h', data)
        	  max_value = max(as_ints)
        	  if max_value > threshold:
        		  frames.append(data)
               	
        stream.stop_stream()
        stream.close()
        p.terminate()
        wf = wave.open(wav_file, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        		
        #utils.wav_to_flac(wav_file, flac_file)
             
    def play_voice(self,wav_file):
        #define stream chunk   
        chunk = 1024  
          
        #open a wav format music  
        f = wave.open(wav_file,"rb")  
        #instantiate PyAudio  
        p = pyaudio.PyAudio()  
        #open stream  
        stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                        channels = f.getnchannels(),  
                        rate = f.getframerate(),  
                        output = True)  
        #read data  
        data = f.readframes(chunk)  
        
        #paly stream  
        while data != '':  
            stream.write(data)  
            data = f.readframes(chunk)  
          
        #stop stream  
        stream.stop_stream()  
        stream.close()  
          
        #close PyAudio  
        p.terminate() 
    
    def get_one_frame(self, cap):
        if cap.isOpened() :
            ret,frame = cap.read()
            return frame
        else:
            print "cap is closed!"
            return False


if __name__ == "__main__":
#    cap = cv2.VideoCapture(2)
#    while(cap.isOpened()):
#        # Capture frame-by-frame
#        ret, frame = cap.read()
#        # Our operations on the frame come here
#        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#        gray = frame
#        # Display the resulting frame
#        cv2.imshow('frame',frame)
#        if cv2.waitKey(1) & 0xFF == ord('q'):
#            break
#    # When everything done, release the capture
#    cap.release()
#    cv2.destroyAllWindows()
#    wav_file = r"hello_world.wav"
#    for i in range(3):
#        play_voice(wav_file)
#        time.sleep(2)
    
    #test audio
    audio = Audio()
    wav_file = 'wav_test.wav'
    audio.record_voice(wav_file,5)
    print "recording endl, playing it"
    audio.play_voice(wav_file)
    #test video
#    cap = cv2.VideoCapture(0)
#    while(True):
#        img = audio.get_one_frame(cap)
#        cv2.imshow('frame',img)
#        if cv2.waitKey(1) & 0xFF == ord('q'):
#            break
#    cap.release()
#    cv2.destroyAllWindows()
        
        
    

