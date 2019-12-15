import tkinter as tk

window = tk.Tk()
h = tk.DoubleVar()
w = tk.DoubleVar()
bmi = tk.DoubleVar()

def get_bmi():
    bmi.set(w.get() / (h.get()/100.0)**2.0)

tk.Label(window,
         width = 30,
         justify='center',
         text = "請輸入身高(公分):"
         ).pack(side = "top")

e1 = tk.Entry(window,
              width = 30,
              justify='center',
              textvariable = h
              ).pack(side = "top")

tk.Label(window,
         width = 30,
         justify='center',
         text = "請輸入體重(公斤):"
         ).pack(side = "top")

e2 = tk.Entry(window,
              width = 30,
              justify='center',
              textvariable = w
              ).pack(side = "top")

tk.Button(window,
          width = 20,
          bg = "#22FF88",
          text = "計算BMI",
          command = get_bmi
          ).pack(side = "top")

e3 = tk.Entry(window,
              width = 15,
              justify='center',
              textvariable = bmi
              ).pack(side = "top")

window.mainloop()
