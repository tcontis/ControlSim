from abc import ABC

"""
Generic abstract class for a single-agent controller
"""
class Controller(ABC):
    def generate_inputs(self, state):
        pass
