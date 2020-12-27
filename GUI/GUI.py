import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from GUI import KheperaGUI

import traceback

class GUI:
    def __init__(self, model, queue):
        """

        :param model_info: A dictionary of information about the simulated model:
            - num_dim: Number of dimensions
            - lims: Ordered list of lower and upper bounds for each axis
        """
        self.fig = plt.figure("ControlSim v0.1.0")
        self.dimensions = model.get_model_info()['num_dim']
        if self.dimensions not in [2, 3]:
            raise ValueError("Argument {num_dim} must be either 2 or 3.")

        self.lims = model.get_model_info()['lims']
        if len(self.lims) != self.dimensions * 2:
            raise ValueError("Size of argument {lims} should be 2 * number of dimensions")

        self.ax = self.fig.add_subplot(1, 1, 1, projection=('3d' if self.dimensions == 3 else 'rectilinear'))
        if self.dimensions == 2:
            self.ax.set_xlim(self.lims[0:2])
            self.ax.set_ylim(self.lims[2:4])
        else:
            self.ax.set_xlim3d(self.lims[0:2])
            self.ax.set_ylim3d(self.lims[2:4])
            self.ax.set_zlim3d(self.lims[4:6])
        self.model = model
        self.artists = model.get_gui().get_artists()
        for artist in self.artists:
            self.ax.add_patch(artist)
        self.queue=queue
        self.ani = animation.FuncAnimation(self.fig, self.update, init_func=None,
                                           interval=1, blit=True)
        plt.show()

    def update(self, i):
        try:
            result = self.queue.get_nowait()
            if result is not None:
                self.model.get_gui().update(result)
        except Exception as e:
            #traceback.print_exc()
            pass

        return self.artists
