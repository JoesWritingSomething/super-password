# 🔥 Super‑Password Forge 🔥

A Python script that transforms password/passphrase combinations into super‑passwords by splitting, mixing, augmenting, and shuffling all components — with optional modes that escalate entropy into the realm of the absurd.

---

## What It Does

Given a line like:

```Code
R3E9X4g7NeiVcbsw sough froth proof yn cadet blast orchid 345
```

It produces output like:

```Code
soughR3Efroth9X4proofg7NyneicadetVcblastbsorchidw345
```

The script:

- Takes a plaintext file of password/passphrase lines to start with

- Splits the password into characters

- Splits the passphrase into words

- Mixes everything together

- Applies optional chaos modes

- Shuffles the entire component list

- Joins it all into one continuous super‑password, per line

- Writes to a new text file, as specified by user

- Each run produces a different result.

---

## Usage

Basic Mode

```bash
python super-password.py
```

You’ll be prompted for:

- Input text file

- Output text file

This produces a shuffled super‑password for each line.

---

## Entropy Modes

The script supports five modes, each adding its own flavor of chaos.

### 🚀 Ludicrous Mode

```bash
python super-password.py --ludicrous
```

Adds:

- 10–20 random special characters

- 8–15 random digits

- 10–20 random letters

- 5–10 duplicated components

- Produces passwords 2–3× longer than normal.

### 🟪 Plaid Mode

```bash
python super-password.py --plaid
```

Adds:

- A UUID

- A timestamp

- A base64‑encoded random byte sequence

Perfect for when Ludicrous Mode is no longer enough.

### ☢️ Ridiculous Mode

```bash
python super-password.py --ridiculous
```

Adds:

- Random science terms

- Random historical references

- Mathematical symbols (π, Σ, ∞, etc.)

This mode is aggressively unnecessary.

### 🌌 WHY Mode

```bash
python super-password.py --why
```

Adds:

- 20 UUIDs

- 10 base64 blobs

- 50 random alphanumeric characters

Produces 500+ character monstrosities that question their own existence.

---

## 🧨 ALL MODES AT ONCE

```bash
python super-password.py --all
```

Generates five sections in the output file:

```Code
===== NORMAL MODE =====
...
===== LUDICROUS MODE =====
...
===== PLAID MODE =====
...
===== RIDICULOUS MODE =====
...
===== WHY MODE =====
...
```

This is the “management asked for a comparison chart” option.

---

## Input File Format

Each line must contain:

- An alphanumeric password (first token)

- A passphrase (remaining tokens)

Example:

```Code
JUgR4vF7iYjMqhT3 tipsy aim %% reeve aging uris chute gates
JVYiCNUPHjEowAfF 54 ) dunce reich mckee 5j wait dn
R3E9X4g7NeiVcbsw sough froth proof yn cadet blast orchid 345
```

Empty lines are ignored.

---

## Encoding Notes (Important on Windows)

- The script reads and writes files using UTF‑8

- BOM characters (U+FEFF) are automatically stripped

- Console output is forced to UTF‑8 for safety

This ensures math symbols, UUIDs, and base64 blobs don’t break the script.

---

## Requirements

- Python 3.6+

- No external dependencies

---

## File Size Limits

The script loads the entire file into memory:

- Up to ~100 MB: fine

- 100–500 MB: depends on RAM

- 1 GB+: possible but not recommended

---

## Example Run

```bash
$ python super-password.py --ludicrous
🚀 LUDICROUS MODE ACTIVATED! 🚀
Prepare for MAXIMUM password entropy!

Enter the input text file name: passwords.txt
Enter the output text file name: super_passwords.txt

Success! Created 150 super-passwords.
Average password length: 127 characters
These passwords are ABSOLUTELY RIDICULOUS! 🎉
Output saved to: super_passwords.txt
```

---

## License

Do whatever you want with it.
Forge responsibly. 🎉