#!/usr/bin/python3
def text_indentation(text):
    i = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    while i < len(text):
        char = text[i]
        if char == " " and text[i + 1] == " ":
            i = i + 1
        elif char == "." or char == "?" or char ==":":
            print(char, end="")
            print("\n")
            i = i + 1 
        else:
            print(char, end="")
        i = i + 1
