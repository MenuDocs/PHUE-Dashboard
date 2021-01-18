from phue import Bridge
from utils.secrets import BRIDGE_IP

bridge = Bridge(BRIDGE_IP)

bridge.connect()

lights = bridge.get_light_objects("name")

def get_lights():
    return lights

def change_light(light: str, on: bool=True, hue: str=None, saturation: int =255, brightness: int=255):
    if hue is not None:
        xy = hue.split()
        lights[light].xy = [float(xy[0]), float(xy[1])]
    
    lights[light].on = on
    lights[light].hue = hue
    lights[light].saturation = saturation
    lights[light].brightness = brightness

