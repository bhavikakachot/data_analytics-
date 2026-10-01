import tkinter as tk
# window app
root=tk.Tk()
# title
root.title("window app data")
# crate geometry
root.geometry("550x450")
# write a label on window
label=tk.Label(text="my name is abc",fg="blue",bg="white",font=("Arial",16))
label.pack(pady=20)
# add button widget
button=tk.Button(text="submit",bg="blue",fg="white",font=("Arial",18))
button.pack(pady=20)
# crate output
tk.mainloop()