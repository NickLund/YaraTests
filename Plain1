import sys
import os
import crypt
    
#dictionary attack function
def crackAttempt(saltFull, trueHash):
    with open("realhuman_phill.txt", "r") as crackerListFile:
        count = 1
        attemptWord = crackerListFile.readline()
        while attemptWord:
            #crypt takes password, then the salt with encoding type, then encrypts it
            hashed = crypt.crypt(attemptWord,saltFull)
            if (trueHash == hashed):
                print("Hash: %s has password %s. Too bad we moving so fast you can't read this huh?" % (trueHash, attemptWord))
                fatCrackedPassList = open("FattyList.txt","wa+")
                fatCrackedPassList.write("Hash: %s has password %s" % (trueHash, attemptWord))
                fatCrackedPassList.close()
                break
            print("Attempt number %s Password: %s is hashed as: %s" % (count, attemptWord, hashed))
            count += 1
            attemptWord = crackerListFile.readline()

def main():
    # open file of pure hashes to compare with later
    trueHashFile = open("compare.txt", "r")
    
    #counter for pure hash line
    count = 1
    #open file of salts, pass single salt and hash into dictionary attack fuction
    #With statement same as try: f=open('file') finally: f.close()
    with open("salts.txt", "r") as saltListFile:
        saltStart = saltListFile.readline()
        while saltStart:
            trueHash = trueHashFile.readline(count)
            #saltFull = encodingType + saltStart
            saltFull = saltStart
            crackAttempt(saltFull, trueHash)
            count += 1
            saltStart = saltListFile.readline()
    trueHashFile.close()

if __name__ == "__main__":
    main()
