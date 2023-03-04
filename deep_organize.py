import os
import shutil

# generic file formats for different file types
file_formats = {
        "Photos" : ["webp","jpg","jpeg","png","heic","opus","webp","bmp","tiff"],
        "Audios" : ["mp3","aac","pcm","wav","aiff","wma","alac","flac"],
        "Videos" : ["mov","mp4","flv","avi","mov","wmv","mkv","webm"],
        "Documents" : ["doc","docx","xls","xlsx","pdf","rtf","txt"],
        "Compressed" : ["rar","7z","zip","tar","gzip"],
        "Misc" : ["This folder will be used to store any other file types"]
    }

# this will create folders to store different types of files such as photos, videos, etc.
def create_storage_folders(output_dir):
    for key in file_formats.keys():
        create_dir = os.path.join(output_dir,key.upper())
        if os.path.isdir(create_dir):
            print(f"ALREADY_EXISTS :: {create_dir}")
        else:
            os.mkdir(create_dir)
            print(f"CREATED_DIR :: {create_dir}")
    print("All storage directories are created/exists.")


# this function organizes the objects into multiple directories based on the file type
def organize_objects(items,OUTPUT_DIR):
    urorganized_objects = []
    organized_type = []
    for item in items:
        extention = item.split(".")[-1]
        if len(extention) <= 5:
            for key in file_formats.keys():
                if extention in file_formats[key]:
                    # copying object to the specific type directory
                    try:
                        shutil.copy(item, os.path.join(OUTPUT_DIR,key))
                        # shutil.move(item, os.path.join(OUTPUT_DIR,key))
                    except:
                        print(f"Duplicate File :: {item}")

                    organized_type.append(key)
        else:
            try:
                shutil.copy(item, os.path.join(OUTPUT_DIR,"Misc"))
                # shutil.move(item, os.path.join(OUTPUT_DIR,key))
            except:
                print(f"Duplicate File :: {item}")
            urorganized_objects.append(item)
    
    print(f"\nOrganized a total of {len(organized_type)} known files for you in below folders:-")
    print(f"Photos :: {organized_type.count('Photos')}",end=" | ")
    print(f"Audios :: {organized_type.count('Audios')}",end=" | ")
    print(f"Videos :: {organized_type.count('Videos')}",end=" | ")
    print(f"Documents :: {organized_type.count('Documents')}",end=" | ")
    print(f"Compressed :: {organized_type.count('Compressed')}")
    print(f"\nOrganized a total of {len(urorganized_objects)} unknown files for you in [Misc] directory.")


# fetches all objects from any given folder until complete depths
def fetch_all_objects(dir,files):
    objects = os.listdir(dir)
    for object in objects:
        path = os.path.join(dir,object)
        if os.path.isdir(path):
            fetch_all_objects(path,files)
        else:
            files.append(path)
        
    return files

if __name__ == "__main__":
    files = []
    
    INPUT_DIR = input("Please enter directory to organize (exlude last slash) : ")
    OUTPUT_DIR = input("Please enter directory where to keep the organized files : ")

    items = fetch_all_objects(INPUT_DIR,files)
    storage = create_storage_folders(OUTPUT_DIR)
    organize_objects(items,OUTPUT_DIR)
