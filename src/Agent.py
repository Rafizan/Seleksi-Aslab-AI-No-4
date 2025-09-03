import random
from Environment import Environment
import math

class QLearningAgent:
    def __init__(self, env, alpha=0.5, gamma=0.99, epsilon=1, exploration_decay_rate=0.001):
        self.env = env
        self.alpha = alpha  # learning rate
        self.gamma = gamma  # discount rate
        self.epsilon = epsilon  # exploration rate
        self.exploration_decay_rate = exploration_decay_rate
        self.episodes = 0
        self.q_table = {}  # key: (state, action), value: Q-value
        self.actions = ['move_forward', 'turn_left', 'turn_right', 'grab', 'climb']

    def get_state(self):
        x, y = self.env.agent_position
        d = self.env.agent_direction
        g = self.env.has_gold
        return (x, y, d, g)

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.choice(self.actions)
        q_values = [self.q_table.get((state, a), 0) for a in self.actions]
        max_q = max(q_values)
        best_actions = [a for a, q in zip(self.actions, q_values) if q == max_q]
        return random.choice(best_actions)

    def update_q(self, state, action, reward, next_state):
        old_q = self.q_table.get((state, action), 0)
        next_qs = [self.q_table.get((next_state, a), 0) for a in self.actions]
        max_next_q = max(next_qs)
        new_q = old_q * (1 - self.alpha) + self.alpha * (reward + self.gamma * max_next_q)
        self.q_table[(state, action)] = new_q

    def decay_epsilon(self, min_epsilon=0.01, max_epsilon=1):
        self.epsilon = max(min_epsilon, (max_epsilon - min_epsilon) * math.exp(-self.exploration_decay_rate * self.episodes) + min_epsilon)

    def take_action(self, action):
        if action == 'move_forward':
            return self.env.move_forward()
        elif action == 'turn_left':
            return self.env.turn_left()
        elif action == 'turn_right':
            return self.env.turn_right()
        elif action == 'grab':
            return self.env.grab()
        elif action == 'climb':
            return self.env.climb()
        else:
            return 0

    def train(self, episodes=1000, max_steps=100):
        for _ in range(episodes):
            self.env.reset()
            total_reward = 0
            step = 0
            while max_steps == float('inf') or step < max_steps:
                state = self.get_state()
                action = self.choose_action(state)
                reward = self.take_action(action)
                next_state = self.get_state()
                self.update_q(state, action, reward, next_state)
                total_reward += reward
                self.episodes += 1
                if self.env.game_over:
                    break

            self.decay_epsilon()
            

    def play(self, max_steps=100):
        self.env.reset()
        for step in range(max_steps):
            state = self.get_state()
            q_values = [self.q_table.get((state, a), 0) for a in self.actions]
            max_q = max(q_values)
            best_actions = [a for a, q in zip(self.actions, q_values) if q == max_q]
            action = random.choice(best_actions)
            print(f"Step {step+1}: State={state}, Action={action}")
            reward = self.take_action(action)
            self.env.print_grid()
            if self.env.game_over:
                print(f"Game ended. Reward: {reward}, Score: {self.env.score}")
                break
        if not self.env.game_over:
            print(f"Max steps reached. Score: {self.env.score}")

class SARSAAgent:
    def __init__(self, env, alpha=0.5, gamma=0.99, epsilon=1, exploration_decay_rate=0.001):
        self.env = env
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.exploration_decay_rate = exploration_decay_rate
        self.episodes = 0
        self.q_table = {}
        self.actions = ['move_forward', 'turn_left', 'turn_right', 'grab', 'climb']

    def get_state(self):
        x, y = self.env.agent_position
        d = self.env.agent_direction
        g = self.env.has_gold
        return (x, y, d, g)

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.choice(self.actions)
        q_values = [self.q_table.get((state, a), 0) for a in self.actions]
        max_q = max(q_values)
        best_actions = [a for a, q in zip(self.actions, q_values) if q == max_q]
        return random.choice(best_actions)

    def update_q(self, state, action, reward, next_state, next_action):
        old_q = self.q_table.get((state, action), 0)
        next_q = self.q_table.get((next_state, next_action), 0)
        new_q = old_q * (1 - self.alpha) + self.alpha * (reward + self.gamma * next_q)
        self.q_table[(state, action)] = new_q

    def decay_epsilon(self, min_epsilon=0.01, max_epsilon=1):
        self.epsilon = max(min_epsilon, (max_epsilon - min_epsilon) * math.exp(-self.exploration_decay_rate * self.episodes) + min_epsilon)

    def take_action(self, action):
        if action == 'move_forward':
            return self.env.move_forward()
        elif action == 'turn_left':
            return self.env.turn_left()
        elif action == 'turn_right':
            return self.env.turn_right()
        elif action == 'grab':
            return self.env.grab()
        elif action == 'climb':
            return self.env.climb()
        else:
            return 0

    def train(self, episodes=1000, max_steps=100):
        for _ in range(episodes):
            self.env.reset()
            total_reward = 0
            state = self.get_state()
            action = self.choose_action(state)
            for step in range(max_steps):
                reward = self.take_action(action)
                next_state = self.get_state()
                next_action = self.choose_action(next_state)
                self.update_q(state, action, reward, next_state, next_action)
                total_reward += reward
                self.episodes += 1
                if self.env.game_over:
                    break
                state = next_state
                action = next_action
            self.decay_epsilon()

    def play(self, max_steps=100):
        self.env.reset()
        state = self.get_state()
        for step in range(max_steps):
            q_values = [self.q_table.get((state, a), 0) for a in self.actions]
            max_q = max(q_values)
            best_actions = [a for a, q in zip(self.actions, q_values) if q == max_q]
            action = random.choice(best_actions)
            print(f"Step {step+1}: State={state}, Action={action}")
            reward = self.take_action(action)
            self.env.print_grid()
            if self.env.game_over:
                print(f"Game ended. Reward: {reward}, Score: {self.env.score}")
                break
            state = self.get_state()
        if not self.env.game_over:
            print(f"Max steps reached. Score: {self.env.score}")


if __name__ == "__main__":
    env = Environment(4, 4)
    agent = QLearningAgent(env)
    print("Training agent...")
    agent.train(episodes=10000, max_steps=20)
    print("Testing agent...")
    agent.play(max_steps=20)