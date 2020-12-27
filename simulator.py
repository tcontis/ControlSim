from GUI.GUI import GUI
import threading
import scipy.integrate
import multiprocessing
import time


class Simulator():
    def __init__(self, dt):
        self.models = []
        self.t = time.time()
        self.model_list = []
        self.num_models = 0
        self.threads = []
        self.GUI = None
        self.dt = 0.005
        self.queue = multiprocessing.Queue()
        self.finished = False
        self.run = True

    def add_model(self, model, controller=None):
        integrator = scipy.integrate.ode(model.state_dot).set_integrator('dopri5', atol=1e-3, rtol=1e-6)
        self.model_list.append(model)
        self.models.append({"model": model, "integrator": integrator, "controller": controller})
        # Set initial conditions
        self.models[-1]["integrator"].set_initial_value(self.models[-1]["model"].get_state(), 0)
        self.num_models += 1

    def begin(self):
        # Get controller inputs from current states
        # Run integrator threads, update quadcopter states
        # Wait until maximum of threads finished or dt hit
        # Update gui
        # Repeat
        simulate = multiprocessing.Process(None, self.integration, args=(self.queue,))
        simulate.start()
        self.GUI = GUI(model=self.models[-1]["model"], queue=self.queue)

    def integration(self, queue):
        self.run = True
        while self.run:
            self.threads.clear()
            for i in range(0, len(self.models)):
                self.threads.append(threading.Thread(target=self.simulate_model, args=(i,)))
            for thread in self.threads:
                thread.start()
            #print("Threads started")
            for thread in self.threads:
                thread.join()
            #print("Threads done")
            queue.put(self.models[-1]["model"].get_state())

    def stop(self):
        self.run = False

    def simulate_model(self, i):
        inputs = self.models[i]["controller"].generate_inputs(self.models[i]["model"].get_state())
        self.models[i]["integrator"].set_f_params(inputs,)
        self.models[i]["model"].update(self.models[i]["integrator"].integrate(self.models[i]["integrator"].t + self.dt))
        time.sleep(0)