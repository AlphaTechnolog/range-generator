from cli_app import Command
from tools.alphabet import Alphabet
from tools.arguments import Arguments

class GenAlphabet(Command):
    """Generate an alphabet range."""

    @staticmethod
    def register_arguments(parser):
        parser.add_argument('-s', '--start',
                            type=str,
                            default='a',
                            help='Starts with?')

        parser.add_argument('-e', '--end',
                            type=str,
                            default='z',
                            help='End with?')

    def get_arguments(self):
        arguments = Arguments(self.app.args)
        return arguments.get_dict_arguments()

    def get_alphabet(self, arguments):
        alphabet_generator = Alphabet(**arguments)
        alphabet = alphabet_generator.gen_alphabet()
        return alphabet

    def show_alphabet(self, alphabet_list):
        for item in alphabet_list:
            print(item, end=" ")
        print()

    def run(self):
        arguments = self.get_arguments()
        self.show_alphabet(self.get_alphabet(arguments))
