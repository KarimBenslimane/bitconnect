from bot.botmanager import BotManager
from bot.bot import Bot
import subprocess

def update():
    print('starting updater....')
    #while true until application is closed
    kill = False
    botmanager = BotManager()
    # while not kill:
    print('waiting for bots')
    #check database for new bot
    new_bots = botmanager.get_new_bot()
    if new_bots:
        print('new bot found')
        #TODO: choose subprocess
        #start each bot and create subprocesses per type bot or exchange?
        for bot in new_bots:
            type = bot.get_type()
            if type == Bot.TYPE_ARBITRAGE:
                #add this bot to the arbitrage subprocess
                subprocess.run(["/usr/bin/python3", "/var/www/bitconnect/processes/process.py"])
                subprocess.run(["/usr/bin/python3", "/var/www/bitconnect/processes/process.py"])

    #loop through


if __name__ == '__main__':
    update()