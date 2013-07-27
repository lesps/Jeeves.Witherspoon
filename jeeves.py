from ttapi import Bot
import re

AUTH = 'otxNYlzKUFqpPLKVeRrOKNjz'
USERID = '51edb9deeb35c16c3e2e61f0'
ROOMID = '4e7cd1024fe7d052e6048e39'

bot = Bot(AUTH,USERID,ROOMID)

def speak(data):
   name = data['name']
   text = data['text']
   if text == '/hello':
      bot.speak('Hey! How are you {0} ?'.format(name))

bot.on('speak', speak)

bot.start()
