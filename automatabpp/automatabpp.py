import logging
from functools import wraps

LOGGER = logging.getLogger(__name__)

from .commandqueue.commandqueue import CommandQueue
from .comparisons.comparisons import COMPARISONS
from .constants import START_COMMAND, STOP_COMMAND, GRAPHS_DIRECTORY
from .machines.machines import Machines
from .xml.xmlread import read_graphml

__all__ = ["BEHAVIOUR", "EXECUTION", "OPERATION", "INTERFACE", "COMPARISONS", "LOGGER"]




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
            LOGGER.warning("Unknown format for reading the graph file: {}".format(graph_file_path))


class EXECUTION:

    @staticmethod
    def state(func):
        machine = Machines().this_machine()
        if machine is not None:
            machine.set_state_function(func.__name__, func)
        return func


class OPERATION:

    @staticmethod
    def start():
        Machines().execute_command(START_COMMAND)

    @staticmethod
    def stop():
        Machines().execute_command(STOP_COMMAND)
        Machines().reset_machines()
        CommandQueue().clear_all()

    @staticmethod
    def reset():
        OPERATION.stop()
        OPERATION.start()

    @staticmethod
    def run(cmd=None):
        if cmd is None:
            Machines().execute_all()
        else:
            Machines().execute_command(cmd)


class INTERFACE:

    @staticmethod
    def run_command_if_lambda_on_result_true(lambda_func: callable, command: str):
        def wrapper_out(func):
            @wraps(func)
            def wrapper_in(*args, **kwargs):
                result = func(*args, **kwargs)
                if lambda_func(result):
                    Machines().execute_command(command)
                return result

            return wrapper_in

        return wrapper_out
