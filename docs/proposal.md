---
layout: default
title: Proposal
---

# {{ page.title }}

### Summary of the Project

Our agent, DashCraft, was just hired by a delivery company. Its goal is to explore the map and make deliveries in the shortest time possible. For each successful delivery, it will receive money as a reward. If it fails to find its destination or is unable to complete a delivery in a given time, the agent will not get paid for that delivery.

The input is the location of a store/place where it picks up goods and the location of the final destination where the goods will be delivered. The agent should find a path and return this path. Eventually, after training, the agent should consistently output the shortest and best path possible.


### AI/ML Algorithms

We plan to use A* search to find the shortest path and Markov reward model and Q-Learning to reward the agent for completing each delivery in the most efficient manner.


### Evaluation Plan

**Quantitative:**
We will evaluate our agent’s performance based on the amount of moves it takes to deliver the food, the quality of the path (such as dirt road or a paved trail), whether it was successful in delivering it, or whether it fell into lava/a pit. The baseline for our agent will be completing each delivery, even if it’s not done in the most efficient way possible. We expect our approach to improve from just completing each delivery to completing each delivery in the shortest amount of time using the best path. We will use Markov reward process in order to rate these different states and the total cost of the path. The agent will then try to optimize its path using the reward system. The data we will evaluate on is the path returned by the agent. We’ll compare it to the shortest path we’ve calculated for each delivery. We’ll also examine the different types of blocks in the path to see if they’re optimal.

**Qualitative:**
Sanity cases for the approach are making sure our agent is able to find its way around the map successfully without falling into any traps and checking to see if our agent is able to consistently find its start and end destinations. We'll visualize the internals of the algorithm by drawing out Markov chains to make sure our agent is correctly rewarded. We'll also create customized instances of maps in which we know the optimal paths so we can use these for testing. We'll compare this known path to the path chosen by our agent and reward the agent for each block it chooses correctly. We'll also reward our agent for each successful delivery. Our moonshoot case is our agent completing every delivery in the shortest time possible using the most optimal path, even if it's put in a new map it hasn't learned yet. If it's not able to find the optimal path right away in a new environment, we hope it'll be able to quickly learn about this environment and optimize based of this information.


### Appointment with the Instructor

**Date:** Monday, April 22, 2019

**Time:** 10:15 AM
