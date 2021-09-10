import tkinter as tk
from PIL import Image, ImageTk
import re

root = tk.Tk()
root.title("Eef")

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=6, rowspan=6)

# Logo
logo = Image.open('eef.jpeg')
logo = logo.resize((300, 300), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0, pady=25)


# Instructions
introduction = tk.Label(root, text="Hi i'm Eef!")
introduction.grid(columnspan=1, column=1, row=1)
site = tk.Label(root, text="Site:")
site.grid(columnspan=1, column=0, row=2)
start = tk.Label(root, text="Start:")
start.grid(columnspan=1, column=0, row=3)
end = tk.Label(root, text="End:")
end.grid(columnspan=1, column=0, row=4)
plus = tk.Label(root, text="Increment:")
plus.grid(columnspan=1, column=0, row=5)

# Text boxes
input1 = tk.Text(root, height=1, width=50)
input1.grid(columnspan=1, column=1, row=2)
input2 = tk.Text(root, height=1, width=50)
input2.grid(columnspan=1, column=1, row=3)
input3 = tk.Text(root, height=1, width=50)
input3.grid(columnspan=1, column=1, row=4)
input4 = tk.Text(root, height=1, width=50)
input4.grid(columnspan=1, column=1, row=5)
text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)


def paginate():
    try:
        url = input1.get("1.0", "end-1c")

        if not '{n}' in url:
            raise ValueError('No replace string in URL. Must contain a "{n}" variable to replace with page numbers')

        file = 'list.txt'
        page_start = input2.get("1.0", "end-1c")
        page_start = int(page_start)
        page_end = input3.get("1.0", "end-1c")
        page_end = int(page_end)
        increment = input4.get("1.0", "end-1c")
        increment = int(increment)

        with open(file, 'w+') as f:
            for n in range(page_start, page_end + 1, increment):
                new_url = re.sub('&(?!amp;)', '&amp;', url)
                new_url = new_url.format(n=n)
                f.write(f'{new_url}/\n')

        with open(file, 'r'):
            for line in reversed(list(open(file))):
                text_box.insert('1.0', line)
                text_box.grid(column=1, row=6)

    except Exception as ex:
        raise ex


# Browse Button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda: paginate(), bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("Submit")
browse_btn.grid(column=0, row=7, pady=25)

# Copy Button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda: paginate(), bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("Copy to clipboard")
browse_btn.grid(column=1, row=7, pady=25)


canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)


root.mainloop()
