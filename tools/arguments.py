class Arguments:
    def __init__(self, raw_arguments):
        self.raw_arguments = raw_arguments

    def get_dict_arguments(self):
        complete_arguments = vars(self.raw_arguments)
        del complete_arguments['command']
        return complete_arguments
