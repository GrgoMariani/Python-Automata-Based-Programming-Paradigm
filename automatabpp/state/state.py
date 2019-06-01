from automatabpp import logger
from automatabpp.commandqueue.commandqueue import CommandQueue


class State(object):

    def __not_defined(self, **_):
        logger.debug("Machine:State [{}:{}] Execution not defined".format(self.machine_name, self.state_name))

    def __init__(self, state_name: str, machine_name: str):
        self.machine_name = machine_name
        self.state_name = state_name
        self.callback = self.__not_defined
        self.transitions = dict()
        self.after_execution_commands = list()

    def GetName(self):
        return self.state_name

    def SetExecuteStateFunction(self, callback: callable):
        self.callback = callback

    def SetTransition(self, command: str, next_state_name):
        self.transitions[command] = next_state_name

    def AddCommandToCallAfterExecution(self, cmd: str):
        if len(cmd) > 0:
            self.after_execution_commands.append(cmd)

    def ExecuteState(self, command):
        self.callback(command=command)
        for cmd in self.after_execution_commands:
            CommandQueue().PushCommandsToQueue(cmd)

    def GetNextStateWithTransition(self, command):
        if command in self.transitions.keys():
            return self.transitions[command]
        return None
