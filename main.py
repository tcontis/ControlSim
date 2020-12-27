from Controllers import *
from GUI.GUI import GUI
from Models.DifferentialDrive import DifferentialDrive
from Controllers.DifferentialDrivePID import DifferentialDrivePID
from simulator import Simulator

if __name__ == '__main__':
    sim = Simulator(dt=0.005)

    diff = DifferentialDrive(body_radius=0.25, wheel_radius=0.25, wheel_width=0.05)
    cont = DifferentialDrivePID()

    sim.add_model(model=diff, controller=cont)
    sim.begin()
