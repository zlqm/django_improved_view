from abc import abstractmethod, ABC
from . import exceptions


class BasePermission(ABC):
    def __init__(self, request, view):
        self.request = request
        self.view = view

    @abstractmethod
    def __call__(self):
        pass


class LoginRequired(BasePermission):
    def __call__(self):
        if not self.request.user.is_authenticated:
            raise exceptions.Unauthorized()


class SuperUserRequired(BasePermission):
    def __call__(self):
        if not self.request.user.is_superuser:
            raise exceptions.Forbidden()
