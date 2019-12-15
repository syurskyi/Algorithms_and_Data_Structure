import tkinter as tk
import tkinter.messagebox

def alert():
    tk.messagebox.askquestion(title='我的對話方塊', message='Hello, World!')
    

window = tk.Tk()
window.geometry('200x100')
btn1 = tk.Button(window, text="顯示訊息", command=alert)
btn1.pack()
window.mainloop

