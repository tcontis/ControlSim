from abc import ABC

"""
Generic abstract class for a 2D Model
"""
class Model2D(ABC):

    # Return x' for the simulator to integrate
    def state_dot(self, t, state, inputs):
        pass

    # Update current state from simulator
    def update(self, new_state):
        pass

    # Return position [x, y]
    def get_position(self):
        pass

    # Return rotation [phi, theta]
    def get_rotation(self):
        pass

    # Return current state
    def get_state(self):
        pass

    """
    Returns a dictionary with important information for GUI:
    number of dimensions, 
    """
    def get_model_info(self):
        pass