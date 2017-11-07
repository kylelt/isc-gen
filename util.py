
def file_namify(human_friendly_name: str):
    """

    Take a human friendly name and convert it to something
    friendly to an operating system
    (remove garbage punctuation and whitespace)

    :param human_friendly_name: string with garbage
    :return: string without garbage
    """
    return human_friendly_name\
        .lower()\
        .strip()\
        .replace(" ", "-")\
        .replace("(", "")\
        .replace(")", "")\
        .replace("'","")