import abc
#把需要tap的類儲存下來
#condition代表channel的标签
#把tap分为几类
class Tap(object):
    def __init__(self, action=str(), trigger: str=str(), condition: list=list(), invalid=False):
        """
        initialize a Tap object
        :param action: the action to be triggered, in the form of "channel.action"
        :param trigger: the event to trigger the TAP program. should be "channel.action" string
                        should be an empty string if this Tap only use state trigger
        :param condition: a list of conditions. each entry should be a "channel.ap" or "!channel.ap" string
        """
        # if action != '' and '.' not in action:
        #     raise Exception('Wrong format of action: %s' % action)
        # if trigger != '' and '.' not in trigger:
        #     raise Exception('Wrong format of trigger: %s' % trigger)
        # for cond in condition:
        #     if cond != '' and '.' not in cond:
        #         raise Exception('Wrong format of condition: %s' % cond)

        self.action = action
        self.trigger = trigger
        self.condition = condition
        self.invalid = invalid

    def __hash__(self):
        action_str = str(self.action)
        trigger_str = str(self.trigger)
        condition_str = str(self.condition)
        return hash((action_str, trigger_str, condition_str))

    def __eq__(self, other):
        return self.action == other.action and self.trigger == other.trigger and self.condition == other.condition

    def __ne__(self, other):
        return not self == other


class TapWrapper(object):
    @abc.abstractmethod
    def toTap(self):
        pass


class Rule(TapWrapper):
    def __init__(self, action):
        self.action = action

    @abc.abstractmethod
    def log(self):
        pass

    @abc.abstractmethod
    def toTap(self):
        pass

#把不同的Rule进行分类
class EERule(Rule):
    def __init__(self, trigger, action):
        self.trigger = trigger
        super().__init__(action)

    def log(self):
        return 'IF <%s>, THEN <%s>.' % (self.trigger, self.action)

    def toTap(self):
        return Tap(self.action, self.trigger, [])
#condition代表状态是多少的时候

class SERule(Rule):
    def __init__(self, condition, action):
        self.condition = condition
        super().__init__(action)

    def log(self):
        return 'IF [%s], THEN <%s>' % (self.condition, self.action)

    def toTap(self):
        return Tap(self.action, '', [self.condition])
#不同的类型进行组成

class SSERule(Rule):
    def __init__(self, condition1, condition2, action):
        self.condition1 = condition1
        self.condition2 = condition2
        super().__init__(action)

    def log(self):
        return 'IF [%s] AND [%s], THEN <%s>' % (self.condition1, self.condition2, self.action)

    def toTap(self):
        return Tap(self.action, '', [self.condition1, self.condition2])


class ESERule(Rule):
    def __init__(self, trigger, condition, action):
        self.trigger = trigger
        self.condition = condition
        super().__init__(action)

    def log(self):
        return 'IF <%s> WHILE [%s], THEN <%s>.' % (self.trigger, self.condition, self.action)

    def toTap(self):
        return Tap(self.action, self.trigger, [self.condition])

#condition代表有一个condition和state对应
def translateTapToRule(tap):
    if not isinstance(tap, Tap):
        raise TypeError('the input should be a Tap instance')
    if len(tap.condition) > 1:
        raise Exception('the rule is too many conditions for fixing')
    if not tap.trigger:
        raise Exception('fixing does not support state based rule currently')

    if tap.condition:
        return ESERule(tap.trigger, tap.condition[0], tap.action)
    else:
        return EERule(tap.trigger, tap.action)
