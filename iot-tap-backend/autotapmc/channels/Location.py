

from autotapmc.model.Channel import Channel


class Location(Channel):
    within = 0

    def enable_walkin(self):
        return self.within == 0

    def extaction_walkin(self):
        self.within = 1

    def enable_walkout(self):
        return self.within == 1

    def extaction_walkout(self):
        self.within = 0

    def ap_within(self):
        return self.within
