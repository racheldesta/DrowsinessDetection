import RPi.GPIO as GPIO
import time

vibration_pin = 17
tilt_pin = 26
ultrasonic_trigger_pin = 20
ultrasonic_echo_pin = 21
mq3_pin = 25
buzzer_pin = 27

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(vibration_pin, GPIO.IN)
GPIO.setup(tilt_pin, GPIO.IN)
GPIO.setup(ultrasonic_trigger_pin, GPIO.OUT)
GPIO.setup(ultrasonic_echo_pin, GPIO.IN)
GPIO.setup(mq3_pin, GPIO.IN)
GPIO.setup(buzzer_pin, GPIO.OUT)

def read_vibration():
    return GPIO.input(vibration_pin)

def read_tilt():
    return GPIO.input(tilt_pin)

def read_ultrasonic():
    GPIO.output(ultrasonic_trigger_pin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(ultrasonic_trigger_pin, GPIO.LOW)
  
    while GPIO.input(ultrasonic_echo_pin) == 0:
        pulse_start = time.time()
      
    while GPIO.input(ultrasonic_echo_pin) == 1:
        pulse_end = time.time()
      
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    return round(distance, 2)

def read_mq3():
    return GPIO.input(mq3_pin)

def activate_buzzer():
    GPIO.output(buzzer_pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(buzzer_pin, GPIO.LOW)

try:
    while True:
        vibration = read_vibration()
        tilt = read_tilt()
        ultrasonic = read_ultrasonic()
        mq3 = read_mq3()
        
        print("Vibration:", vibration)
        print("Tilt:", tilt)
        print("Ultrasonic Distance:", ultrasonic, "cm")
        print("MQ3:", mq3)
        print("-------------------------")
        
        if vibration == 1 or tilt == 1 or mq3 == 1:
            activate_buzzer()
        
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()