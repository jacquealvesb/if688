from enum import Enum

class TokenType(Enum):
    # Literals.
    NUM = "NUM"

    # Single-character tokens for operations.
    MINUS = "-"
    PLUS = "+"
    SLASH = "/" 
    STAR = "*"

    EOF = "EOF"