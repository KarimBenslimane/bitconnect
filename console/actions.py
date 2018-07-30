from exchanges import exchangeshelper
from bot import bothelper


class Actions:
    actions = {}

    def __init__(self):
        self.actions = {
            "L": "List your exchanges",
            "E": "Add exchange information",
            "D": "Delete exchange information",
            "B": "Make a new bot",
            "Q": "Quit"
        }

    def get_action(self):
        print("Of the following actions:")
        for key, value in self.actions.iteritems():
            print("(" + key + ") => " + value)
        action_input = str(raw_input("What would you like to do?")).upper()
        if action_input not in list(self.actions.keys()):
            print("[Error] Action not found, try again.\n")
            return self.get_action()
        else:
            return action_input

    def process_action(self, action, filename, password):
        # @todo convert to foreach operation = exchangeshelper.getOperations && operation.getKey = action?
        # @todo ^ Verbeterd leesbaarheid zodra veel operations geimplement worden + dan alleen in exchangeshelper die zooi definieren
        # @todo uitvogelen hoe verschillende exchanges hierin verwerkt kunnen worden.
        # @todo hierin dan ook console/actions verwerken? Beetje gek dat dat nu aparte file waarin het NOG een keer staat
        if action == "E":
            # add exchange
            exchangeshelper.add_exchange(password, filename)
        elif action == "D":
            # remove exchange
            exchangeshelper.remove_exchange(filename)
        elif action == "B":
            # add new bot
            if exchangeshelper.has_exchanges_saved(password, filename):
                bothelper.add_new_bot(password, filename)
            else:
                print("[Error] Please insert exchange(s) information first.\n")
        elif action == "L":
            exchangeshelper.list_exchanges(password, filename)
        elif action == "Q":
            print("Goodbye...\n")
            dead = True
