import dropbox

access_token = "TOKEN"
dbx = dropbox.Dropbox(access_token)


def upload(file_path, dropbox_path):
    with open(file_path, "rb") as f:
        dbx.files_upload(f.read(), dropbox_path)

def get_file_metadata(path):
    try:
        metadata = dbx.files_get_metadata(path)
        return metadata
    except dropbox.exceptions.ApiError as e:
        if isinstance(e.error, dropbox.exceptions.PathRootError):
            print("Invalid path.")
        elif isinstance(e.error, dropbox.exceptions.AuthError):
            print("Authentication error.")
        else:
            print("Error occurred:", e)
        return None

def delete_file(path):
    try:
        response = dbx.files_delete_v2(path)
        print("File deleted successfully.")
    except dropbox.exceptions.ApiError as e:
        if isinstance(e.error, dropbox.exceptions.PathRootError):
            print("Invalid path.")
        elif isinstance(e.error, dropbox.exceptions.AuthError):
            print("Authentication error.")
        else:
            print("Error occurred:", e)


upload('file.ext', "/path/to/file.txt")

file_path = "/path/to/file.txt"
metadata = get_file_metadata(file_path)
if metadata is not None:
    print("File Name:", metadata.name)
    print("File Size:", metadata.size)
    print("Last Modified:", metadata.server_modified)

file_path = "/path/to/file.txt"
delete_file(file_path)
