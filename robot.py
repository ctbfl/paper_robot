from time import sleep
from gpiozero import DistanceSensor
import RPi.GPIO as GPIO
import time
import signal
import atexit
import cv2

img1 = cv2.imread("gaoxing.jpg")
img2 = cv2.imread("xiaoku.jpg")
img3 = cv2.imread("wuyu.jpg")
img4 = cv2.imread("haipa.jpg")
img5 = cv2.imread("nu.jpg")
img6 = cv2.imread("shengqi.jpg")

out_win = "output_style_full_screen"
cv2.namedWindow(out_win, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(out_win, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)


atexit.register(GPIO.cleanup)
duo1 = 14
pin_hong1=25
duo2 = 27
duo3=22
pin_an1=24
GPIO.setmode(GPIO.BCM)
GPIO.setup(duo1,GPIO.OUT,initial=False)
GPIO.setup(duo2,GPIO.OUT,initial=False)
GPIO.setup(duo3,GPIO.OUT,initial=False)
GPIO.setup(pin_an1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pin_hong1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
p1=GPIO.PWM(duo1,50)	#50HZ:频率就是周期脉冲的周期的倒数
p1.start(0)
p2=GPIO.PWM(duo2,50)	#50HZ:频率就是周期脉冲的周期的倒数
p2.start(0)
p3=GPIO.PWM(duo3,50)	#50HZ:频率就是周期脉冲的周期的倒数
p3.start(0)
a=1
while True:
    p3.ChangeDutyCycle(8)
    status = GPIO.input(pin_an1)
    statu = GPIO.input(pin_hong1)
    if statu == True:
        p2.ChangeDutyCycle(8)
    else:
        p2.ChangeDutyCycle(3)
    time.sleep(0.1)
    if status == False:
        a=a+1
        if a == 2:
            cv2.imshow(out_win, img2)
            cv2.waitKey(500)
            p1.ChangeDutyCycle(8)
        elif a == 3:
            cv2.imshow(out_win, img3)
            cv2.waitKey(500)
            p1.ChangeDutyCycle(8)
        elif a == 4:
            cv2.imshow(out_win, img4)
            cv2.waitKey(500)
            p1.ChangeDutyCycle(8)
        elif a == 5:
            cv2.imshow(out_win, img5)
            cv2.waitKey(500)
            p1.ChangeDutyCycle(8)
        elif a == 6:
            cv2.imshow(out_win, img6)
            cv2.waitKey(500)
            a=1
            p1.ChangeDutyCycle(8)
    else:
        p1.ChangeDutyCycle(3)
        cv2.imshow(out_win, img1)
        cv2.waitKey(500)
    
    time.sleep(0.5)
    p3.ChangeDutyCycle(3)