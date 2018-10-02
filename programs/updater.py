from bot.arbitragemanager import ArbitrageManager
from bot.botmanager import BotManager
from bot.bot import Bot
from helpers.logger import Logger
import json
import traceback
import subprocess

#TODO: add argument for test setup
#TODO: make loop
def update():
    print('starting updater....')
    logger = Logger("updater")
    botmanager = BotManager()
    arbitragemanager = ArbitrageManager()
    active = True
    # while not kill:
    while active:
        print('waiting for bots')
        #check database for new bot
        new_bots = botmanager.get_new_bot()
        if new_bots:
            print('new bot found')
            #TODO: choose subprocess
            #start each bot and create subprocesses per type bot?
            for bot in new_bots:
                try:
                    args = json.dumps({Bot.BOT_ID: bot.get_id(), Bot.BOT_TYPE: bot.get_type()})
                    subprocess.run(["/usr/bin/python3", "/var/www/bitconnect/processes/process.py", args])
                except Exception as e:
                    logger.info(str(e))
                    logger.info(traceback.format_exc())
    #loop through


if __name__ == '__main__':
    update()