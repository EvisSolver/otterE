import inspect

from functools import wraps
from PySide6.QtWidgets import QMessageBox


def show_error(func):
    '''decorator, which call the value-error in QMessageBox window'''
    if inspect.iscoroutinefunction(func):
        @wraps(func)
        async def async_wrapper(self, *args, **kwargs):
            try:
                return await func(self, *args, **kwargs)

            except ValueError as error:
                QMessageBox.warning(
                    self,
                    "Error",
                    str(error)
                )

        return async_wrapper

    @wraps(func)
    def sync_wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except Exception as error:
            QMessageBox.warning(self, "Error", str(error))

    return sync_wrapper