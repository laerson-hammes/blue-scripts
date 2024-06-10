import scapy.all as scapy
from scapy.layers.l2 import Ether

from macaddress import MACAddress

from colorama import Fore
from colorama import init

from windows import Windows
from linux import Linux

from system import system_other_than_error
from system import System

import platform


class DetectARPAttack:

    @classmethod
    def sniff(cls, interface: str, /) -> None:
        scapy.sniff(
            iface=interface,
            store=False,
            prn=DetectARPAttack.process_sniffed_packet
        )

    @classmethod
    def process_sniffed_packet(cls, packet: Ether, /):
        if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:
            try:
                if MACAddress.get(packet[scapy.ARP].psrc) == packet[scapy.ARP].hwsrc:
                    print(f'{Fore.RED}[-] YOU ARE UNDER ATTACK...')
            except IndexError:
                pass


os: dict[str, System] = {
    'Windows': Windows,
    'Linux': Linux
}

def main() -> None:
    if not (system := os.get(platform.system(), None)):
        system_other_than_error()

    DetectARPAttack.sniff(system.get_interface())


if __name__ == '__main__':
    init(autoreset=True)
    main()
