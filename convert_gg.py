#!/usr/bin/env python3
import argparse

ALPHABET = "ABCDEFGHJKLMNPRSTVWXYZ0123456789"

# Maps for encoding/decoding
char_to_bits = {c: format(i, "05b") for i, c in enumerate(ALPHABET)}
bits_to_char = {format(i, "05b"): c for i, c in enumerate(ALPHABET)}

BIT_TEMPLATE = "ijklmnopIJKLMNOPABCDEFGHdefghabcQRSTUVWX"
OUTPUT_LABELS = "ABCDEFGHIJKLMNOPQRSTUVWXabcdefghijklmnop"

def encode(address_hex: str, value_hex: str) -> str:
    address = int(address_hex, 16)
    value = int(value_hex, 16)

    if address > 0xFFFFFF:
        raise ValueError("Address must be <= FFFFFF")
    if value > 0xFFFF:
        raise ValueError("Value must be <= FFFF")

    # Build output bits
    output_bits = f"{address:024b}{value:016b}"
    label_to_bit = dict(zip(OUTPUT_LABELS, output_bits))

    # Rearrange bits into GG order
    gg_bits = "".join(label_to_bit[ch] for ch in BIT_TEMPLATE)

    # Convert into GG chars
    code = ""
    for i in range(0, 40, 5):
        chunk = gg_bits[i:i+5]
        code += bits_to_char[chunk]

    return f"{code[:4]}-{code[4:]}"

def decode(code: str):
    code = code.replace("-", "").upper()

    if len(code) != 8:
        raise ValueError("Code must be 8 characters")

    # Convert GG chars to bitstream
    gg_bits = "".join(char_to_bits[c] for c in code)

    # Reverse mapping
    label_to_bit = dict(zip(BIT_TEMPLATE, gg_bits))

    # Rebuild output bits
    output_bits = "".join(label_to_bit[ch] for ch in OUTPUT_LABELS)

    address_bits = output_bits[:24]
    value_bits = output_bits[24:]

    address = int(address_bits, 2)
    value = int(value_bits, 2)

    return f"{address:06X}", f"{value:04X}"

def main():
    parser = argparse.ArgumentParser(description="Genesis Game Genie converter")
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument("-e", "--encode", nargs=2, metavar=("ADDR", "VAL"),
                       help="Encode address + value into Game Genie")
    group.add_argument("-d", "--decode", metavar="CODE",
                       help="Decode Game Genie into address + value")

    args = parser.parse_args()

    if args.encode:
        addr, val = args.encode
        print(encode(addr, val))

    elif args.decode:
        addr, val = decode(args.decode)
        print(f"Address: {addr}")
        print(f"Value:   {val}")

if __name__ == "__main__":
    main()
