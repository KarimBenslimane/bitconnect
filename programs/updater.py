from bot.botmanager import BotManager
from bot.bot import Bot
from helpers.logger import Logger
import json
import traceback
import subprocess
import atexit

logger = Logger("updater")
running_procs = []


def update_procs():
    for proc in running_procs:
        retcode = proc.poll()
        if retcode is not None:  # Process finished.
            proc.terminate()
            proc.kill()
            running_procs.remove(proc)
            break


def kill_procs():
    for proc in running_procs:
        proc.terminate()
        proc.kill()


def update():
    try:
        print('starting updater....')
        botmanager = BotManager()
        active = True
        # while not kill:
        while active:
            #print('waiting for bots')
            # check database for new bot
            new_bots = botmanager.get_new_bot()
            if new_bots:
                # TODO: choose subprocess
                # start each bot and create subprocesses per type bot?
                for bot in new_bots:
                    try:
                        botmanager.update_bot(bot.set_status(Bot.STATUS_ON))
                        args = json.dumps({Bot.BOT_ID: bot.get_id(), Bot.BOT_TYPE: bot.get_type()})
                        running_procs.append(
                            subprocess.Popen(["/usr/bin/python3", "/var/www/bitconnect/processes/process.py", args])
                        )
                    except Exception as e:
                        logger.info(str(e))
                        logger.info(traceback.format_exc())
                        botmanager.update_bot(bot.set_status(Bot.STATUS_ERROR))
            update_procs()
    except Exception as e:
            kill_procs()
    finally:
        kill_procs()



if __name__ == '__main__':
    update()
    atexit.register(kill_procs)
