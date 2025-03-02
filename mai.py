import tkinter as tk
from tkinter import filedialog, messagebox
from rembg import remove
from PIL import Image, ImageTk
import io

def choisir_image():
    global input_path
    input_path = filedialog.askopenfilename(filetypes=[("Images", "*.png;*.jpg;*.jpeg")])
    if input_path:
        image_preview(input_path)

def image_preview(image_path):
    try:
        img = Image.open(image_path)
        img.thumbnail((200, 200))
        img = ImageTk.PhotoImage(img)
        preview_label.config(image=img)
        preview_label.image = img
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
        else:
            messagebox.showerror("Erreur", "Aucun emplacement choisi pour sauvegarder l'image.")
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur est survenue lors du traitement de l'image : {e}")

root = tk.Tk()
root.title("Suppression d'Arrière-Plan")
root.geometry("600x500")
root.configure(bg="#f0f0f0")

input_path = ""

choisir_button = tk.Button(root, text="Choisir une image", command=choisir_image, width=20, height=2,
                           bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"), relief="raised", bd=3)
choisir_button.pack(pady=30)

preview_label = tk.Label(root, bg="#f0f0f0")
preview_label.pack(pady=20)

enlever_button = tk.Button(root, text="Enlever le fond", command=enlever_fond, width=20, height=2,
                           bg="#FF5722", fg="white", font=("Helvetica", 12, "bold"), relief="raised", bd=3)
enlever_button.pack(pady=30)

root.mainloop()
