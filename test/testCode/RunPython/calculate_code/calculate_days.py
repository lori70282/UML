import tkinter as tk
from datetime import datetime, timedelta

#日曆天計算公式

def calculate_days():
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()
    days_to_add = int(days_to_add_entry.get())
    try:
        start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
        end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')
        days = (end_date_obj - start_date_obj).days
        new_date = (start_date_obj + timedelta(days=days_to_add)).strftime('%Y-%m-%d')
        result_label.config(text=f"開始日期：{start_date}\n結束日期：{end_date}\n日曆天共計：{days} 天\n開始日期加上 {days_to_add} 天後的日期為：{new_date}")
    except ValueError:
        result_label.config(text="日期格式錯誤，請使用 YYYY-MM-DD 格式")

# 創建主視窗
root = tk.Tk()
root.title("日期計算器")

# 創建輸入框和標籤
tk.Label(root, text="開始日期 (YYYY-MM-DD):").grid(row=0, column=0)
start_date_entry = tk.Entry(root)
start_date_entry.grid(row=0, column=1)

tk.Label(root, text="結束日期 (YYYY-MM-DD):").grid(row=1, column=0)
end_date_entry = tk.Entry(root)
end_date_entry.grid(row=1, column=1)

tk.Label(root, text="天數:").grid(row=2, column=0)
days_to_add_entry = tk.Entry(root)
days_to_add_entry.grid(row=2, column=1)

# 創建計算按鈕和結果標籤
calculate_button = tk.Button(root, text="計算", command=calculate_days)
calculate_button.grid(row=3, column=0, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

# 運行主循環
root.mainloop()
