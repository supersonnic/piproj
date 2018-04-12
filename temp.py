import Adafruit_DHT
 
def readSensor(arg):
    
    # Set sensor type : Options are DHT11,DHT22 or AM2302
    sensor=Adafruit_DHT.DHT11
 
    # Set GPIO sensor is connected to
    gpio=4
 
    # Use read_retry method. This will retry up to 15 times to
    # get a sensor reading (waiting 2 seconds between each retry).
    humidity, temperature = Adafruit_DHT.read(sensor, gpio)
 
    # Reading the DHT11 is very sensitive to timings and occasionally
    # the Pi might fail to get a valid reading. So check if readings are valid.
    if arg=='t' and humidity is not None:
        return(temperature)
      
    if arg=='h' and temperature is not None:
        return(humidity)