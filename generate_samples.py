import os

# Folder where sample files will be created
sample_dir = "Test"
os.makedirs(sample_dir, exist_ok=True)

# Sample files per category
files = [
    "photo1.jpg", "photo2.png", "image.gif",
    "document1.pdf", "notes.txt", "report.docx",
    "video1.mp4", "movie.mkv",
    "randomfile.xyz", "script.sh"
]

for file in files:
    with open(os.path.join(sample_dir, file), "w") as f:
        f.write("Sample content for " + file)

print(f"Sample files created in '{sample_dir}'")
