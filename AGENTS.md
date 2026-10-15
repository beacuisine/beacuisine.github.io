# Instructions pour les agents

## Images Open Graph

À chaque nouvelle recette (image dans `images/*.webp`), lancer `python3 scripts/generate_og_images.py` pour générer `images/og/<nom>.jpg` (1200x630), utilisé par le layout `_layouts/recipe.html` pour `og:image`. Il faut Pillow, installé par exemple dans un venv local `.venv`. Les commandes sont dans l'en-tête du script. Commiter les jpg générés.
