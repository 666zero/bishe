

from autotapmc.model.Channel import Channel


class Weather(Channel):
    rain = 0

    def enable_startsRaining(self):
        return self.rain == 0

    def extaction_startsRaining(self):
        self.rain = 1

    def enable_stopsRaining(self):
        return self.rain == 1

    def extaction_stopsRaining(self):
        self.rain = 0

    def ap_raining(self):
        return self.rain
