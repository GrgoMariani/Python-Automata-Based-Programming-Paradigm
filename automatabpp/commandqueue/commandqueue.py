from automatabpp.automatabpp import automata_bpp_logger
from automatabpp.metaclasses.singleton import Singleton


class CommandQueue(object, metaclass=Singleton):
    SEPARATOR = "\n"

    def __init__(self):
        self.__list_of_cmds_to_execute = []

    def __len__(self):
        return len(self.__list_of_cmds_to_execute)

    def GetNextCommand(self):
        if len(self) > 0:
            return self.__list_of_cmds_to_execute.pop(0)
        return None

    def PushCommandsToQueue(self, commands: str):
        for cmd in commands.split(CommandQueue.SEPARATOR):
            if len(cmd) > 0:
                automata_bpp_logger.debug("++++++> {} pushed to CommandQueue <++++++".format(cmd))
                self.__list_of_cmds_to_execute.append(cmd)

    def EmptyAllCommands(self):
        self.__list_of_cmds_to_execute.clear()

