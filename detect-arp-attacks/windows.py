from powershell import PowerShell
from system import System


class Windows(System):

    @classmethod
    def get_interface(cls, *, print_command = True) -> str:
        return PowerShell.run(
            'Get-NetAdapter -Physical | Where-Object Status -EQ "Up" | Select-Object Name | Format-List',
            print_command=print_command
        ).strip().split(' : ')[1]

    @classmethod
    def disable_net_adapter(cls, /) -> None:
        return PowerShell.run(
            f'Disable-NetAdapter -Name "{cls.get_interface(print_command=False)}"'
        )
