import re
from Token import Token
from TokenType import TokenType

class Regex:

    def toTokens(lines):
        tokens = []

        if Regex.isNum(lines[0]):
            tokens.append(Token(TokenType.NUM, lines[0]))
        else:
            raise Exception("Error: Unexpected character: " + line)

        for i in range(1, len(lines), 2):
            line = lines[i] + (lines[i+1] if i+1 < len(lines) else '')
            result = re.match(r'\A([0-9]+)\n([\+\-\\\*])+\n?\Z', line)

            if result != None:
                num, op = result.groups()
                tokens.append(Token(TokenType.NUM, num))
                tokens.append(Token(TokenType(op), op))
            else:
                raise Exception("Error: Unexpected character: " + line.split('\n')[0])
        
        return tokens

    def isNum(token):
        reNum = re.compile(r'\d+\n?')
        return reNum.match(token)
    
    def isOP(token):
        reOP = re.compile(r'^[\+\-\\\*]$')
        return reOP.match(token)