from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

# Define the data structure
class Vitals(BaseModel):
    contactor_closed: bool
    vehicle_connected: bool
    session_s: int
    grid_v: float
    grid_hz: float
    vehicle_current_a: float
    currentA_a: float
    currentB_a: float
    currentC_a: float
    currentN_a: float
    voltageA_v: float
    voltageB_v: float
    voltageC_v: float
    relay_coil_v: float
    pcba_temp_c: float
    handle_temp_c: float
    mcu_temp_c: float
    uptime_s: int
    input_thermopile_uv: int
    prox_v: float
    pilot_high_v: float
    pilot_low_v: float
    session_energy_wh: float
    config_status: int
    evse_state: int
    current_alerts: list


def get_tasmota_current():
    url = "http://172.16.90.72/cm?cmnd=status%208"
    #{"StatusSNS":{"Time":"1970-01-01T17:54:20","ANALOG":{"Temperature":15.0},"ENERGY":{"TotalStartTime":"1970-01-01T00:00:00","Total":2.361,"Yesterday":0.000,"Today":2.361,"Power":2,"ApparentPower":13,"ReactivePower":12,"Factor":0.17,"Voltage":225,"Current":0.056},"TempUnit":"C"}}
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data["StatusSNS"]["ENERGY"]["Current"]
    except requests.RequestException as e:
        raise ValueError(f"Error fetching data from Tasmota device: {e}")

@app.get("/api/1/vitals")
async def get_vitals():
    try:
        current = get_tasmota_current()
    except ValueError as e:
        return {"error": str(e)}
    if current <= 4.5:
        charging = False
    else:
        charging = True
    vitals = Vitals(
        contactor_closed=charging,
        vehicle_connected=True,
        session_s=0,
        grid_v=229.2,
        grid_hz=49.828,
        vehicle_current_a=current,
        currentA_a=current,
        currentB_a=0.0,
        currentC_a=0.0,
        currentN_a=0.0,
        voltageA_v=233,
        voltageB_v=0.0,
        voltageC_v=0.0,
        relay_coil_v=11.9,
        pcba_temp_c=7.4,
        handle_temp_c=1.8,
        mcu_temp_c=15.2,
        uptime_s=26103,
        input_thermopile_uv=-176,
        prox_v=0.0,
        pilot_high_v=11.9,
        pilot_low_v=11.8,
        session_energy_wh=0.000,
        config_status=5,
        evse_state=1,
        current_alerts=[]
        # ... the other static stuf..contactor_closed=True,
    )
    return vitals
