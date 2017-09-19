#!/usr/bin/python

import os, time, sys
os.system("ls")
print("kill {0}".format(sys.argv[2]))
print("sleep for {0}..".format(sys.argv[1]))

time.sleep(int(sys.argv[1]))

os.system("kill -9 {0}".format(sys.argv[2]))

