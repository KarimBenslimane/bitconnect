# Base action which (nearly) all actions should inherit
class BaseAction:
    def __init__(self):
        # Initialize the to be filled variables to None and set default argument flags and description
        self.action = None
        self.func = self.action
        self.flags = [
            ['-p', '--password'],
            ['-u', '--username']
        ]
        self.arguments = [
            {'dest': 'password', 'required': True},
            {'dest': 'username', 'required': True}
        ]

    def init(self, subparser):
        # Make sure we have same number of arguments flags and descriptions to prevent crashes
        if len(self.flags) != len(self.arguments):
            raise Exception('Unequal number of argument flags and descriptions found')

        # Add subparser with given action and default function
        base_subparser = subparser.add_parser(self.action)
        base_subparser.set_defaults(func=self.func)

        # Loop through all of the arguments flags and descriptions to add them to parser
        for i in range(len(self.arguments)):
            base_subparser.add_argument(*(self.flags[i]), **(self.arguments[i]))
        return base_subparser

    # Should be filled by children
    def execute(self, args):
        pass
