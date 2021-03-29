

from autotapmc.channels.Weather import Weather
from autotapmc.channels.GarageDoor import GarageDoor
from autotapmc.model.IoTSystem import IoTSystem
from autotapmc.model.Tap import ESERule
import autotapmc.buchi.Buchi as Buchi


class Test(IoTSystem):
    weather = Weather()
    door = GarageDoor()
    rule = ESERule('weather.startsRaining', 'door.open', 'door.close')


a = Test()
ts = a.transition_system

buchi_ts = Buchi.tsToGenBuchi(ts)
buchi_ltl = Buchi.ltlToBuchi('F (door.open & weather.raining)')

(buchi_final, pairs) = Buchi.product(buchi_ts, buchi_ltl)
buchi_ts.log()
buchi_ltl.log()
buchi_final.log()

group = [s2 for s1, s2 in pairs]

buchi_final.printToGv(group)

