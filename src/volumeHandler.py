import spidev
import os 

spi = spidev.SpiDev()

def setup_adc(bus=0, device=0, max_speed=1350000):
	spi.open(bus, device)
	spi.max_speed_hz=max_speed

def read_adc(channel):
	if channel < 0 or channel > 7:
		return -1
	adc = spi.xfer2([1,(8+channel)<<4,0])
	data = ((adc[1]&3)<<8)+adc[2]
	return data
	
def set_volume(channel=0,max_value=1023):
	adc_value=read_adc(channel, max_value)
	volume=int((adc_value / max_value)*100)
	os.system(f"amixer sset 'Master' {volume}%")
	
def cleanup_adc():
	spi.close()
	

	
