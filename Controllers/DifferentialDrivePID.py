from Controllers.Controller import Controller

class DifferentialDrivePID(Controller):
    def generate_inputs(self, state):
        x = state[0]
        y = state[1]
        phi = state[2]
        return [1, 2]