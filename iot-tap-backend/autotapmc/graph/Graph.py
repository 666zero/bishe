import json
class graph(object):
    # vertices 包含三个元素 trigger, condition, action
    def __init__(self):
        self.rulelists = list();

    def appendRule(self, rule):
        self.rulelists.append(self, rule);

    def log(self):
        for rule in  self.rulelists:
            print("规则集合如下:trigger 为%s, condition为%s, action为%s",
                  str(rule.trigger), str(rule.condition), str(rule.action))



class node(object):
    # param: type为-1,0,1,2
    # param: data存储trigger,action,condition三种类型
    type = -1
    def __init__(self, type, data):
        self.type = type;
        if self.type == 0:
            self.trigger = data;
        elif self.type == 1:
            self.condition = data;
        elif self.type == 2:
            self.action = data;

class rule(object):
    def __init__(self):
        self.trigger = list();
        self.condition = list();
        self.action = list();

    def append(self, trigger, condition, action):
        self.trigger.append(trigger);
        self.condition.append(condition);
        self.action.append(action);
