# -*- coding: utf-8 -*-
"""
All the possible strategies writing here.
Keep the strategies as the players in the Casino,
each class stores the cards and calculates out their decisions for the next step.
"""

import random


class Strategy1:
    """
    make decision randomly
    """

    def __init__(self):
        self.card = []
        self.score = 0
        self.last_step=0

    def distribution(self, new_card):
        self.card.append(new_card)
        self.last_step=self.score
        if new_card >= 10:
            new_card = 10
        self.score += new_card

    def is_boom(self):
        """
        check the card in player's hand is bigger than 21
        :return:
        """
        if self.score > 21:
            return True

    def make_decision(self):
        """
        randomly make the decision whether keep on asking for new cards
        :return:
        """
        decision = random.random()
        if decision > 0.5:
            return True
        else:
            return False


class Strategy2:
    cards = None  # written as a list

    def functions1(self):
        pass

    def functions2(self):
        pass
