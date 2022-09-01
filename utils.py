import os

class SiwssKnife:

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
