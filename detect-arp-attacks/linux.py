from system import System


class Linux(System):

    @classmethod
    def get_interface(cls, /) -> str:
        ...

    @classmethod
    def disable_net_adapter(cls, /) -> None:
        ...
