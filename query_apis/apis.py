from abc import abstractmethod


class API:
    @abstractmethod
    def get_provided_objects(self):
        raise NotImplementedError

    @abstractmethod
    def update_provided_objects(self):
        raise NotImplementedError
