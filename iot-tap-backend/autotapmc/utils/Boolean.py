
from autotapmc.utils.Parser import parse, Operator

ops = {
    '!': Operator('!', 1, 3, 0),
    '&': Operator('&', 2, 1, 0),
    '|': Operator('|', 2, 1, 0)
}

re_splitter = r'(\s+|\(|\)|\&|\||!)'


def calculateBoolean(formula, var_dict):
    """
    given boolean variable value, calculate the value of a boolean formula (!, &, |, brackets are supported)
    :param formula: the formula
    :param var_dict: var_name->value dictionary
    :return:
    """
    token_list = parse(formula, ops, re_splitter)
    stack = list()
    for token in token_list:
        if token == '!':
            stack[-1] = not stack[-1]
        elif token == '&':
            stack[-2] = stack[-1] and stack[-2]
            stack.pop()
        elif token == '|':
            stack[-2] = stack[-1] or stack[-2]
            stack.pop()
        elif token in var_dict:
            stack.append(var_dict[token])
        elif token == '0':
            stack.append(False)
        elif token == '1':
            stack.append(True)
        else:
            raise Exception('Unknown AP token %s in edge formula' % token)
    if len(stack) != 1:
        raise Exception('Wrong edge AP formula format!')

    return stack[0]
