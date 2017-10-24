""" connect to network and print config """
import time
import network
import dht
import urequests
from machine import Pin

def setup_wifi():
    """
    Setup Wi-Fi connection

    connects to an hardcoded WPA network and returns only when
    connection is estabilished.
    Prints IP configuration before exiting
    """
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect('ESSID', 'password')
        while not sta_if.isconnected():
            pass

        print("network config:", sta_if.ifconfig())


def send_value(val):
    """
    Send value to remote host

    uses urequests to send a numeric value to an hardcoded host via
    HTTP POST, with a custom header 'Api_Key'.
    """
    tmp = urequests.post("http://192.168.1.4:5000/api",
                         headers={'Api_Key': 'Antani1234'}, data=str(val))
    tmp.close()


def setup_sensor():
    """
    Setup DHT22 sensor connected to pin 4.
    Waits for 5 seconds to avoid reading data too early
    """
    sensor = dht.DHT22(Pin(4))
    # sleep 5 seconds
    time.sleep(5)
    return sensor


def get_measure(sensor):
    """
    Read data from DHT sensor instance and print it to screen.
    :returns: dictionary with temperature and humidity readings
    """
    sensor.measure()
    time.sleep(5)
    temp = sensor.temperature()
    hum = sensor.humidity()
    print("Temp: %3.1f C" % temp)
    print("Humidity: %3.2f RH" % hum)
    return {'t':temp, 'h':hum}


def write_values(measure):
    """
    Write data on file.
    """
    with open('dati.txt', 'a+') as out_file:
        out_file.write('%f;%f\n' % (measure['t'], measure['h']))

def daicazzo():
    """ main loop """
    dht_sensor = setup_sensor()
    #setup_wifi()
    while True:
        measure = get_measure(dht_sensor)
        #send_value(measure['t'])
        write_values(measure)
        time.sleep(60)
