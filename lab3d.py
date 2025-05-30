#!/usr/bin/env python3
'''lab 3 Part 2 system command'''
# Author ID: 148191232

import subprocess

def free_space():
    process = subprocess.Popen("df -h | grep ' /$' | awk '{print $4}'", stdout=subprocess.PIPE, shell=True)
    output = process.communicate()
    return output[0].decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())
