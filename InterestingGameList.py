# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 16:12:51 2017

@author: tzahi
"""

import gym
env = gym.make('SpaceInvaders-v0')
env.reset()
env.render()

env = gym.make('Go9x9-v0')
env.reset()
env.render()

env = gym.make('CartPole-v0')
env.reset()
env.render()

#Install MujoCo!
env = gym.make('Humanoid-v1')
env.reset()
env.render()