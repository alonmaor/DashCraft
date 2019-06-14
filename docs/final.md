---
layout: default
title: Final Report 
---


## Video
<iframe width="560" height="315" src="https://www.youtube.com/embed/xGej_bth_-Y" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Project Summary
The goal of our project was to program our agent, Dashcraft, to find the most optimal path while delivering food. The most optimal path in our problem was defined as the one that returned the greatest reward. Each house Dashcraft could possibly deliver to was assigned an alpha value. Our agent would calculate the best order to visit houses based off these alpha values (since different alpha values would result in different rewards). We used a simple equation to calculate each reward based of its alpha value. Once an agent reached a house, that house's alpha value was multiplied by the agent's current step count. Therefore, in order to maximize its reward, the agent should visit houses with a higher alpha value last. The reasoning behind this is the agent's step count would increase as it visited houses, so visiting a house with a higher alpha value later would allow it to be multiplied by a higher step count, therefore resulting in a higher reward for that delivery. Once our agent figured out the best order to visit houses, it would have the most optimal path since this ordering would result in the highest reward value.

Here's an image of our setup with examples of corresponding alpha values that could be used for each house:
<img src="https://i.imgur.com/b0cRIEI.png">

This problem isn't trivial because there are many possible ways to solve it and the solution can be quite complex. For example, the most optimal path may not always be the that can be found using a greedy algorithm based off the alpha values. The agent isn't able to base its decision purely off the alpha values of each house because there's other factors, such as the length of the path from one house to the next, that affect the reward. Additionally, the lengths of paths between houses is always changing depending on where the agent is in the map. This leaves a great uncertainty in our reward values, since the step count plays a major role in our calculations. Therefore, machine learning, specifically reinforcement learning, is needed to solve our problem. Utilizing a Q-Table makes our problem possible to solve so our agent can converge to finding the most optimal path after every run. 

In the beginning of our training, we let our agent explore the map and try out several possible paths since there was so much uncertainty and it hadn't learned much about its environment. However, as it continued exploring, our goal was for it to consistently choose the most efficient path and obtain the maximum reward at the end of every run.

## Approaches
In order to manage the states, actions, and their rewards, we used the Q-Learning Reinforcement Learning method. After updating the number of houses from 3 to 6, our state space greatly increased, making our initial implementation unfeasible. In our status report, we thought the ordering of the houses was important, so this was something we kept track of. However, we eventually realized the ordering of the houses has no effect on the state. For this reason, we updated our states to be a frozenset (which is basically the immutable version of a set) rather than tuples, since the keys and states must be immutable in the dictionary. After we made that transition, the state space decreased significantly which made it feasible to use an implementation that was very similar to our inital implementation with a few tweaks, even though we increased the number of houses.

We also updated the way we calculated our rewards. Our new reward equation is shown below:
>reward = alpha_reward[house]*step_count

Each house was assigned a different alpha value which would help calculate the reward given to the agent once it was visited. Initially, we were calculating the reward by multiplying each alpha value by the step count then subtracting this value from 50. However, we realized it made more sense create a more straighforward reward function, which ended up being the product of each alpha value and the step count. Therefore, using this new formula, houses with a higher alpha value should be visited first since they'll be multiplied by a larger number of steps, resulting in a higher reward. Now, instead of having alphas values reflect levels of intolerence, they represent levels of tolerance. In other words, visiting a house with low tolerance in the beginning and high tolerance later would present our agent with a higher reward.

We used Bellman equations like before to choose our action at each state. After monitoring our agent, we found we were still achieving good results even though the state space and number of houses had increased. Every time our agent reached a new state, it evaluated the possible rewards it could gain by choosing a particular action, then chose the action that would maximize its reward. The equation used to calculate the reward for each action is as follows:
><img align="middle" src="https://i.imgur.com/XNl2rQ2.png">
where q = the current state, a = the chosen action, R = the immediate reward, x = the current run, and gamma = discount factor, which determined how much we value future rewards vs. current rewards.

Since our status report, we have found that we may have placed a higher weight than neccessary on future rewards. However, this was a simple fix. Adjusting the gamma value to 0.8, which slightly lowered the weight of future rewards, gave us an optimal result. We also changed the calculation for our epsilon to a different decay algorithm:
>epsilon = initial_epsilon^n

where initial epsilon is 0.995 and n is number of runs thus far. This way our agent is able to explore many paths at first, but later converges down to a few paths and finally to one suboptimal path. We ended up changing our epsilon decay function because we conducted research and found this would produce better results than our initial function, which our results proved to be true.

The advantage of our new approach over the previous approach is big. Earlier we came with the assumption that the agent should come up with the best possible path. But thinking ahead, a better approach would be to try and find a suboptimal path in a reasonable amount of time. If the state space grows significantly, then it would be unreasonable to try and get the optimal path for the agent.

## Evaluation
We first evaluated our project by making sure our agent could navigate a simple map. We used Dijstrak’s shortest path algorithm to ensure our agent could correctly navigate to each house without falling off the map or getting stuck. After this, we implemented a simple version of Q-Learning with only 3 houses. Since there were so few states in our Q-Table, it was easy to see if our agent was consistently choosing the best path every time. We knew our alpha values that would be used to calculate the reward gained from each house. While keeping these values in mind, we would run our agents several times and see if it converged to the best path every time by checking it against these values. Our most optimal path at the time was left house, right house, then middle house. It was clear to see our agent was visiting houses in this order, so we passed this base case and could move on to making our environment more complicated.

Instead of having only 3 houses, we updated our environment to have 6 houses which increased the complexity of our problem and the number of states in our Q-Table.  Again, we assigned alpha values to each house and used these values to calculate the best order to visit houses. While we were running our agent, we printed out the Q-Table every 5 runs and compared these against our expected values.

Here’s an example of our Q-Table after 5 and 10 runs:

<img src="https://i.imgur.com/I7ILiqU.png">

Since our Q-Table printed out the reward at the end of every fifth run, we were able to confirm that our agent was correctly learning better paths and starting to converge as the number of runs increased. 

We also confirmed our algorithm was converging by printing out a graph that mapped the run to the reward:
<img src="https://i.imgur.com/PnMEeFo.png">

As you can see, our graph clearly converged to the highest reward found by the most optimal path as our runs increased since our agent was constantly learning. We were easily able to evaluate our quantitative results by assessing our reward values. Printing out this graph helped us also evaluate our qualitative results, since it showed our agent not only found the highest reward value, but it was also consistently learning since its reward values gradually increased with very few outliers.

These results were achieved through a lot of trial and error relating to the parameters of our Q-learning (such as alpha, gamma, epsilon, etc). Every time we changed a value, we were able to use this as the new basis for our evaluation. We were able to confirm the changes we were making benefited our agent by comparing it to the basis and seeing if the reward values increased or decreased. Tracking these values greatly helped our evaluation and led us to eventually solve our problem and reach our goal. In the end, we were able to train an agent to consistently choose the best path and receive the maximum possible reward value when making deliveries to houses. 

## References

  * [David Silver's Lectures on Reinforcement Learning](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html)
  * [Article on Bellman Equation](https://joshgreaves.com/reinforcement-learning/understanding-rl-the-bellman-equations/)
  * [Q-Learning Tutorial](mnemstudio.org/path-finding-q-learning-tutorial.htm)
