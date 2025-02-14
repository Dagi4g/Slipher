def edit_subject(subject_handler):
    """ Handles user input for editing subject."""
    prompt = "Enter subject to rename:(\"q\" to quit)\n> "
    while True:
        existing_subject = input(prompt)
        if existing_subject.lower() == "q":
            break

        if subject_handler._check_subject(existing_subject):
            prompt = f"Enter the new name for\"{existing_subject}\":\n>"
            new_subject = input(prompt)
            if not subject_handler._check_subject(new_subject):
                subject_handler.edit_subject(existing_subject,new_subject)
                choice = input("Do you want to edit another subject(press enter) or quit(q): ")
                if choice.lower() == "q":
                    prompt = "Enter subject to rename:(\"q\" to quit)\n> " # Insure that the prompt is the original before quiting.
                    break
                else:
                    prompt = "Enter subject to rename:(\"q\" to quit)\n> " # Insure that the prompt is the original before quiting.
                    continue
            else:
                print(f"subject: '{new_subject}' already exists")
                choice = input("Do you want to add another name(press enter) or quit(q): ")
                if choice.lower() == "q":
                    prompt = "Enter subject to rename:(\"q\" to quit)\n> " # Insure that the prompt is the original before quiting.
                    break
                else:
                    prompt = "Please Enter subject name that doesn't exist:(\"q\" to quit)\n> " # Adabt the prompt.
                    continue
        else:
            print(f"subject: '{existing_subject}' doesn't exists")
            choice = input("Do you want to edit another subject(press enter) or quit(q): ")
            if choice.lower() == "q":
                prompt = "Enter subject to rename:(\"q\" to quit)\n> " # Insure that the prompt is the original before quiting.
                break
            else:
                prompt =  "Please existing subject(\"q\" to quit):\n> "
                continue

