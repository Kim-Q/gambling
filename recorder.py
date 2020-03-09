# -*- coding: utf-8 -*-
"""
Simulate the recorder and the manager in the Casino.
It can store the rest cards, distribute the cards randomly and record the gambling process.
At last, it shows the winner, how it wins and give us a visualization for a thousand round.
"""
from strategy import Strategy1
import random
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator


class Recorder:
    def __init__(self, player_num):
        self.card = []
        self.score = 0
        self.cards = []
        self.last_card = 13 * 4 * 4
        for i in range(13):
            self.cards.append(4 * 4)
        self.last_step = 0
        self.next = None
        self.player_num = player_num
        self.player = []  # player number
        for i in range(self.player_num):
            new_player = Strategy1()
            self.player.append(new_player)

    def distribution(self, new_card):
        self.card.append(new_card)
        if new_card >= 10:
            new_card = 10
        self.score += new_card

    def take_card(self):
        temp_card = random.randrange(1, 14, 1)
        while self.cards[temp_card - 1] <= 0 < self.last_card:
            temp_card = random.randrange(1, 14, 1)
        self.cards[temp_card - 1] -= 1
        self.last_card -= 1
        return temp_card

    def check_score(self):
        if 1 in self.card and self.score + 10 <= 21:
            return self.score + 10
        else:
            return self.score

    def is_boom(self):
        if self.score > 21:
            return True

    def play1(self):
        """
        simply statistic the last step scores of single players and record them
        """
        # step 1: distribute the first two cards to each players
        for i in range(self.player_num):
            for j in range(2):
                self.player[i].distribution(self.take_card())
                self.distribution(self.take_card())
        # step 2: begin the playing rounds
        finished = False
        while not finished:
            for i in range(self.player_num):
                # the player continue take the card
                if self.player[i].make_decision():
                    self.player[i].distribution(self.take_card())
                    # distribute card to the recorder
                    self.distribution(self.take_card())
                    # Situation 1: the player has right 21 points
                    finished = (self.player[i].check_the_score() == 21)
                    if finished is True:
                        self.last_step = self.player[i].last_step
                        print(self.last_step, "1")
                        # print("wow")
                        break
                    # Situation 2: the player booms during the game, the last step is 0
                    finished = self.player[i].is_boom()
                    if finished is True:
                        # self.last_step = 0
                        # print("bad decision")
                        break
                    # situation 3: the recorder has right 21 points
                    finished = (self.check_score() == 21)
                    if finished is True:
                        # self.last_step = 0
                        break
                    # Situation 4: the recorder booms during the game, the last step is 0
                    finished = self.is_boom()
                    if finished is True:
                        self.last_step = self.player[i].last_step
                        print(self.last_step, "2")
                        # print("good decision")
                        break
                # the player refuse to take the card
                else:
                    # self.last_step = 0
                    # if self.player[i].check_score() is None or self.check_score() is None:
                    #     self.last_step = 0
                    # print(self.player[i].check_the_score(),self.check_score())
                    # print(self.player[i].card,self.player[i].score)
                    if self.player[i].check_the_score() > self.check_score() and len(self.card) > 2:
                        if self.player[i].card[-1] is not 1:
                            self.last_step = self.player[i].check_the_score() - self.player[i].card[-1]
                            print(self.last_step, "3")
                        else:
                            if self.player[i].check_the_score() - 11 <= 10:
                                self.last_step = self.player[i].check_the_score() - 11
                                print(self.last_step, "4")
                            else:
                                self.last_step = self.player[i].check_the_score() - 1
                                print(self.last_step, "5")
                    else:
                        self.last_step = 0
                    finished = True
                    break

    def make_record(self):
        return self.last_step


class Manager:
    """
    statistic thousands of recorders and show the final report to us
    """

    def __init__(self, table_num):
        self.max_len = table_num
        self.results = []
        for i in range(21):
            self.results.append(0)

    def open1(self):
        """
        the Casino opens and thousands of tables begin to work
        :return:
        """
        for i in range(self.max_len):
            recorder = Recorder(1)
            recorder.play1()
            self.results[recorder.make_record()] += 1

    def statistic(self):
        """
        manager statistic the result and give a visualization
        :return:
        """
        # print(self.results)
        self.results[0] = 0
        sum_frequency = sum(self.results)
        # print(sum_frequency)
        print(sum_frequency / self.max_len)
        for i in range(21):
            self.results[i] = self.results[i] / sum_frequency
        print(self.results)
        x_values = list(range(21))
        plt.figure(figsize=(8, 6))
        x_major_locator = MultipleLocator(1)
        ax = plt.gca()
        ax.xaxis.set_major_locator(x_major_locator)
        plt.plot(x_values, self.results)
        plt.title('No.1 game result')
        plt.xlim(0, 21, 1)
        plt.ylim(0, 0.3)
        plt.xlabel('last step')
        plt.ylabel('frequency times')
        # plt.show()
        plt.savefig("game1.png")


if __name__ == "__main__":
    # test whether the recorder is correct
    # for i in range(1000):
    #     test = Recorder(1)
    #     test.play1()
    #     print(test.make_record())
    # test whether the Manager is correct and the stability of chain
    test = Manager(500000)
    test.open1()
    test.statistic()
