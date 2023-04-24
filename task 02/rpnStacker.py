import sys
from Token import Token
from TokenType import TokenType

class RPNStacker:

    operations = {
        "+": lambda x, y : x + y,
        "-": lambda x, y : x - y,
        "*": lambda x, y : x * y,
        "/": lambda x, y : x / y
    }    

    def getLines(self, inputFile):    
        file = open(inputFile, "r")
        return file.readlines()
    
    def scan(self, inputFile):
        lines = self.getLines(inputFile)
        tokens = []

        first, second, op = None, None, None
        for line in lines:
            line = str.strip(line)

            if first == None:
                try:
                    first = int(line)
                    tokens.append(Token(TokenType.NUM, line))
                except:
                    raise Exception("Error: Unexpected character: " + line)
                
            elif second == None:
                try:
                    second = int(line)
                    tokens.append(Token(TokenType.NUM, line))
                except:
                    raise Exception("Error: Unexpected character: " + line)

            elif op == None:
                op = line
                if op in self.operations:
                    tokens.append(Token(TokenType(op), op))
                else:
                    raise Exception("Error: Unexpected character: " + op)
            
            if first and second and op:
                second = None
                op = None
        
        return tokens

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