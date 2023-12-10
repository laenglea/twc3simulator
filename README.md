# twc3simulator (Tesla Wall Box 3 Simulator)

This program simulates the API output of a Tesla Wallbox 3.

It basically just fakes the output while using information from a Tasmota device to fill the current.

![](media/api.png)

I use this as a workaround to get evcc working with the mobile charger, as evcc requires a proper charger. The twc3 template is special because it lets evcc use Tesla's own api to start/stop and adjust the current level. 


## requirements

- Tasmota outlet to grep the current from. - Something like https://amzn.eu/d/3biI2E2

## Installation

first clone it to the machine you want to run it

    git clone https://github.com/laenglea/twc3simulator.git


## set the correct ip of your tasmota device

    cd twc3simulator
    
for this edit the script and set the proper ip address

    vim main.py
    
## run it

to run it native you have to first install the requirements with pip or your package manager

native:

    pip3 install -r requirements.txt
    sudo uvicorn app.main:app --reload --host 0.0.0.0 --port 80

via docker:

    docker build -t twc3simulator .
    docker run --name twc3simulator -p 80:80 twc3simulator
    
## validate

if it's running properly you should get something back when looking at

http://<ip>/api/1/vitals
