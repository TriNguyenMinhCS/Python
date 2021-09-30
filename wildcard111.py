from pathlib import Path
for path in Path("/").glob("*.*"):
    print(path)