from dataclasses import dataclass


@dataclass(slots=True)
class Event:

    code: str

    value: str | None = None