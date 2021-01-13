from phue import Bridge
from utils.secrets import BRIDGE_IP

bridge = Bridge(BRIDGE_IP)

birdge.connect()

lights = bridge.get_light_objects("name")

def get_lights():
    return lights

def change_lught(light: str, on: bool=True, hue: int=10, saturation: int =255, brightness: int=255):
    lights[light].on = on
    lights[light].hue = hue
    lights[light].saturation = saturation
    lights[light].brightness = brightness

