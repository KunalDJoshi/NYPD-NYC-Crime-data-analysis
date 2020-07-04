"""
Author : KUNAL JOSHI.

File Name : Analytical_Thinking_Preprocess.py
Course: ISTE 600 - Analytical Thinking

Description:
    This is a Python program which will help in breaking down larger CSV files into smaller CSV files based
    upon the years. To do so, this Python program uses Pandas DataFrame to process the CSV file and write into other CSV
    File.

    LOW MEMORY option has been turned off to handle complex and computationally challenging operations.
    Reason :
        Low_memory warning can be issued because guessing data types for each column is very memory demanding.
        Pandas always tries to determine what data type to set by analyzing the data in each column.

    The writing of the newer CSV file is done in universal UTF-8 format for better accessibility and compatibility
    across various Operating Systems.

"""

import sys
import pandas as pd


def analytical_thinking_preprocess(file_Path, to_Path):
    """
    A Lambda Expression at the core of for loop processes every record based on Date field
    and applies the String split upon first / of the date format reverse.

    Read the Large CSV file.
    Split the original file into smaller CSV files based on Year number.

    :param file_Path: File path to original larger CSV dataset
    :param to_Path: Destination Folder file path where the new files will be written into
    :return: Bunch of CSV files (based on Years) in the mentioned destination file path
    """

    AT_DATA = pd.read_csv(file_Path, low_memory=False)

    cols = AT_DATA.columns

    AT_DATA['Year'] = AT_DATA['ARREST_DATE'].apply(lambda x: x.split('/')[-1])
    AT_DATA['Month'] = AT_DATA['ARREST_DATE'].apply(lambda x: x.split('/')[1])

    # for classified by years files

    for i in set(AT_DATA.Year):
        filename = to_Path + "\\" + "Output_File_Year_" + i + ".csv"
        AT_DATA.loc[AT_DATA.Year == i].to_csv(filename, index=False, columns=cols, encoding='UTF-8')


def main():
    """
    Helps in processing larger CSV files.
    :return: None
    """
    file_Path = sys.argv[1]
    to_Path = sys.argv[2]
    analytical_thinking_preprocess(file_Path, to_Path)


if __name__ == '__main__':
    main()
