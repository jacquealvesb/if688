import sys

inputFile = sys.argv[1] if len(sys.argv) > 1 else "Calc1.stk"
file = open(inputFile, "r")
lines = file.readlines()

def sum(x, y): return x + y
def sub(x, y): return x - y
def mul(x, y): return x * y
def div(x, y): return x / y

operations = {
    "+": sum,
    "-": sub,
    "*": mul,
    "/": div
}
 
i = 0
first, second, op = None, None, None
while i < len(lines):
    line = lines[i]

    if first == None:
        first = int(str.strip(line))
        i += 1
    elif second == None:
        second = int(str.strip(line))
        i += 1
    elif op == None:
        op = str.strip(line)
        i += 1
    
    if first and second and op:
        fn = operations[op]
        first = fn(first, second)
        second = None
        op = None

print(first)