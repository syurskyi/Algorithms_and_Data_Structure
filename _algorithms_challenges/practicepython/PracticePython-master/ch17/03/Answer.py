import tkinter as tk

window = tk.Tk()
oC = tk.DoubleVar()
oF = tk.DoubleVar()

def get_bmi():
    oF.set(oC.get() * (9.0/5.0) + 32.0)



tk.Label(window,
         width = 10,
         justify='center',
         text = "攝氏:"
         ).grid(
             row = 0,
             column = 0
             )

tk.Entry(window,
         width = 30,
         justify='center',
         textvariable = oC
         ).grid(
             row = 0,
             column = 1
             )

tk.Label(window,
         width = 10,
         justify='center',
         text = "華氏:"
         ).grid(
             row = 1,
             column = 0
             )

tk.Label(window,
         width = 20,
         justify='center',
         text = "0",
         textvariable = oF
         ).grid(
             row = 1,
             column = 1
             )

tk.Button(window,
          width = 10,
          bg = "#22FF88",
          text = "轉換",
          command = get_bmi
          ).grid(
             row = 2,
             column = 1
             )


window.mainloop()
