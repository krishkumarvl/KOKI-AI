# brain/preprocess.py

WAKE_WORDS = [
    "koki",
    "hey koki",
    "hi koki",
    "hello koki",
]


def normalize_message(message):
    """
    Removes wake words and cleans the user's input.
    """

    message = message.lower().strip()

    for wake_word in sorted(WAKE_WORDS, key=len, reverse=True):
        if message.startswith(wake_word):
            message = message[len(wake_word):].strip(" ,.!?")
            break

    return message