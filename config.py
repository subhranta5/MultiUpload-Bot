import os

class Config(object):
   # The Telegram API things
   API_ID= int(os.environ.get("API_ID" 3566549))
   API_HASH = os.environ.get("API_HASH", "829977f2da962ae570aa0b91572aa8e4")
   # get a token from @BotFather
   BOT_TOKEN = os.environ.get("BOT_TOKEN", "1971079453:AAFmFUuSPcRN61zsHKx5b2bIQACkRErmOgQ")
   # channel id = -100 (for logs)
   LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL" -1001333210651))   
   # Array to store users who are authorized to use the bot 
   AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "461650361").split())    
   # force sub user to the channel (without @)
   CHNAME = os.environ.get("CHNAME", "vidcompr")
                           
