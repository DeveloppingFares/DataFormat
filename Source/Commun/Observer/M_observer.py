from abc import ABCMeta, abstractmethod


class C_observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, **kwargs) -> None:
        raise NotImplementedError
