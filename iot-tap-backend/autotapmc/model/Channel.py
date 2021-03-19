import copy


class MetaChannel(type):
    def __new__(cls, name, parent, dct):
        action_dict = dict()
        enable_dict = dict()
        ap_dict = dict()
        state_dict = dict()
        ext_action_list = list()

        # TODO: we need to do something to enable timer operation in actions
        for key, value in dct.items():
            if key.startswith('enable_') and callable(value):
                enable_dict[key[7:]] = value
            elif key.startswith('action_') and callable(value):
                action_dict[key[7:]] = value
            elif key.startswith('extaction_') and callable(value):
                action_dict[key[10:]] = value
                ext_action_list.append(key[10:])
            elif key.startswith('ap_') and callable(value):
                ap_dict[key[3:]] = value
            elif (isinstance(value, int) or isinstance(value, float) or isinstance(value, str)) \
                    and not isinstance(value, bool):
                state_dict[key] = value

        for key, value in action_dict.items():
            if key not in enable_dict:
                raise Exception('action %s needs a corresponding enable function' % key)

        for key, value in enable_dict.items():
            if key not in action_dict:
                raise Exception('enable function %s needs a corresponding action function' % key)

        dct['action_dict'] = action_dict
        dct['enable_dict'] = enable_dict
        dct['ap_dict'] = ap_dict
        dct['state_dict'] = state_dict
        dct['ext_action_list'] = ext_action_list

        return super().__new__(cls, name, parent, dct)


class Channel(metaclass=MetaChannel):
    def __init__(self):
        # transforming class attributes into instance attributes
        for key, value in self.__class__.__dict__.items():
            super().__setattr__(key, copy.deepcopy(value))

    def __setattr__(self, key, value):
        if key in super().__getattribute__('state_dict'):
            super().__getattribute__('state_dict')[key] = value
        else:
            super().__setattr__(key, value)

    def __getattribute__(self, key):
        if key in super().__getattribute__('state_dict'):
            return self.state_dict[key]
        else:
            return super().__getattribute__(key)

    def __deepcopy__(self, memodict=dict()):
        cls = self.__class__
        new_one = cls.__new__(cls)
        for key, value in super(Channel, self).__getattribute__('__dict__').items():
            super(cls, new_one).__setattr__(key, copy.deepcopy(value))
        return new_one

    def lengthOfStates(self):
        return len(self.state_dict)
#打包一个元组，然后进行分类
    def restoreFromStateVector(self, field):
        if len(field) != len(self.state_dict):
            raise Exception('Length of state vector does not match with channel state length')
        keys = [tup[0] for tup in sorted(self.state_dict.items())]
        for key, value in zip(keys, field):
            self.state_dict[key] = value
#每个设备的属性代表一个状态
    def saveToStateVector(self):
        state_list = [item[1] for item in sorted(self.state_dict.items())]
        return state_list


def generateChannelFromTemplate(template_list, channel_name):
    with open('channels/autogen/%s.py' % channel_name, 'w') as fp:
        fp.write('from model.Channel import Channel\n\n\n')
        fp.write('class %s(Channel):\n' % channel_name)
        for template in template_list:
            fp.write(template.definitionGenerator() + '\n\n')
            for ap in template.apGenerator():
                fp.write(ap + '\n\n')
            for event in template.eventGenerator():
                fp.write(event + '\n\n')
            fp.write('\n')
        fp.flush()
