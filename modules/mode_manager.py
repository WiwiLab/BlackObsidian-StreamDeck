from enum import Enum

from modules.logger import log


class Mode(Enum):

    STREAM = 0
    NORMAL = 1
    EDIT = 2


class ModeManager:

    def __init__(self):

        self.mode = Mode.STREAM

        log("Modo inicial: STREAM")


    def current(self):

        return self.mode


    def current_name(self):

        return self.mode.name


    def next(self):

        if self.mode == Mode.STREAM:

            self.mode = Mode.NORMAL

        elif self.mode == Mode.NORMAL:

            self.mode = Mode.EDIT

        else:

            self.mode = Mode.STREAM

        log(f"Modo cambiado -> {self.mode.name}")

        return self.mode