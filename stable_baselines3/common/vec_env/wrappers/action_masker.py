from typing import List

import numpy as np

from stable_baselines3.common.vec_env import VecEnv, VecEnvWrapper
from stable_baselines3.common.vec_env.base_vec_env import VecEnvObs, VecEnvStepReturn
from stable_baselines3.common.wrappers import ActionMasker


class VecActionMasker(VecEnvWrapper):
    """
    A wrapper for a VecEnv of envs that have themselves been wrapped with the ActionMasker wrapper.

    :param venv: the VecEnv to wrap. The underlying envs must be wrapped with the ActionMasker wrapper.
    """

    def __init__(self, venv: VecEnv):
        super().__init__(venv)

        if not all(self.env_is_wrapped(ActionMasker)):
            raise ValueError("VecEnv's envs must be wrapped with the ActionMasker wrapper")

    def valid_actions(self) -> List[np.ndarray]:
        return self.venv.env_method("valid_actions")

    def reset(self) -> VecEnvObs:
        return self.venv.reset()

    def step_wait(self) -> VecEnvStepReturn:
        return self.venv.step_wait()
