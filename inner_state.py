
def initialize():
    global command_counter
    command_counter = 0

    global last_sound
    last_sound = 0


class memory:

    def __init__(self):
        self.regs = {}

    def check(self, reg_name):
        if (reg_name not in self.regs):
            self.regs[reg_name] = 0
