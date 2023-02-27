# picoAQI
pi pico air quality monitor
A air quality monitor based on the SGP30 air quality sensor, Raspberry Pi Pico microcontroller, AM2302 temperature and humidity sensor, and Nokia 5110 LCD display can be built using the following steps:



Connect the SGP30 air quality sensor to the Raspberry Pi Pico using jumper wires. Connect the VCC pin of the sensor to the 3.3V pin of the Pico, GND pin to the GND pin of the Pico, SCL pin to the GP21 pin of the Pico, and SDA pin to the GP20 pin of the Pico.

Connect the AM2302 temperature and humidity sensor to the Raspberry Pi Pico using jumper wires. Connect the VCC pin of the sensor to the 3.3V pin of the Pico, GND pin to the GND pin of the Pico, and the data pin to the GP16 pin of the Pico.

Connect the Nokia 5110 LCD display to the Raspberry Pi Pico using jumper wires. Connect the VCC pin of the display to the 3.3V pin of the Pico, GND pin to the GND pin of the Pico, CLK pin to the GP10 pin of the Pico, DIN pin to the GP11 pin of the Pico, CS pin to the GP12 pin of the Pico, and RST pin to the GP13 pin of the Pico.

Load the necessary libraries and code onto the Raspberry Pi Pico. You will need to install the adafruit-circuitpython-sgp30, adafruit-circuitpython-am2320, and adafruit-circuitpython-pcd8544 libraries for the SGP30 sensor, AM2302 sensor, and Nokia 5110 display respectively.


Test the air quality monitor by connecting it to a power source and monitoring the readings on the Nokia 5110 display.

Overall, building an air quality monitor with the SGP30 sensor, Raspberry Pi Pico microcontroller, AM2302 sensor, and Nokia 5110 display is a fun and educational project that can help you monitor the air quality in your surroundings.


