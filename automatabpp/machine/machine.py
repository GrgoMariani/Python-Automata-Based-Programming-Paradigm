from automatabpp.automatabpp import LOGGER
from automatabpp.constants import START_STATE
from automatabpp.state.state import State


class Machine(object):

    def __init__(self, machine_name: str):
        self.machine_name = machine_name
        self.states = dict()
        self.curr_state = self.get_state_by_name(START_STATE)

    def get_state_by_name(self, state_name: str):
        if state_name in self.states.keys():
            return self.states[state_name]
        self.states[state_name] = State(state_name, self.machine_name)
        return self.states[state_name]

    def add_transition(self, state_before: str, command: str, state_after: str):
        self.get_state_by_name(state_before).set_transition(command, state_after)

    def set_state_function(self, state_name: str, callback: callable):
        self.get_state_by_name(state_name).set_state_function(callback)

    def transition(self, command: str):
        st_after_name = self.curr_state.transition_to_next(command)
        if st_after_name is not None:
            LOGGER.debug("{}: state change {}->{}".format(self.machine_name, self.curr_state.get_name(), st_after_name))
            self.curr_state = self.get_state_by_name(st_after_name)
            self.curr_state.execute_state(command)
            return True
        return False

    def reset_to_start(self):
        self.curr_state = self.get_state_by_name(START_STATE)
