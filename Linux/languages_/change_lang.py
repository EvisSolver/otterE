from pathlib import Path

from PySide6.QtCore import QTranslator
from PySide6.QtWidgets import QApplication


translator = None


def load_language(code):
    global translator
    app = QApplication.instance()
    new_translator = QTranslator(app)

    file_name = Path(__file__).parent / "language_cfgs" / f"app_{code}.qm"

    if not new_translator.load(str(file_name)):
        print("Translation not found: ",file_name)
        return False
    if translator is not None: app.removeTranslator(translator)

    translator = new_translator
    app.installTranslator(translator)
    return True