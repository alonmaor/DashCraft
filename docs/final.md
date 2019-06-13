---
layout: default
title: Final Report 
---


## Video

## Project Summary
The goal of our project was to program our agent, Dashcraft, to find the most optimal path while delivering food. The most optimal path in our problem was defined as the one that returned the greatest reward. Each house Dashcraft could possibly deliver to was assigned an alpha value. Our agent would calculate the best order to visit houses based off these alpha values (since different alpha values would result in different rewards). We used a simple equation to calculate each reward based of its alpha value. Once an agent reached a house, that house's alpha value was multiplied by the agent's current step count. Therefore, in order to maximize its reward, the agent should visit houses with a higher alpha value last. The reasoning behind this is the agent's step count would increase as it visited houses, so visiting a house with a higher alpha value later would allow it to be multiplied by a higher step count, therefore resulting in a higher reward for that delivery. Once our agent figured out the best order to visit houses, it would have the most optimal path since this ordering would result in the highest reward value.

Here's an image of our setup with examples of corresponding alpha values that could be used for each house:
<img src="https://i.imgur.com/SeRB4tS.png">

This problem isn't trivial because there are many possible ways to solve it and the solution can be quite complex. For example, the most optimal path may not always be the that can be found using a greedy algorithm based off the alpha values. The agent isn't able to base its decision purely off the alpha values of each house because there's other factors, such as the length of the path from one house to the next, that affect the reward. Additionally, the lengths of paths between houses is always changing depending on where the agent is in the map. This leaves a great uncertainty in our reward values, since the step count plays a major role in our calculations. Therefore, machine learning, specifically reinforcement learning, is needed to solve our problem. Utilizing a Q-Table makes our problem possible to solve so our agent can converge to finding the most optimal path after every run. 

In the beginning of our training, we let our agent explore the map and try out several possible paths since there was so much uncertainty and it hadn't learned much about its environment. However, as it continued exploring, our goal was for it to consistently choose the most efficient path and obtain the maximum reward at the end of every run.

## Approaches


## Evaluation
We first evaluated our project by making sure our agent could navigate a simple map. We used Dijstrak’s shortest path algorithms to ensure our agent could correctly navigate to each house without falling off the map or getting stuck. After this, we implemented a simple version of Q-Learning with only 3 houses. Since there were so few states in our Q-Table, it was easy to see if our agent was consistently choosing the best path every time. We knew our alpha values that would be used to calculate the reward gained from each house. While keeping these values in mind, we would run our agents several times and check to see if it converged to the best path every time by checking it against these values. Our most optimal path at the time was left house, right house, then middle house. It was clear to see our agent was visiting houses in this order, so we passed this base cases and could move on to making our environment more complicated.

Instead of having only 3 houses, we updated our environment to have 6 houses which increased the complexity of our problem and the number of states in our Q-Table.  Again, we assigned alpha values to each house and used these values to calculate the best order to visit houses. While we were running our agent, we printed out the Q-Table every 5 runs and compared these against our expected values.

Here’s an example of our Q-Table after 5 and 10 runs:
<img src="https://i.imgur.com/WA4eGoy.png">

Since our Q-Table printed out the reward at the end of every fifth run, we were able to confirm that our agent was correctly learning better paths and starting to converge as the number of runs increased. 

We also confirmed our algorithm was converging by printing out a graph that mapped the run to the reward:
<img src="https://i.imgur.com/PnMEeFo.png">

As you can see, our graph clearly converged to the highest reward found by the most optimal path as our runs increased and our agents continued to learn.



## References

  * [David Silver's Lectures on Reinforcement Learning](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html)
  * [Article on Bellman Equation](https://joshgreaves.com/reinforcement-learning/understanding-rl-the-bellman-equations/)
  * [Q-Learning Tutorial](mnemstudio.org/path-finding-q-learning-tutorial.htm)
