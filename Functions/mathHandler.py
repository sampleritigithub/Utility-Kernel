##########################################
# MADE BY AI                             #
##########################################
import re, operator
allowed_operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '**': operator.pow,
    '^': operator.pow  
}
def safe_eval(expression):
    expression = expression.replace('^', '**')
    if not re.match(r'^[\d\s+\-*/^().]+$', expression):
        return "None"
    else:
        return str(eval(expression, {"__builtins__": None}, allowed_operators))
