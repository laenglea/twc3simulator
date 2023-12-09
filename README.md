# twc3simulator (Tesla Wall Box 3 Simulator)

This program simulates the API output of a Tesla Wallbox 3.

It basically just fakes the output while using information from a Tasmota device to fill the current.

I use this as a workaround to get evcc working with the mobile charger, as evcc requires a proper charger. The twc3 template is special because it lets evcc use Tesla's own api to start/stop and adjust the current level. 
