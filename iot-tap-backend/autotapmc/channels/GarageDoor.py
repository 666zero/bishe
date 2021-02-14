
from autotapmc.model.Channel import Channel


class GarageDoor(Channel):
    door_open = 0

    def enable_open(self):
        return self.door_open == 0

    def action_open(self):
        self.door_open = 1

    def enable_close(self):
        return self.door_open == 1

    def action_close(self):
        self.door_open = 0

    def ap_open(self):
        return self.door_open

