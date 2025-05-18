import sys
import os

# Ajoute le répertoire de ton app au PATH
sys.path.insert(0, os.path.dirname(__file__))

# Import de create_app depuis ton package app
from init import create_app

# App Flask attendue par cPanel
application = create_app()
