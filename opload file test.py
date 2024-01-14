import tkinter as tk
from tkinter import filedialog

def select_file():
    # 创建Tkinter根窗口
    root = tk.Tk()
    # 隐藏根窗口
    root.withdraw()
    # 弹出文件选择对话框，并获取选择的文件路径
    file_path = filedialog.askopenfilename()
    return file_path

# 调用函数，弹出对话框让用户选择文件
selected_file_path = select_file()

# 打印文件路径以确认
print(f"Selected file: {selected_file_path}")
