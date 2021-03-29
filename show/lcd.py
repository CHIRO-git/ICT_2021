import RPi_I2C_driver
from time import *

mylcd = RPi_I2C_driver.lcd()


## a.bc a:페이지 b:번호 c:하위번호

def show(n) :
    if n == 1:  ## 페이지1
        mylcd.lcd_display_string("1. 사용자 등록", 1)
        mylcd.lcd_display_string("2. 타이머", 2)
    elif n == 1.101:  ## 1페이지 1번(사용자등록) 눌렀을 때
        mylcd.lcd_display_string("1. 등록하기", 1)
        mylcd.lcd_display_string("2. 기존파일 삭제하기", 2)
    elif n == 1.102:  ## 1페이지 1번(사용자등록) 옆페이지 눌렀을 때
        mylcd.lcd_display_string("3. 돌아가기", 1)
    elif n == 1.201:  ## 1페이지 2번(타이머) 눌렀을 때
        mylcd.lcd_display_string("1. 시작하기", 1)
        mylcd.lcd_display_string("2. 종료하기", 2)
    elif n == 1.202: ## 1페이지 2번(타이머) 옆페이지 눌렀을 때
        mylcd.lcd_display_string("3. 돌아가기.", 1)
    elif n == 1.21: ## 1페이지 2번의 1번(시작하기) 눌렀을 때
        mylcd.lcd_display_string("타이머를 시작합니다.", 1)
    elif n == 1.22: ## 1페이지 2번의 옆페이지 눌렀을 때
        mylcd.lcd_display_string("타이머를 종료합니다.", 1)
        mylcd.lcd_display_string("종료합니까?", 2)
        sleep(3)
        mylcd.lcd_display_string("1. 네", 1)
        mylcd.lcd_display_string("2. 돌아가기", 2)
    elif n == 2:   ## 페이지2
        mylcd.lcd_display_string("3. 동기화", 1)
        mylcd.lcd_display_string("4. 돌아가기", 2)
    elif n == 2.3: ## 2페이지 3번
        mylcd.lcd_display_string("1. 동기화 진행.", 1)
        mylcd.lcd_display_string("2. 돌아가기", 2)
    elif n == 2.31: ## 2페이지 3번 1번
        mylcd.lcd_display_string("1. 예.", 1)
        mylcd.lcd_display_string("2. 아니요", 2)
