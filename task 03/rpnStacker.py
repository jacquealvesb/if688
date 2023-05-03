import sys
from TokenType import TokenType
from Regex import Regex

class RPNStacker:

    operations = {
        "+": lambda x, y : x + y,
        "-": lambda x, y : x - y,
        "*": lambda x, y : x * y,
        "/": lambda x, y : x / y
    }    
    
    def scan(self, inputFile):
        file = open(inputFile, "r")
        return Regex.toTokens(file.readlines())

    def evalTokens(self, tokens):
        first, second, fn = None, None, None

        for token in tokens:
            if token.type == TokenType.NUM:
                if first == None:
                    first = int(token.lexeme)
                elif second == None:
                    second = int(token.lexeme)

            elif token.type != TokenType.EOF:
                fn = self.operations[token.type.value]
            
            if first and second and fn:
                first = fn(first, second)
                second = None
                fn = None

        return first

    def eval(self, inputFile):
        tokens = self.scan(inputFile)
        return self.evalTokens(tokens)

rpnStacker = RPNStacker()
try:
    inputFile = sys.argv[1] if len(sys.argv) > 1 else "Calc1.stk"
    out = rpnStacker.eval(inputFile)
    print(out)
except Exception as error:
    print(error)