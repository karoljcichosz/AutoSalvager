# poznajdowac buttony na poczatku funkcji
import os

import pyautogui
import pydirectinput
import time
import autoit
from datetime import datetime
from pynput import keyboard


def on_press(key):
    if 'char' in dir(key):     #check if char method exists,
        if key.char == 'r':
            print("xDr")
            os._exit(1)


listener = keyboard.Listener(on_press=on_press)
listener.start()

def clickOnMap(who):
    pydirectinput.keyDown("tab")
    button = pyautogui.locateCenterOnScreen(who, confidence=.8)
    click(button.x,button.y)
    pydirectinput.keyUp("tab")
    autoit.mouse_move(1,1)

def click(x,y, button="left"):
    autoit.mouse_move(x, y)
    autoit.mouse_down(button)
    time.sleep(0.2)
    autoit.mouse_up(button)

def goToHorseSeller():
    # otworz i kliknij na mapie
    clickOnMap("resources\\horse_seller_hd.png")
    # otworz kupowanie rzeczy
    button = None
    while button == None:
        if datetime.now().second%4==0:
            clickOnMap("resources\\horse_seller_hd.png")
        button = pyautogui.locateCenterOnScreen("resources\\barding.png", confidence=.8)
    click(button.x,button.y)


def buyItem(item, item_ch):
    itemTile = pyautogui.locateOnScreen(item, confidence=.8)
    if itemTile == None:
        itemTile = pyautogui.locateOnScreen(item_ch, confidence=.8)
    purchases = pyautogui.locateAllOnScreen("resources\\purchase.png", confidence=.8)
    for button in purchases:
        if itemTile.left < button.left < itemTile.left + itemTile.width and itemTile.top < button.top < itemTile.top + itemTile.height:
            emptyinv = pyautogui.locateCenterOnScreen("resources\\no_space.png", confidence=.8)
            while emptyinv == None:
                click(button.left + round(button.width / 2), button.top + round(button.height / 2))
                time.sleep(0.1)
                pydirectinput.press("enter")
                emptyinv = pyautogui.locateCenterOnScreen("resources\\no_space.png", confidence=.8)
                time.sleep(0.1)
            continue
    pydirectinput.press("esc")
    pydirectinput.press("esc")
    autoit.mouse_move(1,1)


def goToSmith():
    autoit.mouse_move(1,1)
    # otworz i kliknij na mapie
    clickOnMap("resources\\smith.png")
    # otworz kupowanie rzeczy
    button = None
    while button == None:
        if datetime.now().second%4==0:
            clickOnMap("resources\\smith.png")
        button = pyautogui.locateCenterOnScreen("resources\\salvage_items.png", confidence=.8)
    click(button.x,button.y)

def salvageItems(item):
    time.sleep(1)
    autoit.mouse_move(1,1)
    time.sleep(0.2)
    itemTiles = list(pyautogui.locateAllOnScreen(item, confidence=.92))
    counter = 0
    while len(itemTiles)>0:
        while counter < 6 and len(itemTiles)>0:
            item=itemTiles.pop()
            click(item.left + round(item.width / 2), item.top + round(item.height / 2),"right")
            time.sleep(0.2)
            counter = counter + 1
        counter = 0
        button = pyautogui.locateCenterOnScreen("resources\\salvage_btn.png", confidence=.9)
        click(button.x,button.y)
        time.sleep(0.2)
        button = None
        while button is None:
            button = pyautogui.locateCenterOnScreen("resources\\confirm_salvage.png", confidence=.9)
        click(button.x,button.y)
        time.sleep(0.2)
        button = None
        while button is None:
            button = pyautogui.locateOnScreen("resources\\job_done.png", confidence=.85)
        click(button.left+round(button.width/2),button.top+button.height)
        time.sleep(0.2)
    pydirectinput.press("esc")
    pydirectinput.press("esc")


print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)
print(0)
while True:
    goToHorseSeller()
    buyItem("resources\\item1.png","resources\\item1_ch.png")
    goToSmith()
    salvageItems("resources\\item1_sal.png")

