#!/usr/bin/python
import sys, dbus 
knotify = dbus.SessionBus().get_object("org.kde.knotify", "/Notify")
try: app, event, title, text = sys.argv[1:5] 
except: print 'Usage: knotify.py app event title text'; sys.exit(1) 
knotify.event(event, app, [], title, text, [], [], 0, 0,dbus_interface="org.kde.KNotify")

#up the documentation, I suppose :-) :
#* QString event: text description of the event - you can set it to what you want in this case
#* QString fromApp: the application that is generating the event - you can set it to what you want in this case
#* QString text: the message to show the user
#* QString sound: the sound file to play
#* QString file: the file to log to
#* int present: this is an integer that tells KNotify what kind of notication to do, as below:
#1 - play sound
#2 - show message box
#4 - log to file
#8 - print message to standard error
#16 - show 'passive' message box

# The events are declared in the file $KDEDIR/share/knotifications5/schulserver/schulserver.notifyrc

