import os
import shutil

folder_path = input("Enter folder path:")

# files = os.listdir(folder_path)
# for file in files:
#     extension = os.path.splitext(file)[1]
#     print(file, "->", extension)
# print(files)

images_folder = os.path.join(folder_path,"Images")
documents_folder= os.path.join(folder_path,"Documents")
pdfs_folder = os.path.join(folder_path,"PDFs")

os.makedirs(images_folder , exist_ok = True)
os.makedirs(documents_folder,exist_ok=True)
os.makedirs(pdfs_folder,exist_ok=True)

files = os.listdir(folder_path)
for file in files :
    file_path = os.path.join(folder_path,file)

    if os.path.isfile(file_path):
        extension = os.path.splitext(file)[1].lower()
        if extension in [ ".jpg" , ".png" , ".jpeg"]:
            destination = os.path.join(images_folder,file)
            shutil.move(file_path,destination)
            print(f"Moved {file} to Images")
            
        elif extension == ".pdf":
            destination=os.path.join(pdfs_folder,file)
            shutil.move(file_path,destination)
            print(f"Moved {file} to PDFs")

        elif extension in [".txt",".docx"]:
            destination = os.apth.join(documents_folder,file)
            shutil.move(file_path,destination)
            print(f"Moved {file} to documents")


          
print("Folders Created")