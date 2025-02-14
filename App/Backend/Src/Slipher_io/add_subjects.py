def add_subjects(subject_handler):
    """ Handles user input for adding subjects."""
    subject_names = input("Enter subjects (comma-separated):\n> ").split(",")
    subject_names = [s.strip() for s in subject_names if s.strip()]
    if subject_names:
        subject_handler.add_subject(subject_names)
