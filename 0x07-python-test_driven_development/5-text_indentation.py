#!/usr/bin/python3
"""

This module contains a function that indents texts
at the occurence of certain characters(., ?, :)

"""


def text_indentation(text):
    '''This function prints a text with 2 new lines after each of ".", "?", and ":"
    that appears in the text.

    Args:
        text (str): The string to be printed. It could be multiline

    Raises:
        TypeError: If text is not a string

    '''

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = text
    for c in ".:?":
        new_text = new_text.replace(c, f"{c}\n\n")
    text_to_list = new_text.splitlines(keepends=True)
    space_removed = [t.strip(' \t') for t in text_to_list]
    final_text = [("<BLANKLINE>" + t if t.isspace() else t) for t in space_removed]
    text = "".join(final_text)
    print(text)
