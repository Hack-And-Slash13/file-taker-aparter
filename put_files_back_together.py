import os

folder = input("What's the name of the folder all the files are in? (Yes, they all have to be in one folder. Yes, I know you want to throw your computer out the window)")

print("Putting the files back together...")

filename = folder.replace(" - chopped up", "")
files = os.listdir(folder)
files.sort(key=lambda file: int(file.rsplit(".", 1)[1]))

with open(filename, "wb") as new_file:
    for file in files:
        with open(os.path.join(folder, file), "rb") as chunk:
            new_file.write(chunk.read())

print("Done!")
