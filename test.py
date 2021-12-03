"""

Welcome to the test program!
This program finds the average number of dice rolls for an ai
The results are shown on a bar chart

"""


import random as rand
from math import e
from colr import color
import numpy as np
import matplotlib.pyplot as plt




print("This program holds the AIs for the game 'pig'")




############## Roll Functions ##############


def random_gen(a):
    ran_num=rand.randint(1,a)
    return ran_num

def roll_dice():
    num=random_gen(7)
    return num
    

def ai_roll(rolls,r):
    
    '''
    This function decides if the ai will roll the dice or not. 
    It uses a exponential decay function to decide the chance of it rolling the dice again
    '''
    
    y=e**(-r*(rolls-10))+10
    num=random_gen(101)
    if y>num:
        #print("The AI decided to roll")
        return "roll"
    else:
        #print("The AI decided to stop rolling")
        return "no"

def ai3_roll(ai_gained,r):
    '''
    This function decides if the ai will roll the dice or not. 
    It uses a exponential decay function to decide the chance of it rolling the dice again
    '''
    
    y=r/(ai_gained+0.01)
    num=random_gen(101)
    if y>num:
        #print("The AI decided to roll")
        return "roll"
    else:
        #print("The AI decided to stop rolling")
        return "no"

def ai5_roll(ai_gained, point_threshold):
    
    if ai_gained <= point_threshold:
        return True
    else:
        return False
    


############## AI Functions ##############

ai1_score = 0
ai3_score = 0
ai5_score = 0


def ai1(r1): #ai1

    '''
    This function calls 2 other functions. It serves as the brain of the AI.
    It adds up the AI score and tells the player if the AI rolled a 1 or chose to stop rolling
    '''
    
    cont=0
    roll=0
    ai1_gain=0
    r=r1
    global roll_current
    while cont!="no":
        cont=ai_roll(roll,r)
        roll+=1
        roll_current=roll_dice()
        if roll_current==1:
            ai1_gain=0
            cont="no"
        else:
            ai1_gain+=roll_current
            if ai1_gain+ai1_score>=100:
                cont="no"
    #if ai1_gain!=0:
        #print("The AI1 rolled {} times".format(roll-1))
    #else:
        #print("The AI1 rolled a 1")
    return ai1_gain



def ai3(r3): #ai3

    '''
    This function calls 2 other functions. It serves as the brain of the AI. 
    It adds up the AI score and tells the player if the AI rolled a 1 or chose to stop rolling
    '''
    cont=0
    roll=0
    ai3_gain=0
    r=r3
    global roll_current
    while cont!="no":
        cont=ai3_roll(ai3_gain,r)
        roll+=1
        roll_current=roll_dice()
        if roll_current==1:
            ai3_gain=0
            cont="no"
        else:
            ai3_gain+=roll_current
            if ai3_gain+ai3_score>=100:
                cont="no"
    #if ai1_gain!=0:
        #print("The AI1 rolled {} times".format(roll-1))
    #else:
        #print("The AI1 rolled a 1")
    return ai3_gain


def ai5(point_threshold):
    
    """
    This version of ai keeps rolling until it brings in a certain number of points
    This number is the variable point_threshold
    point_threshold will adjust when this ai is close to winning
    
    """
    
    global ai5_score
    
    cont = True
    roll = 0
    ai5_gain = 0
    points_to_win = 100 - ai5_score
    
    if points_to_win <= point_threshold:
        point_threshold = points_to_win
    
    while cont == True:
        
        cont = ai5_roll(ai5_gain, point_threshold)
        roll += 1
        roll_current = roll_dice()
            
        if roll_current == 1:
            ai5_gain = 0
            cont = False
        else:
            ai5_gain += roll_current
            
            if ai5_gain + ai5_score >= 100:
                cont = False
    
    return ai5_gain
    




############## Test Functions ##############


def ai1Test(rate = 1.09):
    
    global ai1_score
    ai1_score = 0
    number_of_rounds_1 = 0
    
    while ai1_score <= 100:
        
        ai1_score += ai1(rate)
        
        number_of_rounds_1 += 1


    return number_of_rounds_1

def ai3Test(rate = 150):
    
    global ai3_score
    ai3_score = 0
    number_of_rounds_3 = 0
    
    while ai3_score <= 100:
        
        ai3_score += ai3(rate)
        
        number_of_rounds_3 += 1


    return number_of_rounds_3


def ai5Test(point_threshold = 20):
    
    global ai5_score
    ai5_score = 0
    number_of_rounds_5 = 0
    
    while ai5_score <= 100:
        
        ai5_score += ai5(point_threshold)
        
        number_of_rounds_5 += 1


    return number_of_rounds_5




############## Main Code ##############


data = []
number_of_trials = 10000000

total_rounds_1 = 0   
total_rounds_3 = 0   
total_rounds_5a = 0   
total_rounds_5b = 0

rate_1 = 1.09
rate_3 = 1500
threshold_1 = 20
threshold_2 = 30



for i in range(number_of_trials):

    
    total_rounds_1 += ai1Test(rate_1)
    total_rounds_3 += ai3Test(rate_3)
    total_rounds_5a += ai5Test(threshold_1)
    total_rounds_5b += ai5Test(threshold_2)
    
average_rounds_1 = total_rounds_1 / number_of_trials
average_rounds_3 = total_rounds_3 / number_of_trials
average_rounds_5a = total_rounds_5a / number_of_trials
average_rounds_5b = total_rounds_5b / number_of_trials


data = [average_rounds_1, average_rounds_3, average_rounds_5a, average_rounds_5b]

    
plt.bar(["Ai1", "Ai3", "Ai5 (20)", "Ai5 (30)"], data)
plt.title("The Grand Ai Gauntlet")
plt.ylabel("Avg Number of Rolls")     
  
plt.ylim([8,12])
    
plt.show()
        
