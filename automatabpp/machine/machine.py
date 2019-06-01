from automatabpp import logger
from automatabpp.state.state import State
from automatabpp.constants import START_STATE_NAME


class Machine(object):

    def __init__(self, machine_name: str):
        self.machine_name = machine_name
        self.states = dict()
        self.curr_state = self.GetStateWithName(START_STATE_NAME)

    def GetActiveState(self):
        return self.curr_state

    def GetStateWithName(self, state_name: str):
        if state_name in self.states.keys():
            return self.states[state_name]
        self.states[state_name] = State(state_name, self.machine_name)
        return self.states[state_name]

    def AddTransition(self, st_before: str, command: str, st_after: str):
        self.GetStateWithName(st_before).SetTransition(command, st_after)

    def SetExecuteStateFunction(self, state_name: str, callback: callable):
        self.GetStateWithName(state_name).SetExecuteStateFunction(callback)

    def ExecuteTransition(self, command: str):
        st_after_name = self.curr_state.GetNextStateWithTransition(command)
        if st_after_name is not None:
            logger.debug("{}: state change {}->{}".format(self.machine_name, self.curr_state.GetName(), st_after_name))
            self.curr_state = self.GetStateWithName(st_after_name)
            self.curr_state.ExecuteState(command)
            return True
        return False

    def ReturnToStart(self):
        self.curr_state = self.GetStateWithName(START_STATE_NAME)
