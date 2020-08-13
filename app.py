# Author: Orion Ford
# This program will speak the text provdied. This is the first program in which introduced me to "win32" library and winc1.

import win32com.client as winc1


speak = winc1.Dispatch("SAPI.SpVoice")
speak.Speak("Greetings.... I am you're personal assistant. Anything you need from me Orion, don't be afraid to ask. I mean, hey.... you did create me right?! Right. So no worries my brother. Side note: Arrest the cops who killed Breonna Taylor!")
