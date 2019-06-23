from automatabpp.automatabpp import LOGGER
from automatabpp.commandqueue.commandqueue import CommandQueue
from automatabpp.machine.machine import Machine
from automatabpp.metaclasses.singleton import Singleton


class Machines(object, metaclass=Singleton):

    def __init__(self):
        self.machines = []
        self.machine = None

    def add_new_machine(self, machine_name: str):
        self.machine = Machine(machine_name)
        self.machines.append(self.machine)
        return self.machine

    def execute_next(self):  # Some patterns could use this
        next_command = CommandQueue().get_next()
        if next_command is not None:
            self.execute_command(next_command)
            return True
        return False

    def execute_all(self):  # Should be used as default
        while len(CommandQueue()) > 0:
            self.execute_next()

    def execute_command(self, command: str):  # Not recommended if states can execute commands
        LOGGER.debug("Executing command [{}]".format(command))
        for machine in self.machines:
            machine.transition(command)

    def this_machine(self):
        return self.machine

    def reset_machines(self):
        for machine in self.machines:
            machine.reset_to_start()
