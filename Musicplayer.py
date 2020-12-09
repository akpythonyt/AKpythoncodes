from tkinter import *
import tkinter.ttk as ttk
from ttkthemes import ThemedTk
from pygame import mixer
mixer.init()
mixer.music.load('/home/arun/Music/Bgmusic (online-audio-converter.com).wav')
def play_song():
    mixer.music.play()
def stop_song():
    mixer.music.stop()
def pause():
    mixer.music.pause()
def resume():
    mixer.music.unpause()
window = ThemedTk(theme="equilux")
window.geometry('300x300')  # set dimension of the window
window.title('Music Player')
playButton = ttk.Button(window,text="Play",command=play_song).grid(column=0,row=1)
stopButton =ttk. Button(window,text="Stop",command=stop_song).grid(column=1,row=1)
pausebutton=ttk.Button(window,text="Pause",command=pause).grid(column=2,row=1)
resbutton=ttk.Button(window,text="Resume",command=resume).grid(column=1,row=2)
window.mainloop()
