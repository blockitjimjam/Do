from abc import ABC, abstractmethod

class Element(ABC):
    @abstractmethod
    def delete_element() -> None: ...