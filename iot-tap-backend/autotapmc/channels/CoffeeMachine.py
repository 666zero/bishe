
from autotapmc.model.Channel import Channel


class CoffeeMachine(Channel):
    status = 0
    # 0: idle, 1: poweroff, 2: wrong, 3: brewing, 4: finish

    def enable_turnon(self):
        return self.status == 1

    def action_turnon(self):
        self.status = 0

    def enable_turnoff(self):
        return self.status != 1 or self.status != 2

    def action_turnoff(self):
        if self.status == 0:
            self.status = 1
        elif self.status == 3 or self.status == 4:
            self.status = 2

    def enable_brew(self):
        return self.status == 0

    def action_brew(self):
        if self.status != 0:
            self.status = 2
        else:
            self.status = 3

    def enable_takeaway(self):
        return self.status == 4

    def action_takeaway(self):
        self.status = 0

    def tick(self):
        if self.status == 3:
            self.status = 4

    def ap_poweron(self):
        return self.status != 1

    def ap_brewing(self):
        return self.status == 3

    def ap_wrong(self):
        return self.status == 2


class SimpleCoffeeMachine(Channel):
    status = 0
    # 0: idle, 1: brewing, 2: wrong

    def enable_brew(self):
        return self.status == 0

    def action_brew(self):
        if self.status != 0:
            self.status = 2
        else:
            self.status = 1

    def tick(self):
        if self.status == 1:
            self.status = 0

    def ap_brewing(self):
        return self.status == 1

    def ap_wrong(self):
        return self.status == 2
