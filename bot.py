#!/usr/bin/python
import socket
import time
import random
import sys
import string
import datetime
from telnetlib import *

host = 'irc.hanirc.org'
port = 6668
#channel = '#fbk'
channel = '#HANOSBOTEST'
prefix = '##'
trans_flag = 0			# 1 is got cryptography, 0 is needed

HEY=["What's going on?", "What's eating you?", "What's wrong?", "What's the problem?", "What's the matter with you?"]

def joinirc(chan):
	irc.send("JOIN " + chan + "\n")

def sendmsg(msg):
	irc.send("PRIVMSG " + channel + " :" + msg + "\n")

def getindex(LIST):
	index = random.randrange(0, len(LIST))
	return index

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((host, port))

irc.send("USER CABON CABON CABON : CABON \n")
time.sleep(1)
print irc.recv(1024)
irc.send("NICK CABON\n")

buf = irc.recv(1024).split()
tmp = buf[1]
ping = tmp[1:]
print ping

irc.send('PONG :' + ping + '\n')
joinirc(channel)

while True:
	data = irc.recv(4096)

	if data.find('PING') != -1:
		print "[*]send pong"
		ping = data.split(":")[1]
		irc.send('PONG :'+ping+"\n")

	if data.find('PRIVMSG') != -1:
		nick = data.split('#')[0].replace(':','')
		message = ':'.join(data.split(':')[2:])
		print nick + ' : ', message
	
		if message.find('##') != -1:
			if message.find('HEY') != -1:
				index = getindex(HEY)
				sendmsg(HEY[index])

################    flack3r    #######################
################  2014.12.08   #######################

############## Example : ##TIME ######################

			if message.find('TIME') != -1:
				now = time.localtime()
				s = "%04d-%02d-%02d/%02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
				sendmsg(s)

######################################################


################     hanos     #######################
################  2014.12.08   #######################

################    Example    #######################
## translate "dmpzgbbclzgrq"
## maketrans 'abcdefghijklmnopqrstuvwxyz' by 'cdefghijklmnopqrstuvwxyzab'

			if message.find('translate') != -1:
				start = message.find("\"")
				end = message.find("\"", start+1)
				target = message[start+1:end]
				sendmsg("I need maketrans")
				trans_flag = 1

			if message.find('maketrans') != -1:
				start = message.find("'")
				end = message.find("'", start+1)
				enc = message[start+1:end]
				
				start = message.find("'", end+1)
				end = message.find("'", start+1)
				unenc = message[start+1:end]

				if trans_flag is not 1:
					sendmsg("I need a cryptograph.")

				elif len(enc) is len(unenc):
					data = string.maketrans(enc, unenc)
					sendmsg("Translate C0mplete")
					sendmsg(string.translate(target, data))
				
				else:
					sendmsg("Error : maketrans arguments must have same length")
					sendmsg("Try Again...")
				
				trans_flag = 0

######################################################
