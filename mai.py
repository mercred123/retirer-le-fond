import customtkinter as ctk
from tkinter import filedialog, messagebox
from rembg import remove
from PIL import Image, ImageTk
from customtkinter import CTkImage

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

def choisir_image():
    global input_path
    input_path = filedialog.askopenfilename(filetypes=[("Images", "*.png;*.jpg;*.jpeg")])
    if input_path:
        image_preview(input_path)

def image_preview(image_path):
    try:
        img = Image.open(image_path)
        img.thumbnail((400, 400))  # Redimensionnement
        img_ctk = CTkImage(light_image=img, size=img.size)
        preview_label.configure(image=img_ctk)
        preview_label.image = img_ctk
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de l'ouverture de l'image : {e}")

def enlever_fond():
    if not input_path:
        messagebox.showerror("Erreur", "Veuillez choisir une image d'abord.")
        return
    try:
        with open(input_path, "rb") as inp_file:
            input_data = inp_file.read()
        output_data = remove(input_data)
        output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Images", "*.png")])
        if output_path:
            with open(output_path, "wb") as out_file:
                out_file.write(output_data)
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur est survenue : {e}")

root = ctk.CTk()
root.title("Suppression d'Arrière-Plan")
root.geometry("700x600")

choisir_button = ctk.CTkButton(
    root, 
    text="📂 Choisir une image", 
    command=choisir_image,
    width=220,
    height=45,
    corner_radius=20,
    font=("Arial", 14, "bold")
)
choisir_button.pack(pady=15)

preview_label = ctk.CTkLabel(root, text="")
preview_label.pack(pady=10)

enlever_button = ctk.CTkButton(
    root, 
    text="✂️ Enlever le fond", 
    command=enlever_fond,
    width=220,
    height=45,
    fg_color="#FF5722",
    hover_color="#E64A19",
    corner_radius=20,
    font=("Arial", 14, "bold")
)
enlever_button.pack(pady=15)

input_path = ""

root.mainloop()
