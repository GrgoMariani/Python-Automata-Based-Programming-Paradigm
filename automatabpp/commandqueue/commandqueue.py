from automatabpp.automatabpp import LOGGER
from automatabpp.metaclasses.singleton import Singleton


class CommandQueue(object, metaclass=Singleton):
    SEPARATOR = "\n"

    def __init__(self):
        self.__commands = []

    def __len__(self):
        return len(self.__commands)

    def get_next(self):
        if len(self) > 0:
            return self.__commands.pop(0)
        return None

    def push_commands(self, commands: str):
        for cmd in commands.split(CommandQueue.SEPARATOR):
            if len(cmd) > 0:
                LOGGER.debug("++++++> {} pushed to CommandQueue <++++++".format(cmd))
                self.__commands.append(cmd)

    def clear_all(self):
        self.__commands.clear()
