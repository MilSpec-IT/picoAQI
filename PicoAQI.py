





python
Copy code
import time
import board
import busio
import adafruit_sgp30
import adafruit_am2320
import adafruit_pcd8544

# Create I2C bus for SGP30 and AM2320 sensors
i2c = busio.I2C(board.GP21, board.GP20)

# Initialize SGP30 sensor
sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)

# Initialize AM2320 sensor
am2320 = adafruit_am2320.AM2320(i2c)

# Create SPI bus for Nokia 5110 display
spi = busio.SPI(board.GP11, board.GP10, board.GP12)
dc = board.GP13
cs = board.GP14
rst = board.GP15

# Initialize Nokia 5110 display
display = adafruit_pcd8544.PCD8544(spi, dc, cs, rst)

# Clear the display
display.fill(0)
display.show()

# Initialize SGP30 sensor and start measurement
sgp30.iaq_init()
sgp30.set_iaq_baseline(0x8973, 0x8aae)

# Display header on the Nokia 5110 display
display.text("Air Quality", 10, 0, 1)
display.line(0, 10, display.width, 10, 1)
display.show()

while True:
    # Read temperature and humidity from AM2320 sensor
    temperature_c, humidity = am2320.measurements

    # Read air quality data from SGP30 sensor
    eCO2, TVOC = sgp30.iaq_measure()

    # Print data to the console
    print("Temperature: ", temperature_c, "C")
    print("Humidity: ", humidity, "%")
    print("eCO2: ", eCO2, "ppm")
    print("TVOC: ", TVOC, "ppb")

    # Display data on the Nokia 5110 display
    display.fill(0)
    display.text("Temp: " + str(temperature_c) + " C", 0, 10, 1)
    display.text("Humidity: " + str(humidity) + " %", 0, 20, 1)
    display.text("eCO2: " + str(eCO2) + " ppm", 0, 30, 1)
    display.text("TVOC: " + str(TVOC) + " ppb", 0, 40, 1)
    display.show()

    # Wait for 1 second before taking another measurement
    time.sleep(1)
