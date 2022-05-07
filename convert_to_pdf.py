import os
import img2pdf
from PIL import Image
import datetime

def pdf_convert(dt_str):
    pdf_fileName = "slides_{}.pdf".format(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
    png_folder = "images/" + dt_str + "/"
    extension  = ".png"
    pdf_folder = "pdf\\"

    with open(os.path.join(pdf_folder, pdf_fileName),"wb") as f:
        # 画像フォルダの中にあるPNGファイルを取得し配列に追加、バイナリ形式でファイルに書き込む
        f.write(
            img2pdf.convert(
                [Image.open(png_folder + j).filename for j in os.listdir(png_folder)if j.endswith(extension)]
            )
        )
