""" Open the file invited_names.txt and read the names one by one"""
with open("./Input/Names/invited_names.txt") as names:
    individual_names = names.readlines()  # Reading the names line by line and save it as a list
    # print(individual_names)

    """ Open the file starting_letter.txt and read everything at one shot """
    with open("./Input/Letters/starting_letter.txt") as letter:
        content = letter.read()  # Read the whole file at once
        for name in individual_names:  # Loop through the names saved in the list
            # print(name)
            """ Remove the extra line from the name """
            stripped_name = name.strip()
            replace_name = content.replace("[name],", f"{stripped_name},")  # Replace [name] with the name
            # print(replace_name)

            """ Create the letters with the name and place all the contents from starting_letter.txt """
            with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as result:
                result.write(replace_name)