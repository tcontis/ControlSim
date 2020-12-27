from GUI.GUIObject import GUIObject
import matplotlib.pyplot as plt
import numpy as np

class KheperaGUI(GUIObject):

    def __init__(self, wheel_radius, body_radius, wheel_width, initial_pos):
        self.wheel_radius = wheel_radius
        self.wheel_width = wheel_width
        self.body_radius = body_radius
        self.body = plt.Circle(tuple(initial_pos), radius=body_radius, color='red')
        init_x, init_y = initial_pos
        self.left_wheel = plt.Rectangle((init_x-body_radius-wheel_width, init_y-wheel_radius),
                                        height=wheel_radius*2, width=wheel_width, color='black')
        self.right_wheel = plt.Rectangle((init_x+body_radius, init_y-wheel_radius),
                                         height=wheel_radius*2, width=wheel_width, color='black')
        self.phi_marker = plt.Rectangle((init_x, init_y), height=wheel_radius, width=body_radius/100, color='lime')

    def update(self, new_state):
        new_x, new_y = new_state[0:2]
        phi = new_state[2]
        self.body.set_center((new_x, new_y))
        self.left_wheel.set_x(new_x+self.body_radius*np.cos(phi+np.pi/2)+self.wheel_width*np.cos(phi+np.pi/2)+self.wheel_radius*np.cos(phi+np.pi))
        self.left_wheel.set_y(new_y+self.body_radius*np.sin(phi+np.pi/2)+self.wheel_width*np.sin(phi+np.pi/2)+self.wheel_radius*np.sin(phi+np.pi))
        self.left_wheel.angle = phi / np.pi * 180-90
        self.right_wheel.set_x(new_x - self.body_radius * np.cos(phi + np.pi / 2) + self.wheel_radius * np.cos(phi + np.pi))
        self.right_wheel.set_y(new_y - self.body_radius * np.sin(phi + np.pi / 2) + self.wheel_radius * np.sin(phi + np.pi))
        self.right_wheel.angle = phi / np.pi * 180 - 90
        self.phi_marker.set_x(new_x)
        self.phi_marker.set_y(new_y)
        self.phi_marker.angle = phi / np.pi * 180 - 90

    def get_position(self):
        pass

    def get_rotation(self):
        pass

    def get_artists(self):
        return [self.body, self.left_wheel, self.right_wheel, self.phi_marker]
