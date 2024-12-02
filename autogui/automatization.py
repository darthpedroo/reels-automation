import pyautogui
import os
import time
import win32clipboard
import shutil 

from settings import ROOT_DIR

#print("Working dir:", os.getcwd())
#print("Files in here:", os.listdir("../tts_audios"))

#input()

BROWSE_BUTTON = os.path.join(ROOT_DIR, "autogui","browse.png")
RELOAD_BUTTON = os.path.join(ROOT_DIR, "autogui","reload.png")
CONVERT_BUTTON = os.path.join(ROOT_DIR, "autogui","convert.png")
SUCCES_BUTTON = os.path.join(ROOT_DIR, "autogui","success.png")
AUDIOS_HOMERO = os.path.join(ROOT_DIR, "audios_homero/")

def search_image(file_location:str, confidence=0.8):
    image_position = pyautogui.locateOnScreen(file_location, grayscale=True, confidence=confidence)
    return image_position


def process_audios_auto():
    
    TTS_AUDIOS_DIR = os.path.join(ROOT_DIR, "tts_audios")
    AMOUNT_OF_AUDIOS_TO_PROCESS = os.listdir(TTS_AUDIOS_DIR)
    LOCATION_TO_SAVE_FILES = r"E:\Darthpedro\ProyectosProgramacion\reels-automation\tts_audios"
    

    print("Proccesing audio: ", AMOUNT_OF_AUDIOS_TO_PROCESS)
    
    for audio in AMOUNT_OF_AUDIOS_TO_PROCESS:
        print("Proccesing audio: ", audio)
        browse_button_image = search_image(os.path.join(BROWSE_BUTTON))
        pyautogui.moveTo(browse_button_image)
        pyautogui.click()
        time.sleep(0.5)

        reload_button_image = search_image(RELOAD_BUTTON)
        pyautogui.moveTo(reload_button_image)
        pyautogui.moveRel(-100,0)
        pyautogui.click()

    #   print("XD")
    ##    print(LOCATION_TO_SAVE_FILES)
    #   print("XD")
        pyautogui.typewrite(LOCATION_TO_SAVE_FILES)
        pyautogui.keyDown("enter")
        pyautogui.moveRel(0,100)
        pyautogui.click()
        pyautogui.keyDown("f2")
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')  # ctrl-c to copy

        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
    #  print("DATA : ", data)


        pyautogui.click()

        time.sleep(0.5)
        convert_image = search_image(CONVERT_BUTTON, 0.9)
        pyautogui.moveTo(convert_image)
        pyautogui.click()

        succes = False

        while not succes:
            try:
                succes_image = search_image(SUCCES_BUTTON)
                succes = True
            except:
                print("Image not found")
                time.sleep(1)

        FILE = os.path.join(LOCATION_TO_SAVE_FILES, data)
        os.remove(FILE)

        WAV_FILE = data.strip(".mp3") + "_RVC_1.wav"

    #   print("XD")
    #   print(WAV_FILE)
    #  print("XD")

        WAV_FILE_DIR = os.path.join(LOCATION_TO_SAVE_FILES, WAV_FILE)

    #  print("DOP")
    #  print(WAV_FILE_DIR)
    #  print("DOP")

        shutil.move(WAV_FILE_DIR, AUDIOS_HOMERO + WAV_FILE)
        time.sleep(1)