import tkinter as tk
# from def_helper import hod_kockou, open_lose_window, load_record, save_record
import random
def hod_kockou():
    cube_number = random.randint(1, 6)
    if not cube_number == 1:
        global body
        body += 1
        if body > record:
            save_record()
            label_record.config(text=f"Rekord: {body}")
        label_body.config(text=f"Body: {body}")
        label_title = tk.Label(frame, text=f"Hodil si {cube_number} a vyhrávaš!", font="Arial, 10")
        label_title.grid(row=3, column=1)
    else:
        body = 0
        label_body.config(text=f"Body: {body}")
        label_title = tk.Label(frame, text=f"Hodil si {cube_number} a prehral si!", font="Arial, 10")
        label_title.grid(row=3, column=1)
        open_lose_window()
    pass
def open_lose_window():
    new_window = tk.Toplevel(root)
    new_window.title("Lose")
    new_window.geometry("300x200")
    label = tk.Label(new_window, text="Prehral si!")
    label.pack()
def load_record():
    try:
        with open('record.txt', 'r') as file:
            return int(file.read())
    except FileNotFoundError:
        return 0
def save_record():
    with open('record.txt', 'w') as file:
        file.write(str(body))


# Premenné
body = 0
record = load_record()


# Main kod
root = tk.Tk()
root.title("Hádzanie kockou")

frame = tk.Frame(root)
frame.pack(padx=100, pady=100)

label_body = tk.Label(frame, text=f"Body: {body}")
label_body.grid(row=4, column=0, pady=10, padx=0)
label_record = tk.Label(frame, text=f"Rekord: {record}")
label_record.grid(row=4, column=2, pady=10, padx=0)

label_title = tk.Label(frame, text="HOD KOCKOU", font="Arial, 15")
label_title.grid(row=0, column=1, pady=10)

button = tk.Button(frame, text="Hodiť kockou", command=hod_kockou)
button.grid(row=1, column=1, pady=5)

root.mainloop()