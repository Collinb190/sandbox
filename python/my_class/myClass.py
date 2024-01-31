#!/usr/bin/python3
"""This module will define my function"""


class User:
    """
    This class will define users
    """
    def __init__(self, game_tag) -> None:
        self.name = game_tag
        self.points = 0

    def display_user_info(self):
        """Displays the users information"""
        print(f"Name: {self.name}\nScore: {self.points}")

if __name__ == "__main__":
    player_1 = User("Elden Lord")
    player_1.display_user_info()
