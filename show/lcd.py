from . import RPi_I2C_driver
from time import *

mylcd = RPi_I2C_driver.lcd()


## abc a:페이지 b:번호 c:하위번호

def show(n,indicator) :
    if n == 100:  ## 페이지1
        mylcd.lcd_display_string(indicator[0] + "1. Register ", 1)
        mylcd.lcd_display_string(indicator[1] + "2. Timer    ", 2)
    elif n == 111:  ## 1페이지 1번(사용자등록) 눌렀을 때
        mylcd.lcd_display_string(indicator[0] + "1. Regist   ", 1)
        mylcd.lcd_display_string(indicator[1] + "2. Delete   ", 2)
    elif n == 112:  ## 1페이지 1번(사용자등록) 옆페이지 눌렀을 때
        mylcd.lcd_display_string('>' + "3. Back     ", 1)
    elif n == 121:  ## 1페이지 2번(타이머) 눌렀을 때
        mylcd.lcd_display_string(indicator[0] + "1. Start    ", 1)
        mylcd.lcd_display_string(indicator[1] + "2. Quit     ", 2)
    elif n == 122: ## 1페이지 2번(타이머) 옆페이지 눌렀을 때
        mylcd.lcd_display_string('>' + "3. Back.    ", 1)
    elif n == 1.21: ## 1페이지 2번의 1번(시작하기) 눌렀을 때
        mylcd.lcd_display_string("Start timer", 1)
    elif n == 1.22: ## 1페이지 2번의 옆페이지 눌렀을 때
        mylcd.lcd_display_string("Stop timer.", 1)
        mylcd.lcd_display_string("Quit?", 2)
        sleep(3)
        mylcd.lcd_display_string(indicator[0] + "1. Yes      ", 1)
        mylcd.lcd_display_string(indicator[1] + "2. Back     ", 2)
    elif n == 200:   ## 페이지2
        mylcd.lcd_display_string(indicator[0] + "3. Sync     ", 1)
        mylcd.lcd_display_string(indicator[1] + "4. Back     ", 2)
    elif n == 210: ## 2페이지 3번
        mylcd.lcd_display_string(indicator[0] + "1. Upload   ", 1)
        mylcd.lcd_display_string(indicator[1] + "2. Back     ", 2)
    elif n == 211: ## 2페이지 3번 1번
        mylcd.lcd_display_string(indicator[0] + "1. Yes      ", 1)
        mylcd.lcd_display_string(indicator[1] + "2. No       ", 2)

def show_clock(timestr) :
    mylcd.lcd_display_string(timestr, 1)
    mylcd.lcd_display_string("Study Hard...", 2)