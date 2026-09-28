from functools import wraps
from PySide6.QtWidgets import QMessageBox


def show_error(func):
    '''decorator, which call the value-error in QMessageBox window'''
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)

        except ValueError as error:
            QMessageBox.warning(
                self,
                "Error",
                str(error)
            )

            return None

    return wrapper