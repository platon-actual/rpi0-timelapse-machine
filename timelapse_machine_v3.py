from picamera import PiCamera
from time import sleep

camera = PiCamera()

horas = 8
fotos_por_hora = 20

# camera.start_preview() # pero es HEADLESS


# for i in range (300):
for i in range(horas * fotos_por_hora):
	sleep(3600/fotos_por_hora)
	# sleep(60)
	camera.capture('/home/pi/fotos_timelapse/las_14hs__%03d.jpg' % i)

sleep(5)

print ("Timelapse finalizado. Mica, te amo <3")



