#!/usr/bin/python
#Written by Moses

#!/usr/bin/python

import sys, getopt
import os


def ping(inputFile, outputFile):
   cwd = os.getcwd()
   path = (cwd+' '+inputFile)
   with open(path, encoding='utf8') as f:
      data = f.read()
   print(data)


def main(argv):
   inputFile = ''
   outputFile = ''

   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print ('ping.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h' or opt == '-H':
         print ('ping.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--input"):
         inputfile = arg
      elif opt in ("-o", "--output"):
         outputfile = arg
   print ('Input file is "', inputFile)
   print ('Output file is "', outputFile)
   ping(inputFile, outputFile)

if __name__ == "__main__":
   main(sys.argv[1:])


