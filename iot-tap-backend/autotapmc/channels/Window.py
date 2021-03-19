
from autotapmc.model.Channel import Channel

class Window(Channel):
    open = 0

    def enable_open(self):
        return self.open == 0

    def action_open(self):
        self.open = 1

    def enable_close(self):
        return self.open == 1

    def action_close(self):
        self.open = 0

    def ap_open(self):
        return self.open
