import argparse
from console.action.exchange.add import Add as ExchangeAdd
from console.action.exchange.list import List as ExchangeList
from console.action.exchange.remove import Remove as ExchangeRemove
from console.action.bot.add import Add as BotAdd
from console.action.user.create import Create as UserCreate
from console.action.user.list import List as UserList
from user.login import Login


class Actions:
    login = None

    def __init__(self):
        # Add new actions here to have them included automatically
        self.actions = [
            ExchangeAdd(),
            ExchangeList(),
            ExchangeRemove(),
            BotAdd(),
            UserCreate(),
            UserList()
        ]

        # Sets up class variables for the parsers, subparsers array has the filled parsers for each action
        self.login = Login()
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
        try:
            # Parse the given arguments and execute the correct action after checking login
            args = self.parser.parse_args()
            if self.login.check_login(username=args.username, password=args.password):
                args.func(args)
            else:
                print("No user found with that username and password.")
        except AttributeError as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
