from todo.importance import Importance
# not currently used but will be used later
class Todo:
    def __init__(self, importance: Importance, name: str, desc: str) -> None:
        self.importance = importance
        self.name = name
        self.desc = desc