# TODO 1: Pull Wedding Invitation Text

#  Completed : File Path => /Input/Letters/wedding_invitation_text.txt

# TODO 2: Generate Invitees List

#  Completed : File Path => /Input/Names/invited_names.txt

# TODO 3: Prepare a Personalized Wedding Invitation


# Accesses the text of the wedding invitation

with open("./input/Letters/wedding_invitation_text.txt") as file:
    doc = file.read()
    text = doc

# Accesses the invited names file

with open("./input/Names/invited_names.txt") as file:
    name = file.read()
    name = name.replace(" ", '')
    names = name.replace('\n', ' ')

    list_of_names = names.split()

# Prepares Personalized Wedding Invitation

for i in list_of_names:
    with open(f"./Output/ReadyToSend/.{i}.txt", mode="w") as file:
        file.write(text)

    with open(f"./Output/ReadyToSend/.{i}.txt", mode="w") as file:
        file.write(text.replace("[name]", f"{i}"))

