from DepthASTNode import DepthASTNode
import re
from Util import Util


class BigramExtractor():
    # hex_reg_ex = re.compile(r'0[xX][0-9a-fA-F]+')
    nr_reg_ex = re.compile(r'\d+\t')
    multi_sp_reg_ex = re.compile(r'\s+')
    multi_dots_reg_ex = re.compile(r'\..+')

    def getASTNodeBigrams(self, dirPath):
        u = Util()
        test_file_paths = u.listFiles(dirPath, ".dep")
        bigrams = []
        lines = set()
        for file in test_file_paths:
            print (file)
            f = open(file).read()
            featureText = f.split("\n")
            dan = DepthASTNode()
            # print (f)
            lines = dan.getASTDepLines(f)
            print ("ASTDEpLines")
            print (lines)
            textAST = ""
            inputTextParanthesisRemoved = ""
            arr = []
            for j in lines:
                # textAST = dan.readLineNumber(f, j)
                textAST = featureText[j]
    #            print ("TEXTAST")
     #           print (textAST)
                inputTextParanthesisRemoved = textAST.replace("(", " ")
                inputTextParanthesisRemoved = inputTextParanthesisRemoved.replace(
                    ")", " ")
                inputTextParanthesisRemoved = re.sub(
                    self.nr_reg_ex, " ", inputTextParanthesisRemoved)
                inputTextParanthesisRemoved = re.sub(
                    self.multi_sp_reg_ex, " ", inputTextParanthesisRemoved)
                # print (inputTextParanthesisRemoved)
                arr = re.split(self.multi_sp_reg_ex,
                               inputTextParanthesisRemoved.strip())
                # print (arr)
                if (len(arr) > 1):
                    for i in range(1, len(arr)):
                        bigram = arr[i-1].strip() + " " + arr[i].strip()
                        if bigram not in bigrams and arr[i-1] and arr[i]:
                            bigrams.append(bigram)
        # print (bigrams)
        # print (len(bigrams))
        return bigrams

    def getASTNodeBigramsTF(self, featureText, ASTNodeBigrams):
        dict_TF = {}
        bigrams = []
        # f = open(file).read()
        f = featureText.split("\n")
        dan = DepthASTNode()
        # print (f)
        lines = dan.getASTDepLines(featureText)
        # print ("ASTDEpLines")
        # print (lines)
        textAST = ""
        inputTextParanthesisRemoved = ""
        arr = []
        for j in lines:
            # textAST = dan.readLineNumber(f, j)
            textAST = f[j]
            # print ("TEXTAST")
            # print (textAST)
            inputTextParanthesisRemoved = textAST.replace("(", " ")
            inputTextParanthesisRemoved = inputTextParanthesisRemoved.replace(
                ")", " ")
            inputTextParanthesisRemoved = re.sub(
                self.nr_reg_ex, " ", inputTextParanthesisRemoved)
            inputTextParanthesisRemoved = re.sub(
                self.multi_sp_reg_ex, " ", inputTextParanthesisRemoved)
            # print (inputTextParanthesisRemoved)
        arr = re.split(self.multi_sp_reg_ex,
                       inputTextParanthesisRemoved.strip())
        print (len(ASTNodeBigrams))
        if (len(arr) > 1):
            for i in range(1, len(arr)):
                bigram = arr[i-1].strip() + " " + arr[i].strip()
                if bigram not in bigrams and arr[i-1] and arr[i]:
                    bigrams.append(bigram)
        for node in ASTNodeBigrams:
            # count = sum(1 for _ in re.finditer(r'\b%s\b' %
           #                                    re.escape(inputTextParanthesisRemoved), node))
            # dict_TF[node] = count
            #dict_TF[node] = len(re.findall(inputTextParanthesisRemoved, node))
            dict_TF[node] = bigrams.count(node.strip())
        return dict_TF


def main():
    print("here")


main()
