import sys

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

    def eval(self, inputFile):
        lines = self.getLines(inputFile)

        i = 0
        first, second, op = None, None, None
        while i < len(lines):
            line = str.strip(lines[i])

            if first == None:
                first = int(line)
                i += 1
                
            elif second == None:
                second = int(line)
                i += 1
                
            elif op == None:
                op = line
                i += 1
            
            if first and second and op:
                fn = self.operations[op]
                first = fn(first, second)
                second = None
                op = None

        return first

rpnStacker = RPNStacker()
inputFile = sys.argv[1] if len(sys.argv) > 1 else "Calc1.stk"
out = rpnStacker.eval(inputFile)
print(out)