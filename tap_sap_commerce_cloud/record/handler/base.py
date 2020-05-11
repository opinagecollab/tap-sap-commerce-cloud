from abc import abstractmethod


class BaseHandler:

    @abstractmethod
    def generate(self, record, **options):
        pass
