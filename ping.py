#!/usr/bin/python
#Written by Moses


import getopt
import os
import sys
import sched
import time


def ping(inputfile):
   cwd = os.getcwd()
   #path = (cwd+'\\'+inputfile)
   path = (cwd+'\\'+'IP.txt')
   with open(path, encoding='utf8') as f:
      data = f.read().splitlines()

   array_length = len(data)

   for i in range(array_length):
      hostname = data[i]
      response = os.system("ping " + hostname)

      if response == 0:
         print(hostname, 'Is Up!')
      else:
         print(hostname, 'Is Down!')


def main(argv):
   inputfile = ''

   try:
      opts, args = getopt.getopt(argv, "hi:o:", ["ifile="])
   except getopt.GetoptError:
      print ('ping.py -i <inputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h' or opt == '-H':
         print ('ping.py -i <inputfile>')
         sys.exit()
      elif opt in ("-i", "--input"):
         inputfile = arg
   print ('Input file is: ', inputfile)
   ping(inputfile)


if __name__ == "__main__":
   main(sys.argv[1:])
