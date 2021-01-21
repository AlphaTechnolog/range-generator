from cli_app import Command
from tools.number import Number
from tools.arguments import Arguments

class GenNumber(Command):
    """Generate a numbers list."""

    @staticmethod
    def register_arguments(parser):
        parser.add_argument('-s', '--start',
                            type=int,
                            default=1,
                            help='Starts with?')

        parser.add_argument('-e', '--end',
                            type=int,
                            default=10,
                            help='Ends with?')

    def get_arguments(self):
        arguments = Arguments(self.app.args)
        return arguments.get_dict_arguments()

    def get_numbers(self, arguments):
        numbers = Number(**arguments)
        return numbers.gen_numbers()

    def show_numbers(self, numbers):
        for item in numbers:
            print(item, end=' ')
        print()

    def run(self):
        arguments = self.get_arguments()
        self.show_numbers(self.get_numbers(arguments))
