import tkinter as tk

root = tk.Tk()
root.title("Food Nutrition")
root.geometry("650x350")
root.configure(bg="#252625")

status_text = tk.StringVar()
status_text.set("Please enter a food name to get nutrition data.")

def change_ui():
    if get_metrics() == False:
        return
    
    status_text.set("Showing nutrition data for: " + food_name.get())
    root.geometry("750x650")
    input_frame.pack_forget()
    search_button.pack_forget()
    results_frame.pack(pady=20)
    redo_button.pack(pady=10)

def change_ui_back():
    status_text.set("Please enter a food name to get nutrition data.")
    root.geometry("650x350")
    input_frame.pack(pady=20)
    search_button.pack(pady=10)
    results_frame.pack_forget()
    redo_button.pack_forget()

def get_metrics():
    food = food_name.get().lower()

    if food == "banana":
        data_label.config(text="NUTRITION DATA: \n"
        "- Calories: 105\n" 
        "- Carbohydrates: 27g\n"
        "- Protein: 1.3g\n"
        "- Fat: 0.4g\n")
    elif food == "apple":
        data_label.config(text="NUTRITION DATA: \n"
        "- Calories: 95\n" 
        "- Carbohydrates: 25g\n"
        "- Protein: 0.5g\n"
        "- Fat: 0.3g\n")
    else:
        status_text.set("Food not found. Please enter a valid food name.")
        status_label.config(fg="red")
        return False
    

title_label = tk.Label(
    root,
    text="Know Your Food Nutrition",
    font=("Arial",30, "bold"),
    bg="#252625",
    fg="#F0ED36"
)
title_label.pack(pady=20)

status_label = tk.Label(
    root,
    textvariable=status_text,
    font=("Arial", 16, "bold"),
    bg="#252625",
    fg="white"
)
status_label.pack(pady=10)
input_frame = tk.Frame(
    root,
    bg="#252625"
)
input_frame.pack(pady=20)
food_label= tk.Label(
    input_frame,
    text="Enter Food Name:",
    font=("Arial", 24,"bold"),
    bg="#252625",
    fg="white"
)
food_label.pack(side="left", pady=10)
food_name = tk.Entry(
    input_frame,
    font=("Arial", 24, "bold"),
    bd=2,
    relief="groove",
    justify="center"
)
food_name.pack(side="left")

search_button = tk.Button(
    root,
    text="Search",
    bg="#8DBCF3",
    fg="white",
    font=("Arial", 20, "bold"),
    command=change_ui
)
search_button.pack(pady=10)

results_frame = tk.Frame(
    root,
    bg="#252625"
)

image_label = tk.Label(
    results_frame,
    text="IMAGE PLACEHOLDER",
    font=("Arial", 20, "bold"),
    bg="#252625",
    fg="white"
)
image_label.pack(side="left", pady=10)

data_label = tk.Label(
    results_frame,
    text="NUTRITION DATA: \n" 
    "- Calories: 200\n" 
    "- Carbohydrates: 30g\n"  
    "- Protein: 5g\n" 
    "- Fat: 10g",
    font=("Arial", 20, "bold"),
    bg="#252625",   
    fg="white"
)
data_label.pack(side="left", padx=20)

redo_button = tk.Button(
    root,
    text="Search Again",
    font=("Arial", 20, "bold"),
    bg="#DD6B49",
    fg="white",
    command=change_ui_back
)

root.mainloop()