# Suppression d'Arrière-Plan d'Images avec CustomTkinter et Rembg

Ce projet permet de supprimer le fond d'une image de manière simple et rapide à l'aide de l'outil **Rembg**, une bibliothèque Python spécialisée dans la suppression de l'arrière-plan des images.  
L'application utilise **CustomTkinter** pour créer une interface graphique moderne et intuitive, permettant à l'utilisateur de choisir une image, d'apercevoir l'image sélectionnée et de sauvegarder l'image après la suppression de son fond.

---

## 🚀 Fonctionnalités

- 📂 Choisir une image depuis votre ordinateur.  
- 👀 Visualiser l'aperçu de l'image choisie directement dans l'application.  
- ✂️ Supprimer automatiquement l'arrière-plan de l'image sélectionnée.  
- 💾 Sauvegarder l'image traitée au format **PNG** avec fond transparent.  

---

## 🖥️ Utilisation

1. Exécutez le fichier Python `mai.py`.  
2. Cliquez sur le bouton **Choisir une image** pour sélectionner une image depuis votre ordinateur.  
3. Un aperçu de l’image choisie s’affichera dans la fenêtre (sans texte, uniquement l’image).  
4. Cliquez sur le bouton **Enlever le fond** pour supprimer l’arrière-plan.  
5. Un explorateur de fichiers s’ouvrira pour vous permettre d’enregistrer l’image sans fond.  

---

## ⚙️ Structure et explications du code

### 1. **Choisir une image**
- La fonction `choisir_image()` ouvre un explorateur via `filedialog.askopenfilename`.  
- Si une image est choisie, elle est transmise à `image_preview()`.  

### 2. **Aperçu de l’image**
- La fonction `image_preview()` utilise **Pillow** pour ouvrir et redimensionner l’image.  
- L’image est ensuite affichée dans un `CTkLabel` avec **CTkImage** (meilleure compatibilité avec les écrans HD/4K).  

### 3. **Suppression de l’arrière-plan**
- La fonction `enlever_fond()` lit l’image en binaire.  
- Elle utilise **Rembg** pour retirer l’arrière-plan.  
- L’utilisateur choisit ensuite l’emplacement d’enregistrement via `filedialog.asksaveasfilename`.  

### 4. **Interface graphique**
- L’interface est construite avec **CustomTkinter** :  
  - Un bouton pour sélectionner une image.  
  - Un aperçu central de l’image.  
  - Un bouton pour enlever le fond et sauvegarder.  

### 5. **Gestion des erreurs**
- Des boîtes de dialogue s’affichent si aucune image n’est choisie ou en cas de problème lors du traitement.  

---

## 📦 Installation

### Prérequis

- Python **3.9+**  
- Bibliothèques nécessaires :  

```bash
pip install rembg pillow customtkinter onnxruntime
```
(Tkinter est généralement inclus par défaut avec Python)

---

### Lancer l’application:

```bash
python mai.py
```
---

### 🤝 Contributions

Les contributions sont les bienvenues !
Si vous souhaitez améliorer cette application n’hésitez pas à ouvrir une pull request.