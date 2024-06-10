from system import System


class Linux(System):

    @classmethod
    def get_interface(cls, /) -> str:
        ...
