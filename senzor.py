import RPi.GPIO as GPIO
import time

#Definisanje GPIO pinova
GPIO_TRIGGER=23
GPIO_ECHO=24

#Postavljanje moda za GPIO pinove
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)

def measure_distance():
    #Slanje ultrazvucnog impulsa
    GPIO.output(GPIO_TRIGGER,True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER,False)

    start_time=time.time()
    stop_time=time.time()

    #Biljezenje vremena pocetka i kraja odziva
    while GPIO.input(GPIO_ECHO)==0:
        start_time=time.time()

    while GPIO.input(GPIO_ECHO)==1:
        stop_time=time.time()

    #Izracunavanje trajanja pulsa i udaljenosti
    time_elapsed=stop_time-start_time
    distance=(time_elapsed*34300)/2

    return distance

def cleanup():
    GPIO.cleanup()
