from PIL import Image
import os

downloadsFolder = "/Users/[user]/Downloads/"
picturesFolder = "/Users/[user]/Pictures/"

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(downloadsFolder + filename)
            picture.save(picturesFolder + "compressed_"+filename, optimize=True, quality=60)
            os.remove(downloadsFolder + filename)
            print(name + ": " + extension)

        if extension in [".mp3"]:
            musicFolder = "/Users/[user]/Music/"
            os.rename(downloadsFolder + filename, musicFolder + filename)

        if extension in [".docx",".pptx","xlsm",".ppt", ".pdf"]:
            documentFolder ="/Users/[user]/Documents"
            os.rename(downloadsFolder + filename, documentFolder + filename)



