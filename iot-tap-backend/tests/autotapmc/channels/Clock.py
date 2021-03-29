
from autotapmc.model.Channel import Channel

class Clock(Channel):
    inzone = 0

    def enable_enterzone(self):
        return not self.inzone

    def extaction_enterzone(self):
        self.inzone = 1

    def enable_leavezone(self):
        return self.inzone

    def extaction_leavezone(self):
        self.inzone = 0

    def ap_inzone(self):
        return self.inzone
