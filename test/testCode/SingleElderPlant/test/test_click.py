import pygetwindow as gw
import pyautogui
import time
from PIL import ImageGrab
import pytesseract

def check_for_popup():
    for window in gw.getAllWindows():
        if all(keyword in window.title for keyword in ["警告", "個人"]):
            print("窗口存在...")
            return window
    return None

def check_for_clickable_button(popup_window):
    # 獲取彈出視窗的截圖
    left, top, right, bottom = popup_window.left, popup_window.top, popup_window.right, popup_window.bottom
    screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
    # 使用 pytesseract 識別截圖中的文本
    data = pytesseract.image_to_data(screenshot, lang='chi_tra', output_type=pytesseract.Output.DICT)
    # 檢查是否存在按鈕文本
    for i, text in enumerate(data['text']):
        if '按鈕' in text:  # 假設按鈕上有「按鈕」字樣
            x = data['left'][i]
            y = data['top'][i]
            width = data['width'][i]
            height = data['height'][i]
            center_x = x + width // 2
            center_y = y + height // 2
            # 檢查按鈕是否可點擊
            if pyautogui.pixelMatchesColor(center_x, center_y, (r, g, b)):  # 替換 (r, g, b) 為按鈕顏色
                print("Yes")
                return True
    return False

while True:
    popup_window = check_for_popup()
    if popup_window:
        print("找到彈出視窗，檢查是否有可點擊的按鈕...")
        if check_for_clickable_button(popup_window):
            print("彈出視窗中有可點擊的按鈕。")
        else:
            print("彈出視窗中無可點擊的按鈕。")
    else:
        print("未找到彈出視窗。")
    time.sleep(10)
