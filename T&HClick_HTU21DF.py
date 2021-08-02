from machine import I2C, Pin
import time


device = 0x40
regAddresstemp = 0xE3
regAddresshum = 0xE5
TO_READ = 6
buff = bytearray(6)

class HTU21DF():
    def __init__(self,i2c,addr=device):
        self.addr = addr
        self.i2c = i2c
        b = bytearray(1) 
        b[0] = 0 convert 
        self.i2c.writeto_mem(self.addr,0xE6,b) #enabled sensor ic by writing to control register 
        b[0] = 8
        self.i2c.writeto_mem(self.addr,0xE6,b) #0xE6 is POWER_CTL register
        
        
    def temperature(self):
        buff = self.i2c.readfrom_mem(self.addr,regAddresstemp,TO_READ) #read 6 bytes of data from register address
        temp=(buff[0] << 8) + buff[0] #Parse data
        return -46.85 + (175.72 * temp / 65536) #formula from datasheet
    
    def humidity(self):
        buff = self.i2c.readfrom_mem(self.addr,regAddresshum,TO_READ) #read 6 bytes of data from register address
        hum=(buff[0] << 8) + buff[0] #Parse data
        return -6 + (125.0 * hum/ 65536) #formula from datasheet
    
i2c = I2C("I2C_0") #Initialise I2C class
tandh=HTU21DF(i2c)
while True:
    t=tandh.temperature()
    h=tandh.humidity()
    print("HUMIDITY = %d rh \t TEMPERATURE = %d °C" % (h,t))
    




