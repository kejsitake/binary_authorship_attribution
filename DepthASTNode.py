import numpy as np
import re


class DepthASTNode():

    def getASTDepLines(self, featureText):
        functionIds = set()
        functionIds2 = set()
        firstWord = ""
        for line in featureText:
                firstWord = line[0:2]
                if (firstWord not in functionIds) :
                        functionIds.add(firstWord)
        ASTDepLines = np.empty(len(functionIds), dtype=int)
        i=0
        for f in featureText:
                firstWord = f[0:2]
                if (i==0):
                        functionIds2.add(firstWord)
                else:
                        if (firstWord in functionIds2):
                                lineNumber = i
                                ASTDepLines [len(functionIds2)-1] = lineNumber
                        if (i == (len(featureText)-1)):
                                lineNumber = i-1
                                ASTDepLines [len(functionIds2)-1] = lineNumber
                        functionIds2.add(firstWord)
                i+=1
        return ASTDepLines

    def frequencyCountAndPositions(self, mainStr, subStr):
        counter = pos = 0
        indexpos = []
        substrs = [")"+subStr +"(","("+subStr +"(","("+subStr +")",")"+subStr +")"]
        for subStr in substrs:
            index=0
            text = subStr
            while index < len(mainStr):
                index = mainStr.find(text, index)
                if index == -1:
                    break
                else:
                    indexpos.append(index)
                index += len(text)
        return indexpos


    def wholeWordIndexFinder(self, textAST, st):
        import pdb; pdb.set_trace()
        result = [m.start() for m in re.finditer(st, textAST)]
        return result

    def getAvgDepthASTNode(self, featureText, ASTTypes):
        lines = self.getASTDepLines(featureText)
        #print (lines)
        #import pdb; pdb.set_trace()
        occurrences = {}
        totalDepth = {}
        avgDepth = {}
        textAST = ""
        for l in lines:
            textAST = featureText[l]
            #import pdb; pdb.set_trace()
            for ast in ASTTypes:
                finder = self.frequencyCountAndPositions(textAST, ast)
                if ast in occurrences:
                    occurrences[ast] += len(finder)
                else:
                    occurrences[ast] = len(finder)
                #import pdb; pdb.set_trace()
                for k in finder:
                    import pdb;# pdb.set_trace()
                    rightParanthesis = 0
                    leftParanthesis = 0
                    for c in textAST[0:k]:
                        if c=='(':  
                            rightParanthesis += 1
                        if c==')':
                            leftParanthesis +=1
                    if ast in totalDepth:
                        totalDepth[ast] += rightParanthesis -leftParanthesis
                    else:
                        totalDepth[ast] = rightParanthesis -leftParanthesis
                if occurrences[ast]==0:
                    avgDepth[ast]=0
                elif totalDepth[ast]==0:
                    avgDepth[ast]=0
                else:
                    #pdb.set_trace()
                    avgDepth[ast] = totalDepth[ast]/occurrences[ast]
        return avgDepth
def main ():
    print ("here")
main()
