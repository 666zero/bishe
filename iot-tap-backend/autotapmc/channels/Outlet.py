

from autotapmc.model.Channel import Channel


class Outlet(Channel):
    power = 0

    def enable_poweron(self):
        return not self.power

    def action_poweron(self):
        self.power = 1

    def enable_poweroff(self):
        return self.power

    def action_poweroff(self):
        self.power = 0

    def ap_on(self):
        return self.power
