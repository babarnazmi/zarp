from commands import getoutput
import sys, os
import util

#
# scan for wireless APs.  useful when searching for WEP or unprotected APs.
# This is essentially an interface to airodump-ng because its output is better
# than anything i could come up with.
#
def initialize():
	try:
		if not util.check_program('airmon-ng'):
			print '[-] airomon-ng not installed.  Please install to continue.'
			return
		print '[!] (cntrl^c) when finished.'
		iface = util.get_monitor_adapter()
		if iface is None:
			print '[!] No devices found in monitor mode.  Enabling...'
			iface = util.enable_monitor()
		print '[dbg] using interface %s'%iface
		ap_scan(iface)
	except Exception, KeyboardInterrupt:
		return

#
# Sniff on the monitoring adapter 
#
def ap_scan(adapt):
	try:
		print '[!] Scanning for access points...'
		os.system('airodump-ng %s'%adapt)
	except KeyboardInterrupt:
		util.disable_monitor()
		print '[!] Exiting..'
	util.disable_monitor()
