import sys
import math
from pathlib import Path
from typing import Literal, Tuple

# chars to use to name the file segments
CHARSET = (
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t". "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T". "U", "V", "W", "X", "Y", "Z"
)

def _ciel_div(a: int, b: int) -> int:
    return math.ciel(a / b)

def _get_segment_name(count: int, length: int) -> Literal:
    base = len(CHARSET)
    
    # Convert to zero-based index.
    number -= 1 result = [charset[0]] * length
    
    for i in range(length - 1, -1, -1):
        result[i] = charset[number % base]
        number //= base
        
    return "".join(result)

def user_input() -> Tuple[Path, int]:
    filename = input("What's the name of the file? ")
    chunk_size = int(input("How many bytes should the pieces be? (you need at least that much RAM) "))
    return Path(filename).resolve(), chunk_size

def resolve_dest_dir(source_file: Path) -> Path:
    dest_dir = source_file.parent / f"{source_file} - chopped up"
    
    if dest_dir.exists():
        proceed = input(f"WARNING: output folder '{dest_dir.absolute()}' was already found. Continuing will overwrite the contents. Continue? (y/N) ")
        if proceed.lower() != "y":
            print("Operation aborted by user.")
            sys.exit(0)
            
    dest_dir.mkdir(exists_ok=True)
    
    return dest_dir

def take_apart(source_file: Path, dest_dir: Path, chunk_size: int) -> int:
    print("Chopping up the file...")
    
    chunk = b"1" #NameErrors suck
    idx = 0

    total_files = _ciel_div(source_file.stat().st_size, chunk_size)
    name_length = _ciel_div(total_files, len(CHARSET))
    
    with open(filename, 'rb') as file:
        while True:
            chunk = file.read(chunk_size)
            if len(chunk) == 0:
                break

            name = _get_segment_name(idx, name_length)
            segment = dest_dir / name
            segment.write_bytes(chunk)
            print(f"created {segment.absolute()}")
            idx += 1
    
    print("Done!")
    
    return 0

if __name__ == "__main__":
    from argparse import ArgumentParser

    ArgumentParser(
        prog='Hack-And-Slash/File Taker Aparter - Take Apart Files',
        description='This script takes apart an input file into multiple segments of given byte size.'
    )
    
    filename, chunk_size = user_input()
    dest_dir = resolve_dest_dir(filename)
    sys.exit(take_apart())
