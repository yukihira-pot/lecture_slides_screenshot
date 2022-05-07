from pynput import mouse #module pynputをインポート
import pyautogui #module pyautoguiをインポート 

#リスナー起動
def click_pos(event):
    #マウスイベントハンドラを定義
    def on_move(x, y):
        return
    def on_click(x, y, button, pressed):
        if pressed:
            return False
    def on_scroll(x, y, dx, dy):
        return
    with mouse.Listener(
            on_move=on_move,
            on_click=on_click,
            on_scroll=on_scroll
        ) as listener:
        listener.join()
    recttop_x, recttop_y = pyautogui.position()
    return recttop_x, recttop_y