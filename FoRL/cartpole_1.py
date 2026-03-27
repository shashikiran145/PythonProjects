import gymnasium as gym

env = gym.make("CartPole-v1", render_mode="human")

obs, info = env.reset()

print(f"Starting Observations: {obs}")
#[cart_position, cart_velocity, pole_angle, pole_angular_velocity]

episode_over = False
total_reward = 0

class SimpleAgent:

    def act(self, observation):
        pole_angle = observation[2]

        if pole_angle > 0:
            return 1
        else:
            return 0

agent = SimpleAgent()


while not episode_over:
    agent = SimpleAgent()

    #action = env.action_space.sample()

    observation, reward, terminated, truncated, info = env.step(agent.act(obs))

    # reward: +1 for each step the pole stays upright
    # terminated: True if pole falls too far (agent failed)
    # truncated: True if we hit the time limit (500 steps)

    total_reward += reward
    episode_over = truncated

print(f"Episode finished. Reward: {total_reward}")
env.close()
