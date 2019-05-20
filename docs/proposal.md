---
layout: default
title: Proposal
---

# {{ page.title }}

### Summary of the Project

Our agent, DashCraft, was just hired by a delivery company. Its goal is to try to maximize its profits. For each successful delivery, it will receive a tip as a reward. For each house the agent delivers to there is a certain reward, determined by the time it took and how tolerant the customers are. In order to maximize profit, DashCraft would need to find the best combination and order of houses to deliver to.

The input for our agent would be a set of houses represented as x,y coordinates which the agent would need to pick from. Our agent will then output its choice and navigate to that house using Dijkstra's Algorithm. Additionally, the agent has to return to the distribution center in order to refuel and pick up more orders to deliver. If the agent fails to do so, it will run out of gas and will receive a reward of negative infinity. Eventually, after training, the agent should consistently pick the houses in an order that would yield the best profits/rewards while making sure the fuel tank is never empty. In game, fuel will be represented as hearts for the agent.


### AI/ML Algorithms

We plan to use Dijkstra's Algorithm to find the shortest path from the distribution center to each house. We'll also use Q-Learning to compute the reward for the agent for completing each delivery, according to the time and an alpha variable representing the tolerance of the residents.


### Evaluation Plan

**Quantitative:**
We will evaluate our agent’s performance based on how it optimizes its rewards from run to run. The baseline for our agent will be completing each delivery, even if it’s not done in the most efficient way possible. We expect our approach to improve from just completing all the deliveries and having enough fuel to actually completing its missions with the most optimal reward. We will evaluate the path from each house to another by distance and use that as the time variable when assessing the reward. We'll also evaluate the reward the agent receives from each customer it delivers to. The agent will then try to optimize its path using the reward system, which is based on Markov Reward Process.

**Qualitative:**
Sanity cases for the approach are making sure our agent is able to find its way around a small map successfully with a few house, and checking to see if our agent is able to consistently find the optimal path. We'll visualize the internals of the algorithm by drawing out Markov chains to make sure our agent is correctly rewarded. We'll also create customized instances of maps with simple rewards system in which we know the optimal paths so we can use these for testing. We'll compare this known path to the path chosen by our agent and reward the agent for each house it chooses correctly. We'll also reward our agent for each successful delivery. Our moonshoot case is our agent consistently completing all the deliveries using the most optimal path, even in a very large environment.


### Appointment with the Instructor

**Date:** Monday, April 22, 2019

**Time:** 10:15 AM
