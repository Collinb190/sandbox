#!/usr/bin/python3
"""This module will define my function"""


class User:
    """
    This class will define users
    """
    def __init__(self, full_name) -> None:
        self.name = full_name
        self.points = 0

    def display_user_info(self):
        """Displays the users information"""
        print(f"Name: {self.name}\nScore: {self.points}")

player_1 = User("Gamer_Tag")
player_1.display_user_info()
