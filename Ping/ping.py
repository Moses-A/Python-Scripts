#!/usr/bin/python3
#Written by Moses


import getopt
import os
import sys
import time


def ping(inputfile, loop):
   k = 0
   cwd = os.getcwd()
   path = (cwd+'/'+inputfile)
   #path = (cwd+'\\'+'IP.txt')
   with open(path, encoding='utf-8') as f:
      data = f.read().splitlines()
   array_length = len(data)
   while k < loop:
       k += 1
       time.sleep(10)
       for i in range(array_length):
           hostname = data[i]
           response = os.system("ping -c 1 " + hostname)
           if response == 0:
               print(hostname, 'Is Up!')
           else:
               print(hostname, 'Is Down!')
       

def main(argv):
   inputfile = ''
   loop = 1

   try:
      opts, args = getopt.getopt(argv, 'i:o:', ["ifile=","ofile="])
   except getopt.GetoptError:
      print ('ping.py -i <inputfile> -l <ping loop #>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h' or opt == '-H':
         print ('ping.py -i <inputfile> -l <ping loop #>')
         sys.exit()
      elif opt in ("-i", "--input"):
         inputfile = arg
      elif opt in ("-l", "--loop"):
         loop = arg
   print ('Input file is: ', inputfile) 
   print('Loop: ', loop)
   ping(inputfile, loop)


if __name__ == "__main__":
    main(sys.argv[1:])
