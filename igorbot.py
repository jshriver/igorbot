import os
import discord
import time
import datetime
from timeit import default_timer as timer

client = discord.Client()
sTime = timer()
eTime = timer()
sTime2 = timer()
eTime2 = timer()
sTime3 = timer()
eTime3 = timer()
timerFlag = 0
timerFlag2 = 0
timerFlag3 = 0

@client.event
async def on_message(message):
    global sTime
    global eTime
    global timerFlag
    global sTime2
    global eTime2
    global timerFlag2
    global sTime3
    global eTime3
    global timerFlag3

    if message.content == '/spray' or message.content == '~spray':
            response = 'https://i.imgur.com/Ic7Lxi6.gif'
            await message.channel.send(response)	
    if message.content == 'marry me igor':
            response = 'I would love to master! ❤ 🤗 '
            await message.channel.send(response)	
    if message.content == 'love you igor' or message.content == 'i love you igor':
            response = 'Love you too master! ❤ 🤗 '
            await message.channel.send(response)	
    if message.content == 'Love you igor':
            response = 'Love you too master! ❤ 🤗 '
            await message.channel.send(response)	
    if message.content == 'thank you igor':
            response = 'Very welcome master! ❤ 🤗 '
            await message.channel.send(response)	
    if message.content == 'Thank you igor':
            response = 'Very welcome master! ❤ 🤗 '
            await message.channel.send(response)	
    if message.content == 'hi igor':
            response = 'Hello master! ❤ 🤗 '
            await message.channel.send(response)	
    if message.content == 'Hi igor':
            response = 'Hello master! ❤ 🤗 '
            await message.channel.send(response)	
    if message.content == 'do my bidding igor':
            response = 'whatever you say master!'
            await message.channel.send(response)	
            response = 'https://i.imgur.com/Z6Z7A9E.gif'
            await message.channel.send(response)	

    if message.content == 'igor flip the switch' or message.content == 'flip the switch igor':
        if timerFlag == 1:
            response = 'Timer already started, please stop first master.'
            await message.channel.send(response)	
        else:
            timerFlag = 1
            response = 'COUNTDOWN HAS STARTED HIT PLAY AT 🚨  🇬  🇴 🚨'
            await message.channel.send(response)	
            time.sleep(1)
            response = '5️⃣'
            await message.channel.send(response)	
            time.sleep(1)
            response = '4️⃣'
            await message.channel.send(response)	
            time.sleep(1)
            response = '3️⃣'
            await message.channel.send(response)	
            time.sleep(1)
            response = '2️⃣'
            await message.channel.send(response)	
            time.sleep(1)
            response = '1️⃣'
            await message.channel.send(response)	
            time.sleep(1)
            response = '🚨  🇬 🇴   🚨'
            await message.channel.send(response)	
            response = 'Timer has started master'
            await message.channel.send(response)	
            sTime = timer()
            response = 'https://i.imgur.com/PnBpPeJ.gif'
            await message.channel.send(response)	
    
    if message.content == 'igor let them fight' or message.content == 'let them fight igor':
        if timerFlag3 == 1:
            response = 'Timer already started, please stop first master.'
            await message.channel.send(response)	
        else:
            timerFlag3 = 1
            response = 'COUNTDOWN HAS STARTED HIT PLAY AT 🚨  🇬  🇴 🚨'
            await message.channel.send(response)	
            time.sleep(1)
            response = '5️⃣'
            await message.channel.send(response)	
            time.sleep(1)
            response = '4️⃣'
            await message.channel.send(response)	
            time.sleep(1)
            response = '3️⃣'
            await message.channel.send(response)	
            time.sleep(1)
            response = '2️⃣'
            await message.channel.send(response)	
            time.sleep(1)
            response = '1️⃣'
            await message.channel.send(response)	
            time.sleep(1)
            response = '🚨  🇬 🇴   🚨'
            await message.channel.send(response)	
            response = 'Timer has started master'
            await message.channel.send(response)	
            sTime3 = timer()
            response = 'https://i.imgur.com/5OUy7C7.gif'
            await message.channel.send(response)	

    if message.content == '/elvira':
            response = 'https://i.imgur.com/xnPxfO0.gif'
            await message.channel.send(response)	

    if message.content == '~start timer':
        if timerFlag == 1:
            response = 'Timer already started, please stop first master.'
            await message.channel.send(response)	
        else:
            timerFlag = 1
            response = 'COUNTDOWN HAS STARTED HIT PLAY AT 🚨  🇬  🇴 🚨'
            await message.channel.send(response)	
            time.sleep(1)
            response = '5️⃣'
            await message.channel.send(response)	
            time.sleep(1)
            response = '4️⃣'
            await message.channel.send(response)	
            time.sleep(1)
            response = '3️⃣'
            await message.channel.send(response)	
            time.sleep(1)
            response = '2️⃣'
            await message.channel.send(response)	
            time.sleep(1)
            response = '1️⃣'
            await message.channel.send(response)	
            time.sleep(1)
            response = '🚨  🇬 🇴   🚨'
            await message.channel.send(response)	
            response = 'Timer has started master'
            await message.channel.send(response)	
            sTime = timer()
    if message.content == '~start timer2':
        if timerFlag2 == 1:
            response = 'Timer already started, please stop first master.'
            await message.channel.send(response)	
        else:
            timerFlag2 = 1
            response = 'COUNTDOWN HAS STARTED HIT PLAY AT 🚨  🇬  🇴 🚨'
            await message.channel.send(response)	
            time.sleep(1)
            response = '5️⃣'
            await message.channel.send(response)	
            time.sleep(1)
            response = '4️⃣'
            await message.channel.send(response)	
            time.sleep(1)
            response = '3️⃣'
            await message.channel.send(response)	
            time.sleep(1)
            response = '2️⃣'
            await message.channel.send(response)	
            time.sleep(1)
            response = '1️⃣'
            await message.channel.send(response)	
            time.sleep(1)
            response = '🚨  🇬 🇴   🚨'
            await message.channel.send(response)	
            response = 'Timer has started master'
            await message.channel.send(response)	
            sTime2 = timer()

    # Stop timer
    if message.content == '~stop timer' or message.content == '~stop time':
        if timerFlag == 0:
            response = 'No timer is currently running master'
            await message.channel.send(response)	
        else:
            eTime = timer()
            elapsedSeconds = eTime - sTime
            elapsed = str(datetime.timedelta(seconds=int(elapsedSeconds)))
            response = 'Timer has stopped after {} elapsed master'.format(elapsed)
            await message.channel.send(response)	
            timerFlag = 0

    if message.content == '~stop timer2':
        if timerFlag2 == 0:
            response = 'No timer is currently running master'
            await message.channel.send(response)	
        else:
            eTime2 = timer()
            elapsedSeconds = eTime2 - sTime2
            elapsed = str(datetime.timedelta(seconds=int(elapsedSeconds)))
            response = 'Timer has stopped after {} elapsed master'.format(elapsed)
            await message.channel.send(response)	
            timerFlag2 = 0

    if message.content == '~stop fight':
        if timerFlag3 == 0:
            response = 'No timer is currently running master'
            await message.channel.send(response)	
        else:
            eTime3 = timer()
            elapsedSeconds = eTime3 - sTime3
            elapsed = str(datetime.timedelta(seconds=int(elapsedSeconds)))
            response = 'Timer has stopped after {} elapsed master'.format(elapsed)
            await message.channel.send(response)	
            timerFlag3 = 0

    # Check timer
    if message.content == '~check timer' or message.content == '~check time' :
        if timerFlag == 0:
            response = 'No timer is currently running master'
            await message.channel.send(response)	
        else:
            eTime = timer()
            elapsedSeconds = eTime - sTime
            elapsed = str(datetime.timedelta(seconds=int(elapsedSeconds)))
            response = 'Current elapsed time {}'.format(elapsed)
            await message.channel.send(response)	

    if message.content == '~check timer2':
        if timerFlag2 == 0:
            response = 'No timer is currently running master'
            await message.channel.send(response)	
        else:
            eTime2 = timer()
            elapsedSeconds = eTime2 - sTime2
            elapsed = str(datetime.timedelta(seconds=int(elapsedSeconds)))
            response = 'Current elapsed time {}'.format(elapsed)
            await message.channel.send(response)	
    
    if message.content == '~check fight':
        if timerFlag3 == 0:
            response = 'No timer is currently running master'
            await message.channel.send(response)	
        else:
            eTime3 = timer()
            elapsedSeconds = eTime3 - sTime3
            elapsed = str(datetime.timedelta(seconds=int(elapsedSeconds)))
            response = 'Current elapsed time {}'.format(elapsed)
            await message.channel.send(response)	

client.run('Nzk5MzM0NDEzMjQ2NjYwNjEw.YACELw.tSloUa5-5DDqjrb5mBcghUYHa8U')
