from Models.Model2D import Model2D
import numpy as np
from GUI.KheperaGUI import KheperaGUI

class DifferentialDrive(Model2D):

    def __init__(self, wheel_radius, wheel_width, body_radius):
        """
        Constructs a model of a two-wheeled differential drive robot with state
        [x, y, phi]
        where
        - x and y are coordinate locations of robot's center in meters
        - phi is robot heading in radians (0 is east, +/- pi/2 is west)

        and inputs
        [v_l, v_r]
        where
        - v_l and v_r are the velocities of the left and right wheels, respectively, in revolutions/sec

        :param wheel_radius: Radius of both wheels, in meters
        :param body_radius: Radius of body, or distance from center of robot to each wheel, in meters
        """
        self.wheel_radius = wheel_radius
        self.wheel_width = wheel_width
        self.body_radius = body_radius
        self.state = [0.0, 0.0, 0.0]
        self.model_info = {'num_dim': 2, 'lims': [-2.0, 2.0, -2.0, 2.0]}
        self.gui = KheperaGUI(wheel_radius=wheel_radius, body_radius=body_radius, wheel_width=wheel_width, initial_pos=[0.5, 0.5])

    # Return x' for the simulator to integrate
    def state_dot(self, t, state, inputs):
        v_l, v_r = inputs
        x, y, phi = state
        state_dot = np.zeros((3, 1))
        state_dot[0] = self.wheel_radius / 2 * (v_r + v_l) * np.cos(phi)
        state_dot[1] = self.wheel_radius / 2 * (v_r - v_l) * np.sin(phi)
        state_dot[2] = self.wheel_radius / (2 * self.body_radius) * (v_r - v_l)
        return state_dot

    # Update current state from simulator
    def update(self, new_state):
        self.state = new_state

    # Return position [x, y]
    def get_position(self):
        return self.state[0:2]

    # Return rotation [phi]
    def get_rotation(self):
        return self.state[2]

    # Return current state [x, y, phi]
    def get_state(self):
        return self.state

    """
        Returns a dictionary with important information for GUI:
        number of dimensions, 
        """

    def get_model_info(self):
        return self.model_info

    def get_gui(self):
        return self.gui

