from enum import StrEnum


class StateEnum(StrEnum):
    new = "NEW"
    installing = "INSTALLING"
    running = "RUNNING"
