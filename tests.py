import os
import sys
from argparse import ArgumentParser
import yara

# File containing rules
#rules = yara.compile(filepath='/foo/bar/myrules')
# Compile directly from string
#rules = yara.compile(source='rule dummy { condition: true }')

#ROL encodes the file
def rolFun (strung, amount, bits):
  RoL = lambda val, r_bits, num_bits: \
    (val << r_bits%num_bits) & (2**num_bits-1) | ((val & (2**num_bits-1)) >> (num_bits-(r_bits%num_bits)))
  return rotated = RoL(strung, amount, bits)

#ROR encodes the file
def rorFun (strung, amount, bits):
  RoR = lambda val, r_bits, num_bits: \
    ((val & (2**num_bits-1)) >> r_bits%num_bits) | (val << (num_bits-(r_bits%num_bits)) & (2**num_bits-1))
  return rotated = RoR(strung, amount, bits)

#ADD encodes the file ----- NOT DONE, IDK HOW TO CONTINUE
def addFun (strung, key):
  #Stuff
  return encoded

def chooseEncode(strung, args)
num_bits = len(strung.encode('utf-16-le'))
if (args.ENCODE == ROL):
  encoded = rolFun(strung, args.AMOUNT, num_bits)
elif (args.ENCODE == ROR):
  encoded = rorFun(strung, args.AMOUNT, num_bits)
elif (args.ENCODE == ADD):
  encoded = addFun(strung, args.AMOUNT)
else:
    print('Argument Typo')
    return false

#Reads file into string variable
def fileStrung(file):
  f = open(file, "r")
  strung = f.read()
  f.close()
  return strung

#Makes YARA Rule
def makeRule(varString, method):
  lineStart = "rule"
  lineBracket = "{"
  line2 = " strings:"
  lineStrings = "   $string = \"%s\" %s" % varString, method
  lineCondition = " condition:"
  lineconditionList = "   $string"
  lineCloseBracket = "}"
  with open('rule_file','w') as out:
    out.writelines([lineStart, lineBracket, line2, lineStrings, lineCondition, lineconditionList, lineCloseBracket])
  return

#Creates rule, loads file, and scans it using YARA
def useYara(args):
  if (args.FILERULE != false):
    StringRules = fileStrung(args.FILERULE)
    makeRule(StringRules, args.ENCODE)
  else:
    with open('rule_file','w') as out:
        out.write(fileStrung(args.FILERULECOMP))
  rules = yara.compile('rule_file')
  matches = rules.match('new_data.txt')
  return matches

#Runs encoding functions on specified file then saves it
def runEncode(args):
  strung = fileStrung(args.FILE)
  encoded = chooseEncode(strung, args)
  if (encoded == false):
    return
  with open('new_data.txt','w') as out:
    out.write(encoded)
  return
  
#Get command line arguments
def get_args():
    parser = ArgumentParser(description="ADD, ROL, or ROR")
    parser.add_argument("-ENCODE", required=True, help="List type of Bitwise operation: ADD, ROL, or ROR")
    parser.add_argument("-MODIFY", required=True, help="Enter key for ADD operation or amount for ROL/ROR")
    parser.add_argument("-FILE", required=True, help="Filename for plaintext")
    parser.add_argument("-FILERULE", default=False, help="Filename for plaintext rule strings")
    parser.add_argument("-FILERULECOMP", default=False, help="Filename for complete Rules")
    parser.add_argument("-FILEENCODED", default=False, help="Flag for if the file is already encoded")
    args = parser.parse_args()
    return args

def main():
    args = get_args()
    if (args.FILEENCODED != true):
      encodedSuccess = runEncode(args)
      if (encodedSuccess == false):
        return
    else:
      with open('new_data.txt','w') as out:
        out.write(fileStrung(args.FILE))
    matches = useYara(args)
    print(matches)
    return
    
if __name__ == '__main__':
    main()
