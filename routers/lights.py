from flask import Blueprint, render_template, request, redirect, session
from utils import light_handler

lightHandler = Blueprint("lights", __name__)

@lightHandler.route("/hue/<light>/<hue>", methods=["POST"])
def hue_route(light, hue):
    light_handler.change_light(light=str(light), on=True, hue=int(hue))
    resp = {
        "error": False, "output": "None"
    }

    return resp

@lightHandler.route("/bri/<light>/<brightness>", method=["POST"])
def bri_route(light, brightness):
    light_handler.change_light(light=str(light), on=True, brightness=int(brightness))
    resp = {
        "error": False, "output": "None"
    }

    return resp

