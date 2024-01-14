
import time
import pyautogui
import time

def TokenBlaster():
    game_State = False
    if pyautogui.locateOnScreen('rc_items/TokenBlaster.png', confidence=0.9) != None:
        print("Token Blaster game start clicked")
        image = pyautogui.locateOnScreen('rc_items/TokenBlaster.png', confidence=0.9)
        if image != None:
            x, y = pyautogui.center(image)
            pyautogui.moveTo(x + 5, y + 20)
            time.sleep(1)
            pyautogui.click()

            time.sleep(7)

            if pyautogui.locateOnScreen('rc_items/start_game.png', confidence=0.9) != None:
                time.sleep(1)
                image = pyautogui.locateOnScreen('rc_items/start_game.png', confidence=0.9)
                if image != None:
                    x, y = pyautogui.center(image)
                    pyautogui.moveTo(x, y)
                    time.sleep(1)
                    pyautogui.click()
                    game_State = True
                    time.sleep(3)

    while game_State == True:
        try:
            aliens = pyautogui.locateAllOnScreen('rc_items/alienshipgreen.png', confidence=0.5)

            for alns in aliens:
                if alns != None:
                    x, y, w , h = alns
                    
                    pyautogui.moveTo(alns[0],alns[1])
                    pyautogui.mouseDown()
                    time.sleep(0.001)
                    break

                if pyautogui.locateOnScreen('rc_items/gain_power.png', confidence=0.9) != None:
                    Game_Playing = False
                    game_State = False

                if pyautogui.locateOnScreen('rc_items/quit.png', confidence=0.9) != None:
                    image = pyautogui.locateOnScreen('rc_items/quit.png', confidence=0.9)
                    if image != None:
                        print("quit button pressed")
                        x, y = pyautogui.center(image)
                        pyautogui.moveTo(x, y)
                        time.sleep(2)
                        pyautogui.click()

                    
                        Game_Playing = False
                        time.sleep(3)
        except:
            pass


    time.sleep(3)
    if pyautogui.locateOnScreen('rc_items/gain_power.png', confidence=0.9) != None:
        image = pyautogui.locateOnScreen('rc_items/gain_power.png', confidence=0.9)
        if image != None:
            x, y = pyautogui.center(image)
            pyautogui.moveTo(x, y)
            time.sleep(1)
            pyautogui.click()
            Game_Playing = False
            time.sleep(15)

            if pyautogui.locateOnScreen('rc_items/choose_game.png', confidence=0.9) != None:
                image = pyautogui.locateOnScreen('rc_items/choose_game.png', confidence=0.9)
                if image != None:
                    print("choose game button pressed")
                    x, y = pyautogui.center(image)
                    pyautogui.moveTo(x, y)
                    time.sleep(1)
                    pyautogui.click()
                    time.sleep(3)


TokenBlaster()