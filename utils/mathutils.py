import math
# may never be used but you never know
class MathUtils:
    @staticmethod 
    def triangle_area(b, h) -> float:
        return (b * h) / 2
    @staticmethod
    def pythagoras_for_hyp(a, b) -> float:
        return math.sqrt((a ** 2) + (b ** 2))
    @staticmethod
    def pythagoras_for_other(c, b) -> float:
        return math.sqrt((c ** 2) - (b ** 2))