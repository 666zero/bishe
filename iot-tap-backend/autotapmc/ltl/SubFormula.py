
from autotapmc.ltl.Operators import ops
from collections import deque


class Relation(object):
    def __init__(self, op, index_dest, fml_dest):
        self.op = op
        self.index_dest = index_dest
        self.fml_dest = fml_dest


class UnaryRelation(Relation):
    def __init__(self, op, index_dest, fml_dest, index_src, fml_src):
        super(UnaryRelation, self).__init__(op, index_dest, fml_dest)
        self.index_src = index_src
        self.fml_src = fml_src

    def log(self):
        return 'op=\'%s\', index_dest=%d, fml_dest=\'%s\', index_src=%d, fml_src=\'%s\'' % \
               (self.op, self.index_dest, self.fml_dest, self.index_src, self.fml_src)


class BinaryRelation(Relation):
    def __init__(self, op, index_dest, fml_dest, index_src1, fml_src1, index_src2, fml_src2):
        super(BinaryRelation, self).__init__(op, index_dest, fml_dest)
        self.index_src1 = index_src1
        self.fml_src1 = fml_src1
        self.index_src2 = index_src2
        self.fml_src2 = fml_src2

    def log(self):
        return 'op=\'%s\', index_dest=%d, fml_dest=\'%s\', index_src1=%d, fml_src1=\'%s\', ' \
               'index_src2=%d, fml_src2=\'%s\'' % (self.op, self.index_dest, self.fml_dest,
                                                   self.index_src1, self.fml_src1, self.index_src2, self.fml_src2)


def analyze(rna_formula):
    # return tuple (subformula list, subformula relation list)
    rna_formula = deque(rna_formula)
    stack = list()
    subformula_list = list()
    relation_list = list()

    while rna_formula:
        token = rna_formula.popleft()
        # print(token)
        # print(stack)
        if token in ops:
            if ops[token].n_args == 1:
                new_subformula = '%s (%s)' % (token, stack[-1])
                if new_subformula not in subformula_list:
                    subformula_list.append(new_subformula)
                rel = UnaryRelation(token, subformula_list.index(new_subformula),
                                    new_subformula, subformula_list.index(stack[-1]), stack[-1])
                relation_list.append(rel)
                stack[-1] = new_subformula
            elif ops[token].n_args == 2:
                new_subformula = '(%s) %s (%s)' % (stack[-2], token, stack[-1])
                if new_subformula not in subformula_list:
                    subformula_list.append(new_subformula)
                rel = BinaryRelation(token, subformula_list.index(new_subformula), new_subformula,
                                     subformula_list.index(stack[-2]), stack[-2],
                                     subformula_list.index(stack[-1]), stack[-1])
                relation_list.append(rel)
                stack.pop()
                stack[-1] = new_subformula
        else:
            if token not in subformula_list:
                subformula_list.append(token)
            stack.append(token)

    return subformula_list, relation_list
