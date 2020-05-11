import random
import numpy as np
import matplotlib.pyplot as plt
import math

class Person:
    # initialize person w/Name and starting weight
    def __init__(self, name_, init_weight):
        self.name = name_
        self.weight = init_weight
        self.inter_weights = [init_weight]
        self.losing_weight = False

    # runs simulation on number of weeks of calorie surplus/deficit
    def simulate_n_weeks(self, n, _extra_cal_per_day=0):
        '''
        Simulates extra calorie intake over n weeks
        :param n: number of weeks
        :param _extra_cal_per_day: extra calories/day
        :return: end weight at the end of simulation
        '''
        if _extra_cal_per_day < 0:
            self.losing_weight = True
        fat_poundage = 0 # 3500 extra cals is a pound of fat
        for week in range(n):
            week_extra_cals = []
            for day in range(8):
                week_extra_cals.append(_extra_cal_per_day + random.randint(-350, 350))
            fat_poundage += sum(week_extra_cals)/3500
            self.inter_weights.append(self.weight+fat_poundage)
        self.weight += fat_poundage
        return self.weight




    # get weight function
    def get_weight(self):
        '''returns current weight of the person'''
        return self.weight
    # returns String of weight of the person

    def create_plot(self, one_point=False):

        x = np.arange(0, len(self.inter_weights), 1)
        y = self.inter_weights
        print("x: ", x)
        print("y: ", y)
        plt.xlabel("time in weeks")
        plt.ylabel("weight")
        if self.losing_weight:
            plt.plot(x, y, 'g', label="projected weight loss", linewidth=2, linestyle="dashed")
        else:
            plt.plot(x, y, 'r', label="projected weight gain", linewidth=2, linestyle="dashed")
        ax = plt.gca()
        # ax.set_facecolor('#42b3f5')

        plt.axis('equal')
        plt.show()


    # graphs the simulation using NumPy
    def graph_sim(self):
        if len(self.inter_weights) == 1:
            self.create_plot(True)
        else:
            self.create_plot()

if __name__ == "__main__":
    p1 = Person("Person 1", 180)

    print(p1.simulate_n_weeks(3, 250))

    p1.graph_sim()

