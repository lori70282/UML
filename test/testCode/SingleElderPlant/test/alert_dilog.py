import tkinter as tk

def create_popup():
    popup = tk.Toplevel()  # 使用Toplevel而不是Tk創建新窗口
    popup.title("警告 - 個人")
    tk.Label(popup, text="這是內容").pack()
    tk.Button(popup, text="繼續播放", command=popup.destroy).pack(side=tk.LEFT, padx=10, pady=10)

def schedule_popup():
    create_popup()
    root.after(30000, schedule_popup)  # 每30秒調用一次schedule_popup

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # 隱藏主窗口
    schedule_popup()  # 首次調度彈跳視窗
    root.mainloop()  # 開始主事件循環
