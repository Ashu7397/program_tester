import os
import re
import zipfile
import shutil

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)


def do_validate_files_and_sort(folder_name, log_file_name, folder_to_copy):
    folder_name = folder_name + os.path.sep
    path_to_copy = '..' + os.path.sep + '..' + os.path.sep + folder_to_copy + os.path.sep
    counter = 0
    error_log_file = open(log_file_name, 'a')
    os.chdir(folder_name)
    all_folders = sorted(os.listdir())
    for folder in all_folders:
        if os.path.isdir(folder):  # Folder of student files
            with cd(folder):
                zip_file = os.listdir()  # Here assuming only file is uploaded
                if len(zip_file) > 1:  # If greater than one, then validation is probably already done
                    continue
                # Check if submission format is right
                zip_file_name, counter = check_zip_filename(folder, str(zip_file[0]), error_log_file, counter)
                if zip_file_name:
                    counter = do_file_sorting(folder, zip_file_name, error_log_file, path_to_copy, counter)
    error_log_file.write("Not processed: {} files\n".format(counter))
    error_log_file.write('*'*25 + 'End of File' + '*'*25 + '\n')
    error_log_file.close()



def do_file_sorting(folder_name, zip_file_name, error_log_file, path_to_copy, not_used_counter):
    try:
        with zipfile.ZipFile(os.getcwd() + os.path.sep + zip_file_name, 'r') as zip_ref:
            zip_ref.extractall()
    except zipfile.BadZipFile:
        not_used_counter += 1
        error_log_file.write('ERROR: Bad Zipfile: ' + str(zip_file_name) + ', ' + str(folder_name).split('_')[0])
    all_c_files = sorted(os.listdir())  # Get all the files in the zip
    for c_file in all_c_files:
        if os.path.isdir(c_file):
            # Student uploaded in a nested folder probably
            not_used_counter += 1
            error_string = 'ERROR_FILENAME_NESTED_FOLDER: ' + str(folder_name).split('_')[0] + ' ' + c_file + '\n'
            error_log_file.write(error_string)
            print("Have to manually look at it..: " + error_string)
            # TODO: Have to solve it somehow
        if '.c' in c_file:
            c_file = check_c_filename(folder_name, c_file, error_log_file)
            if c_file:  # Is a match so valid candidate to be moved
                q_number = ''.join(c for c in str(c_file).split('_')[1] if c.isdigit())
                id_number = ''.join(c for c in str(c_file).split('_')[2].strip('.c') if c.isdigit())
                original_id_number = str(folder_name.split('_')[4])
                if not id_number == original_id_number:
                    error_log_file.write('ERROR_WRONG_ID: ' + str(folder_name).split('_')[0] + ' ' + original_id_number\
                                       + ' '  + id_number + '\n')
                dst_folder = path_to_copy + str(folder_name.split('_')[0]) + '_' + original_id_number + os.path.sep \
                             + 'q' + q_number + os.path.sep
                if os.path.exists(dst_folder):
                    error_log_file.write('ERROR_DST_FOLDER: ALREADY_EXISTS_' + str(c_file) + ' in ' + folder_name + '\n')
                else:
                    os.makedirs(dst_folder, exist_ok=True)
                shutil.copy2(c_file, dst_folder)
    return not_used_counter

def check_zip_filename(folder_name, zip_filename, error_log_file, not_used_counter):
    if re.match(r"^ex3_\d{9}.zip$", zip_filename, re.IGNORECASE):
        return zip_filename, not_used_counter
    error_log_file.write('ERROR_FILENAME: ' + str(folder_name).split('_')[0] + ' ' + zip_filename + '\n')
    if re.match(r"^ex3_\d{9}.zip.zip$", zip_filename, re.IGNORECASE):
        re.sub(".zip", "", zip_filename, count=1)
        return zip_filename, not_used_counter
    if re.match(r"^hw3_\d{9}.zip$", zip_filename, re.IGNORECASE):
        re.sub("hw", "ex", zip_filename, count=1, flags=re.IGNORECASE)
        return zip_filename, not_used_counter
    not_used_counter += 1
    # They can make more mistakes, but I am not creative enough ot catch all of them...
    return None, not_used_counter


def check_c_filename(folder_name, c_filename, error_log_file):
    if re.match(r"^ex3_q[1-3]_\d{9}.c$", str(c_filename), re.IGNORECASE):
        return c_filename
    error_log_file.write('ERROR_C_FILENAME: ' + str(folder_name).split('_')[0] + ', ' + str(c_filename) + '\n')
    if re.match(r"^ex3_q[1-3]_\d{9}.c.c$", str(c_filename), re.IGNORECASE):
        re.sub(".c", "", c_filename, count=1)
        return c_filename
    if re.match(r"^ex3_q[1-3]_\d{9}..c$", str(c_filename), re.IGNORECASE):
        re.sub(".", "", c_filename, count=1)
        return c_filename
    # They can make more mistakes, but I am not creative enough ot catch all of them...
    return None


if __name__ == "__main__":
    do_validate_files_and_sort('New_Data_Test_Raw', 'ERROR_LOG_FILE.txt', 'New_Data_TEST_PROCESSED')