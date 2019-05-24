#!/usr/bin/env python
#

import setuptools
setuptools.setup(
	name="Netmax_AutoDetect_and_I2C_Mutex",
	description="Netmax Technologies Robot Autodetection and I2C Mutex Security",
	author="Netmax Technologies",
	url="http://www.Netmax.co.in/netmaxiot/",
	py_modules=['auto_detect_rpi', 'I2C_mutex', 'net_i2c', 'net_mutex','di_i2c','di_mutex'],
	install_requires=['smbus-cffi', 'pyserial', 'python-periphery', 'wiringpi'],
)
