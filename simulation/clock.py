class SimulationClock:


    def __init__(self):

        self.current_time = 0


    def advance(self, minutes=1):

        self.current_time += minutes


    def get_time(self):

        return self.current_time
