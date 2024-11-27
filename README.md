# Suppression d'Arrière-Plan d'Images avec Tkinter et Rembg

Ce projet permet de supprimer le fond d'une image de manière simple et rapide à l'aide de l'outil **Rembg**, une bibliothèque Python spécialisée dans la suppression de l'arrière-plan des images. L'application utilise **Tkinter** pour créer une interface graphique, permettant à l'utilisateur de choisir une image, d'apercevoir l'image sélectionnée et de sauvegarder l'image après la suppression de son fond.

## Fonctionnalités

- Choisir une image depuis votre ordinateur.
- Visualiser l'aperçu de l'image choisie.
- Supprimer automatiquement l'arrière-plan de l'image sélectionnée.
- Sauvegarder l'image traitée dans un fichier au format PNG.

## Technologies utilisées

- **Tkinter** : Bibliothèque Python pour l'interface graphique.
- **Rembg** : Bibliothèque pour la suppression d'arrière-plan des images.
- **Pillow (PIL)** : Bibliothèque pour la gestion et l'affichage des images.

## Comment utiliser l'application ?

1. Exécutez le fichier Python `mai.py`.
2. Cliquez sur le bouton **Choisir une image** pour sélectionner une image depuis votre ordinateur.
3. Une fois l'image choisie, un aperçu de l'image s'affichera à l'écran.
4. Cliquez sur le bouton **Enlever le fond** pour supprimer l'arrière-plan de l'image.
5. Un explorateur de fichiers s'ouvrira pour vous permettre de choisir où sauvegarder l'image sans son arrière-plan.

## Comment comprendre et modifier le code ?

Le code est structuré pour être simple à comprendre et à modifier. Voici une explication détaillée des principales parties :

### 1. **Choisir une image**
   - La fonction `choisir_image()` utilise un dialogue de fichier (`filedialog.askopenfilename`) pour permettre à l'utilisateur de choisir une image.
   - Si une image est choisie, la fonction `image_preview()` est appelée pour afficher un aperçu de l'image.

### 2. **Affichage de l'image**
   - La fonction `image_preview()` charge l'image choisie à l'aide de **Pillow**, la redimensionne pour l'aperçu et l'affiche dans une **Label** de Tkinter.
   
### 3. **Suppression du fond**
   - La fonction `enlever_fond()` lit l'image sélectionnée en mode binaire, utilise la bibliothèque **Rembg** pour supprimer l'arrière-plan, et enregistre l'image résultante au format PNG.

### 4. **Interface graphique**
   - L'interface est construite avec Tkinter, qui contient deux boutons principaux : un pour choisir une image et un pour enlever l'arrière-plan.
   - Les boutons et autres éléments graphiques sont stylisés pour offrir une expérience utilisateur agréable.

### 5. **Gestion des erreurs**
   - Des boîtes de dialogue d'erreur sont affichées si l'utilisateur tente d'effectuer une action sans avoir sélectionné une image ou si une erreur se produit lors du traitement de l'image.

## Installation

### Prérequis

- Python 3.x
- Les bibliothèques suivantes doivent être installées :
  - `tkinter` (généralement inclus dans l'installation Python)
  - `rembg` : `pip install rembg`
  - `Pillow` : `pip install Pillow`

### Lancer l'application

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/votre-utilisateur/suppression-arriere-plan.git




## Contributions

Les contributions sont les bienvenues ! Si vous souhaitez améliorer cette application ou ajouter de nouvelles fonctionnalités, n'hésitez pas à ouvrir une pull request.