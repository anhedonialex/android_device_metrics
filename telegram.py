import requests

import secrets


def bot_sendtext(bot_message):

   bot_token = secrets.MONITOR_BOT_TOKEN
   bot_chatID = secrets.MONITOR_CHAT_ID
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
   response = requests.get(send_text)
   return response.json()
