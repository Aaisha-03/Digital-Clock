import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Advanced Digital Clock")
root.geometry("600x350")
root.configure(bg="black")

# Functions 
def update_time():
    time_string = strftime('%I:%M:%S %p' if is_12_hour.get() else '%H:%M:%S')
    label_time.config(text=time_string)

    date_string = strftime('%A, %d %B %Y')  # Day, Date Month Year
    label_date.config(text=date_string)

    label_time.after(1000, update_time)

def toggle_format():
    is_12_hour.set(not is_12_hour.get())
    update_time()

def change_bg(*args):
    color = selected_color.get()
    root.configure(bg=color)
    label_time.configure(bg=color)
    label_date.configure(bg=color)
    btn_frame.configure(bg=color)

#  For Widgets 
is_12_hour = tk.BooleanVar(value=True)  # Default 12-hour format

label_time = tk.Label(root, font=("TT Ricordi Allegria", 50, "bold"), background="black", foreground="Blue")
label_time.pack(anchor="center", pady=10)

label_date = tk.Label(root, font=("Algerian", 28, "bold "), background="black", foreground="#50C878")
label_date.pack(anchor="center")

# Buttons & Color Options
btn_frame = tk.Frame(root, bg="black")
btn_frame.pack(pady=20)

toggle_btn = tk.Button(btn_frame, text="Toggle 12/24 Hr", command=toggle_format, bg="black", fg="white")
toggle_btn.grid(row=0, column=0, padx=10)

exit_btn = tk.Button(btn_frame, text="Exit", command=root.quit, bg="red", fg="white")
exit_btn.grid(row=0, column=1, padx=10)


# If you want exit button in circle
# circle_canvas = tk.Canvas(btn_frame, width=60, height=60, bg="black", highlightthickness=0)
# circle_canvas.grid(row=0, column=1, padx=10)

# circle = circle_canvas.create_oval(5, 5, 55, 55, fill="red", outline="white")
# text = circle_canvas.create_text(30, 30, text="Exit", fill="white", font=("Arial", 10, "bold"))
# 
# def exit_app(event=None):
    # root.quit()

# circle_canvas.tag_bind(circle, "<Button-1>", exit_app)
# circle_canvas.tag_bind(text, "<Button-1>", exit_app)


# Dropdown Menu for Colors
colors = ["black", "Gold", "grey", "yellow", "brown", "green", "red","purple","silver","Midnight Blue","Orange","pink","Crimson"]
selected_color = tk.StringVar(value="black")

color_menu = tk.OptionMenu(btn_frame, selected_color, *colors, command=change_bg)
color_menu.config(bg="black", fg="white")
color_menu.grid(row=0, column=2, padx=10)

# this command use for running the code 
update_time()
root.mainloop()
