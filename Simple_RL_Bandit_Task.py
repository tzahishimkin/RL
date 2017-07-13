# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 18:18:50 2017
From:
https://medium.com/@awjuliani/super-simple-reinforcement-learning-tutorial-part-1-fd544fab149

Complete


@author: tzahi
"""

import tensorflow as tf
import numpy as np

bandits = [-1, 2, 4, 5]  #The bandit value defines what value the bandit will return positive value. Thus the lower the value the better
num_of_bandits = len(bandits)

def PullBandit(bandit):
    num = np.random.randn(1)
    if bandit < num:
        return 1
    else:
        return 0
        
tf.reset_default_graph()
#Feed-forward part:
wieghts = tf.Variable(tf.ones(num_of_bandits))
chosen_action = tf.argmax(wieghts,0)