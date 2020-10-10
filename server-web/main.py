from server import *
import tkinter as tk

master = tk.Tk()
tk.Label(master,
         text="Adress").grid(row=0)
tk.Label(master,
         text="Port").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.insert(0, "")
e2.insert(0, 8888)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)


tk.Button(master,
          text='Quit',
          command=master.quit).grid(row=3,
                                    column=0,
                                    sticky=tk.W,
                                    pady=4)
tk.Button(master,
          text='Show', command=lambda: lauchServer(int(e2.get()), e1.get())).grid(row=3,
                                                       column=1,
                                                       sticky=tk.W,
                                                       pady=4)

tk.mainloop()