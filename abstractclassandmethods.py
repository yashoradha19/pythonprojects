from abc import ABC,abstractmethod
class computer(ABC):
    @abstractmethod
    def process(self):
        pass

class laptop(computer):
    def process(self):
        print('its runnig')

com1=laptop()
com1.process()