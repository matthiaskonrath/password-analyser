"""
# Author: Matthias Konrath
# Email: matthias.konrath@bbmk.at
"""


import os
import operator
import pickle
import re


passwords = {}

file_path = "/Volumes/ENC_SSD_APFS/BreachCompilation/data/"

counter = 0

delimiters = [";", ":", "\t", "|", "\n"]


def store_password(passwords, tmp_password, counter):
    # Password does not exist
    if tmp_password in passwords:
        # Password does exist
        passwords[tmp_password] = (int(passwords.get(tmp_password)) + 1)
    else:
        passwords[tmp_password] = 1


def split(delimiters, string, maxsplit=0):
    import re
    regexPattern = '|'.join(map(re.escape, delimiters))
    return re.split(regexPattern, string, maxsplit)


def print_top_10(passwords):
    tmp_passwords = passwords
    for _ in range(0, 10):
        passwd = max(tmp_passwords.items(), key=operator.itemgetter(1))[0]
        print(passwd, tmp_passwords[passwd])
        del(tmp_passwords[passwd])


def password_list_size(passwords):
    print(len(passwords))



for directory, subdirectories, files in os.walk(file_path):
    for file in files:
        print(os.path.join(directory, file))
        with open(os.path.join(directory, file), "r") as file_handler:
            for line in file_handler:
                try:
                    tmp_password = split(delimiters, line)[1]
                    store_password(passwords, tmp_password, counter)
                except IndexError:
                    print(line)

                except Exception as exc:
                    print(exc)
                    print(line)




#passwords = pickle.load(open("passwords.p", "rb"))

#print_top_10(passwords)
#password_list_size(passwords)

pickle.dump(passwords, open("passwords.pickle", "wb"))



#