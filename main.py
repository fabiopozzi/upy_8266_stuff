""" connect to network and print config """
import network
import dht
import time
from machine import Pin

def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.is_connected():
        sta_if.active(True)
        sta_if.connect('laSpadaNellaDoccia', 'GinoPilotino00')
        while not sta_if.isconnected():
            pass

        print("network config:", sta_if.ifconfig())


def setup_sensor()
    d = dht.DHT22(Pin(2))
    # sleep 5 seconds
    time.sleep(5)
    return d


def measure(dht):
    dht.measure()
    print("Temp: %3.1f C" % dht.temperature())
    print("Humidity: %3.2f RH" % dht.humidity())


