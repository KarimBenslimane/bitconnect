from user import login
from console.actions import Actions

name_input = str(raw_input("What is your name, trader?\n"))
password_input = login.get_password()
filename_lower = name_input.lower()

if login.check_name(filename_lower):
    # open the file and read the file
    print("Welcome back " + name_input + ".\n")
else:
    # create the file and put in values
    print("Welcome newcomer " + name_input + ".\n")

dead = False
actions = Actions()

while not dead:
    action = str(actions.get_action())
    actions.process_action(action, filename_lower, password_input)

print("Exiting application...")
