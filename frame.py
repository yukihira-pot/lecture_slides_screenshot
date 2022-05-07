import tkinter as tk
from tkinter import ttk
import datetime
import calendar
import getpos
# from vars import recording_stop_time, top_x, top_y, bottom_x, bottom_y
from main import mainfunc

top_x = 0
top_y = 0
bottom_x = 0
bottom_y = 0

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.dt_now = datetime.datetime.now()
        master.geometry("600x200")
        master.title("Chot ScreenShot")
        self.rec_year = 0
        self.rec_month = 0
        self.rec_day = 0
        self.rec_hour = 0
        self.rec_minute = 0
        self.__top_x = 0
        self.__top_y = 0
        self.__bottom_x = 0
        self.__bottom_y = 0

        self.create_widgets()
        self.setvalue_widgets()
        self.setcurrentvalue_widgets()
        self.setpos_widgets()
        self.setbind_widgets()

    def change_date(self, event):
        def inner(self):
            last_day = calendar.monthrange(int(self.__cb_year.get()), int(self.__cb_month.get()))[1]
            if int(self.__cb_date.get()) > last_day:
                self.__cb_date.set(str(last_day).zfill(2))
            self.__cb_date.config(values=[str(date).zfill(2) for date in range(1, last_day+1)])
        return inner

    def create_widgets(self):
        self.year_list = [self.dt_now.year]
        self.month_list = [self.dt_now.month]
        self.date_list = [self.dt_now.day, self.dt_now.day + 1]
        self.hours_list = [str(date).zfill(2) for date in range(24)]
        self.minutes_list = [str(date).zfill(2) for date in range(60)]

        self.__label_datetime = ttk.Label(text="終了予定日時: ")
        self.__cb_year = ttk.Combobox(self.master, values=self.year_list, width=5, state='readonly')
        self.__cb_month = ttk.Combobox(self.master, values=self.month_list, width=5, state='readonly')
        self.__cb_date = ttk.Combobox(self.master, values=self.date_list, width=5, state='readonly')
        self.__label_space = ttk.Label(self.master, text=' ')
        self.__cb_hours = ttk.Combobox(self.master, values=self.hours_list, width=5, state='readonly')
        self.__cb_minutes = ttk.Combobox(self.master, values=self.minutes_list, width=5, state='readonly')
        self.__datetime_confirm_btn = tk.Button(self.master, text="確定")

        self.__label_slash1 = ttk.Label(self.master, text='/')
        self.__label_slash2 = ttk.Label(self.master, text='/')
        self.__label_colon1 = ttk.Label(self.master, text=':')
        self.__label_colon2 = ttk.Label(self.master, text=':')

        self.__label_area = ttk.Label(self.master, text="領域を選択")
        self.__area_top_btn = tk.Button(self.master, text="左上の座標を選択")
        self.__area_bottom_btn = tk.Button(self.master, text="右下の座標を選択")

        self.__recording_start_btn = tk.Button(self.master, text="スクショ開始")
    
    def click_pos_top(self, event):
        self.__top_x, self.__top_y = getpos.click_pos(event)
        print(self.__top_x, self.__top_y)

    def click_pos_bottom(self, event):
        self.__bottom_x, self.__bottom_y = getpos.click_pos(event)
    
    def set_year(self, event):
        self.rec_year = self.__cb_year.get()
    def set_month(self, event):
        self.rec_month = self.__cb_month.get()
    def set_day(self, event):
        self.rec_day = self.__cb_date.get()
    def set_hour(self, event):
        self.rec_hour = self.__cb_hours.get()
    def set_minute(self, event):
        self.rec_minute = self.__cb_minutes.get()
    def datetime_combine(self, event):
        self.set_year(event)
        self.set_month(event)
        self.set_day(event)
        self.set_hour(event)
        self.set_minute(event)
        year = int(self.rec_year)
        month = int(self.rec_month)
        date = int(self.rec_day)
        hour = int(self.rec_hour)
        minute = int(self.rec_minute)
        
        if year * month * date * hour * minute == 0: return
        dt = datetime.datetime(year, month, date, hour, minute)
        print(dt)
        return dt

    def recording_start(self, event):
        self.set_year(event)
        self.set_month(event)
        self.set_day(event)
        self.set_hour(event)
        self.set_minute(event)
        year = int(self.rec_year)
        month = int(self.rec_month)
        date = int(self.rec_day)
        hour = int(self.rec_hour)
        minute = int(self.rec_minute)
        print(self.__top_x, self.__top_y)
        mainfunc(year, month, date, hour, minute, top_x=self.__top_x, top_y=self.__top_y, bottom_x=self.__bottom_x, bottom_y=self.__bottom_y)


    def setbind_widgets(self):
        self.__cb_year.bind('<<ComboboxSelected>>', self.change_date)
        self.__cb_month.bind('<<ComboboxSelected>>', self.change_date)
        self.__datetime_confirm_btn.bind("<Button-1>", self.datetime_combine)
        self.__area_top_btn.bind("<Button-1>", self.click_pos_top)
        self.__area_bottom_btn.bind("<Button-1>", self.click_pos_bottom)
        self.__recording_start_btn.bind("<Button-1>", self.recording_start)

        self.__cb_year.bind("<<ComboboxSelected>>", self.set_year, add='+')
        self.__cb_month.bind("<<ComboboxSelected>>", self.set_month , add='+')
        self.__cb_date.bind("<<ComboboxSelected>>", self.set_day, add='+')
        self.__cb_hours.bind("<<ComboboxSelected>>", self.set_hour, add='+')
        self.__cb_minutes.bind("<<ComboboxSelected>>", self.set_minute, add='+')


    def setcurrentvalue_widgets(self):
        self.__cb_hours.current(self.dt_now.hour)
        self.__cb_minutes.current(self.dt_now.minute)

    def setvalue_widgets(self):
        self.__cb_year.set(self.year_list[0])
        self.__cb_month.set(self.month_list[0])
        self.__cb_date.set(self.date_list[0])
        self.__cb_hours.set(self.hours_list[0])
        self.__cb_minutes.set(self.minutes_list[0])

    def setpos_widgets(self):
        self.__label_datetime.grid(row=1, column=0)
        self.__cb_year.grid(row=1, column=1)
        self.__label_slash1.grid(row=1, column=2)
        self.__cb_month.grid(row=1, column=3)
        self.__label_slash2.grid(row=1, column=4)
        self.__cb_date.grid(row=1, column=5)
        self.__label_space.grid(row=1, column=6)
        self.__cb_hours.grid(row=1, column=7)
        self.__label_colon1.grid(row=1, column=8)
        self.__cb_minutes.grid(row=1, column=9)
        self.__label_colon2.grid(row=1, column=10)
        self.__label_area.grid(row=2, column=0)
        self.__area_top_btn.grid(row=2, column=1, columnspan=3)
        self.__area_bottom_btn.grid(row=2, column=4, columnspan=4)
        self.__datetime_confirm_btn.grid(row=1, column=12)
        self.__recording_start_btn.grid(row=3, column=5)

def main():
    window = tk.Tk()
    app = Application(master=window)
    app.mainloop()

if __name__ == "__main__":
    main()