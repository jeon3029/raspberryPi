# LED on-off by Code

### 구동 방법
```sh
1. C
    $ make
    $ ./gpio_pwm
2. Python
    $ python3 gpio_pwm.py
# make clean : cleanup a.out files
```

### 동작 과정(C)
1. WiringSetup
2. gpio 설정 (pinMode)
3. digitalWrite 로 출력(High or Low)
4. pwmWrite 로 밝기 설정


### 동작 과정(Python)
1. setmode 로 gpio설정
2. setup 로 out 설정
3. output 로 출력(High or Low)
4. GPIO.PWM.changeDutyCycle 을 통해 밝기 설정

### 연결방법
- GPIO 18 에 led 연결  /  3.3V & 220Ω 저항 사용
![led-pi](./pi_image.png)