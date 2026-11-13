from pathlib import Path

from PySide6.QtCore import QTranslator
from PySide6.QtWidgets import QApplication


translator = None


def load_language(code):
    global translator
    app = QApplication.instance()
    new_translator = QTranslator(app)