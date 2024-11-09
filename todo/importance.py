from enum import Enum
# made to easily show levels of importance
class Importance(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    def value(self, imp):
        if imp == self.LOW:
            return 1
        elif imp == self.MEDIUM:
            return 2
        else:
            return 3