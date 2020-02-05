import os
import sys
from argparse import ArgumentParser
import yara

FirstPlain = "Test1/PlainText"
FirstADD = "Test1/First_ADD_Encoded"
FirstROL = "Test1/ROL_Encoded"
FirstROR = "Test1/ROR_Encoded"

SecondPlain = "Test2/Plain1"
SecondADD = "Test2/ADD1"
SecondROL = "Test2/ROL1"
SecondROR = "Test2/ROR1"

#Reads file into string variable
def fileStrung(file):
  f = open(file, "r")
  strung = f.read()
  f.close()
  return strung

#Creates rule, loads file, and scans it using YARA
def useYara(args):
rules = yara.compile('rule_file')
matches = rules.match('new_data.txt')

def main():

    
if __name__ == '__main__':
    main()
