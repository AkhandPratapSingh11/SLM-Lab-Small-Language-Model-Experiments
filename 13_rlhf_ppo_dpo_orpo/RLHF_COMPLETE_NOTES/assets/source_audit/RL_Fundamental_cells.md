# RL_Fundamental.ipynb
Metadata: {"colab": {"provenance": [], "gpuType": "T4"}, "kernelspec": {"name": "python3", "display_name": "Python 3"}, "language_info": {"name": "python"}, "accelerator": "GPU"}

## Cell 1 [code] execution_count=1
# RL basic form

## Cell 2 [code] execution_count=2
import random

actions = ["left", "right"]

# Q-table (memory)
Q = {
    "left": 0,
    "right": 0
}

## Cell 3 [code] execution_count=3
# reward system
def get_reward(action):
    if action == "right":
        return 1
    else:
        return -1

## Cell 4 [code] execution_count=4
# learning rate
alpha = 0.1

for i in range(50):

    # choose action (exploration)
    action = random.choice(actions)

    reward = get_reward(action)

    # update Q value (learning happens here)
    Q[action] = Q[action] + alpha * (reward - Q[action])

    print(f"Step {i}, Action: {action}, Reward: {reward}, Q: {Q}")
OUTPUT 1: stream
Step 0, Action: right, Reward: 1, Q: {'left': 0, 'right': 0.1}
Step 1, Action: left, Reward: -1, Q: {'left': -0.1, 'right': 0.1}
Step 2, Action: right, Reward: 1, Q: {'left': -0.1, 'right': 0.19}
Step 3, Action: right, Reward: 1, Q: {'left': -0.1, 'right': 0.271}
Step 4, Action: left, Reward: -1, Q: {'left': -0.19, 'right': 0.271}
Step 5, Action: left, Reward: -1, Q: {'left': -0.271, 'right': 0.271}
Step 6, Action: right, Reward: 1, Q: {'left': -0.271, 'right': 0.34390000000000004}
Step 7, Action: left, Reward: -1, Q: {'left': -0.34390000000000004, 'right': 0.34390000000000004}
Step 8, Action: right, Reward: 1, Q: {'left': -0.34390000000000004, 'right': 0.40951000000000004}
Step 9, Action: right, Reward: 1, Q: {'left': -0.34390000000000004, 'right': 0.46855900000000006}
Step 10, Action: right, Reward: 1, Q: {'left': -0.34390000000000004, 'right': 0.5217031000000001}
Step 11, Action: left, Reward: -1, Q: {'left': -0.40951000000000004, 'right': 0.5217031000000001}
Step 12, Action: right, Reward: 1, Q: {'left': -0.40951000000000004, 'right': 0.5695327900000001}
Step 13, Action: left, Reward: -1, Q: {'left': -0.46855900000000006, 'right': 0.5695327900000001}
Step 14, Action: right, Reward: 1, Q: {'left': -0.46855900000000006, 'right': 0.6125795110000001}
Step 15, Action: right, Reward: 1, Q: {'left': -0.46855900000000006, 'right': 0.6513215599000001}
Step 16, Action: right, Reward: 1, Q: {'left': -0.46855900000000006, 'right': 0.68618940391}
Step 17, Action: right, Reward: 1, Q: {'left': -0.46855900000000006, 'right': 0.717570463519}
Step 18, Action: left, Reward: -1, Q: {'left': -0.5217031000000001, 'right': 0.717570463519}
Step 19, Action: right, Reward: 1, Q: {'left': -0.5217031000000001, 'right': 0.7458134171671}
Step 20, Action: right, Reward: 1, Q: {'left': -0.5217031000000001, 'right': 0.7712320754503901}
Step 21, Action: left, Reward: -1, Q: {'left': -0.5695327900000001, 'right': 0.7712320754503901}
Step 22, Action: left, Reward: -1, Q: {'left': -0.6125795110000001, 'right': 0.7712320754503901}
Step 23, Action: left, Reward: -1, Q: {'left': -0.6513215599000001, 'right': 0.7712320754503901}
Step 24, Action: right, Reward: 1, Q: {'left': -0.6513215599000001, 'right': 0.7941088679053511}
Step 25, Action: right, Reward: 1, Q: {'left': -0.6513215599000001, 'right': 0.814697981114816}
Step 26, Action: right, Reward: 1, Q: {'left': -0.6513215599000001, 'right': 0.8332281830033343}
Step 27, Action: left, Reward: -1, Q: {'left': -0.68618940391, 'right': 0.8332281830033343}
Step 28, Action: left, Reward: -1, Q: {'left': -0.717570463519, 'right': 0.8332281830033343}
Step 29, Action: right, Reward: 1, Q: {'left': -0.717570463519, 'right': 0.8499053647030009}
Step 30, Action: left, Reward: -1, Q: {'left': -0.7458134171671, 'right': 0.8499053647030009}
Step 31, Action: right, Reward: 1, Q: {'left': -0.7458134171671, 'right': 0.8649148282327008}
Step 32, Action: right, Reward: 1, Q: {'left': -0.7458134171671, 'right': 0.8784233454094308}
Step 33, Action: left, Reward: -1, Q: {'left': -0.7712320754503901, 'right': 0.8784233454094308}
Step 34, Action: right, Reward: 1, Q: {'left': -0.7712320754503901, 'right': 0.8905810108684877}
Step 35, Action: left, Reward: -1, Q: {'left': -0.7941088679053511, 'right': 0.8905810108684877}
Step 36, Action: left, Reward: -1, Q: {'left': -0.814697981114816, 'right': 0.8905810108684877}
Step 37, Action: right, Reward: 1, Q: {'left': -0.814697981114816, 'right': 0.901522909781639}
Step 38, Action: right, Reward: 1, Q: {'left': -0.814697981114816, 'right': 0.911370618803475}
Step 39, Action: right, Reward: 1, Q: {'left': -0.814697981114816, 'right': 0.9202335569231275}
Step 40, Action: left, Reward: -1, Q: {'left': -0.8332281830033343, 'right': 0.9202335569231275}
Step 41, Action: right, Reward: 1, Q: {'left': -0.8332281830033343, 'right': 0.9282102012308148}
Step 42, Action: left, Reward: -1, Q: {'left': -0.8499053647030009, 'right': 0.9282102012308148}
Step 43, Action: left, Reward: -1, Q: {'left': -0.8649148282327008, 'right': 0.9282102012308148}
Step 44, Action: left, Reward: -1, Q: {'left': -0.8784233454094308, 'right': 0.9282102012308148}
Step 45, Action: left, Reward: -1, Q: {'left': -0.8905810108684877, 'right': 0.9282102012308148}
Step 46, Action: left, Reward: -1, Q: {'left': -0.901522909781639, 'right': 0.9282102012308148}
Step 47, Action: left, Reward: -1, Q: {'left': -0.911370618803475, 'right': 0.9282102012308148}
Step 48, Action: left, Reward: -1, Q: {'left': -0.9202335569231275, 'right': 0.9282102012308148}
Step 49, Action: right, Reward: 1, Q: {'left': -0.9202335569231275, 'right': 0.9353891811077333}



{}

## Cell 5 [code] execution_count=5
Q[action] = Q[action] + alpha * (reward - Q[action])

## Cell 6 [code] execution_count=6
Q
OUTPUT 1: execute_result

{'left': -0.9202335569231275, 'right': 0.94185026299696}

{}

## Cell 7 [code] execution_count=None
# # Initially:
# Q(left) = 0
# Q(right) = 0

# # After training:
# Q(right) → higher (good)
# Q(left) → lower (bad)

# # RESULT:
# Agent learns:
# "right is better"

# # Greedy policy:
# action = max(Q, key=Q.get)

# # FINAL TRUTH:
# RL = interaction + reward + update

# # SUPER SIMPLE:
# No update → No learning
# Update + feedback → RL

## Cell 8 [markdown] execution_count=None
Have you ever wondered…

how a machine learns without anyone telling it the correct answer?

No one says:

“Right is correct”

Still… the model learns. How?

Let’s break it down.

---

**Concept Start**

Imagine a very simple world.

You have only two actions:
Left
Right

Initially, the model knows nothing.

So internally:

Q(left) = 0
Q(right) = 0

Both are equal. No intelligence yet.

---

**Learning Begins**

Now the model starts taking actions randomly.

Suppose:

It goes Right → gets reward +1
It goes Left → gets reward -1

Important point:
No one told the model what is correct.

It only gets feedback.

---

**Update Happens (THIS IS THE MAGIC)**

The model updates its memory:

Q(right) becomes positive
Q(left) becomes negative

Now something interesting happens…

---

**Emerging Intelligence**

The agent starts realizing:

“Right is better than Left”

No teacher.
No labeled data.
Only experience.

---

**Decision Phase**

Now if we make the model greedy:

action = max(Q, key=Q.get)

It will always choose:

Right

---

**Final Truth (MOST IMPORTANT)**

Reinforcement Learning is NOT randomness.

RL = interaction + reward + update

Without update → no learning
With feedback + update → intelligence

---

**Super Simple Line (Mic Drop)**

The model is not told what is right.
It discovers what is right.

---

**Outro**

And this simple idea…
is what powers everything from game-playing AI
to ChatGPT training using PPO.

In the next video,
we’ll see how this small idea scales to Deep Q Networks and PPO.


## Cell 9 [code] execution_count=16
import torch
import torch.nn as nn
import torch.optim as optim

# Q Network
class DQN(nn.Module):
    def __init__(self, state_size, action_size):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(state_size, 128),
            nn.ReLU(),
            nn.Linear(128, action_size)
        )

    def forward(self, x):
        return self.net(x)

state_size = 4
action_size = 2

## Cell 10 [code] execution_count=17
model = DQN(state_size, action_size)
target_model = DQN(state_size, action_size)

# Copy weights from main model to target model
target_model.load_state_dict(model.state_dict())

optimizer = optim.Adam(model.parameters(), lr=1e-3)
loss_fn = nn.MSELoss()

## Cell 11 [code] execution_count=19
# Dummy batch
state = torch.randn(32, state_size)
next_state = torch.randn(32, state_size)

## Cell 12 [code] execution_count=20
reward = torch.randn(32)
done = torch.randint(0, 2, (32,)).float()
action = torch.randint(0, action_size, (32,))

## Cell 13 [code] execution_count=21
# Predicted Q values for current state
q_values = model(state)

## Cell 14 [code] execution_count=22
# Pick Q-value of the action actually taken
q_value = q_values.gather(1, action.unsqueeze(1)).squeeze(1)

## Cell 15 [code] execution_count=23
# Compute target Q value
with torch.no_grad():
    next_q = target_model(next_state).max(1)[0]
    target = reward + 0.99 * next_q * (1 - done)

## Cell 16 [code] execution_count=24
# Compute loss
loss = loss_fn(q_value, target)

## Cell 17 [code] execution_count=25
# Update model weights
optimizer.zero_grad()
loss.backward()
optimizer.step()

## Cell 18 [markdown] execution_count=None
No one explicitly tells the model:

“Right is correct”

Instead, it only gets signals like:

Right → +1
Left → -1

The model learns on its own

Random action → reward feedback

## Cell 19 [code] execution_count=28
!pip install stable-baselines3
OUTPUT 1: stream
Requirement already satisfied: stable-baselines3 in /usr/local/lib/python3.12/dist-packages (2.8.0)
Requirement already satisfied: gymnasium<1.3.0,>=0.29.1 in /usr/local/lib/python3.12/dist-packages (from stable-baselines3) (1.2.3)
Requirement already satisfied: numpy<3.0,>=1.20 in /usr/local/lib/python3.12/dist-packages (from stable-baselines3) (2.0.2)
Requirement already satisfied: torch<3.0,>=2.3 in /usr/local/lib/python3.12/dist-packages (from stable-baselines3) (2.10.0+cu128)
Requirement already satisfied: cloudpickle in /usr/local/lib/python3.12/dist-packages (from stable-baselines3) (3.1.2)
Requirement already satisfied: pandas in /usr/local/lib/python3.12/dist-packages (from stable-baselines3) (2.2.2)
Requirement already satisfied: matplotlib in /usr/local/lib/python3.12/dist-packages (from stable-baselines3) (3.10.0)
Requirement already satisfied: typing-extensions>=4.3.0 in /usr/local/lib/python3.12/dist-packages (from gymnasium<1.3.0,>=0.29.1->stable-baselines3) (4.15.0)
Requirement already satisfied: farama-notifications>=0.0.1 in /usr/local/lib/python3.12/dist-packages (from gymnasium<1.3.0,>=0.29.1->stable-baselines3) (0.0.4)
Requirement already satisfied: filelock in /usr/local/lib/python3.12/dist-packages (from torch<3.0,>=2.3->stable-baselines3) (3.25.2)
Requirement already satisfied: setuptools in /usr/local/lib/python3.12/dist-packages (from torch<3.0,>=2.3->stable-baselines3) (75.2.0)
Requirement already satisfied: sympy>=1.13.3 in /usr/local/lib/python3.12/dist-packages (from torch<3.0,>=2.3->stable-baselines3) (1.14.0)
Requirement already satisfied: networkx>=2.5.1 in /usr/local/lib/python3.12/dist-packages (from torch<3.0,>=2.3->stable-baselines3) (3.6.1)
Requirement already satisfied: jinja2 in /usr/local/lib/python3.12/dist-packages (from torch<3.0,>=2.3->stable-baselines3) (3.1.6)
Requirement already satisfied: fsspec>=0.8.5 in /usr/local/lib/python3.12/dist-packages (from torch<3.0,>=2.3->stable-baselines3) (2025.3.0)
Requirement already satisfied: cuda-bindings==12.9.4 in /usr/local/lib/python3.12/dist-packages (from torch<3.0,>=2.3->stable-baselines3) (12.9.4)
Requirement already satisfied: nvidia-cuda-nvrtc-cu12==12.8.93 in /usr/local/lib/python3.12/dist-packages (from torch<3.0,>=2.3->stable-baselines3) (12.8.93)
Requirement already satisfied: nvidia-cuda-runtime-cu12==12.8.90 in /usr/local/lib/python3.12/dist-packages (from torch<3.0,>=2.3->stable-baselines3) (12.8.90)
Requirement already satisfied: nvidia-cuda-cupti-cu12==12.8.90 in /usr/local/lib/python3.12/dist-packages (from torch<3.0,>=2.3->stable-baselines3) (12.8.90)
Requirement already satisfied: nvidia-cudnn-cu12==9.10.2.21 in /usr/local/lib/python3.12/dist-packages (from torch<3.0,>=2.3->stable-baselines3) (9.10.2.21)
Requirement already satisfied: nvidia-cublas-cu12==12.8.4.1 in /usr/local/lib/python3.12/dist-packages (from torch<3.0,>=2.3->stable-baselines3) (12.8.4.1)
Requirement already satisfied: nvidia-cufft-cu12==11.3.3.83 in /usr/local/lib/python3.12/dist-packages (from torch<3.0,>=2.3->stable-baselines3) (11.3.3.83)
Requirement already satisfied: nvidia-curand-cu12==10.3.9.90 in /usr/local/lib/python3.12/dist-packages (from torch<3.0,>=2.3->stable-baselines3) (10.3.9.90)
Requirement already satisfied: nvidia-cusolver-cu12==11.7.3.90 in /usr/local/lib/python3.12/dist-packages (from torch<3.0,>=2.3->stable-baselines3) (11.7.3.90)
Requirement already satisfied: nvidia-cusparse-cu12==12.5.8.93 in /usr/local/lib/python3.12/dist-packages (from torch<3.0,>=2.3->stable-baselines3) (12.5.8.93)
Requirement already satisfied: nvidia-cusparselt-cu12==0.7.1 in /usr/local/lib/python3.12/dist-packages (from torch<3.0,>=2.3->stable-baselines3) (0.7.1)
Requirement already satisfied: nvidia-nccl-cu12==2.27.5 in /usr/local/lib/python3.12/dist-packages (from torch<3.0,>=2.3->stable-baselines3) (2.27.5)
Requirement already satisfied: nvidia-nvshmem-cu12==3.4.5 in /usr/local/lib/python3.12/dist-packages (from torch<3.0,>=2.3->stable-baselines3) (3.4.5)
Requirement already satisfied: nvidia-nvtx-cu12==12.8.90 in /usr/local/lib/python3.12/dist-packages (from torch<3.0,>=2.3->stable-baselines3) (12.8.90)
Requirement already satisfied: nvidia-nvjitlink-cu12==12.8.93 in /usr/local/lib/python3.12/dist-packages (from torch<3.0,>=2.3->stable-baselines3) (12.8.93)
Requirement already satisfied: nvidia-cufile-cu12==1.13.1.3 in /usr/local/lib/python3.12/dist-packages (from torch<3.0,>=2.3->stable-baselines3) (1.13.1.3)
Requirement already satisfied: triton==3.6.0 in /usr/local/lib/python3.12/dist-packages (from torch<3.0,>=2.3->stable-baselines3) (3.6.0)
Requirement already satisfied: cuda-pathfinder~=1.1 in /usr/local/lib/python3.12/dist-packages (from cuda-bindings==12.9.4->torch<3.0,>=2.3->stable-baselines3) (1.4.3)
Requirement already satisfied: contourpy>=1.0.1 in /usr/local/lib/python3.12/dist-packages (from matplotlib->stable-baselines3) (1.3.3)
Requirement already satisfied: cycler>=0.10 in /usr/local/lib/python3.12/dist-packages (from matplotlib->stable-baselines3) (0.12.1)
Requirement already satisfied: fonttools>=4.22.0 in /usr/local/lib/python3.12/dist-packages (from matplotlib->stable-baselines3) (4.62.1)
Requirement already satisfied: kiwisolver>=1.3.1 in /usr/local/lib/python3.12/dist-packages (from matplotlib->stable-baselines3) (1.5.0)
Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.12/dist-packages (from matplotlib->stable-baselines3) (26.0)
Requirement already satisfied: pillow>=8 in /usr/local/lib/python3.12/dist-packages (from matplotlib->stable-baselines3) (11.3.0)
Requirement already satisfied: pyparsing>=2.3.1 in /usr/local/lib/python3.12/dist-packages (from matplotlib->stable-baselines3) (3.3.2)
Requirement already satisfied: python-dateutil>=2.7 in /usr/local/lib/python3.12/dist-packages (from matplotlib->stable-baselines3) (2.9.0.post0)
Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.12/dist-packages (from pandas->stable-baselines3) (2025.2)
Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.12/dist-packages (from pandas->stable-baselines3) (2025.3)
Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.12/dist-packages (from python-dateutil>=2.7->matplotlib->stable-baselines3) (1.17.0)
Requirement already satisfied: mpmath<1.4,>=1.1.0 in /usr/local/lib/python3.12/dist-packages (from sympy>=1.13.3->torch<3.0,>=2.3->stable-baselines3) (1.3.0)
Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.12/dist-packages (from jinja2->torch<3.0,>=2.3->stable-baselines3) (3.0.3)



{}

## Cell 20 [code] execution_count=29
!pip install swig
OUTPUT 1: stream
Requirement already satisfied: swig in /usr/local/lib/python3.12/dist-packages (4.4.1)



{}

## Cell 21 [code] execution_count=30
!pip install "gymnasium[box2d]"
OUTPUT 1: stream
Requirement already satisfied: gymnasium[box2d] in /usr/local/lib/python3.12/dist-packages (1.2.3)
Requirement already satisfied: numpy>=1.21.0 in /usr/local/lib/python3.12/dist-packages (from gymnasium[box2d]) (2.0.2)
Requirement already satisfied: cloudpickle>=1.2.0 in /usr/local/lib/python3.12/dist-packages (from gymnasium[box2d]) (3.1.2)
Requirement already satisfied: typing-extensions>=4.3.0 in /usr/local/lib/python3.12/dist-packages (from gymnasium[box2d]) (4.15.0)
Requirement already satisfied: farama-notifications>=0.0.1 in /usr/local/lib/python3.12/dist-packages (from gymnasium[box2d]) (0.0.4)
Collecting box2d==2.3.10 (from gymnasium[box2d])
  Downloading Box2D-2.3.10-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (573 bytes)
Requirement already satisfied: pygame>=2.1.3 in /usr/local/lib/python3.12/dist-packages (from gymnasium[box2d]) (2.6.1)
Requirement already satisfied: swig==4.* in /usr/local/lib/python3.12/dist-packages (from gymnasium[box2d]) (4.4.1)
Downloading Box2D-2.3.10-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.7 MB)
[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m3.7/3.7 MB[0m [31m42.5 MB/s[0m eta [36m0:00:00[0m
[?25hInstalling collected packages: box2d
Successfully installed box2d-2.3.10



{}

## Cell 22 [code] execution_count=31
import gymnasium as gym
from stable_baselines3 import PPO
OUTPUT 1: stream
Gym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.
Please upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.
See the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.
/usr/local/lib/python3.12/dist-packages/jupyter_client/session.py:203: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
  return datetime.utcnow().replace(tzinfo=utc)



{}

## Cell 23 [code] execution_count=32
# Create environment (real RL env)
env = gym.make("CarRacing-v3", render_mode="human")
OUTPUT 1: stream
<frozen importlib._bootstrap>:488: DeprecationWarning: builtin type SwigPyPacked has no __module__ attribute
<frozen importlib._bootstrap>:488: DeprecationWarning: builtin type SwigPyObject has no __module__ attribute
<frozen importlib._bootstrap>:488: DeprecationWarning: builtin type swigvarlink has no __module__ attribute
/usr/local/lib/python3.12/dist-packages/pygame/pkgdata.py:25: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
  from pkg_resources import resource_stream, resource_exists
/usr/local/lib/python3.12/dist-packages/pkg_resources/__init__.py:3154: DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('google')`.
Implementing implicit namespace packages (as specified in PEP 420) is preferred to `pkg_resources.declare_namespace`. See https://setuptools.pypa.io/en/latest/references/keywords.html#keyword-namespace-packages
  declare_namespace(pkg)
/usr/local/lib/python3.12/dist-packages/pkg_resources/__init__.py:3154: DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('google.cloud')`.
Implementing implicit namespace packages (as specified in PEP 420) is preferred to `pkg_resources.declare_namespace`. See https://setuptools.pypa.io/en/latest/references/keywords.html#keyword-namespace-packages
  declare_namespace(pkg)
/usr/local/lib/python3.12/dist-packages/pkg_resources/__init__.py:3154: DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('sphinxcontrib')`.
Implementing implicit namespace packages (as specified in PEP 420) is preferred to `pkg_resources.declare_namespace`. See https://setuptools.pypa.io/en/latest/references/keywords.html#keyword-namespace-packages
  declare_namespace(pkg)
/usr/local/lib/python3.12/dist-packages/jupyter_client/session.py:203: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
  return datetime.utcnow().replace(tzinfo=utc)



{}

## Cell 24 [code] execution_count=33
# Create RL model (agent)
model = PPO(
    "CnnPolicy",
    env,
    verbose=1,
    learning_rate=0.0003,
    n_steps=2048,
    batch_size=64
)
OUTPUT 1: stream
Using cuda device
Wrapping the env with a `Monitor` wrapper
Wrapping the env in a DummyVecEnv.
Wrapping the env in a VecTransposeImage.



{}

## Cell 25 [code] execution_count=34
# Train agent
model.learn(total_timesteps=100)
OUTPUT 1: stream
---------------------------------
| rollout/           |          |
|    ep_len_mean     | 1e+03    |
|    ep_rew_mean     | -58.6    |
| time/              |          |
|    fps             | 30       |
|    iterations      | 1        |
|    time_elapsed    | 67       |
|    total_timesteps | 2048     |
---------------------------------



{}
OUTPUT 2: execute_result

<stable_baselines3.ppo.ppo.PPO at 0x7b3436d2acf0>

{}

## Cell 26 [code] execution_count=35
# Test agent
obs, _ = env.reset()

## Cell 27 [code] execution_count=36
for _ in range(1000):
    action, _ = model.predict(obs)
    obs, reward, done, truncated, info = env.step(action)

    if done or truncated:
        obs, _ = env.reset()

## Cell 28 [markdown] execution_count=None
This code shows the core training step of DQN

DQN uses a neural network instead of a Q-table

The neural network takes the state as input

The network outputs Q-values for all possible actions

model is the main network that is being trained

target_model is a separate network used to create stable targets

target_model.load_state_dict(model.state_dict()) copies the main model weights into the target model

The optimizer is used to update neural network weights

The loss function measures how far the predicted Q-value is from the target Q-value

state represents the current state

next_state represents the next state after taking an action

reward is the feedback received from the environment

done tells whether the episode has ended or not

action tells which action was actually taken

q_values = model(state) predicts Q-values for all actions for each state in the batch

gather(...) selects the Q-value of the action that was actually taken

q_value represents the predicted value of the chosen action

target_model(next_state) predicts Q-values for the next state

.max(1)[0] selects the best possible future Q-value from the next state

target = reward + 0.99 * next_q * (1 - done) computes the target using the
Bellman equation

If done = 1, future reward is ignored

The loss compares the current predicted Q-value with the target Q-value

optimizer.zero_grad() clears old gradients

loss.backward() computes gradients

optimizer.step() updates the network weights

This is how the neural network gradually learns better Q-values

In Q-learning, values are stored in a table

In DQN, values are learned by a neural network

This code is not the full DQN pipeline

It only shows the core learning/update step

Full DQN also includes replay buffer, epsilon-greedy exploration, environment
interaction, and periodic target network updates