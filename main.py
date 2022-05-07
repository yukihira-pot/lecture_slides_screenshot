import pyautogui as gui
from time import sleep
import datetime
import glob
import cv2
import numpy as np
import os
from getpos import click_pos
from convert_to_pdf import pdf_convert

def mainfunc(year, month, date, hour, minute, top_x, top_y, bottom_x, bottom_y):
    dt = datetime.datetime(year, month, date, hour, minute)
    rect_area = (top_x, top_y, bottom_x - top_x, bottom_y - top_y)

    cur_dir = os.getcwd()
    dt_str = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    image_dir = cur_dir + "/images/" + dt_str + "/"
    os.makedirs("images", exist_ok=True)
    os.makedirs(image_dir, exist_ok=True)

    while datetime.datetime.now() < dt:
        sleep(5)
        print("screenshot will be saved after 30 seconds")
        screen_shot = gui.screenshot(region=rect_area)
        file_name = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + ".png"

        # file_base_dir = os.path.join(cur_dir, "images\\")
        # file_dir = os.path.join(file_base_dir )
        print(image_dir + file_name)
        screen_shot.save(image_dir + file_name)

        files = glob.glob(image_dir + "*")

        for i, file1 in enumerate(files):
            img1 = cv2.imread(file1)
            for j, file2 in enumerate(files):
                if i >= j:
                    continue
                try:
                    img2 = cv2.imread(file2)

                    img1_hist = cv2.calcHist([img1], [0], None, [256], [0, 256])
                    img2_hist = cv2.calcHist([img2], [0], None, [256], [0, 256])

                    if cv2.compareHist(img1_hist, img2_hist, 0) > 0.99999:
                        os.remove(file2)
                except FileNotFoundError:
                    pass
                files = glob.glob(image_dir + "*")

    pdf_convert(dt_str)
