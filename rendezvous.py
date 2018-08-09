import sys
import hashlib

from typing import List, Tuple, Iterable


class Server:

    def __init__(self, name: str) -> None:
        self.name = name
        self.name_b = name.encode("utf-8")


class LB:

    def __init__(self, server_list: Iterable[Server]) -> None:
        self.server_list = server_list

    def assign(self, packet: bytes) -> Server:
        choices: List[Tuple[Server, int]] = []
        for s in self.server_list:
            h = int(hashlib.blake2b(s.name_b + packet).hexdigest(), 16)
            choices.append((s, h))

        choices = sorted(choices, key=lambda x: x[1])
        for c in choices:
            print(c[0].name, c[1])

        return c[0]


def main() -> int:
    servers: List[Server] = []
    servers.append(Server("serv1"))
    servers.append(Server("serv2"))
    servers.append(Server("serv3"))

    lb1 = LB(servers)
    lb2 = LB(servers)

    packet = b"DEADBEEF"

    s1 = lb1.assign(packet)
    s2 = lb2.assign(packet)

    if s1 != s2:
        print("hashes weren't the same")
        return 1

    print("hashes match, chose:", s1.name)
    return 0


if __name__ == '__main__':
    sys.exit(main())
