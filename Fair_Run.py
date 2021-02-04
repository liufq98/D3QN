from env import Env_VR

EPISODE_Length = 500
STEP_Length = 50

env = Env_VR()
Per_User_Block = int(env.Resource_Block_NUM/env.USER_NUM)


for episode in EPISODE_Length:
    env.reset()
    for step in STEP_Length:
        env.User_Data_Rate = env.Per_Block_Rate * Per_User_Block
        watch_reward = env.VR_Watch_Reward()
        env.STATE_TRANSITION()
        #记录每个step/episode的reward。