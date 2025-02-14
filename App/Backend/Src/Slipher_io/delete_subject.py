def delete_subject(subject_handler):
    """Handles user input for deleting a subject."""
    subject = input("Enter subject to delete:\n> ").strip()
    if subject:
        subject_handler.delete_subject(subject)
