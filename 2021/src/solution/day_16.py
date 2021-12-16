from input_loader import load_input_line
from math import log2, prod

INPUT = load_input_line(day=16)

OP_BY_TYPE_ID = {
    0: sum,
    1: prod,
    2: min,
    3: max,
    5: lambda x: 1 if x[1] > x[0] else 0,
    6: lambda x: 1 if x[1] < x[0] else 0,
    7: lambda x: 1 if x[1] == x[0] else 0
}


def part1(transmission: str) -> int:
    processor = TransmissionDecoder()
    processor.run(transmission)
    return processor.total_version


def part2(transmission: str) -> int:
    processor = TransmissionDecoder()
    processor.run(transmission)
    return processor.stack.pop()


class TransmissionDecoder:
    def __init__(self):
        self.total_version = 0
        self.stack = []

    def run(self, transmission: str):
        packet = _hex_to_binary(transmission)
        self._process_packet(packet)

    def _process_packet(self, packet: str) -> str:
        version = _to_decimal(packet[:3])
        type_id = _to_decimal(packet[3:6])
        packet = packet[6:]

        if type_id == 4:
            packet = self._process_literal_value_packet(packet)
        else:
            self.stack.append(OP_BY_TYPE_ID[type_id])
            packet = self._process_operator_packet(packet)
            self.stack.append(self._process_stack())

        self.total_version += version

        return packet

    def _process_literal_value_packet(self, packet: str) -> str:
        group_size = 5
        prefix = "1"
        literal_value = ""

        while prefix == "1":
            group = packet[:group_size]
            packet = packet[group_size:]
            literal_value += group[1:]
            prefix = group[0]

        self.stack.append(_to_decimal(literal_value))

        return packet

    def _process_operator_packet(self, packet: str) -> str:
        length_type_id = packet[0]
        packet = packet[1:]

        if length_type_id == "0":
            total_length = _to_decimal(packet[:15])
            packet = packet[15:]

            while total_length > 0:
                remaining_packet = self._process_packet(packet)
                total_length -= len(packet) - len(remaining_packet)
                packet = remaining_packet
        else:
            n_sub_packets = _to_decimal(packet[:11])
            packet = packet[11:]

            for i in range(n_sub_packets):
                packet = self._process_packet(packet)

        return packet

    def _process_stack(self) -> int:
        values = []
        next_item = self.stack.pop()

        while isinstance(next_item, int):
            values.append(next_item)
            next_item = self.stack.pop()

        return next_item(values)


def _hex_to_binary(hex_string: str) -> str:
    scale = 16
    num_of_bits = int(len(hex_string) * log2(scale))
    return bin(int(hex_string, scale))[2:].zfill(num_of_bits)


def _to_decimal(binary_string: str) -> int:
    return int(binary_string, 2)


if __name__ == "__main__":
    print(f"part1={part1(INPUT)}")
    print(f"part2={part2(INPUT)}")
