# converter.py

# Author: Luca Ghislotti
# Version: 1.0.0

from requests import get
import numpy as np
from pathlib import Path
import pandas as pd

path_first = str(
    r"C:\Users\ghisl\Documents\GitHub\GAPS-Fine-Threshold-DAQ-Converter\modules\FR4"
)
path_second = (
    r"\1\analysis_matlab\ThresholdScan\Thr_disp_minimization_fine_thresholds.dat"
)

pt = 5


def get_folder_name(num_report):
    if num_report < 10:
        folder_name = "MODULE_00" + str(num_report)  # + "b"
    elif num_report < 100:
        folder_name = "MODULE_0" + str(num_report)  # + "b"
    else:
        folder_name = "MODULE_" + str(num_report)  # + "b"

    return folder_name


def write_file(file, channel, fth):
    file.write("fine threshold ch#" + str(channel) + " = " + str(fth) + "\n")


start = int(input("Range START: "))
stop = int(input(" Range STOP: "))

for i in range(start, stop + 1):
    folder_name = get_folder_name(i)
    full_path = str(path_first) + str("\\") + str(folder_name) + str(path_second)

    if Path(full_path).is_file():
        data = pd.read_csv(full_path, skiprows=1, sep="\t")
        output_path = (
            str("fthr_files")
            + str("\\")
            + str("FTH_test_defaults_")
            + str(folder_name[7:])
            + str(".defs")
        )

        output = open(output_path, "a")
        ch = 0

        for j in range(0, len(data)):
            if data.iloc[j, 0] == ch and data.iloc[j, 1] == pt:
                fth_dec = data.iloc[j, 2]
                fth_bin = bin(fth_dec).replace("0b", "").zfill(3)
                write_file(output, ch, fth_bin)
                ch = ch + 1

        output.close()
