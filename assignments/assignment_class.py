class Food:
    def __init__(self, name=None, kind=None):
        self.name = name
        self.kind = kind

    @classmethod
    def describe(cls, name=None, kind=None):
        print(f'{name} is a {kind}')

Food().describe('Elder', 'wizard')