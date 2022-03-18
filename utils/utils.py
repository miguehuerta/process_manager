import os
import re
import string
import subprocess
import time
from subprocess import check_output

import constants as cons


def execute_shell(command):
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    return proc.communicate()


def string_to_list(string):
    list_replaced = string.replace('\t', '|').replace(
        '\n', '|').replace(' ', '|').split('|')
    output_list_cleaned = [i for i in list_replaced if i]
    return output_list_cleaned


def clean_bytes_string(str):
    return str.decode("utf-8")
