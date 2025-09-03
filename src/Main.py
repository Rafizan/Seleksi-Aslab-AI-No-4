import sys
from Environment import Environment
from Agent import QLearningAgent, SARSAAgent

def print_q_table(agent):
	print("\nQ-table:")
	for key, value in agent.q_table.items():
		print(f"State: {key[0]}, Action: {key[1]}, Q-value: {value:.2f}")

def main():
	print("Choose agent type:\n(1) Q-Learning\n(2) SARSA")
	agent_type = input("Enter 1/2: ").strip()
	alpha = float(input("Learning rate (ex: 0.5): ").strip())
	gamma = float(input("Discount factor (ex: 0.99): ").strip())
	epsilon = float(input("Exploration rate (ex: 1): ").strip())
	decay = float(input("Exploration decay rate (ex: 0.001): ").strip())
	episodes = int(input("Number of training episodes (ex: 10000): ").strip())
	max_steps = int(input("Max steps per episode (ex: 20): ").strip())

	env = Environment(4, 4)
	if agent_type == '2':
		agent = SARSAAgent(env, alpha=alpha, gamma=gamma, epsilon=epsilon, exploration_decay_rate=decay)
	else:
		agent = QLearningAgent(env, alpha=alpha, gamma=gamma, epsilon=epsilon, exploration_decay_rate=decay)

	print("\nTraining agent...")
	agent.train(episodes=episodes, max_steps=max_steps)
	print_q_table(agent)
	print("\nTesting agent...")
	agent.play(max_steps=max_steps)

if __name__ == "__main__":
	main()
