from env import Env_VR
import numpy as np

EPISODE_Length = 500
STEP_Length = 50

env = Env_VR()
per_user_block = int(env.Resource_Block_NUM/env.USER_NUM)

for episode in EPISODE_Length:
    env.reset()
    for step in STEP_Length:
        requested_block = np.zeros(env.USER_NUM)
        for i in range(env.USER_NUM):
            requested_block[i] = int((env.Viewport_Tile_Size - env.Buffer_H[i])/env.Per_Block_Rate[i])
        estimated_reward = env.return_bandwidth_reward(requested_block)
        env.VCG_Auction(requested_block,estimated_reward)
        watch_reward = env.VR_Watch_Reward()
        env.STATE_TRANSITION()
