import RPi.GPIO as GPIO
import time

class PWMController:
    def __init__(self, pin, start):
        print("Constructor")
        print(pin)
        self.pin = pin
        self.start = start
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(pin, 50)
        self.pwm.start(start) 
        time.sleep(0.1)
        

    def set_pwm(self, frequency, duty_cycle, duration):
        if self.pwm is not None:
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(duration)
            return 
        #self.pwm = GPIO.PWM(self.pin, frequency)
        #self.pwm.start(duty_cycle)
        #time.sleep(duration)
        
    # angle 0 for x axis is 6.6        
    def set_x_pwm(self, angle):
        self.pwm.ChangeDutyCycle(self.start - angle)
        #if self.pwm is not None:
        #    self.pwm.ChangeDutyCycle(6.6+angle)
        #    time.sleep(0.5)
        #    return 
        #self.pwm = GPIO.PWM(self.pin, frequency)
        #self.pwm.start(6.6) 
        #time.sleep(0.5)

    # angle 0 for y axis is 7.6
    def set_y_pwm(self, angle):
        self.pwm.ChangeDutyCycle(self.start - angle)
        #if self.pwm is not None:
        #    pwm.ChangeDutyCycle(7.6+angle)
        #    time.sleep(0.5)
        #    return 
        #self.pwm = GPIO.PWM(self.pin, frequency)
        #self.pwm.start(7.6)
        #time.sleep(0.5) 
        

    def cleanup(self):
        if self.pwm is not None:
            self.pwm.stop()
        GPIO.cleanup()

