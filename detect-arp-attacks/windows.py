from powershell import PowerShell
from system import System


class Windows(System):

    @classmethod
    def get_interface(cls, /) -> str:
        return PowerShell.run(
            'Get-NetAdapter -Physical | Where-Object Status -EQ "Up" | Select-Object Name | Format-List',
            print_command=False
        ).strip().split(' : ')[1]
