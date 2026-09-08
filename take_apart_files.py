import os

number = 0
chunk = b"1" #NameErrors suck

filename = input("What's the name of the file?")
size = int(input("How many bytes should the pieces be? (you need at least that much RAM)"))
print("Chopping up the file...")

os.makedirs(filename + " - chopped up", exist_ok=True)

with open(filename, 'rb') as file:
    while len(chunk) > 0:
        chunk = file.read(size)
        if len(chunk) == 0:
            break

        with open(os.path.join(filename + " - chopped up", filename + f".{number}"), "wb") as new_file:
            new_file.write(chunk)
        print(f"created {filename}.{number}")
        number += 1

print("Done!")
