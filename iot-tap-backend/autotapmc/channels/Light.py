


from autotapmc.model.Channel import Channel


class Light(Channel):
    power = 0
    color = 0

    def enable_turnon(self):
        return not self.power

    def action_turnon(self):
        self.power = 1

    def enable_turnoff(self):
        return self.power

    def action_turnoff(self):
        self.power = 0

    def enable_turnblue(self):
        return self.color != 0

    def action_turnblue(self):
        self.color = 0

    def enable_turnred(self):
        return self.color != 1

    def action_turnred(self):
        self.color = 1


class SimpleLight(Channel):
    power = 0

    def enable_turnon(self):
        return not self.power

    def action_turnon(self):
        self.power = 1

    def enable_turnoff(self):
        return self.power

    def action_turnoff(self):
        self.power = 0

    def ap_on(self):
        return self.power
