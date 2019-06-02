__all__ = ["BEHAVIOUR", "EXECUTION", "OPERATION", "INTERFACE", "COMPARISONS"]

import logging
automata_bpp_logger = logging.getLogger(__name__)

from . machines.machines import Machines
from . xml.xmlread import read_graphml
from . commandqueue.commandqueue import CommandQueue
from . constants import GRAPHS_DIRECTORY, START_COMMAND_NAME, STOP_COMMAND_NAME
from . comparisons.comparisons import COMPARISONS

from functools import wraps


class BEHAVIOUR:

    @staticmethod
    def set_default_graph_directory(new_path: str):
        global GRAPHS_DIRECTORY
        GRAPHS_DIRECTORY = new_path

    @staticmethod
    def load_behaviour_from_graph(graph_file_path: str, machine_name: str):
        if graph_file_path[-8:] == ".graphml":
            read_graphml("{}/{}".format(GRAPHS_DIRECTORY, graph_file_path), machine_name)
        else:
            automata_bpp_logger.warning("Unknown format for reading the graph file: {}".format(graph_file_path))


class EXECUTION:

    @staticmethod
    def state(func):
        current_machine = Machines().GetCurrentDefinedMachine()
        if current_machine is not None:
            current_machine.SetExecuteStateFunction(func.__name__, func)
        return func


class OPERATION:

    @staticmethod
    def start_fsm():
        Machines().ExecuteCommand(START_COMMAND_NAME)

    @staticmethod
    def stop_fsm():
        Machines().ExecuteCommand(STOP_COMMAND_NAME)
        Machines().ReturnToStart()
        CommandQueue().EmptyAllCommands()

    @staticmethod
    def reset_fsm():
        OPERATION.stop_fsm()
        OPERATION.start_fsm()

    @staticmethod
    def run_fsm(cmd=None):
        if cmd is None:
            Machines().ExecuteAllCommands()
        else:
            Machines().ExecuteCommand(cmd)


class INTERFACE:

    @staticmethod
    def run_command_if_lambda_on_result_true(lambda_func: callable, command: str):
        def wrapper_out(func):
            @wraps(func)
            def wrapper_in(*args, **kwargs):
                result = func(*args, **kwargs)
                if lambda_func(result):
                    Machines().ExecuteCommand(command)
                return result
            return wrapper_in
        return wrapper_out
