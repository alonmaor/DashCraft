---
layout: default
title: Status
---

## Project Summary

Our agent, Dashcraft, must deliver pizzas to houses in the most efficient way possible. To do so, it must evaluate the different paths it can take and the different rewards that will result from these combinations of paths. In the beginning, our agent will explore the map and try out different paths. Our goal is for our agent to consistently choose the most efficient path in order to obtain the maximum reward at the end of every run.

## Approach

We used reinforcement learning to train our agent. We utilized a q-table to keep track of our states, actions, and rewards. Our space consisted of 4 states (three houses and the base location) and 4 actions (travel to each of the three houses or the base location). Each house had a different alpha value which would help calculate the reward given once it was visited. The rewards would be calculated by multiplying each alpha value by the number of steps our agent has taken then subtracting this value from 100. Therefore, using this formula, houses with a higher alpha value should be visited first since they'll be multiplied by a small number of steps, resulting in a higher reward. 
We also evaluated and adjusted the parameters used for our q-table in order to optimize our agent's performance. We made our alpha value (aka learning rate) 0.3 so our agent wouldn't converge too slow and alos wouldn't overshoot the minimum. We also made our gamma 1 so future rewards would have more weight since we could train our agent for many iterations and didn't focus as much on immediate results. For our epsilon value, we implement epsilon decay based on the maximum step count of our agent. We started our epsilon value at 1 so our agent would have the chance to explore the map, the decreased it as the agent's step count started to increase. Therefore, our agent would begin to explore less and make more intelligent decisions the closer it got to the end of its run.

## Remaining Goals and Challenges


## VIDEO

