inputFile = arg[1]
file = io.open(inputFile or "Calc1.stk")
fileIterator = file:lines()
lines = {}

for line in fileIterator do
    table.insert(lines, line)
end

operations = {}
operations["+"] = function(x,y) return x + y end
operations["-"] = function(x,y) return x - y end
operations["*"] = function(x,y) return x * y end
operations["/"] = function(x,y) return x / y end

first, second, op = None
i = 1
while i <= #lines do
    line = lines[i]

    if(first == None) then
        first = line
        i = i + 1
    elseif(second == None) then
        second = line
        i = i + 1
    elseif(op == None) then
        op = line
        i = i + 1
    end

    if(first and second and op) then
        fn = operations[op]
        first = fn(first, second)
        second = None
        op = None
    end
end

print(first)