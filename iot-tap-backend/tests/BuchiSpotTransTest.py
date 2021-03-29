

import autotapmc.buchi.Buchi as Buchi
import spot

sp = spot.translate('F q')
buchi = Buchi.spotToBuchi(sp)
buchi.log()
sp_back, state_map = buchi.toSpot()
print(sp_back.to_str())
