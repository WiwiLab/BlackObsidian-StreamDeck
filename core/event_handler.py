from core.event import Event
from modules.logger import log


class EventHandler:

    def __init__(self, app):

        self.app = app


    def handle(self, code):

        event = Event(code)

        log(
            f"Evento recibido: {event.code}"
        )


        # Cambio de modo

        if event.code == "BD":

            modo = self.app.profile.next_profile()

            log(
                f"Cambio de perfil -> {modo}"
            )

            return


        # Buscar acción en perfil

        action = self.app.profile.get_action(
            event.code
        )


        if action:

            log(
                f"Acción encontrada: {action}"
            )

            self.app.actions.execute(
                action
            )

        else:

            log(
                f"Sin acción asignada para {event.code}"
            )