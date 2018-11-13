#!/usr/bin/env python3
import zipfile
import re
import sys

# This parser is to parse bugreport logs and find Bugle health information
#unzip
def unzip_log_file(logfile):
        zip_ref = zipfile.ZipFile(logfile, 'r')
        zip_ref.extractall(".")
        zip_ref.close()

def create_bugle_log(raw_file_path):
        raw_file = open(raw_file_path, "rU")
        line = raw_file.readline()
        bugle_file = open("bugle_log.txt", "w+")
        while line:
                for bugle in line:
                        if re.match("(.*)(B|b)ugle(.*)", bugle):
                                bugle_file.write(bugle)
                line = raw_file.readline()

# def get_version_info():
# def get_rcs_verbose_status():
# def get_rcs_info():
# def get_rcs_connectivity_health():
# def get_rcs_provisioning_health():
# def get_rcs_bugle_exceptions():      

def main():
        #Read Arg and input to untar
        if len (sys.argv) != 2 :
                print ("Usage: python ex.py PATH of LOG FILE")
                sys.exit (1)
        program_name = sys.argv[0]
        path_to_log_file = sys.argv[1]
        unzip_log_file(path_to_log_file)
        file = open("main_entry.txt", "r") 
        raw_file_name = file.readline()
        create_bugle_log(raw_file_name)

# main Function 
if __name__ == "__main__":
        main()