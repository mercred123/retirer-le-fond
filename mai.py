import customtkinter as ctk
from tkinter import filedialog, messagebox
from rembg import remove
from PIL import Image
from customtkinter import CTkImage
import os, tempfile, atexit, traceback

temp_files = []
def cleanup_temp_files():
    for f in list(temp_files):
        try:
            if os.path.exists(f):
                os.remove(f)
        except Exception:
            pass
atexit.register(cleanup_temp_files)

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

input_path = None

def nettoyer_image(path):
    """Ouvre l'image, force conversion en RGBA et enregistre dans un fichier temporaire .png."""
    try:
        img = Image.open(path)
        img.load()
        rgba = img.convert("RGBA")
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
        rgba.save(tmp.name, format="PNG")
        tmp.close()
        temp_files.append(tmp.name)
        print(f"[DEBUG] image convertie vers: {tmp.name}")
        return tmp.name
    except Exception as e:
        print("[ERROR] nettoyer_image:", e)
        traceback.print_exc()
        messagebox.showerror("Erreur", f"Impossible d'ouvrir/convertir l'image :\n{e}")
        return None

def choisir_image():
    global input_path
    path = filedialog.askopenfilename(filetypes=[("Images", "*.png;*.jpg;*.jpeg;*.bmp;*.webp")])
    if not path:
        return
    fixed = nettoyer_image(path)
    if fixed:
        input_path = fixed
        image_preview(fixed)
        file_label.configure(text=os.path.basename(path))

def image_preview(image_path):
    try:
        img = Image.open(image_path)
        img.thumbnail((400, 400))
        img_ctk = CTkImage(light_image=img, size=img.size)
        preview_label.configure(image=img_ctk)
        preview_label.image = img_ctk
    except Exception as e:
        print("[ERROR] image_preview:", e)
        traceback.print_exc()
        messagebox.showerror("Erreur", f"Erreur lors de l'affichage de l'image :\n{e}")

def enlever_fond():
    global input_path
    if not input_path:
        messagebox.showerror("Erreur", "Veuillez choisir une image d'abord.")
        return
    if not os.path.exists(input_path):
        messagebox.showerror("Erreur", "Le fichier temporaire a été supprimé. Re-sélectionnez l'image.")
        input_path = None
        return
    try:
        with open(input_path, "rb") as f:
            input_data = f.read()
        output_data = remove(input_data)
        if not output_data or len(output_data) < 8:
            raise RuntimeError("Données de sortie vides ou corrompues.")
        # Vérif simple : début PNG ?
        if not output_data.startswith(b"\x89PNG"):
            print("[WARNING] remove() n'a pas retourné un PNG standard.")
        output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png")])
        if output_path:
            with open(output_path, "wb") as out_f:
                out_f.write(output_data)
            messagebox.showinfo("Succès", f"Image enregistrée :\n{output_path}")
    except Exception as e:
        print("[ERROR] enlever_fond:", e)
        traceback.print_exc()
        messagebox.showerror("Erreur", f"Une erreur est survenue :\n{e}")

root = ctk.CTk()
root.title("Suppression d'Arrière-Plan")
root.geometry("700x600")

choisir_button = ctk.CTkButton(root, text="📂 Choisir une image", command=choisir_image,
                               width=220, height=45, corner_radius=20, font=("Arial", 14, "bold"))
choisir_button.pack(pady=15)

preview_label = ctk.CTkLabel(root, text="")
preview_label.pack(pady=10)

file_label = ctk.CTkLabel(root, text="", font=("Arial", 12))
file_label.pack(pady=5)

enlever_button = ctk.CTkButton(root, text="✂️ Enlever le fond", command=enlever_fond,
                                width=220, height=45, fg_color="#FF5722", hover_color="#E64A19",
                                corner_radius=20, font=("Arial", 14, "bold"))
enlever_button.pack(pady=15)

root.mainloop()