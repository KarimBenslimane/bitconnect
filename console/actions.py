def get_action_list():
    return ["L", "E", "D", "B", "Q"]


def get_action():
    actions = {
        "L": "List your exchanges",
        "E": "Add exchange information",
        "D": "Delete exchange information",
        "B": "Make a new bot",
        "Q": "Quit"
    }
    print("Of the following actions:")
    for key, value in actions.iteritems():
        print("(" + key + ") => " + value)
    action_input = str(raw_input("What would you like to do?")).upper()
    if action_input not in get_action_list():
        print("[Error] Action not found, try again.\n")
        return get_action()
    else:
        return action_input
