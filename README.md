# Bluetooth Proximity Locker
A Python 3 program used to lock your PC when a specified Bluetooth device is a certain distance away.

# Installation
*Bluetooth Proximity Locking only runs on Linux.*
To install it, please run the following commands:  
`git clone https://github.com/mgrove36/bluetooth-proximity-locker.git`  
`cd bluetooth-proximity-locker`  
`chmod +x config`  
`./config [options]`

`[options]` must be 6 arguments long, corresponding to the following setup parameters:  
* Bluetooth address - `xx:xx:xx:xx:xx:xx`
* Scan period (how often BTPL should scan for device connectivity status) - a number, in seconds
* Left range command (the command that is run when your chosen device leaves the specified range) - a string (e.g. `"gnome-screensaver-command -l"`)
* Enters range command (the command that is run when your chosen device enters the specified range) - a string (e.g. `"gnome-screensaver-command -d"`)
* Maximum missed (the number of connectivity status that can be 'out of range' before your PC locks - an integer
* Range limit (the maximum range your device can be at before your PC locks) - an integer
  * The negative value of the range limit corresponds to the RSSI of your device

These arguments must be in order; if you wish to leave any of these parameters except Bluetooth address as the default (see below), use `x` as the option value.  

You are then free to start Bluetooth Proximity Locker at any time by running:  
* `btpl`,
* `btpl -r`, or
* `btpl --run`

In order to stop Bluetooth Proximity Locker, run:  
`btpl -s` or `btpl --stop`

# Defaults
* Bluetooth address has no default - it must be set by running the configuration file
* Scan period: `2.5`
* Left range command: `"gnome-screensaver-command -l"`
* Enters range command: `"gnome-screensaver-command -d"`
* Maximum missed: `3`
* Range limit: `7`

# Editing Configuration Later
In order to edit any configuration options later, from any folder, simply run:  
`btpl-reconfig [options]`  
Where `[options]` is the same as above, except `x` *can* be used as a value for the Bluetooth address, and `x` keeps the currently set value, instead of setting it to the default.
