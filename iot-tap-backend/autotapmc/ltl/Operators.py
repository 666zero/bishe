
class Operator(object):
    def __init__(self, op, n_args, precedence, associativity):
        self.op = op
        self.n_args = n_args
        self.precedence = precedence
        self.associativity = associativity


ops = {
    '!': Operator('!', 1, 3, 0),
    'U': Operator('U', 2, 2, 1),
    'V': Operator('V', 2, 2, 1),
    'X': Operator('X', 1, 3, 0),
    '&': Operator('&', 2, 1, 0),
    '|': Operator('|', 2, 1, 0)
}


re_splitter = r'(\s+|U|V|X|\(|\)|\&|\||!)'
