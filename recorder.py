# -*- coding: utf-8 -*-
"""
Simulate the recorder and the manager in the Casino.
It can store the rest cards, distribute the cards randomly and record the gambling process.
At last, it shows the winner, how it wins and give us a visualization for a thousand round.
"""
import numpy


class Recorder:
    def __init__(self, next_recorder=None):
        cards = None  # the rest cards in the recorder hands
        next_recorder = next_recorder

    def distribute_card(self):
        pass

    def sentence_winner(self):
        pass

    def make_record(self):
        pass

    def statistics(self):
        pass


class Manager:
    """
    statistic thousands of recorders and show the final report to us
    """
    recorders = Recorder()  # init the Casino, it means the total recorders in is.

    def visualization(self):
        pass
