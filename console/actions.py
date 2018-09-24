import argparse
from console.action.bot.create import Create as BotCreate
from console.action.bot.delete import Delete as BotDelete
from console.action.bot.list import List as BotList
from console.action.exchange.create import Create as ExchangeCreate
from console.action.exchange.delete import Delete as ExchangeDelete
from console.action.exchange.list import List as ExchangeList
from console.action.user.create import Create as UserCreate
from console.action.user.delete import Delete as UserDelete
from console.action.user.list import List as UserList
from user.login import Login
from helpers.logger import Logger
import traceback


class Actions:
    login = None
    logger = Logger("main")

    def __init__(self):
        """
        Add new actions here to have them included automatically
        Sets up class variables for the parsers, subparsers array has the filled parsers for each action
        Set up all the actions in the parsers and then execute the correct action
        """
        self.actions = [
            BotCreate(),
            BotDelete(),
            BotList(),
            ExchangeCreate(),
            ExchangeDelete(),
            ExchangeList(),
            UserCreate(),
            UserDelete(),
            UserList()
        ]
        self.login = Login()
        self.parser = None
        self.subparser = None
        self.subparsers = []
        self.set_up()
        self.execute()

    def set_up(self):
        """
        Set up parser and create subparser
        Add each actions arguments and store its particular subparser
        """
        # TODO is storing this 'new' subparser needed?
        self.parser = argparse.ArgumentParser()
        self.subparser = self.parser.add_subparsers()

        for i in range(len(self.actions)):
            self.subparsers.append(self.actions[i].init(self.subparser))

    def execute(self):
        """
        Parse the given arguments and execute the correct action after checking login
        """
        try:
            args = self.parser.parse_args()
            if self.login.check_login(username=args.username, password=args.password):
                args.func(args)
            else:
                print("No user found with that username and password.")
        except AttributeError as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            self.logger.info(str(ex))
            self.logger.info(traceback.format_exc())
