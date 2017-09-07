""" connect to network and print config """
import time
import network
import dht
from machine import Pin

def setup_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect('ESSID', 'password')
        while not sta_if.isconnected():
            pass

        print("network config:", sta_if.ifconfig())


def setup_sensor():
    d = dht.DHT22(Pin(4))
    # sleep 5 seconds
    time.sleep(5)
    return d


def measure(sensor):
    sensor.measure()
    time.sleep(5)
    print("Temp: %3.1f C" % sensor.temperature())
    print("Humidity: %3.2f RH" % sensor.humidity())


def daicazzo():
    setup_wifi()
    dht = setup_sensor()
    while True:
        measure(dht)
        time.sleep(5)
