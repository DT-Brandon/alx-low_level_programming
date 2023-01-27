#!/bin/bash
wget -P /tmp https://github.com/DT-Brandon/alx-low_level_programming/raw/master/0x18-dynamic_libraries/winmillions.so
export LD_PRLOAD=/tmp/winmillions.so
