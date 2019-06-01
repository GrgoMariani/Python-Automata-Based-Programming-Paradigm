from automatabpp import automata_bpp_logger
from automatabpp.metaclasses.singleton import Singleton
from automatabpp.machine.machine import Machine
from automatabpp.commandqueue.commandqueue import CommandQueue


class Machines(object, metaclass=Singleton):

    def __init__(self):
        self.__list_of_machines = []
        self.curr_machine_to_define = None

    def AddNewMachine(self, machine_name: str):
        self.curr_machine_to_define = Machine(machine_name)
        self.__list_of_machines.append(self.curr_machine_to_define)
        return self.curr_machine_to_define

    def ExecuteNextCommand(self):                   # Some patterns could use this
        next_command = CommandQueue().GetNextCommand()
        if next_command is not None:
            self.ExecuteCommand(next_command)
            return True
        return False

    def ExecuteAllCommands(self):                   # Should be used as default
        while len(CommandQueue()) > 0:
            self.ExecuteNextCommand()

    def ExecuteCommand(self, command: str):         # Not recommended if states can execute commands
        automata_bpp_logger.debug("Executing command [{}]".format(command))
        for machine in self.__list_of_machines:
            machine.ExecuteTransition(command)

    def _AddTransitionToCurrDefined(self, st_before: str, command: str, st_after: str):
        self.curr_machine_to_define.AddTransition(st_before, command, st_after)

    def GetCurrentDefinedMachine(self):
        return self.curr_machine_to_define

    def ReturnToStart(self):
        for machine in self.__list_of_machines:
            machine.ReturnToStart()
