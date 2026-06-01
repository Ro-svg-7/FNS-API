import tkinter as tk
from nutrition_api import get_nutrition_info
from image_api import get_food_image
from io import BytesIO
from PIL import Image, ImageTk
import requests

root = tk.Tk()
root.title("Food Nutrition")
root.geometry("650x350")
root.configure(bg="#252625")

status_text = tk.StringVar()
status_text.set("Please enter a food name to get nutrition data.")

def change_ui():
    root.configure(cursor="watch")
    root.update()
    status_text.set("Fetching data for: "+food_name.get().strip())
    success = get_metrics()
    root.configure(cursor="")
    if not success:
        return 
    status_text.set("Data fetched successfully for: "+food_name.get().strip())
    root.geometry("950x650")
    input_frame.pack_forget()
    search_button.pack_forget()
    results_frame.pack(pady=20)
    redo_button.pack(pady=10)

def change_ui_back():
    
    status_text.set("Please enter a food name to get nutrition data.")
    root.geometry("650x350")
    food_name.delete(0, tk.END)
    image_label.config(image="", text="🍌")
    image_label.image = None
    input_frame.pack(pady=20)
    search_button.pack(pady=10)
    results_frame.pack_forget()
    redo_button.pack_forget()

def get_metrics():
    
    food_item = food_name.get().strip()

    if not food_item:
        status_text.set("Please enter a food name.")
        status_label.config(fg="red")
        return False
    
    nutrition_info = get_nutrition_info(food_item)
    if nutrition_info is not None:
        status_label.config(fg="white")

        image_url = get_food_image(food_item)
        if image_url:
            try:
                response = requests.get(image_url)
                img = Image.open(BytesIO(response.content))
                img.thumbnail((300, 300))
                photo = ImageTk.PhotoImage(img)
                image_label.config(image=photo, text="")
                image_label.image = photo
            except Exception as e:
                print(f"Error loading image: {e}")
                image_label.config(image="", text="🍌")

        data_label.config(
            text=f"{food_item.upper()}:\n\n"
              f"{'Calories:':<15} {nutrition_info['calories']:.0f} kcal\n"
              f"{'Sugars:':<15} {nutrition_info['sugars']:.1f} g\n"
              f"{'Carbohydrates:':<15} {nutrition_info['carbohydrates']:.1f} g\n"
              f"{'Protein:':<15} {nutrition_info['protein']:.1f} g\n"
              f"{'Fat:':<15} {nutrition_info['fat']:.1f} g"
              )
        return True
    else:
        status_text.set("Food not found. Please enter a valid food name.")
        status_label.config(fg="red")
        return False
    
title_label = tk.Label(
    root,
    text="Know Your Food Nutrition",
    font=("Segoe UI",30, "bold"),
    bg="#252625",
    fg="#F0ED36"
)
title_label.pack(pady=20)

status_label = tk.Label(
    root,
    textvariable=status_text,
    font=("Segoe UI", 16, "bold"),
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
    font=("Segoe UI", 24,"bold"),
    bg="#252625",
    fg="white"
)
food_label.pack(side="left", pady=10)
food_name = tk.Entry(
    input_frame,
    font=("Segoe UI", 24, "bold"),
    bd=2,
    relief="groove",
    justify="center"
)
food_name.pack(side="left")
food_name.bind(
    "<Return>",
    lambda event: change_ui()
)

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

image_frame = tk.Frame(
    results_frame,
    bg="#333333",
    width=350,
    height=350,
    bd=2,
    relief="ridge"
)
image_frame.pack(side="left", padx=20)
image_label = tk.Label(
    image_frame,
    bg="#333333"
)
image_label.pack(expand=True)

nutrition_frame = tk.Frame(
    results_frame,
    bg="#333333",
    width=350,
    height=350,
    bd=2,
    relief="ridge"
)
nutrition_frame.pack(side="left", padx=20)
nutrition_frame.pack_propagate(False)

data_label = tk.Label(
    nutrition_frame,
    text="NUTRITION DATA:",
    font=("Consolas", 18, "bold"),
    bg="#333333",   
    fg="white",
    justify="left"
)
data_label.pack()

redo_button = tk.Button(
    root,
    text="Search Again",
    font=("Arial", 20, "bold"),
    bg="#DD6B49",
    fg="white",
    command=change_ui_back
)

root.mainloop()