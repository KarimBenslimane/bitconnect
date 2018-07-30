import argparse
from console.action.exchange.add import Add as AddExchange
from console.action.exchange.list import List as ListExchanges
from console.action.exchange.remove import Remove as RemoveExchange
from console.action.bot.add import Add as AddBot
from console.action.user.create import Create as CreateUser
from console.action.user.list import List as ListUser
from user import login


class Actions:
    def __init__(self):
        # Add new actions here to have them included automatically
        self.actions = [
            AddExchange(),
            ListExchanges(),
            RemoveExchange(),
            AddBot(),
            CreateUser(),
            ListUser()
        ]

        # Sets up class variables for the parsers, subparsers array has the filled parsers for each action
        self.parser = None
        self.subparser = None
        self.subparsers = []

        # Set up all the actions in the parsers and then execute the correct action
        self.set_up()
        self.execute()

    def set_up(self):
        # Set up parser and create subparser
        self.parser = argparse.ArgumentParser()
        self.subparser = self.parser.add_subparsers()

        # Add each actions arguments and store its particular subparser
        # TODO is storing this 'new' subparser needed?
        for i in range(len(self.actions)):
            self.subparsers.append(self.actions[i].init(self.subparser))

    def execute(self):
        # Parse the given arguments and execute the correct action after checking login
        # TODO add correct login functionality + actual database > see file/helper.py?
        args = self.parser.parse_args()
        # TODO REPLACE LOGIN CHECKNAME WITH OTHER LOGIN
        #login.check_name(args.filename)
        args.func(args)
