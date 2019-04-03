#!/usr/bin/env python
# import required libraries
import subprocess
import bluetooth
import time
import sys
import os

# function for retrieving the RSSI of the desired bluetooth device
def getRSSI():
	# get output from terminal command that retrieves device name
	try:
	    rssi = subprocess.check_output('hcitool rssi [bluetooth address]', shell=True, stderr=subprocess.DEVNULL)
	except Exception as e:
	    rssi = str(e.output)

	# remove unwanted text from command output
	rssi = str(rssi).split("\\n")[0].replace("b","").replace("'","").replace("RSSI return value: ","")
	# return very small RSSI if device isn't connected, otherwise return the retrieved RSSI
	if (rssi == ""):
		return -255
	else:
		return int(rssi)

# ensure Bluetooth address has been provided as an argument
if len(sys.argv) < 2:
	print("Usage: btpl.py <bluetooth address>")
	sys.exit(1)

# time between searches for device, in seconds
scanPeriod = 2.5
# command to run when the device leaves desired range
leftRange = "gnome-screensaver-command -l"
# command to run when the device enters desired range
enteredRange = "gnome-screensaver-command -d"
# maximum number of times the device can be out of range before the PC is locked
maxMissed = 3
# range at which PC is locked (0 - rangeLimit = RSSI)
rangeLimit = 7
# get Bluetooth address of target device
BTAddress = sys.argv[1]
# initiate variables for use when processing RSSIs
status = "gone"
awayCounter = maxMissed
screenLocked = False
BTInRange = True
firstRun = True

# tell user the program is running
print("Identifying device...")

try:
	# display device name, with the first part bold & green
	print("\033[1;32m[OK]\033[0;37m Device found:", bluetooth.lookup_name(BTAddress,timeout=5))

	# run forever
	while True:
		# reset previous status, so screen status is only changed when status changes
		prev_status = status
		# retrieve the current RSSI of the bluetooth device
		rssi = getRSSI()
		# if device is close enough:
		if rssi > (0 - rangeLimit):
			status = "near"
			BTInRange = True
			screenLocked = False
			awayCounter = 0
			if (prev_status == "gone") and not(firstRun):
				os.system(enteredRange)
			if firstRun:
				firstRun = False

		# if device isn't in range, increment the away counter
		else:
			awayCounter += 1
			BTInRange = False
			# ensure correct status is set, as if awayCounter is greater than maxMissed, the status is set to *away*, when is should be *gone*
			if awayCounter >= maxMissed:
				status = "gone"
			else:
				status = "away"

		# if device has been away for too long:
		if awayCounter == maxMissed:
			status = "gone"
			BTInRange = False
			screenLocked = True
			# only run if a change in status has occured, to avoid unnecessary screen blanking
			if (status != prev_status):
				# lock screen
				os.system(leftRange)

		# print current Bluetooth data, with the first part bold & green
		print("\033[1;32m[OK]\033[0;37m RSSI:", rssi, "|", "Status:", status, "|", "Away counter:", awayCounter, "|", "Device in range:", BTInRange, "|", "Screen locked:", screenLocked, "|", time.strftime('%H:%M:%S'))

		# wait for specified time before checking device status again
		time.sleep(scanPeriod)

# usually happens when bluetooth is disabled
except:
	# display error message, with the first part bold & red
	print("\033[1;31m[ERROR]\033[0;37m Bluetooth on PC is not active")
