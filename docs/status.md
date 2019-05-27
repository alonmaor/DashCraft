---
layout: default
title: Status
---

## Project Summary

Our agent, Dashcraft, must deliver food to houses in the most efficient way possible. To do so, it must evaluate the different paths it can take and the different rewards that will result from these combinations of paths. In the beginning, our agent will explore the map and try out different paths, learning which are better along the way. Our goal is for our agent to consistently choose the most efficient path in order to obtain the maximum reward at the end of every run.

<img src="game.jpg">

## Approach

We used reinforcement learning to train our agent. We utilized a Q-Table to keep track of our states, actions, and rewards. Our space consisted of 4 states (three houses and the base location) and 4 actions (travel to each of the three houses or return to the base location). Each house had a different alpha value which would help calculate the reward given once it was visited. The rewards would be calculated by multiplying each alpha value by the number of steps our agent has taken then subtracting this value from 50. Therefore, using this formula, houses with a higher alpha value should be visited first since they'll be multiplied by a smaller number of steps, resulting in a higher reward. Additionally, the agent should combine that decision with the path taken to minimize the amount of total steps at the end of each run.

We also evaluated and adjusted the parameters used for our Q-Table in order to optimize our agent's performance. We made our alpha value (aka learning rate) 0.3 so our agent wouldn't converge too slow and also wouldn't overshoot the minimum. We also made our gamma 1 so future rewards would have more weight since we could train our agent for many iterations and didn't focus as much on immediate results. For our epsilon value, we implemented epsilon decay based on the maximum step count of our agent. We started our epsilon value at 1 so our agent would have the chance to explore the map, then decreased it as the agent's step count started to increase. Therefore, our agent would begin to explore less and make more intelligent decisions the closer it got to the end of its runs.

We used the Bellman equations to choose our action at each state. Every time our agent reached a new state, it evaluated the possible rewards it could gain by choosing a particular action, then chose the action with the maximum reward. The equation used to calculate the reward for each action is as follows:
<img align="middle" src="https://i.imgur.com/XNl2rQ2.png">
where q = the current state, a = the chosen action, R = the immediate reward, x = the current run, and gamma = how much we value future rewards vs. current rewards.

After considering all these factors, this was our final algorithm:
1. create and initialize all variables, parameters, and rewards 
2. randomly select the initial state
3. choose next action either based off randomness or maximum reward from this action (determined by epsilon)
4. update q-table based off chosen action and remaining possible states
5. update current state to be chosen state
6. repeat steps 3-6 if the list of possible actions isn't empty

## Evaluation

We evaluated our agent by first making sure it passed our sanity cases. None of us have working in the Malmo environment before, so it took some time to get used to. Once we created a simple enviroment, we just had our agent navigate to each of the houses using our shortest path algorithm. After our agent was able to complete this task successfully, we implemented Q-Learning.

Once we implemented a basic Q-Learning algorithm, we made sure it was actually calculating and updating values. We were able to check this by printing out our Q-Table during every run. We compared the values it was calculating against our expected values. Since our expected values could be calculated using a fairly simple math equation (50 - alpha * step count), this wasn't too difficult to be evaluate. 
Example of Q-Table and rewards being printed during every run:
<img align="middle" src="https://i.imgur.com/VKrENK8.png">

Based off the alpha values we created for each house, we knew the most optimal path was left house, right house, middle house. As we watched our agent complete its runs, we would note how long it took to consistently take this path. Originally, it would take many runs before it would take this path multiple times in the row. Even at this point, it'd still occasionally take a less optimal path. Although this wasn't the ideal situation, it brought us closer to our end goal. Eventually, after adjusting many parameters, our agent started to converge to the correct solution much quicker. 
Graph of policy rewards for each run during training:
<img src="https://cdn.discordapp.com/attachments/576232242750291970/582376049489215522/Figure_1.png">

For our final evalution, we let our agent complete several runs. While this was happening, we observed it to make sure it consistently chose the most optimal path once it learned which produced the highest reward. Our agent performed well and produced results that were accurate to what we expected, which concluded our status report evalution. We'll complete similar evalutions in the future once we add more features to our agent and its environment.

## Remaining Goals and Challenges

Our prototype at the moment is limited because it consists of a small environment. There are only four states and actions, which doesn't give our agent a lot of information to evaluate when making decisions. The way rewards are calculated right now is also fairly simple. Each state has a specific value that is directly used to calculate rewards. Instead of this, we plan on adding conditions that alter the way rewards are calculated. For example, visiting house 1 before houses 2 and 3 could make the reward gained from house 1 larger than visiting house 1 in a different order.

Some of our next goals if time permits:
  * Make the decision process more complex - possibly with deep neural network
  * Expand the environment and add more houses
  * Add a feature where agent has to return to origin to "refuel"
    - Decrease its hearts after every delivery to track how much fuel is remaining
    - Hearts recharge after agent returns to "distribution center" at origin
  * Make the environment more interesting by adding roads, obstacles, and more
  * Add conditionals and factors that affect our agent’s decision making
  * Adjust parameters so DashCraft can find the most optimal path sooner and more consistently
  
Expected Challenges:
  * An environment too large could make the decision process inefficient
  * Obstacles could make shortest path problem much harder
  * Must figure out how to control agent's heart count
  
## Resources Used
  * [David Silver's Lectures on Reinforcement Learning](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html)
  * [Article on Bellman Equation](https://joshgreaves.com/reinforcement-learning/understanding-rl-the-bellman-equations/)
  * [Q-Learning Tutorial](mnemstudio.org/path-finding-q-learning-tutorial.htm)
  
  
## VIDEO

[![](http://img.youtube.com/vi/Dm4Q7a0MgqM/0.jpg)](http://www.youtube.com/watch?v=Dm4Q7a0MgqM "Status Report - DashCraft")

