import sys
import time
import random
import os
import datetime
import telepot

global songLink
global songName
songLink = ""
songName = ""

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    commandArgs = command.split()

    command = commandArgs[0]
    print(commandArgs)
    if len(commandArgs) > 1:
        songLink = commandArgs[1]
        songName = commandArgs[2]

    print ('Got command: %s' % command)

    if command == '/roll':
        bot.sendMessage(chat_id, random.randint(1,6))
    elif command == '/time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))
    elif command == '/ip':
        bot.sendMessage(chat_id, get("https://api.ipify.org").text)
    elif command == '/song':
        downloadSong(songLink, songName)
        bot.sendAudio(chat_id,open('/home/pi/waspy/' + songName + '.mp3','rb'))

def downloadSong(songLink, songName):
    os.system("youtube-dl -x --audio-format mp3 -o '" + songName + ".%(ext)s' " + songLink)

bot = telepot.Bot('ENTER YOUR BOT KEY HERE AND DO NOT COMMIT IT')
bot.message_loop(handle)
print ('Im listening')

while 1:
    time.sleep(10)
