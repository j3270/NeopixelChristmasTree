"""****************************************************************************
* Module for Neopixel Christmas Tree Display
****************************************************************************"""

import machine, neopixel
import utime

NUM_PIXELS = 121 
HALF_NUM_PIXELS = NUM_PIXELS//2

rowOrginList = [0, 45, 80, 104, 117]
numPixelList = [45, 35, 24, 13, 4]

np = neopixel.NeoPixel(machine.Pin(4), NUM_PIXELS)

christmasColors = {
	0: (255, 0, 0),    #Red
	1: (0, 255, 0),    #Green
	2: (0, 0, 255),    #Blue
	3: (255, 140, 0),  #Orange
	4: (102, 0, 102),  #Puprle
    5: (0, 0, 0)       #off
}


#******************************************************************************
def get_random_color():
    """Returns pseudo random color from 'christmasColors' Dictionary"""

    randomVal = utime.ticks_cpu() % 5
    return christmasColors[randomVal]


#******************************************************************************
def get_random_pixel():
    """Returns pseudo random pixel between 0..NUM_PIXELS"""

    return (utime.ticks_cpu() % NUM_PIXELS)


#******************************************************************************
def fill_row(row, color):
    """"Fills row with given color
        row - row to fill (0..4)
        color - color from christmasColors dictionary
        Returns - none
    """

    idxStart = rowOrginList[row]
    numPixels = numPixelList[row]

    for idx in range(idxStart, (idxStart + numPixels)):
        np[idx] = color	


#******************************************************************************
def clear_display():
    """Clears display"""

    for idx in range(0, 5):
        fill_row(idx, christmasColors[5])


#******************************************************************************
def twinkle():
    """Randomly fills pixels with random color"""

    print("Twinkle Routine")
	
    delay_count = 0
    while(delay_count < 1000):
        np[get_random_pixel()] = get_random_color()
        np.write()
        utime.sleep_ms(10)
        delay_count = delay_count + 1

    random_color = get_random_color()
	
    for idx in range(0, NUM_PIXELS/2):
        np[idx] = random_color
        np[(NUM_PIXELS - 1) - idx] = random_color
        np.write()
        utime.sleep_ms(10)
		
    utime.sleep_ms(250)
	
    for idx in range(0, NUM_PIXELS/2):
        np[HALF_NUM_PIXELS + idx] = get_random_color()
        np[(HALF_NUM_PIXELS - 1) - idx] = get_random_color()
        np.write()
        utime.sleep_ms(10)


#******************************************************************************
def scroll_rows(color, loop, count):
    """Scrolls rows of pixels through 'christmasColors' dictionary"""
        
    print("Scroll Rows Routine")

    while(loop < count):

        color = loop % 5

        for row in range(0, 5):
            if(color > 4):
                color = 0
            fill_row(row, christmasColors[color])
            color = color + 1

        np.write()
        utime.sleep_ms(500)
        loop = loop + 1


#******************************************************************************
def chaser():
    """Fills display with color and then moves to next color with chasing
       effect
    """
    print("Chaser Routine""")
	
    for idx in range(0, NUM_PIXELS):
        np[idx] = get_random_color()
        np.write()
        utime.sleep_ms(25)
		
    for idy in range(0, 5):
        for idx in range(0, NUM_PIXELS):
            np[idx] = christmasColors[idy]
            np.write()
            utime.sleep_ms(25)
		
    for idx in range(0, NUM_PIXELS):
        np[idx] = get_random_color()
        np.write()
        utime.sleep_ms(25)


#******************************************************************************	
def dashed_chaser():
    """Fills display with all colors in linear segments, then shifts"""

    print("Dashed Chaser Routine""")
    color = 0
    loops = 130 * 3
	
    for idx in range(0, NUM_PIXELS):
        np[idx] = christmasColors[color]
        np.write()
        utime.sleep_ms(25)

        if(((idx + 1) % 26) == 0):
            color = color + 1
            if(color > 4):
                color = 0
	
    while(loops):
        loops = loops - 1
        temp = np[NUM_PIXELS - 1]
        for idx in range((NUM_PIXELS - 1), -1, -1):
            if(idx):
                np[idx] = np[idx -1]
        np[0] = temp
        np.write()
		

#******************************************************************************
def main():
    print("Starting NeoPixel Christmas Tree")
    while(1):
        twinkle()
        scroll_rows(0, 0, 25)
        chaser()
        dashed_chaser()


if __name__ == "__main__":
    main()


