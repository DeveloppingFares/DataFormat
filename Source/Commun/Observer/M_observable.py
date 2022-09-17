from Source.Commun.Observer.M_observer import C_observer


class C_observable(object):
    def __init__(self):
        self._observers = list()

    def add_observer(self, observer: C_observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer: C_observer) -> None:
        self._observers.remove(observer)

    def notify(self, **kwargs) -> None:
        for observer in self._observers:
            observer.update(type_emetteur=self.__class__.__name__,
                            nom_emetteur=self.nom if hasattr(self, 'nom') else None,
                            **kwargs)
