<<<<<<< HEAD
import os,glob

class Util():
        #def __init__(self,file_path):
        #       __init__(self, file_path)
        
                
        def write_file(allLines,fileName, append):
                if (append == TRUE):            
                        file = open(fileName , 'a+') 
                else:
                        file = open(fileName , 'w+')
        
        def readNDISASMFile(self,fileName):
                fileStr = ' '
                f = open(fileName , "r")
                for x in f:
                        temp = x.split(' ',3)
                        #print(temp)
                        fileStr += ' ' + str(temp[3]).strip()
                return fileStr

        def listFiles (self, dirPath, extension):
                allFiles = []
                #os.chdir("/mydir")
                for r,d,files in os.walk(dirPath):
                        #for d in dirs:
                        for file in files:
                                fileExt = os.path.splitext(file)[-1]
                                #print (fileExt)
                                if (fileExt == extension):
                                        #print (os.path.join(r,file))
                                        allFiles.append(os.path.join(r,file))
                return allFiles
                #for file in glob.glob("*.txt"):        
                #       textFiles.append(file)
                #       print (file)
                #return textFiles
                
        def listAllFiles(self, dirPath):
                allFiles = []
                #os.chdir("/mydir")
                for file in os.listdir(dirPath):
                        allFiles.append(os.path.join(dirPath, file))
                return allFiles
        
        def listAllFilesFolders(self, dirPath):
                all = []
                for r, d, f in os.walk(dirPath):
                        all.append(d)
                        all.append(f)
                return all

        def listBinaryFiles(self, dirPath):
                binaryFiles = []
                for r, d, files in os.walk(dirPath):
                        for file in files:                              
                                fileExt = os.path.splitext(file)[-1]
                                if ('' == fileExt): # and os.path.isfile(os.path.join(d,file))):
                                        binaryFiles.append(os.path.join(r, file))
                                        #import pdb; pdb.set_trace()
                                        #binaryFiles.append(os.path.join(d,file))
                return binaryFiles
        
        def readFile(self, fileName, readAll):
                allWords = []
                f = open(fileName , "r")
                for dataLine in f:
                        if (readAll):   
                                allWords.append(dataLine)
                        else:
                                if (not allWords.contain(dataLine)):
                                        allWords.add(dataLine)
                return allWords

        def readFile(self, fileName):
                allLines = []
                for dataLine in f:
                        allLines.append (dataLine)
                        allLines.append ('\n')
                return allLines
                        #temp = x.split(' ',3)
                        #print(temp)
                        #fileStr += ' ' + str(temp[3]).strip()

#TODO readFile and readCFG, ast dep
#For testing purposes
def main ():
        print ("here")
        u = Util()
        #print (u.readNDISASMFile('/home/kejsi/3authors/kAc/1645485_1673486_kAc.dis'))
main()
