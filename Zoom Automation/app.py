import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime


def sign_in(meetingId, pswd):
    # Opens the zoom application
    subprocess.call([r'C:\\Users\Rohan\AppData\Roaming\Zoom\bin\Zoom.exe'])

    time.sleep(2)

    # Clicks the join button
    join_btn = pyautogui.locateCenterOnScreen('join_button.PNG')
    pyautogui.click(join_btn)

    time.sleep(2)

    # Enters the meeting Id
    pyautogui.press('enter')
    pyautogui.write(meetingId)
    # Hits the Join button
    join_btn_2 = pyautogui.locateCenterOnScreen('join_btn.PNG')
    pyautogui.click(join_btn_2)
    # Enter the meeting password
    time.sleep(2)
    pyautogui.press('enter')
    pyautogui.write(pswd)
    # Hits Join meeting
    join_meeting = pyautogui.locateCenterOnScreen('Join_Meeting.PNG')
    pyautogui.click(join_meeting)


# Reads the csv file
db = pd.read_csv('schedule.csv')

while True:
    now = datetime.now().strftime("%H:%M")
    if now in str(db['timings']):

        row = db.loc[db['timings'] == now]
        m_id = str(row.iloc[0, 1])
        m_pswd = str(row.iloc[0, 2])

        sign_in(m_id, m_pswd)
        time.sleep(40)
        print('signed in')
