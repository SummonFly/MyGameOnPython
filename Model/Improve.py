from abc import ABC, abstractmethod

# В методе Improve класса IImproveable не возможно аргумент сделать типа IImprovement из-за особенностей Python
class IImproveable(ABC):
    def Improve(self, improvement):
        improvement.Accept(self)


class IImprovement(ABC):
    @abstractmethod
    def Accept(self, obj: IImproveable):
        pass

