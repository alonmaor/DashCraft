---
layout: default
title: Final Report 
---


## Video

## Project Summary
The goal of our project was to program our agent, Dashcraft, to find the most optimal path while delivering food. The most optimal path in our problem was defined as the one that returned the greatest reward. Each house Dashcraft could possibly deliver to was assigned an alpha value. Our agent would calculate the best order to visit houses based off these alpha values (since different alpha values would result in different rewards). We used a simple equation to calculate each reward based of its alpha value. Once an agent reached a house, that house's alpha value was multiplied by the agent's current step count. Therefore, in order to maximize its reward, the agent should visit houses with a higher alpha value last. The reasoning behind this is the agent's step count would increase as it visited houses, so visiting a house with a higher alpha value later would allow it to be multiplied by a higher step count, therefore resulting in a higher reward for that delivery. Once our agent figured out the best order to visit houses, it would have the most optimal path since this ordering would result in the highest reward value.
Here's an image of our setup with examples of corresponding alpha values that could be used for each house:
<img src="https://i.imgur.com/XfXKkoB.png">
This problem isn't trivial because there are many possible ways to solve it and the solution can be quite complex. For example, the most optimal path may not always be the that can be found using a greedy algorithm based off the alpha values. The agent isn't able to base its decision purely off the alpha values of each house because there's other factors, such as the length of the path from one house to the next, that affect the reward. Additionally, the lengths of paths between houses is always changing depending on where the agent is in the map. This leaves a great uncertainty in our reward values, since the step count plays a major role in our calculations. Therefore, machine learning, specifically reinforcement learning, is needed to solve our problem. Utilizing a Q-Table makes our problem possible to solve so our agent can converge to finding the most optimal path after every run. 
In the beginning of our training, we let our agent explore the map and try out several possible paths since there was so much uncertainty and it hadn't learned much about its environment. However, as it continued exploring, our goal was for it to consistently choose the most efficient path and obtain the maximum reward at the end of every run.

## Approaches


## Evaluation


## References

  * [David Silver's Lectures on Reinforcement Learning](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html)
  * [Article on Bellman Equation](https://joshgreaves.com/reinforcement-learning/understanding-rl-the-bellman-equations/)
  * [Q-Learning Tutorial](mnemstudio.org/path-finding-q-learning-tutorial.htm)
