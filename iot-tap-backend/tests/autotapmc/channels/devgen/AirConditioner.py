from autotapmc.model.Template import BoolCapTemplate, NumericCapTemplate


def generateAirConditionerChannel(crit_value_list, init_value=None):
    if not init_value:
        init_value = crit_value_list[0]
    power_template = BoolCapTemplate('power', False)
    thermostat_template = NumericCapTemplate(crit_value_list, 'thermostat', init_value=init_value)
    return [power_template, thermostat_template]
