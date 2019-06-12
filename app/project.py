# from future import standard_library
# standard_library.install_aliases()
# from builtins import range
# from builtins import object
import MalmoPython
import json
import logging
import os
import random
import sys
import time
import numpy
import matplotlib.pyplot as plt
from collections import defaultdict, deque
from priority_dict import priorityDictionary as PQ


class DashAgent(object):
    """Dash craft agent for learning best deliveries"""
    def __init__(self, destinations):
        self.epsilon = 1
        self.epsilon_decay = 0.995
        self.epsilon_min = 0.02
        self.n = 1
        self.gamma = 1
        self.alpha = 1
        self.rewards_map = {}
        self.alpha_reward = {210: 0.5, 409: 0.7, 167: 0.2, 178: 0.9, 418: 0.5, 399: 0.5}
        self.q_table = {}
        self.current_state = ()
        self.step_count = 0 # time
        self.current_location = 0
        self.mission_number = 0
        self.items = ['cooked_porkchop','cooked_fish','cake','cooked_chicken','cooked_beef']

        self.possible_actions = destinations
        self.grid = []

        

    def run(self, agent_host):
        start = 0
        world_state = agent_host.getWorldState()
        self.grid = self.get_grid(world_state, agent_host)
        S, A, R = deque(), deque(), deque()
        present_reward = 0
        done_update = False
        while not done_update:
            a0 = self.choose_action(self.current_state, self.possible_actions, self.epsilon, self.mission_number)
            S.append(self.current_state)
            A.append(a0)
            R.append(0)

            T = sys.maxsize
            for t in range(sys.maxsize):
                # print(self.q_table)
                time.sleep(0.1)
                if t < T:
                    current_r = self.act(self.current_location, A[-1], self.grid)
                    self.possible_actions.remove(A[-1])
                    R.append(current_r)

                    if len(self.possible_actions) == 0:
                        # Terminating state
                        T = t + 1
                        # present_reward = current_r
                        # print("Reward:", present_reward)
                    else:
                        s = self.current_state
                        S.append(s)
                        possible_actions = self.possible_actions
                        next_a = self.choose_action(s, possible_actions, self.epsilon, self.mission_number)
                        A.append(next_a)

                tau = t - self.n + 1
                if tau >= 0:
                    self.update_q_table(tau, S, A, R, T)

                if tau == T - 1:
                    while len(S) > 1:
                        tau = tau + 1
                        self.update_q_table(tau, S, A, R, T)
                    done_update = True
                    self.act(self.current_location, 0, self.grid)
                    break

    def act(self, source, dest, grid):
        path = self.get_shortest_path(grid, source, dest)
        action_list = self.extract_action_list_from_path(path)
        self.step_count += len(action_list)
        self.execute_actions(agent_host, world_state, action_list)
        self.current_location = dest
        if dest == 0:
            return 0
        self.current_state += (dest,)
        return 30 - self.alpha_reward[dest]*self.step_count

    def execute_actions(self, agent_host, world_state, action_list):
        action_index = 0
        #while world_state.is_mission_running:
        for action_index in range(len(action_list)):
            time.sleep(0.1)

            agent_host.sendCommand(action_list[action_index])
            action_index += 1
            if len(action_list) == action_index:
                time.sleep(2)
            world_state = agent_host.getWorldState()
            for error in world_state.errors:
                print("Error:",error.text)


    def extract_action_list_from_path(self, path_list):
        action_trans = {-21: "movenorth 1", 21: "movesouth 1", -1: "movewest 1", 1: "moveeast 1"}
        alist = []
        for i in range(len(path_list) - 1):
            curr_block, next_block = path_list[i:(i + 2)]
            alist.append(action_trans[next_block - curr_block])

        return alist

    def init_pq(self, grid, pq):
        for i, block in enumerate(grid):
            if block == 'air' or block == 'wooden_door':
                pq[i] = float("inf")

    def get_shortest_path(self, grid_obs, source, dest):
        print(grid_obs)
        q = PQ()
        self.init_pq(grid_obs, q)
        q[source] = 0
        prev = dict()
        dist = q.copy()
        [prev.update({key:None}) for key in q.keys()]

        for node in q:
            #neighbors = [node-21,node-1,node+1,node+21]
            neighbors = []
            if node not in range(0,21) and grid_obs[node-21] in ['air','wooden_door','tallgrass','double_plant']:
                neighbors.append(node-21)
            if (node + 1) % 21 != 0 and grid_obs[node+1] in ['air','wooden_door','tallgrass','double_plant']:
                neighbors.append(node+1)
            if node % 21 != 0 and grid_obs[node-1] in ['air','wooden_door','tallgrass','double_plant']:
                neighbors.append(node-1)
            if node not in range(420, 441) and grid_obs[node+21] in ['air','wooden_door','tallgrass','double_plant']:
                neighbors.append(node+21)
            for n in neighbors:
                alt = 0
                if n in dist:
                    alt = dist[node] + 1
                    if alt < dist[n]:
                        dist[n] = alt
                        prev[n] = node
                        q[n] = alt

        path_list = [dest]
        last = dest
        while last != source:
            path_list = [prev[last]] + path_list
            last = prev[last]

        return path_list

    def get_grid(self, world_state, agent_host):
        grid = []
        while world_state.is_mission_running:
            time.sleep(0.1)
            world_state = agent_host.getWorldState()
            if len(world_state.errors) > 0:
                raise AssertionError('Could not load grid.')

            if world_state.number_of_observations_since_last_state > 0:
                msg = world_state.observations[-1].text
                observations = json.loads(msg)
                grid = observations.get(u'floorAll', 0)
                break
        return grid

    def choose_action(self, curr_state, possible_actions, eps, mission_number):
        if curr_state not in self.q_table:
            self.q_table[curr_state] = {}
        for action in possible_actions:
            if action not in self.q_table[curr_state]:
                self.q_table[curr_state][action] = 0

        if len(possible_actions) == 3 and mission_number != 0 and (mission_number % 5 == 0):
            print("eps = ", self.epsilon)
            if self.epsilon > self.epsilon_min:
                self.epsilon *= self.epsilon_decay

        choice = numpy.random.choice([1,2],1, [eps, 1-eps])
        a = []
        if choice == 1: 
            # rnd = random.random()
            a = random.randint(0, len(possible_actions) - 1)
            return possible_actions[a]
        else:
            max_val = max(self.q_table[curr_state].values())
            for act, v in self.q_table[curr_state].items():
                if v == max_val:
                    a.append(act)
            return random.choice(a)


    def is_solution(self, reward):
        return reward == 300

    def best_action(self, curr_state):
        if curr_state in self.q_table:
            a = []
            max_val = max(self.q_table[curr_state].values())
            for act, v in self.q_table[curr_state].items():
                if v == max_val:
                    a.append(act)
            return random.choice(a)
        else:
            return None

    def best_policy(self, agent_host):
        """Reconstructs the best action list according to the greedy policy. """
        policy = []
        total_r = 0
        while len(self.possible_actions) > 0:
            curr_state = self.current_state
            possible_actions = self.possible_actions
            next_a = self.best_action(curr_state)
            if next_a == None:
                break
            policy.append(next_a)
            total_r += self.act(self.current_location, next_a, self.grid)
            self.possible_actions.remove(next_a)
        self.act(self.current_location, 0, self.grid)
        print('Best reward: ' + str(total_r))
        return total_r

    def update_q_table(self, tau, S, A, R, T):
        """Performs relevant updates for state tau.

        Args
            tau: <int>  state index to update
            S:   <dequqe>   states queue
            A:   <dequqe>   actions queue
            R:   <dequqe>   rewards queue
            T:   <int>      terminating state index
        """
        # curr_s, curr_a, curr_r = S.popleft(), A.popleft(), R.popleft()
        # G = sum([self.gamma ** i * R[i] for i in range(len(S))])
        # if tau + self.n < T:
        #     G += self.gamma ** self.n * self.q_table[S[-1]][A[-1]]

        # old_q = self.q_table[curr_s][curr_a]
        # self.q_table[curr_s][curr_a] = old_q + self.alpha * (G - old_q)
        curr_s, curr_a, curr_r = S.popleft(), A.popleft(), R.popleft()

        q_value = R[0]
        G = 0
        if tau < T - 1:
            G = self.gamma*max(self.q_table[S[-1]].values())
        self.q_table[curr_s][curr_a] = q_value + G


destinations = [210, 409, 167, 178, 418, 399]
agent = DashAgent(destinations.copy())
agent_host = MalmoPython.AgentHost()
try:
    agent_host.parse( sys.argv )
except RuntimeError as e:
    print('ERROR:',e)
    print(agent_host.getUsage())
    exit(1)
if agent_host.receivedArgument("help"):
    print(agent_host.getUsage())
    exit(0)

# -- set up the mission -- #


max_retries = 3

if agent_host.receivedArgument("test"):
    num_repeats = 1
else:
    num_repeats = 21


mission_file = './project.xml'
with open(mission_file, 'r') as f:
    print("Loading mission from %s" % mission_file)
    mission_xml = f.read()
    my_mission = MalmoPython.MissionSpec(mission_xml, True)
my_mission_record = MalmoPython.MissionRecordSpec()
my_mission.requestVideo(800, 500)
my_mission.setViewpoint(1)
for retry in range(max_retries):
    try:
        agent_host.startMission(my_mission, my_mission_record)
        break
    except RuntimeError as e:
        if retry == max_retries - 1:
            print("Error starting mission:",e)
            exit(1)
        else:
            time.sleep(2.5)
print("Waiting for the mission to start", end=' ')
best_rewards = []
for i in range(num_repeats):
    if i > 0:
        print(agent.q_table)
        agent.current_state = ()
        agent.possible_actions = destinations.copy()
        agent.step_count = 0
        best_rewards.append(agent.best_policy(agent_host))
   
    world_state = agent_host.getWorldState()
    while not world_state.has_mission_begun:
        print(".", end="")
        time.sleep(0.1)
        world_state = agent_host.getWorldState()
        for error in world_state.errors:
            print("Error:",error.text)
    print()
    print("Mission", (i+1), "running.")

    # Initialize
    agent.current_state = ()
    agent.possible_actions = destinations.copy()
    agent.step_count = 0
    agent.run(agent_host)
    
    #time.sleep(0.5) # (let the Mod reset)

plt.plot([i for i in range(20)], best_rewards, 'ro')
plt.axis([0, 21, 25, 45])
plt.show()

print("Done.")

print()
print("Cumulative rewards for all %d runs:" % num_repeats)
# print(cumulative_rewards)
