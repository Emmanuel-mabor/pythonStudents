import tkinter as tk

def open_link(link_name):
    # You can implement actions to open the respective links here
    # For now, it just shows the name of the clicked link.
    print(f"You clicked on: {link_name}")

root = tk.Tk()
root.title("E-Learning Portals")

elearning_label = tk.Label(root, text="Links to E-Learning Portals", font=("Arial", 14))
elearning_label.grid(row=0, column=0, columnspan=3, pady=10)

# Create buttons for the links
links = ["Virtual and DIBEL Portal", "Day, Evening & Weekend Portal", "Examination Portal", "E-Learning Students Tutorial", "Online Help and Ticket System", "Library E-Resources"]

row_num = 1
col_num = 0

for link_name in links:
    link_button = tk.Button(root, text=link_name, command=lambda name=link_name: open_link(name))
    link_button.grid(row=row_num, column=col_num, padx=10, pady=5)

    col_num += 1
    if col_num > 2:
        col_num = 0
        row_num += 1

root.mainloop()
