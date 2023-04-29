class Token:
    def __init__(self, type, value):
        self.type = type
        self.lexeme = value

    def toString(self):
        return "Token [type=" + self.type.name + ", lexeme=" + self.lexeme + "]"