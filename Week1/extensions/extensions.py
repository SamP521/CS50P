file_name = input("Enter the filename: ")
split_file = file_name.strip().lower().split(".")
file_ext = split_file[-1]

if len(split_file) == 1:
    print("application/octet-stream")
else:
    match file_ext:
        case "gif":
            print("image/gif")
        case "jpg":
            print("image/jpeg")
        case "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")
