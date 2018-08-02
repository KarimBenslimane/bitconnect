# Base action which (nearly) all actions should inherit
class BaseAction:
    def __init__(self):
        # Initialize the to be filled variables to None and set default argument flags and description
        self.action = None
        self.func = self.action
        self.flags = [
            ['-u', '--username'],
            ['-p', '--password']
        ]
        self.arguments = [
            {'dest': 'username', 'required': True},
            {'dest': 'password', 'required': True}
        ]

    def init(self, subparser):
        """
        Make sure we have same number of arguments flags and descriptions to prevent crashes
        Add subparser with given action and default function
        Loop through all of the arguments flags and descriptions to add them to parser
        :param subparser:
        :return base_subparser:
        """
        if len(self.flags) != len(self.arguments):
            raise Exception('Unequal number of argument flags and descriptions found')

        base_subparser = subparser.add_parser(self.action)
        base_subparser.set_defaults(func=self.func)

        for i in range(len(self.arguments)):
            base_subparser.add_argument(*(self.flags[i]), **(self.arguments[i]))
        return base_subparser

    def execute(self, args):
        """
        Should be filled by children
        :param args:
        """
        pass

    def ask_confirmation(self):
        """
        Ask for confirmation
        :return bool:
        """
        return input("Are you sure? [Y/n]").lower() == "y"
