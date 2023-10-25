# File-Splitter
This is a GUI based python app that can take a large csv file and split it into X number of files with X rows while inserting the file header onto each file. This program will also be able to take any csv file and extract the top X rows and save as a short file and trim the top X rows off the original file as to not have duplicate records.

pyinstaller --onefile .\main_psg.py -w

-w does not open a cmd window when running the exe