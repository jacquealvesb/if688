import re

class Regex:

    def isNum(token):
        reNum = re.compile(r'\d+')
        return reNum.match(token)
    
    def isOP(token):
        reOP = re.compile(r'^[\+\-\\\*]$')
        return reOP.match(token)