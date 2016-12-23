#On reset, after boot.py, this file is called.

import network
import neopixel_christmas_tree as npTree
import gpio


#******************************************************************************	
def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect("SSID", "PWD")
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())


#******************************************************************************	
def main():

    #do_connect()
    #npTree.main()


#******************************************************************************	
if __name__ == "__main__":
    main()

