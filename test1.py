import tkinter as tk
from tkinter import ttk
import datetime
import calendar


dt_now = datetime.datetime.now()

year_list = [dt_now.year]
month_list = [dt_now.month]
date_list = [dt_now.day, dt_now.day + 1]
hours_list = [str(date).zfill(2) for date in range(24)]
minutes_list = [str(date).zfill(2) for date in range(60)]
seconds_list = [str(date).zfill(2) for date in range(60)]

def change_date():
    def inner(self):
        last_day = calendar.monthrange(int(cb_year.get()), int(cb_month.get()))[1]
        if int(cb_date.get()) > last_day:
            cb_date.set(str(last_day).zfill(2))
        cb_date.config(values=[str(date).zfill(2) for date in range(1, last_day+1)])
    return inner

root = tk.Tk()
root.title('Chot ScreenShot')
root.geometry('500x200')

label_datetime = ttk.Label(text="終了予定日時: ")
label_datetime.grid(row=1, column=0)

cb_year = ttk.Combobox(root, values=year_list, width=5, state='readonly')
cb_year.set(year_list[0])
cb_year.bind('<<ComboboxSelected>>', change_date())
cb_year.grid(row=1, column=1)

label_slash = ttk.Label(root, text='/')
label_slash.grid(row=1, column=2)

cb_month = ttk.Combobox(root, values=month_list, width=5, state='readonly')
cb_month.set(month_list[0])
cb_month.bind('<<ComboboxSelected>>', change_date())
cb_month.grid(row=1, column=3)

label_slash = ttk.Label(root, text='/')
label_slash.grid(row=1, column=4)

cb_date = ttk.Combobox(root, values=date_list, width=5, state='readonly')
cb_date.set(date_list[0])
cb_date.grid(row=1, column=5)

label_space = ttk.Label(root, text=' ')
label_space.grid(row=1, column=6)

cb_hours = ttk.Combobox(root, values=hours_list, width=5, state='readonly')
cb_hours.set(hours_list[0])
cb_hours.current(dt_now.hour)
cb_hours.grid(row=1, column=7)

label_colon = ttk.Label(root, text=':')
label_colon.grid(row=1, column=8)

cb_minutes = ttk.Combobox(root, values=minutes_list, width=5, state='readonly')
cb_minutes.set(minutes_list[0])
cb_minutes.current(dt_now.minute)
cb_minutes.grid(row=1, column=9)

label_colon = ttk.Label(root, text=':')
label_colon.grid(row=1, column=10)

cb_seconds = ttk.Combobox(root, values=seconds_list, width=5, state='readonly')
cb_seconds.set(seconds_list[0])
cb_seconds.grid(row=1, column=11)

label_area = ttk.Label(text="領域を選択")
label_area.grid(row=2, column=0)



root.mainloop()