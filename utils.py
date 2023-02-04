import os.path
import pandas as pd


# ---------------------------------------------------------------------------------------*
# -----------------------------------Check Dir-------------------------------------------*
# ---------------------------------------------------------------------------------------*
def check_dir(_dir):
    # MYDIR = ("CSV")
    MYDIR = _dir
    CHECK_FOLDER = os.path.isdir(MYDIR)

    if not CHECK_FOLDER:
        os.makedirs(MYDIR)
        print("created folder : ", MYDIR)

    else:
        print(MYDIR, "folder already exists.")


# ---------------------------------------------------------------------------------------*
# -----------------------------------Make CSV File --------------------------------------*
# ---------------------------------------------------------------------------------------*
def create_csv(file_name, temp_list):

    if not os.path.exists(file_name):
        # print("in if")
        # fresh_start = False
        print("File is creating")
        df = pd.DataFrame.from_records(temp_list)
        df.to_csv(file_name, header=True, index=False)
    else:
        print("File is already exist")
        # print("in else")
        df = pd.DataFrame.from_records(temp_list)
        df.to_csv(file_name, mode='a',
                  header=False, index=False)
