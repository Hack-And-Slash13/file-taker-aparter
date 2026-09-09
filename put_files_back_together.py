from pathlib import Path

def user_input():
    retun input("What's the name of the folder all the files are in? (Yes, they all have to be in one folder. Yes, I know you want to throw your computer out the window) ")

def resolve_filename(segments_dir: Path) -> Path:
    segments_dir = segments_dir.resolve()
    filename = segment_dir.parts[-1].replace(" - chopped up", "")
    return segment_dir.parent / filename
    
def take_back_together(segments_dir: Path, path: Path) -> int:
    print("Putting the files back together...")
    
    segments = sorted(tuple(segments_dir.glob("*")))
    
    with open(path, "wb") as new_file:
        for segment in segments:
            new_file.write(segment.read_bytes())
    
    print("Done!")
    
    return 0

if __name__ == "__main__":
    import sys
    from argparse import ArgumentParser

    ArgumentParser(
        prog='Hack-And-Slash/File Taker Aparter - Put Files Back Together',
        description='This script reconstructs any file segmented by `Take Apart Files` by putting back together every file in the given folder.'
    )
    
    segments_dir = Path(user_input())
    original_file = resolve_filename(segment_dir)
    sys.exit(take_back_together(segments_dir, original_file))
