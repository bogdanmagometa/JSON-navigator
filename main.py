"""
This module provides functions for navigating through JSON object/file.

To use the implemented functionality, run this module with python in terminal or import and
utilize the implemented functions.
"""

import json
from typing import Union


def ask_json() -> Union[dict, list]:
    """
    Ask user a path to JSON file to navigate it.
    Return a JSON object from file entered by user.
    """

    print("Hello! This is JSON navigator. Please provide us with the path to .json file.")
    path = input("Please, enter a path to the file: ")

    with open(path, 'r') as infile:
        json_obj = json.load(infile)

    return json_obj


def navigate_json(json_obj: Union[list, dict]) -> None:
    """
    Navigate through the specified json_obg, asking the user on each step what index or key to
    choose until there's an empty array, empty object or a non iterable object.
    """

    print()
    if (not isinstance(json_obj, list) and not isinstance(json_obj, dict)) or \
                                            (isinstance(json_obj, dict) and not json_obj) or \
                                            (isinstance(json_obj, list) and not json_obj):
        print("Here's the end value:", json_obj)
    elif isinstance(json_obj, list):
        print(f"This is an array with {len(json_obj)} elements.")
        idx = None
        while not idx:
            try:
                idx = input("Please enter an index of the array: ")
                idx = int(idx)
                navigate_json(json_obj[idx])
            except (ValueError, IndexError):
                idx = None
                print("You should have entered a valid index. Now try again.")

    else:
        print(f"This is a dictionary with {len(json_obj)} pairs. The keys are the following:")
        print(*json_obj.keys(), sep='\n')

        key = None
        while not key:
            try:
                key = input("Please, enter an existing key: ")
                navigate_json(json_obj[key])
            except KeyError:
                key = None
                print("You should have entered an existing key. Now try again.")


if __name__ == "__main__":
    json_obj = ask_json()

    navigate_json(json_obj)
