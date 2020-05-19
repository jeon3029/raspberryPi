# LED on-off by Code

### 구동 방법
```sh
1. C
    $ make
    $ ./blink_sw
2. Python
    $ python3 sw_led.py
# make clean : cleanup a.out files
```

### 동작 과정(C)
1. WiringSetup
2. gpio 설정 (pinMode -> SW, LED)
3. digitalWrite 로 출력(High or Low)

### 동작 과정(Python)
1. setmode 로 gpio설정
2. setup 로 out 설정(SW, LED)
3. output 로 출력(High or Low)

### 연결방법
- GPIO 17 에 led 연결, GPIO 4 에 switch 연결 /  5V & 220Ω 저항 사용
![led-pi](./pi_image.png)