from automatabpp.automatabpp import LOGGER
from automatabpp.commandqueue.commandqueue import CommandQueue


class State(object):

    def __not_defined(self, **_):
        LOGGER.debug("Machine:State [{}:{}] Execution not defined".format(self.machine_name, self.name))

    def __init__(self, state_name: str, machine_name: str):
        self.machine_name = machine_name
        self.name = state_name
        self.callback = self.__not_defined
        self.transitions = dict()
        self.post_commands = list()

    def get_name(self):
        return self.name

    def set_callback(self, callback: callable):
        self.callback = callback

    def set_transition(self, command: str, next_state_name):
        self.transitions[command] = next_state_name

    def add_post_command(self, cmd: str):
        if len(cmd) > 0:
            self.post_commands.append(cmd)

    def execute_state(self, command):
        self.callback(command=command)
        for cmd in self.post_commands:
            CommandQueue().push_commands(cmd)

    def transition_to_next(self, command):
        if command in self.transitions.keys():
            return self.transitions[command]
        return None
