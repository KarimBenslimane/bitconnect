from bot.arbitragemanager import ArbitrageManager
from bot.botmanager import BotManager
from bot.bot import Bot
from helpers.logger import Logger
import json
import traceback
import subprocess
from twisted.internet import reactor, task, defer
from twisted.web.server import Site
from twisted.web.resource import Resource
import queue

#TODO: add argument for test setup
#TODO: make loop

logger = Logger("updater")

@defer.inlineCallbacks
def process_task(name, work_queue):
    try:
        print(1)
    except Exception as e:
        print(str(e))

class OrderReceiver(Resource):
    def render_POST(self, request):
        print(request)
        return '<html><body>You submitted: %s</body></html>' % (cgi.escape(request.args["the-field"][0]),)

def update():
    print('starting updater....')
    botmanager = BotManager()
    arbitragemanager = ArbitrageManager()
    active = True
    # while not kill:
    while active:
        print('waiting for bots')
        #check database for new bot
        new_bots = botmanager.get_new_bot()
        if new_bots:
            #put work in the queue
            print('new bots found')
            work_queue = queue.Queue()
            for bot in new_bots:
                work_queue.put(bot)
            #run tasks per bot type
            defer.DeferredList([
                task.deferLater(reactor, 0, process_task, 'Process Tasks', work_queue)
            ])
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
    root = Resource()
    root.putChild("orders", OrderReceiver())
    factory = Site(root)
    reactor.listenTCP(8880, factory)
    reactor.run()
