
import os
import re
from Util import Util
from pathlib import Path
from array import *


class FeatureExtractorBjoern():
    #u = Util()
    dirPath = "/home/kejsi/3authors_small"
    hex_reg_ex = re.compile(r'0[xX][0-9a-fA-F]+')
    nr_reg_ex = re.compile(r'\d+')
    multi_sp_reg_ex = re.compile(r'\s+')
    multi_dots_reg_ex = re.compile(r'\..+')

    def getBjoernCFGGraphmlNodeUnigrams(self):
        words = []
        nodes = []
        to_add = []
        u = Util()
        test_file_paths = u.listFiles(self.dirPath, ".graphml")
        #print ("Graphml files"  + str(test_file_paths))
        for file in test_file_paths:
            f = open(file).readlines()
            replace_map = {
                "<node id=": "\n <node id=",
                "<edge id=": "\n <edge id=",
            }
            for line in f:
                for key, word in replace_map.items():
                    line = re.sub(key, word, line)
                #nodes.append( line.split("\n"))
                nodes += line.split("\n")
                #print (line.split("\n"))
            for node in nodes:
                if (">BB</data>" in node):
                    #print (node)
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
                    #print (node)
            for add in to_add:
                #print (add)
                temp = add.split(" ")
                for t in temp:
                    #print (t)
                    if t not in words and (t):
                        #print (t)
                        words.append(t)
        #print (words)
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
            print (file)
            featureText = open(file, errors="ignore").read()
            print (featureText)
            featureText = featureText.replace(',', ' ')
            featureText = featureText.replace("\"repr\">", " ")
            featureText = featureText.replace("</data><", " ")
            featureText = featureText.replace('|', ' ')
            featureText = featureText.replace('\s+', ' ')
            featureText = re.sub(self.hex_reg_ex, "hexadecimal", featureText)
            featureText = re.sub(self.nr_reg_ex, "number", featureText)
            featureText = re.sub(self.multi_sp_reg_ex, " ", featureText)
            #print (featureText)
            print ("____________________")
            for token in cfgGraphmlNodeUnigrams:
                #print (featureText.count(token))
                if token in dict_TF:
                    dict_TF[token] += featureText.count(token.strip())
                else:
                    dict_TF[token] = featureText.count(token.strip())
        #print (dict_TF)
        return dict_TF

    def getBjoernCFGGraphmlNodeBigrams(self):
        words = []
        edges = []
        nodes = []
        bigrams = []
        allBigrams = ""
        to_add = []
        u = Util()
        rdm_count = 0
        test_file_paths = u.listFiles(self.dirPath, ".graphml")
        print ("Numbe rof files: " + str(len(test_file_paths)))
        #import pdb; pdb.set_trace()
        for file in test_file_paths:
            edges = []
            f = open(file).readlines()
            replace_map = {
                "<node id=": "\n <node id=",
                "<edge id=": "\n <edge id=",
            }
            for line in f:
                for key, word in replace_map.items():
                    #print (re.sub (key, word, line))
                    line = re.sub(key, word, line)
                edges += line.split("\n")
                #print (line.split("\n"))
            #print ("length of edgessss" +str(len(edges)))
            for edge in edges:
                nodes = []
                #print (edge)
                if ("CFLOW" in edge):
                    rdm_count += 1
                    #print ("--------"+edge)
                    arr = edge.split('=', 5)
                    #print (arr)
                    sourceNode = arr[2]
                    sourceNode = sourceNode.replace(" target", "")
                    sourceNode = "<node id="+sourceNode
                    targetNode = arr[3]
                    targetNode = targetNode.replace(" label", "")
                    targetNode = "<node id=" + targetNode
                    #print ("Target Node: " +targetNode)
                    #print ("Source Node: " +sourceNode)
                    for node in edges:
                        #print ("Node")
                        #print (node)
                        nodeTarget = node
                        #print ("Source node")
                        #print (sourceNode)
                        if (sourceNode in node):
                            #print ("here-----")
                            arrSrc = node.split("data key=", 5)
                            #print (node)
                            #arrSrc = node.split("=",5)
                            node = arrSrc[1]
                            #print (node)
                            node = node.replace('\\,', ' ')
                            node = node.replace("\"repr\">", "")
                            node = node.replace("</data><", "")
                            node = node.replace('|', ' ')
                            #node = node.replace('\s+', ' ')
                            #node = node.replace('\\..+', ' ')
                            node = re.sub(self.hex_reg_ex, "hexadecimal", node)
                            node = re.sub(self.nr_reg_ex, "number", node)
                            node = re.sub(self.multi_sp_reg_ex, " ", node)
                            node = re.sub(self.multi_dots_reg_ex, " ", node)
                            sourceNodeRepr = node
                            #print ("Transformed"+node)
                            allBigrams += " " + sourceNodeRepr.strip()
                        if (targetNode in nodeTarget):
                            #print ("here")
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
                            #print("Target"+ nodeTarget)
                            allBigrams += " " + targetNodeRepr.strip()

                        #print ("---------------------")
        #print ("Edge count" + str(rdm_count))
        #print ("String length: " + str(len(allBigrams)))
        bigram_list = allBigrams.split(" ")
        #print ("Length: " + str(len(bigram_list)))
        for i in range(len(bigram_list)-1):
            for j in range(i+1, len(bigram_list)-1):
                #import pdb; pdb.set_trace()
                bigram = bigram_list[i].strip() + " " + bigram_list[j].strip()
            #print (bigram)
            # bigrams.append(bigram)
                if (bigram) not in bigrams and (bigram_list[i].strip()) and (bigram_list[j].strip()):
                    bigrams.append(bigram)
                    #print (bigram)
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
            #edges =[]
            f = open(file).readlines()
            replace_map = {
                "<node id=": "\n <node id=",
                "<edge id=": "\n <edge id=",
            }
            for line in f:
                for key, word in replace_map.items():
                    #print (re.sub (key, word, line))
                    line = re.sub(key, word, line)
                edges += line.split("\n")
            for edge in edges:
                nodes = []
                #print (edge)
                if ("CFLOW" in edge):
                    #print ("--------"+edge)
                    arr = edge.split('=', 5)
                    #print (arr)
                    sourceNode = arr[2]
                    sourceNode = sourceNode.replace(" target", "")
                    sourceNode = "<node id="+sourceNode
                    targetNode = arr[3]
                    targetNode = targetNode.replace(" label", "")
                    targetNode = "<node id=" + targetNode
                    #print ("Target Node: " +targetNode)
                    #print ("Source Node: " +sourceNode)
                    '''for line in f:
						for key, word in replace_map.items():
							line = re.sub (key, word, line)
						nodes += line.split("\n")'''
                    for node in edges:
                        #print ("Node")
                        #print (node)
                        nodeTarget = node
                        #print ("Source node")
                        #print (sourceNode)
                        if (sourceNode in node):
                            #print ("here-----")
                            arrSrc = node.split("data key=", 5)
                            #print (node)
                            #arrSrc = node.split("=",5)
                            node = arrSrc[1]
                            #print (node)
                            node = node.replace('\\,', ' ')
                            node = node.replace("\"repr\">", "")
                            node = node.replace("</data><", "")
                            node = node.replace('|', ' ')
                            #node = node.replace('\s+', ' ')
                            #node = node.replace('\\..+', ' ')
                            node = re.sub(self.hex_reg_ex, "hexadecimal", node)
                            node = re.sub(self.nr_reg_ex, "number", node)
                            node = re.sub(self.multi_sp_reg_ex, " ", node)
                            node = re.sub(self.multi_dots_reg_ex, " ", node)
                            sourceNodeRepr = node
                            #print ("Transformed"+node)
                            allBigrams += " " + sourceNodeRepr.strip()
                        if (targetNode in nodeTarget):
                            #print ("here")
                            arrTarget = nodeTarget.split("data key=", 5)
                            nodeTarget = arrTarget[1]
                            nodeTarget = nodeTarget.replace('\\,', ' ')
                            nodeTarget = nodeTarget.replace("\"repr\">", "")
                            nodeTarget = nodeTarget.replace("</data><", "")
                            nodeTarget = nodeTarget.replace('|', ' ')
                            #nodeTarget = nodeTarget.replace('\s+', ' ')
                            nodeTarget = re.sub(
                                self.hex_reg_ex, "hexadecimal", nodeTarget)
                            nodeTarget = re.sub(
                                self.nr_reg_ex, "number", nodeTarget)
                            nodeTarget = re.sub(
                                self.multi_sp_reg_ex, " ", nodeTarget)
                            nodeTarget = re.sub(
                                self.multi_dots_reg_ex, " ", nodeTarget)
                            targetNodeRepr = nodeTarget
                            # print(nodeTarget)
                            allBigrams += " " + targetNodeRepr.strip()
            #import pdb; pdb.set_trace()
            #print ("Graphml Node Bigrams:" + str(cfgGraphmlNodeBigrams))
        for token in cfgGraphmlNodeBigrams:
            #print (featureText.count(token))
            if token in dict_TF:
                #import pdb; pdb.set_trace()
                dict_TF[token] += allBigrams.count(token.strip())
            else:
                dict_TF[token] = allBigrams.count(token.strip())
        #dict_TF[bigram] = allBigrams.count (bigram)
        print (dict_TF)
        return dict_TF

    def getBjoernDisassemblyInstructionUnigrams(self, dirPath):
        u = Util()
        unigrams = []
        test_file_paths = self.listBjoernNodeFiles()
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
        test_file_paths = self.listBjoernNodeFiles()
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
        if token in dict_TF:
            dict_TF[token] += featureText.count(token)
        else:
            dict_TF[token] = featureText.count(token)
        return dict_TF

    def getBjoernDisassemblyInstructionTrigrams(self, dirPath):
        u = Util()
        trigrams = []
        test_file_paths = self.listBjoernNodeFiles()
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
            dict_TF[token] = featureText.count(token)
        return dict_TF

    def getBjoernLineUnigrams(self):
        u = Util()
        uniqueLineUnigrams = []
        lineUnigrams = []
        test_file_paths = self.listBjoernNodeFiles()
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
        featureText = re.sub(self.multi_dots_reg_ex, " ", featureText)
        for token in lineUnigrams:
            dict_TF[token] = featureText.count(token)
            #import pdb;pdb.set_trace()
        #print (dict_TF)
        return (dict_TF)

    def getBjoernLineBigrams(self):
        u = Util()
        uniqueLineBigrams = []
        lineBigrams = []
        test_file_paths = self.listBjoernNodeFiles()
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
                    lineBigrams.append(tmp.strip() + " " + line.strip()+" ")
                    tmp = line
        lineBigrams = list(dict.fromkeys(lineBigrams))
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
        featureText = re.sub(self.multi_sp_reg_ex, " ", featureText)
        #featureText = re.sub(self.multi_dots_reg_ex, " ", featureText)
        #import pdb
        # pdb.set_trace()
        for token in lineBigrams:
            dict_TF[token] = featureText.count(token)
        #print (dict_TF)
        return (dict_TF)

    # def getBjoernLineBigrams(self, dirPath):
    # def getBjoernLineBigramsTF(self, text, lineUnigrams):
    def listBjoernNodeFiles(self):
        u = Util()
        node_file_paths = []
        test_file_paths = u.listFiles(self.dirPath, ".csv")
        #import pdb
        # pdb.set_trace()
        for file in test_file_paths:
            #print (file)
            if "nodes.csv" in file:
                node_file_paths.append(file)
        return node_file_paths


def main():
    u = Util()
    f = open("/home/kejsi/PythonBda/py_test.arff", 'w+')
    testDir = "/home/kejsi/3authors_small/"
    test_binary_paths = u.listBinaryFiles(testDir)
    print (test_binary_paths)
    f.write("@relation " + testDir + "BjoernCFGDisassembly" + "\n\n")
    f.write("@attribute instanceID_original {")
    for file in test_binary_paths:
        f.write(str(file) + '_'+testDir.split('/')
                [len(testDir.split('/'))-2] + ',')
    f.write('}' + '\n')
    #authorFileName = ' '
    f.write("@attribute 'authorName_original' {")
    authors = []
    for file in test_binary_paths:
        print (file)
        authorFileName = (file.split('_')[2])
        #print ("author: " + authorFileName)
        if authorFileName not in authors:
            authors.append(authorFileName)
    for name in authors:
        f.write(name + ',')
    f.write('}' + '\n \n')
    # BJOERN FEATURES START
    # Related files:
    # 1645485_1480492_a9108_bjoernDisassembly/nodes.csv
    # 1645485_1480492_a9108_bjoernDisassembly/1645485_1480492_a9108CFG/*.graphml
    # get the basic block node unigrams in bjoern CFG and write the node unigram features
    fe = FeatureExtractorBjoern()
    # CFG NODE UNIGRAMS
    '''bjoernCFGNodeUnigrams = fe.getBjoernCFGGraphmlNodeUnigrams()
	count = 0
	for unigram in bjoernCFGNodeUnigrams: 
		print ( "@attribute 'bjoernCFGNodeUnigrams" + str(count)+ " "+ unigram)
		f.write("@attribute 'BjoernCFGGraphmlNodeUnigrams " + str(count) + "=["+ unigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
		count += 1
	
	# CFG NODE BIGRAMS AKA EDGES - REPR
	# get the cflow edges in bjoern CFG and write the node bigram features
	bjoernCFGNodeBigrams = fe.getBjoernCFGGraphmlNodeBigrams()
	count = 0
	for bigram in bjoernCFGNodeBigrams: 
               print ( "@attribute 'bjoernCFGNodeBigrams" + str(count)+ " "+ str(bigram))
               f.write("@attribute 'BjoernCFGGraphmlNodeBigrams " + str(count) + "=["+ bigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
               count += 1'''
    #print (fe.getBjoernCFGGraphmlNodeUnigrams(testDir))
    #print (fe.listBjoernNodeFiles(testDir))
    # DISASSEMBLY INSTRUCTION UNIGRAMS
    # CFG NODE UNIGRAMS - REPR
    # get the instruction unigrams in bjoern disassembly and write the instruction unigram features
    '''bjoernDisassemblyUnigrams = fe.getBjoernDisassemblyInstructionUnigrams(testDir)
	count = 0
	for unigram in bjoernDisassemblyUnigrams:
                print ( "@attribute 'bjoernDisassemblyInstructionUnigrams" + str(count) + "=[" + unigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
                f.write( "@attribute 'bjoernDisassemblyInstructionUnigrams" + str(count) + "=[" + unigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
                count+=1
	bjoernDisassemblyBigrams = fe.getBjoernDisassemblyInstructionBigrams(testDir)
	count = 0
	for bigram in bjoernDisassemblyBigrams:
		print ( "@attribute 'bjoernDisassemblyInstructionBigrams" + str(count) + "=[" + bigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
		f.write( "@attribute 'bjoernDisassemblyInstructionBigrams" + str(count) + "=[" + bigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
		count+=1   '''
    bjoernDisassemblyTrigrams = fe.getBjoernDisassemblyInstructionTrigrams(
        testDir)
    count = 0
    for trigram in bjoernDisassemblyTrigrams:
        #print ( "@attribute 'bjoernDisassemblyInstructionTrigrams" + str(count) + "=[" + trigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
        f.write("@attribute 'bjoernDisassemblyInstructionTrigrams" + str(count) +
                "=[" + trigram.replace("'", "apostrophesymbol")+"]' numeric" + "\n")
        count += 1

    '''lineUnigrams = fe.getBjoernLineUnigrams()
	count = 0
	for unigram in lineUnigrams:
                print ( "@attribute 'bjoernLineUnigrams" + str(count) + "=[" + unigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
                f.write( "@attribute 'bjoernLineUnigrams" + str(count) + "=[" + unigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
                count+=1
	lineBigrams = fe.getBjoernLineBigrams()
	count = 0
	for bigram in lineBigrams:
		print ( "@attribute 'bjoernLineBigrams" + str(count) + "=[" + bigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
		f.write( "@attribute 'bjoernLineBigrams" + str(count) + "=[" + bigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
		count+=1
	lineUnigrams = fe.getBjoernLineUnigrams()
        count = 0
        for unigram in lineUnigrams:
                print ( "@attribute 'bjoernLineUnigrams" + str(count) + "=[" + unigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
                f.write( "@attribute 'bjoernLineUnigrams" + str(count) + "=[" + unigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
                count+=1
        lineBigrams = fe.getBjoernLineBigrams()'''
    f.write('@data \n')
    for file in test_binary_paths:
        f.write(str(file) + '_'+testDir.split('/')
                [len(testDir.split('/'))-2] + ',')
        '''cfgNodeUniCount = fe.getBjoernCFGGraphmlNodeUnigramsTF(os.path.join(testDir,file.split('_')[2]+'/'+file) , bjoernCFGNodeUnigrams)			   
		for cfgNodeUni in cfgNodeUniCount:
			f.write(str(cfgNodeUniCount[cfgNodeUni]) + ",")
		cfgNodeBiCount = fe.getBjoernCFGGraphmlNodeBigramsTF(os.path.join(testDir,file.split('_')[2]+'/'+file) , bjoernCFGNodeBigrams)                          
		for cfgNodeBi in cfgNodeBiCount:
			f.write(str(cfgNodeBiCount[cfgNodeBi]) + ",")'''

        '''wordUniCount = fe.getBjoernDisassemblyInstructionUnigramsTF(str(open(os.path.join(testDir,file.split('_')[2]+'/'+file), errors= 'ignore').readlines()),bjoernDisassemblyUnigrams )
		for  wordUnigram in wordUniCount:
			f.write(str(wordUniCount[wordUnigram]) + ", ")
		wordBigramsCount = fe.getBjoernDisassemblyInstructionBigramsTF(str(open(os.path.join(testDir,file.split('_')[2]+'/'+file), errors= 'ignore').readlines()),bjoernDisassemblyBigrams )
		for  wordBigram in wordBigramsCount:
			f.write(str(wordBigramsCount[wordBigram]) + ", ")'''
        wordTrigramsCount = fe.getBjoernDisassemblyInstructionTrigramsTF(str(open(os.path.join(
            testDir, file.split('_')[2]+'/'+file), errors='ignore').readlines()), bjoernDisassemblyTrigrams)
        for wordTrigram in wordTrigramsCount:
            f.write(str(wordTrigramsCount[wordTrigram]) + ", ")

        #print (os.path.join(testDir,file.split('_')[2]+'/'+file))

        '''lineUnigramsCount = fe.getBjoernLineUnigramsTF(str(open(os.path.join(testDir,file.split('_')[2]+'/'+file), errors= 'ignore').readlines()),lineUnigrams )
		for  lineUnigram in lineUnigramsCount:
			f.write(str(lineUnigramsCount[lineUnigram]) + ", ")

		lineBigramsCount = fe.getBjoernLineBigramsTF(str(open(os.path.join(testDir,file.split('_')[2]+'/'+file), errors= 'ignore').readlines()),lineBigrams )
		for  lineBigram in lineBigramsCount:
			f.write(str(lineBigramsCount[lineBigram]) + ", ")'''


main()
