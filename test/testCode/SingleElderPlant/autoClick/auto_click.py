import pytesseract
from PIL import ImageGrab
import pygetwindow as gw
import pyautogui
import time
import pytesseract


# 设置 Tesseract 的路径
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # 根据你的 Tesseract 安装路径进行修改

# 检查特定窗口是否存在
def check_for_popup():
    for window in gw.getAllWindows():
        if all(keyword in window.title for keyword in ["警告", "個人"]):
            print("窗口存在...")
            return window
    return None

# 检查屏幕上是否有「繼續播放」文本
def check_continue_play_text():
    # 截取屏幕左半部分的图像
    screen_width, screen_height = pyautogui.size()
    screenshot = ImageGrab.grab(bbox=(0, 0, screen_width // 2, screen_height))
    # 使用 Tesseract 识别屏幕上的文本
    text = pytesseract.image_to_string(screenshot, lang='chi_tra')
    # 检查是否包含「繼續播放」
    if '繼續播放' in text:
        print("包含【繼續播放】文字")
        return True
    return False


# 点击「繼續播放」按钮
def click_continue_play_button():
    # 截取当前屏幕的图像
    screenshot = ImageGrab.grab()
    # 使用 Tesseract 识别屏幕上的文本
    text = pytesseract.image_to_string(screenshot, lang='chi_tra')
    # 寻找「繼續播放」文本的坐标
    for line in text.split('\n'):
        if '繼續播放' in line:
            # 假设文本位于屏幕中心，可以根据实际情况调整
            pyautogui.click(screenshot.width / 2, screenshot.height / 2)
            break

i = 0  # 初始化计数器
# 主循环
while True:
    if check_for_popup() and check_continue_play_text():
        print("找到弹出窗口，正在點擊【繼續播放】按钮...")
        click_continue_play_button()
        i = 0  # 如果找到弹出窗口并点击后，重置计数器
    else:
        print(f"未找到彈出窗口。計數: {i}")
        i += 1  # 增加计数器
    time.sleep(1)  # 每 1 秒检查一次
