

from autotapmc.channels.template.DbTemplate import template_dict
from autotapmc.analyze.Fix import generateCompactFix, generateNamedFix
from autotapmc.model.Tap import Tap

def printTap(tap):
    return 'IF %s WHILE %s, THEN %s' % (tap.trigger, str(tap.condition), str(tap.action))

def testall():
    print('----------------------------task16--------------------------------')
    ltl = '!(!F(bedroom_window.openclose_window_position=true & weather_sensor.is_it_raining_condition=true))'
    tap_dict = {'0': Tap(action='bedroom_window.openclose_window_position=false', condition=[], trigger='weather_sensor.is_it_raining_condition=true')}
    new_patch, label = generateNamedFix(ltl, tap_dict, init_value_dict={}, template_dict=template_dict)
    for patch, label in zip(new_patch, label):
        print(label, printTap(patch))
    print('------------------------------------------------------------------')
