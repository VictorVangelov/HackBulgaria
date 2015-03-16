class CommandParser():

    def __init__(self):
        self.__commands = {}
        self.__descriptions = {}

    def add_command(self, command, function, description):
        self.__commands[command] = function
        self.__descriptions = description

    def execute(self,the_input):
        the_input = the_input.split(" ")
        command = the_input[0]
        argumets = the_input[1:]

        try:
            return self.__commands[command](*argumets)
        except KeyError:
            return " no such command"
        except TypeError:
            return self.__descriptions[command[0]]
