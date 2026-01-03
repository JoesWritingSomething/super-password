# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

import random
import argparse
import uuid
import base64
from datetime import datetime
import string


def create_super_password(line, ludicrous=False, plaid=False, ridiculous=False, why=False):
    """
    Takes a line with password and passphrase, splits and shuffles everything.
    Returns a super-password with no spaces.
    """

    parts = line.strip().split()
    if not parts:
        return ""

    # Base components
    password = parts[0]
    passphrase_parts = parts[1:]
    all_components = list(password) + passphrase_parts

    # -----------------------------------------
    # LUDICROUS MODE
    # -----------------------------------------
    if ludicrous:
        special_chars = [
            '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
            '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\',
            ':', ';', '"', "'", '<', '>', ',', '.', '?', '/', '~', '`'
        ]

        num_specials = random.randint(10, 20)
        all_components.extend(random.choices(special_chars, k=num_specials))

        num_digits = random.randint(8, 15)
        all_components.extend([str(random.randint(0, 9)) for _ in range(num_digits)])

        num_letters = random.randint(10, 20)
        all_components.extend(random.choices(string.ascii_letters, k=num_letters))

        num_duplicates = random.randint(5, 10)
        all_components.extend(random.choices(all_components, k=num_duplicates))

    # -----------------------------------------
    # PLAID MODE
    # -----------------------------------------
    if plaid:
        all_components.append(str(uuid.uuid4()))
        all_components.append(datetime.now().strftime("%Y%m%d%H%M%S"))
        all_components.append(base64.urlsafe_b64encode(uuid.uuid4().bytes).decode('utf-8'))

    # -----------------------------------------
    # RIDICULOUS MODE
    # -----------------------------------------
    if ridiculous:
        science_terms = ["quark", "boson", "isotope", "entropy", "vector", "tensor"]
        history_terms = ["Hammurabi", "Thermopylae", "Byzantium", "Waterloo"]
        math_terms = ["π", "φ", "Σ", "Δ", "∞", "∇"]

        all_components.extend(random.choices(science_terms, k=5))
        all_components.extend(random.choices(history_terms, k=5))
        all_components.extend(random.choices(math_terms, k=5))

    # -----------------------------------------
    # WHY MODE (500+ characters)
    # -----------------------------------------
    if why:
        for _ in range(20):
            all_components.append(str(uuid.uuid4()))
        for _ in range(10):
            all_components.append(base64.urlsafe_b64encode(uuid.uuid4().bytes).decode('utf-8'))
        for _ in range(50):
            all_components.append(random.choice(string.ascii_letters + string.digits))

    # Final shuffle + join
    random.shuffle(all_components)
    return ''.join(all_components)


def main():
    parser = argparse.ArgumentParser(description='Create super-passwords from password files')
    parser.add_argument('--ludicrous', action='store_true', help='Enable LUDICROUS MODE')
    parser.add_argument('--plaid', action='store_true', help='Enable PLAID MODE')
    parser.add_argument('--ridiculous', action='store_true', help='Enable RIDICULOUS MODE')
    parser.add_argument('--why', action='store_true', help='Enable WHY MODE')
    parser.add_argument('--all', action='store_true', help='Generate ALL modes into one output file')
    args = parser.parse_args()

    # Input/output
    input_file = input("Enter the input text file name: ").strip()
    output_file = input("Enter the output text file name: ").strip()

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # Strip BOM from all lines
        lines = [ln.replace("\ufeff", "") for ln in lines]

        # -----------------------------------------
        # --all MODE
        # -----------------------------------------
        if args.all:
            all_modes = [
                ("NORMAL",      dict(ludicrous=False, plaid=False, ridiculous=False, why=False)),
                ("LUDICROUS",   dict(ludicrous=True,  plaid=False, ridiculous=False, why=False)),
                ("PLAID",       dict(ludicrous=False, plaid=True,  ridiculous=False, why=False)),
                ("RIDICULOUS",  dict(ludicrous=False, plaid=False, ridiculous=True,  why=False)),
                ("WHY",         dict(ludicrous=False, plaid=False, ridiculous=False, why=True)),
            ]

            with open(output_file, 'w', encoding='utf-8') as f:
                for mode_name, flags in all_modes:
                    f.write(f"===== {mode_name} MODE =====\n")
                    for line in lines:
                        line = line.replace("\ufeff", "")
                        if line.strip():
                            sp = create_super_password(line, **flags)
                            f.write(sp + "\n")
                    f.write("\n")

            print(f"\nSuccess! ALL modes written to {output_file}")
            return

        # -----------------------------------------
        # SINGLE MODE EXECUTION
        # -----------------------------------------
        super_passwords = []
        for line in lines:
            line = line.replace("\ufeff", "")
            if line.strip():
                sp = create_super_password(
                    line,
                    ludicrous=args.ludicrous,
                    plaid=args.plaid,
                    ridiculous=args.ridiculous,
                    why=args.why
                )
                super_passwords.append(sp)

        with open(output_file, 'w', encoding='utf-8') as f:
            for sp in super_passwords:
                f.write(sp + "\n")

        print(f"\nSuccess! Created {len(super_passwords)} super-passwords.")
        print(f"Output saved to: {output_file}")

    except FileNotFoundError:
        print(f"Error: Could not find file '{input_file}'")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
