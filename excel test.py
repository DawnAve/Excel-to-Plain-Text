import pandas as pd
import tkinter as tk
from tkinter import filedialog

class Message:
    def __init__(self, serial, date, group_number, vehicle_type, vehicle_number, driver_name, phone, id_number, insurance_expiry, chassis_number, tare_weight, estimated_arrival, route, remarks):
        self.serial = serial  #序号
        self.date = pd.to_datetime(date).date()  #时间
        self.group_number = group_number   #组号
        self.vehicle_type = vehicle_type   #母子
        self.vehicle_number = vehicle_number   #车牌
        self.driver_name = driver_name   #司机
        self.phone = phone   #电话
        self.id_number = id_number  #身份证
        self.insurance_expiry = pd.to_datetime(insurance_expiry).date()  #保险到期
        self.chassis_number = chassis_number  #车架号
        self.tare_weight = tare_weight  #皮重
        self.estimated_arrival = estimated_arrival  #预计时间
        self.route = route  #路线
        self.remarks = remarks   #备注

    def __repr__(self):
        message = f"车牌: {self.vehicle_number}\n" \
                  f"皮重: {self.tare_weight}\n" \
                  f"姓名: {self.driver_name}\n" \
                  f"电话: {self.phone}\n" \
                  f"身份证: {self.id_number}\n"\
                  f"保险到期日期: {self.insurance_expiry}\n"
        return message



# 一个转换Excel序列号为日期的函数
def excel_date_converter(serial):
    if pd.isnull(serial):
        return None
    return pd.to_datetime('1900-01-01') + pd.to_timedelta(serial - 2, unit='D')

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
# 读取Excel文件
file_path = selected_file_path
df = pd.read_excel(file_path, converters={
    '日期': excel_date_converter,
    '保险到期日': excel_date_converter
})

# 创建Message对象列表
messages = [Message(*row) for row in df.itertuples(index=False, name=None)]
df['组号'] = df['组号'].ffill()
df['组号'] = df['组号'].astype(int).astype(str) # 将组号列转换为字符串类型

for message in messages:  
    print(message)
    print("---------------\n")
