
import os
import re
from Util import Util
from pathlib import Path
from array import *


class FeatureExtractorBjoern():
    hex_reg_ex = re.compile(r'0[xX][0-9a-fA-F]+')
    nr_reg_ex = re.compile(r'\d+')
    multi_sp_reg_ex = re.compile(r'\s+')
    multi_dots_reg_ex = re.compile(r'\..+')

    def getBjoernCFGGraphmlNodeUnigrams(self, dirPath):
        words = []
        nodes = []
        to_add = []
        u = Util()
        test_file_paths = u.listFiles(dirPath, ".graphml")
        for file in test_file_paths:
            f = open(file).readlines()
            replace_map = {
                "<node id=": "\n <node id=",
                "<edge id=": "\n <edge id=",
            }
            for line in f:
                for key, word in replace_map.items():
                    line = re.sub(key, word, line)
                nodes += line.split("\n")
            for node in nodes:
                if (">BB</data>" in node):
                    temp = node.split("data key=", 5)
                    node = temp[1]
                    node = node.replace(',', ' ')
                    node = node.replace("\"repr\">", " ")
                    node = node.replace("</data><", " ")
                    node = node.replace('|', ' ')
                    node = node.replace('\s+', ' ')
                    node = re.sub(self.hex_reg_ex, "hexadecimal", node)
                    node = re.sub(self.nr_reg_ex, "number", node)
                    node = re.sub(self.multi_sp_reg_ex, " ", node)
                    to_add.append(node)
            for add in to_add:
                temp = add.split(" ")
                for t in temp:
                    if t not in words and (t):
                        words.append(t)
        return words

    def getBjoernCFGGraphmlNodeUnigramsTF(self, fileName, cfgGraphmlNodeUnigrams):
        u = Util()
        dict_TF = {}
        nodes = []
        tmp = {}
        graphmlCFGFiles = u.listFiles(
            (fileName+"_bjoernDisassembly"), ".graphml")
        print ("Files: " + str(graphmlCFGFiles))
        for file in graphmlCFGFiles:
            featureText = open(file, errors="ignore").read()
            featureText = featureText.replace(',', ' ')
            featureText = featureText.replace("\"repr\">", " ")
            featureText = featureText.replace("</data><", " ")
            featureText = featureText.replace('|', ' ')
            featureText = featureText.replace('\s+', ' ')
            featureText = re.sub(self.hex_reg_ex, "hexadecimal", featureText)
            featureText = re.sub(self.nr_reg_ex, "number", featureText)
            featureText = re.sub(self.multi_sp_reg_ex, " ", featureText)
            for token in cfgGraphmlNodeUnigrams:
                if token in dict_TF:
                    dict_TF[token] += featureText.count(token.strip())
                else:
                    dict_TF[token] = featureText.count(token.strip())
        return dict_TF

    def getBjoernCFGGraphmlNodeBigrams(self, dirPath):
        words = []
        edges = []
        nodes = []
        bigrams = []
        allBigrams = ""
        to_add = []
        u = Util()
        rdm_count = 0
        test_file_paths = u.listFiles(dirPath, ".graphml")
        for file in test_file_paths:
            edges = []
            f = open(file).readlines()
            replace_map = {
                "<node id=": "\n <node id=",
                "<edge id=": "\n <edge id=",
            }
            for line in f:
                for key, word in replace_map.items():
                    line = re.sub(key, word, line)
                edges += line.split("\n")
            for edge in edges:
                nodes = []
                if ("CFLOW" in edge):
                    rdm_count += 1
                    arr = edge.split('=', 5)
                    sourceNode = arr[2]
                    sourceNode = sourceNode.replace(" target", "")
                    sourceNode = "<node id="+sourceNode
                    targetNode = arr[3]
                    targetNode = targetNode.replace(" label", "")
                    targetNode = "<node id=" + targetNode
                    for node in edges:
                        nodeTarget = node
                        if (sourceNode in node):
                            arrSrc = node.split("data key=", 5)
                            node = arrSrc[1]
                            node = node.replace('\\,', ' ')
                            node = node.replace("\"repr\">", "")
                            node = node.replace("</data><", "")
                            node = node.replace('|', ' ')
                            node = re.sub(self.hex_reg_ex, "hexadecimal", node)
                            node = re.sub(self.nr_reg_ex, "number", node)
                            node = re.sub(self.multi_sp_reg_ex, " ", node)
                            node = re.sub(self.multi_dots_reg_ex, " ", node)
                            sourceNodeRepr = node
                            allBigrams += " " + sourceNodeRepr.strip()
                        if (targetNode in nodeTarget):
                            arrTarget = nodeTarget.split("data key=", 5)
                            nodeTarget = arrTarget[1]
                            nodeTarget = nodeTarget.replace('\\,', ' ')
                            nodeTarget = nodeTarget.replace("\"repr\">", "")
                            nodeTarget = nodeTarget.replace("</data><", "")
                            nodeTarget = nodeTarget.replace('|', ' ')
                            nodeTarget = nodeTarget.replace('\s+', ' ')
                            nodeTarget = re.sub(
                                self.hex_reg_ex, "hexadecimal", nodeTarget)
                            nodeTarget = re.sub(
                                self.nr_reg_ex, "number", nodeTarget)
                            nodeTarget = re.sub(
                                self.multi_sp_reg_ex, " ", nodeTarget)
                            nodeTarget = re.sub(
                                self.multi_dots_reg_ex, " ", nodeTarget)
                            targetNodeRepr = nodeTarget
                            allBigrams += " " + targetNodeRepr.strip()

        bigram_list = allBigrams.split(" ")
        for i in range(len(bigram_list)-1):
            for j in range(i+1, len(bigram_list)-1):
                bigram = bigram_list[i].strip() + " " + bigram_list[j].strip()
                if (bigram) not in bigrams and (bigram_list[i].strip()) and (bigram_list[j].strip()):
                    bigrams.append(bigram)
        return bigrams

    def getBjoernCFGGraphmlNodeBigramsTF(self, fileName, cfgGraphmlNodeBigrams):
        u = Util()
        dict_TF = {}
        edges = []
        allBigrams = " "
        nodes = []
        bigrams = []
        graphmlCFGFiles = u.listFiles(
            (fileName+"_bjoernDisassembly"), ".graphml")
        for file in graphmlCFGFiles:
            f = open(file).readlines()
            replace_map = {
                "<node id=": "\n <node id=",
                "<edge id=": "\n <edge id=",
            }
            for line in f:
                for key, word in replace_map.items():
                    line = re.sub(key, word, line)
                edges += line.split("\n")
            for edge in edges:
                nodes = []
                if ("CFLOW" in edge):
                    arr = edge.split('=', 5)
                    sourceNode = arr[2]
                    sourceNode = sourceNode.replace(" target", "")
                    sourceNode = "<node id="+sourceNode
                    targetNode = arr[3]
                    targetNode = targetNode.replace(" label", "")
                    targetNode = "<node id=" + targetNode
                    for node in edges:
                        nodeTarget = node
                        if (sourceNode in node):
                            arrSrc = node.split("data key=", 5)
                            node = arrSrc[1]
                            node = node.replace('\\,', ' ')
                            node = node.replace("\"repr\">", "")
                            node = node.replace("</data><", "")
                            node = node.replace('|', ' ')
                            node = re.sub(self.hex_reg_ex, "hexadecimal", node)
                            node = re.sub(self.nr_reg_ex, "number", node)
                            node = re.sub(self.multi_sp_reg_ex, " ", node)
                            node = re.sub(self.multi_dots_reg_ex, " ", node)
                            sourceNodeRepr = node
                            allBigrams += " " + sourceNodeRepr.strip()
                        if (targetNode in nodeTarget):
                            arrTarget = nodeTarget.split("data key=", 5)
                            nodeTarget = arrTarget[1]
                            nodeTarget = nodeTarget.replace('\\,', ' ')
                            nodeTarget = nodeTarget.replace("\"repr\">", "")
                            nodeTarget = nodeTarget.replace("</data><", "")
                            nodeTarget = nodeTarget.replace('|', ' ')
                            nodeTarget = re.sub(
                                self.hex_reg_ex, "hexadecimal", nodeTarget)
                            nodeTarget = re.sub(
                                self.nr_reg_ex, "number", nodeTarget)
                            nodeTarget = re.sub(
                                self.multi_sp_reg_ex, " ", nodeTarget)
                            nodeTarget = re.sub(
                                self.multi_dots_reg_ex, " ", nodeTarget)
                            targetNodeRepr = nodeTarget
                            allBigrams += " " + targetNodeRepr.strip()
        for token in cfgGraphmlNodeBigrams:
            if token in dict_TF:
                dict_TF[token] += allBigrams.count(token.strip())
            else:
                dict_TF[token] = allBigrams.count(token.strip())
        print (dict_TF)
        return dict_TF

    def getBjoernDisassemblyInstructionUnigrams(self, dirPath):
        u = Util()
        unigrams = []
        test_file_paths = self.listBjoernNodeFiles(dirPath)
        for file in test_file_paths:
            f = open(file).readlines()
            for line in f:
                arr = re.split(r'\s+', line, maxsplit=4)
                #arr = line.split("  ",5)
                #import pdb; pdb.set_trace()
                if (len(arr) > 4):
                    # print("Here")
                    line = arr[4]
                    #print (line)
                    line = line.replace("\"", " ")
                    line = line.replace(",", " ")
                    line = line.replace("'", " ")
                    #line = line.replace("\|", " ")
                    line = line.replace("..+", " ")
                    line = line.replace("|", " ")
                    line = re.sub(self.hex_reg_ex, "hexadecimal", line)
                    line = re.sub(self.nr_reg_ex, "number", line)
                    line = re.sub(self.multi_sp_reg_ex, " ", line)
                    line = re.sub(self.multi_dots_reg_ex, " ", line)
                    toAdd = line.strip().split(" ")
                for add in toAdd:  # check if empty
                    if add not in unigrams and (add):
                        unigrams.append(add)
        return unigrams

    def getBjoernDisassemblyInstructionUnigramsTF(self, featureText, instrUnigrams):
        u = Util()
        unigrams = []
        dict_TF = {}
        #import pdb
        # pdb.set_trace()
        featureText = featureText.replace("\"", " ")
        featureText = featureText.replace(",", " ")
        featureText = featureText.replace("'", " ")
        #featureText = featureText.replace("\|", " ")
        featureText = featureText.replace("..+", " ")
        featureText = featureText.replace("|", " ")
        featureText = re.sub(self.hex_reg_ex, "hexadecimal", featureText)
        featureText = re.sub(self.nr_reg_ex, "number", featureText)
        featureText = re.sub(self.multi_sp_reg_ex, " ", featureText)
        #featureText = re.sub(self.multi_dots_reg_ex, " ", featureText)
        for token in instrUnigrams:
            if token in dict_TF:
                dict_TF[token] += featureText.count(token)
            else:
                dict_TF[token] = featureText.count(token)
        return dict_TF

    def getBjoernDisassemblyInstructionBigrams(self, dirPath):
        u = Util()
        bigrams = []
        test_file_paths = self.listBjoernNodeFiles(dirPath)
        for file in test_file_paths:
            f = open(file).readlines()
            for line in f:
                arr = re.split(r'\s+', line, maxsplit=4)
                #arr = line.split("  ",5)
                if (len(arr) > 4):
                    # print("Here")
                    line = arr[4]
                    #print (line)
                    line = line.replace("\"", " ")
                    line = line.replace(",", " ")
                    line = line.replace("'", " ")
                    #line = line.replace("\|", " ")
                    line = line.replace("..+", " ")
                    line = line.replace("|", " ")
                    line = re.sub(self.hex_reg_ex, "hexadecimal", line)
                    line = re.sub(self.nr_reg_ex, "number", line)
                    line = re.sub(self.multi_sp_reg_ex, " ", line)
                    line = re.sub(self.multi_dots_reg_ex, " ", line)
                    toAdd = line.strip().split(" ")
                    #print( toAdd)
                    for i in range(1, len(toAdd)):  # check if empty
                        bigram = toAdd[i-1] + " " + toAdd[i]
                        if (toAdd[i-1] != "number") and i == 1:
                            continue
                        if (bigram not in bigrams):
                            bigrams.append(bigram)
        return bigrams

    def getBjoernDisassemblyInstructionBigramsTF(self, featureText, instrBigrams):
        u = Util()
        bigrams = []
        dict_TF = {}
        featureText = featureText.replace("\"", " ")
        featureText = featureText.replace(",", " ")
        featureText = featureText.replace("'", " ")
        featureText = featureText.replace("..+", " ")
        featureText = featureText.replace("|", " ")
        featureText = re.sub(self.hex_reg_ex, "hexadecimal", featureText)
        featureText = re.sub(self.nr_reg_ex, "number", featureText)
        featureText = re.sub(self.multi_sp_reg_ex, " ", featureText)
        #featureText = re.sub(self.multi_dots_reg_ex, " ", featureText)
        for token in instrBigrams:
            if token in dict_TF:
                dict_TF[token] += featureText.count(token)
            else:
                dict_TF[token] = featureText.count(token)
        return dict_TF

    def getBjoernDisassemblyInstructionTrigrams(self, dirPath):
        u = Util()
        trigrams = []
        test_file_paths = self.listBjoernNodeFiles(dirPath)
        for file in test_file_paths:
            f = open(file).readlines()
            for line in f:
                arr = re.split(r'\s+', line, maxsplit=4)
                #arr = line.split("  ",5)
                if (len(arr) > 4):
                    # print("Here")
                    line = arr[4]
                    #print (line)
                    line = line.replace("\"", " ")
                    line = line.replace(",", " ")
                    line = line.replace("'", " ")
                    #line = line.replace("\|", " ")
                    line = line.replace("..+", " ")
                    line = line.replace("|", " ")
                    line = re.sub(self.hex_reg_ex, "hexadecimal", line)
                    line = re.sub(self.nr_reg_ex, "number", line)
                    line = re.sub(self.multi_sp_reg_ex, " ", line)
                    line = re.sub(self.multi_dots_reg_ex, " ", line)
                    toAdd = line.strip().split(" ")
                    #print( toAdd)
                    for i in range(2, len(toAdd)):  # check if empty
                        trigram = toAdd[i-2] + " " + toAdd[i-1] + " "+toAdd[i]
                        if (toAdd[i-2] != "number") and i == 2:
                            continue
                        if (trigram not in trigrams):
                            trigrams.append(trigram)
        return trigrams

    def getBjoernDisassemblyInstructionTrigramsTF(self, featureText, instrTrigrams):
        u = Util()
        bigrams = []
        dict_TF = {}
        featureText = featureText.replace("\"", " ")
        featureText = featureText.replace(",", " ")
        featureText = featureText.replace("..+", " ")
        featureText = featureText.replace("|", " ")
        featureText = re.sub(self.hex_reg_ex, "hexadecimal", featureText)
        featureText = re.sub(self.nr_reg_ex, "number", featureText)
        featureText = re.sub(self.multi_sp_reg_ex, " ", featureText)
        #featureText = re.sub(self.multi_dots_reg_ex, " ", featureText)
        for token in instrTrigrams:
            if token in dict_TF:
                dict_TF[token] += featureText.count(token)
            else:
                dict_TF[token] = featureText.count(token)
        return dict_TF

    def getBjoernLineUnigrams(self, dirPath):
        u = Util()
        uniqueLineUnigrams = []
        lineUnigrams = []
        test_file_paths = self.listBjoernNodeFiles(dirPath)
        #print (test_file_paths)
        for file in test_file_paths:
            f = open(file).readlines()
            for line in f:
                arr = re.split(r'\s+', line, maxsplit=4)
                #arr = line.split("  ",5)
                if (len(arr) > 4):
                    # print("Here")
                    line = arr[4]
                    #print (line)
                    line = line.replace(",", " ")
                    line = line.replace("\"", " ")
                    #line = line.replace("\|", " ")
                    line = line.replace("..+", " ")
                    line = line.replace("|", " ")
                    line = re.sub(self.hex_reg_ex, "hexadecimal", line)
                    line = re.sub(self.nr_reg_ex, "number", line)
                    line = re.sub(self.multi_sp_reg_ex, " ", line)
                    line = re.sub(self.multi_dots_reg_ex, " ", line)
                    #print (line)
                if (line):  # check if empty
                    if line not in lineUnigrams:
                        lineUnigrams.append(line)
        return lineUnigrams

    def getBjoernLineUnigramsTF(self, featureText, lineUnigrams):  # this returns 0
        u = Util()
        dict_TF = {}
        featureText = featureText.replace("\"", " ")
        featureText = featureText.replace("..+", " ")
        featureText = featureText.replace("|", " ")
        featureText = featureText.replace(",", " ")
        featureText = re.sub(self.hex_reg_ex, "hexadecimal", featureText)
        featureText = re.sub(self.nr_reg_ex, "number", featureText)
        featureText = re.sub(self.multi_sp_reg_ex, " ", featureText)
        #featureText = re.sub(self.multi_dots_reg_ex, " ", featureText)
        import pdb; pdb.set_trace()
        for token in lineUnigrams:
            token = token.strip()
            if token in dict_TF:
                dict_TF[token] += featureText.count(token)
            else:
                dict_TF[token] = featureText.count(token)
        return dict_TF

    def getBjoernLineBigrams(self, dirPath):
        u = Util()
        uniqueLineBigrams = []
        lineBigrams = []
        test_file_paths = self.listBjoernNodeFiles(dirPath)
        #print (test_file_paths)
        tmp = ""
        for file in test_file_paths:
            f = open(file).readlines()
            for line in f:
                arr = re.split(r'\s+', line, maxsplit=4)
                #arr = line.split("  ",5)
                if (len(arr) > 4):
                    # print("Here")
                    line = arr[4]
                    #print (line)
                    line = line.replace("\"", " ")
                    #line = line.replace("\|", " ")
                    line = line.replace("..", " ")
                    line = line.replace("|", " ")
                    line = line.replace(",", " ")
                    line = re.sub(self.hex_reg_ex, "hexadecimal", line)
                    line = re.sub(self.nr_reg_ex, "number", line)
                    line = re.sub(self.multi_sp_reg_ex, " ", line)
                    line = re.sub(self.multi_dots_reg_ex, " ", line)
                if (line):  # check if empty
                    if line not in lineBigrams:
                        lineBigrams.append(tmp.strip() + " " + line.strip()+" ")
                        tmp = line
        return lineBigrams

    def getBjoernLineBigramsTF(self, featureText, lineBigrams):  # this returns 0
        u = Util()
        dict_TF = {}
        featureText = featureText.replace("\"", " ")
        featureText = re.sub(self.hex_reg_ex, "hexadecimal", featureText)
        featureText = re.sub(self.nr_reg_ex, "number", featureText)
        featureText = featureText.replace("..", " ")
        featureText = featureText.replace("|", " ")
        featureText = featureText.replace(",", " ")
        #featureText = re.sub(self.multi_sp_reg_ex, " ", featureText)
        for token in lineBigrams:
            token = token.strip()
            if token in dict_TF:
                dict_TF[token] += featureText.count(token)
            else:
                dict_TF[token] = featureText.count(token)
        return dict_TF

    def listBjoernNodeFiles(self, dirPath):
        u = Util()
        node_file_paths = []
        test_file_paths = u.listFiles(dirPath, ".csv")
        for file in test_file_paths:
            if "nodes.csv" in file:
                node_file_paths.append(file)
        return node_file_paths



