def delete_topic(topic_handler):
    """Handles user input for deleting a topic."""
    subject = input("Enter subject of the topic to delete:\n> ").strip()
    topic = input("Enter topic to delete:\n> ").strip()
    if subject and topic:
        topic_handler.delete_topic(subject, topic)                                      
