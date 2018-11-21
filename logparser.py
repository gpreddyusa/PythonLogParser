#!/usr/bin/env python3
import zipfile
import re
import sys

# This parser is to parse bugreport logs and find Bugle health information
#unzip
log_file = open("helth_matrics.txt", "w+")
def unzip_log_file(logfile):
        zip_ref = zipfile.ZipFile(logfile, 'r')
        zip_ref.extractall(".")
        zip_ref.close()

def create_bugle_log(raw_file_path):
    raw_file = open(raw_file_path, "r")
    bugle_file = open("bugle_log.txt", "w+")
    for bugle in raw_file:
        if re.match("(.*)(B|b)ugle(.*)", bugle):
            bugle_file.write(bugle)
            continue
        elif re.match("(.*)(R|r)cs(.*)", bugle):
              bugle_file.write(bugle)
              continue
        elif re.match("(.*)(S|s)ip(.*)", bugle):
             bugle_file.write(bugle)

def create_displey_log():
   
    bugle_file = open('bugle_log.txt', 'r')   
    RCSNOTEnabled  = "BugleRcs: MCCMNC is NOT RCS enabled"
    RCSenabled = "BugleRcs: MCCMNC is RCS enabled"
    RCSNOTcounts=0
    RCSCount=0
    for line in bugle_file.readlines():
        input = line  
        if RCSNOTEnabled in input: #see if one of the words in the sentence is the word we want
                RCSNOTcounts= RCSNOTcounts+1  
        elif RCSenabled in input:
                RCSCount = RCSCount +1

    log_file.write("------------> Health matrcis of RCS log <---------------- \n \n")
    if RCSNOTEnabled == 0 and RCSCount == 0:
        log_file.write("Sorry not find any RCS Status Log")
    else:
        log_file.write("RCS Enabled and Desabled status \n")
        log_file.write("RCS enabled "+ str(RCSCount) +" times \n")
        log_file.write("RCS Not enabled "+ str(RCSNOTcounts) +" times \n\n")

def get_rcs_bugle_exceptions():
        bugle_file = open('bugle_log.txt', 'r')
        keyword = "Exception"  
        log_file.write("RCS Bugle some Usefull logs for exceptions  \n")
        for line in bugle_file.readlines():
                input = line  
                if keyword in input: 
                        log_file.write(line)

# for Provisioning health logs for RCS 
def get_rcs_provisioning_health():
        bugle_file = open('bugle_log.txt', 'r')
        keyword = "provisioning"  
        log_file.write("\n \n RCS Bugle provisioning logs   \n")
        for line in bugle_file.readlines():
                input = line  
                if keyword in input: 
                        log_file.write(line)

def get_rcs_verbose_status():
        bugle_file = open('bugle_log.txt', 'r')
        keyword = "V Bugle"  
        log_file.write("\n \n RCS Bugle Verbose logs status  \n")
        for line in bugle_file.readlines():
                input = line  
                if keyword in input: 
                        log_file.write("\n \n Verbose is Enabled in logs   \n")
                else:
                        log_file.write(" Verbose is Not Enabled in logs  \n")
                break

def get_version_info(raw_file_path):
        raw_file = open(raw_file_path, "r")
        Packagename  = "Package [com.google.android.apps.messaging]"
        versionName = "versionName"
        for line in raw_file.readlines():
                input = line  
                if Packagename in input: #see if one of the words in the sentence is the word we want
                        log_file.write("\n--------- AM version details --------\n")
                        log_file.write(line)
              

               
                                
                


# def get_rcs_connectivity_health():

      

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
    create_displey_log()
    get_rcs_verbose_status()
    get_version_info(raw_file_name)
    get_rcs_bugle_exceptions()
    get_rcs_provisioning_health()


if __name__ == "__main__":
        main()