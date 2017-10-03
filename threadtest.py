#!/usr/bin/python

import thread
import time

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print "%s: %s" % ( threadName, time.ctime(time.time()) )

# Define a function for the thread
def print_name( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print "%s: %s" % ( threadName, "Vishal")

# Create two threads as follows
try:

    #either start serial or parallel not both.

    #start serial execution
    print_time( "One", 1)
    print_name( "Two", 1)
    #end serial execution

    #start parallel execution
    #thread.start_new_thread( print_time, ("One", 1, ) )
    #thread.start_new_thread( print_name, ("Two", 1, ) )
    #end parallel execution

except:
   print "Error: unable to start thread"


print "crtl +c to kill"
while 1:
    pass
