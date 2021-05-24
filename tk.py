import tkinter as tk
import time
import threading
from threading import Thread
import keyboard
import subprocess
class Test():
    def __init__(self):
        self.np = np = tk.Label(text="Таймер фуриона")
        self.npt = npt = tk.Label(text="00:00")
        pg = tk.Label(text="Таймер пуджа")
        self.pgt = pgt = tk.Label(text="00:00")
        es = tk.Label(text="Таймер земели")
        self.est = est = tk.Label(text="00:00")
        sk = tk.Label(text="Таймер санд кинг")
        self.skt = skt = tk.Label(text="00:00")
        vm = tk.Label(text="Таймер веник")
        self.vmt = vmt = tk.Label(text="00:00")
        ty = tk.Label(text="Таймер тини")
        self.tyt = tyt = tk.Label(text="00:00")
        np.grid(row=0,column=0)
        npt.grid(row=1,column=0)
        pg.grid(row=0,column=1)
        pgt.grid(row=1,column=1)
        es.grid(row=0,column=2)
        est.grid(row=1,column=2)
        sk.grid(row=0,column=3)
        skt.grid(row=1,column=3)
        vm.grid(row=0,column=4)
        vmt.grid(row=1,column=4)
        ty.grid(row=0,column=5)
        tyt.grid(row=1,column=5)
        self.take_a_key()

    def thread(func):
        def wrapper(*args, **kwargs):
            current_thread = threading.Thread(
                target=func, args=args, kwargs=kwargs)
            current_thread.start()

        return wrapper

    @thread
    def take_a_key(self):
        def np():
            for i in range(60):
                self.npt.config(text=f"00:{i}")
                time.sleep(1)
            subprocess.run("Msg lexa324sa Пора ебашить фуру")
            self.npt.config(text="00:00")
        def pg():
            for i in range(60):
                self.pgt.config(text=f"00:{i}")
                time.sleep(1)
            subprocess.run("Msg lexa324sa Пора ебашить пуджа")
            self.pgt.config(text="00:00")
        def es():
            for i in range(60):
                self.est.config(text=f"00:{i}")
                time.sleep(1)
            subprocess.run("Msg lexa324sa Пора ебашить спирита")
            self.est.config(text="00:00")
        def sk():
            for i in range(60):
                self.skt.config(text=f"00:{i}")
                time.sleep(1)
            subprocess.run("Msg lexa324sa Пора ебашить санд кинга")
            self.skt.config(text="00:00")
        def vm():
            for i in range(60):
                self.vmt.config(text=f"00:{i}")
                time.sleep(1)
            subprocess.run("Msg lexa324sa Пора ебашить веника")
            self.vmt.config(text="00:00")
        def ty():
            for i in range(60):
                self.tyt.config(text=f"00:{i}")
                time.sleep(1)
            subprocess.run("Msg lexa324sa Пора ебашить тиника")
            self.tyt.config(text="00:00")
        th1 = Thread(target=np)
        th2 = Thread(target=pg)
        th3 = Thread(target=es)
        th4 = Thread(target=sk)
        th5 = Thread(target=vm)
        th6 = Thread(target=ty)
        keyboard.add_hotkey('Ctrl+1', lambda:th1.start())
        keyboard.add_hotkey('Ctrl+2', lambda:th2.start())
        keyboard.add_hotkey('Ctrl+3', lambda:th3.start())
        keyboard.add_hotkey('Ctrl+4', lambda:th4.start())
        keyboard.add_hotkey('Ctrl+5', lambda:th5.start())
        keyboard.add_hotkey('Ctrl+6', lambda:th6.start())
        keyboard.add_hotkey('Ctrl+F1', lambda:window.destroy())
        keyboard.wait()

window = tk.Tk()
window.attributes("-topmost",True)
window.geometry("675x60+1235+0")
obj = Test()
window.mainloop()
