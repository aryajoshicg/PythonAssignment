
files = input("Enter file extension: ").lower()

match files:
    case "pdf":
        print("Document")
    case "jpg":
        print("Image")
    case "png":
        print("Image")
    case "mp3":
        print("Audio")
    case "mp4":
        print("Audio")
    case _:
        print("Unknown file type")