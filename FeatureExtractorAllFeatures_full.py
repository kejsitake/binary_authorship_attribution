import os
import re
from Util import Util
from FeatureExtractorBjoern import FeatureExtractorBjoern
from BigramExtractor import BigramExtractor
from pathlib import Path
from array import *


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
    # authorFileName = ' '
    f.write("@attribute 'authorName_original' {")
    authors = []
    for file in test_binary_paths:
        authorFileName = (file.split('_')[2])
        # print ("author: " + authorFileName)
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
		f.write("@attribute 'BjoernCFGGraphmlNodeUnigrams " + str(count) + \
		        "=["+ unigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
		count += 1

	# CFG NODE BIGRAMS AKA EDGES - REPR
	# get the cflow edges in bjoern CFG and write the node bigram features
	bjoernCFGNodeBigrams = fe.getBjoernCFGGraphmlNodeBigrams()
	count = 0
	for bigram in bjoernCFGNodeBigrams:
               print ( "@attribute 'bjoernCFGNodeBigrams" + \
                      str(count)+ " "+ str(bigram))
               f.write("@attribute 'BjoernCFGGraphmlNodeBigrams " + str(count) + \
                       "=["+ bigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
               count += 1'''
    # print (fe.getBjoernCFGGraphmlNodeUnigrams(testDir))
    # print (fe.listBjoernNodeFiles(testDir))
    # DISASSEMBLY INSTRUCTION UNIGRAMS
    # CFG NODE UNIGRAMS - REPR
    # get the instruction unigrams in bjoern disassembly and write the instruction unigram features
    bjoernDisassemblyUnigrams = fe.getBjoernDisassemblyInstructionUnigrams(
        testDir)
    for unigram in bjoernDisassemblyUnigrams:
        print ("@attribute 'bjoernDisassemblyInstructionUnigrams" + str(count) +
               "=[" + unigram.replace("'", "apostrophesymbol")+"]' numeric" + "\n")
        f.write("@attribute 'bjoernDisassemblyInstructionUnigrams" + str(count) +
                "=[" + unigram.replace("'", "apostrophesymbol")+"]' numeric" + "\n")
        count += 1

	'''bjoernDisassemblyBigrams = fe.getBjoernDisassemblyInstructionBigrams(testDir)
	count = 0
	for bigram in bjoernDisassemblyBigrams:
	print ( "@attribute 'bjoernDisassemblyInstructionBigrams" + str(count) + \
	       "=[" + bigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
	f.write( "@attribute 'bjoernDisassemblyInstructionBigrams" + str(count) + \
	        "=[" + bigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
	count+=1
	bjoernDisassemblyTrigrams = fe.getBjoernDisassemblyInstructionTrigrams(
	    testDir)
	count = 0
	for trigram in bjoernDisassemblyTrigrams:
	print ( "@attribute 'bjoernDisassemblyInstructionTrigrams" + str(count) + \
	       "=[" + trigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
	f.write( "@attribute 'bjoernDisassemblyInstructionTrigrams" + str(count) + \
	        "=[" + trigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
	count+=1'''

	'''lineUnigrams = fe.getBjoernLineUnigrams()
	count = 0
	for unigram in lineUnigrams:
        print ( "@attribute 'bjoernLineUnigrams" + str(count) + \
               "=[" + unigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
        f.write( "@attribute 'bjoernLineUnigrams" + str(count) + \
                "=[" + unigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
        count+=1
	lineBigrams = fe.getBjoernLineBigrams()
count = 0
for bigram in lineBigrams:
        print ( "@attribute 'bjoernLineBigrams" + str(count) + \
               "=[" + bigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
        f.write( "@attribute 'bjoernLineBigrams" + str(count) + \
                "=[" + bigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
        count+=1
lineUnigrams = fe.getBjoernLineUnigrams()
count = 0
for unigram in lineUnigrams:
        print ( "@attribute 'bjoernLineUnigrams" + str(count) + \
               "=[" + unigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
        f.write( "@attribute 'bjoernLineUnigrams" + str(count) + \
                "=[" + unigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
        count+=1
lineBigrams = fe.getBjoernLineBigrams()'''


'''# AST Features Start
be = BigramExtractor()
count = 0
ASTNodeBigrams = be.getASTNodeBigrams(testDir)
for bigram in ASTNodeBigrams:
f.write("@attribute 'ASTNodeBigramsTF " + str(count) +
        "=[" + bigram.replace("'", "apostrophesymbol")+"]' numeric"+"\n")
# print ("@attribute 'ASTNodeBigramsTF " + str(count) +
#       "=[" + bigram.replace("'", "apostrophesymbol")+"]' numeric"+"\n")
count += 1'''
	f.write('@data \n')
	for file in test_binary_paths:
    		f.write(str(file) + '_'+testDir.split('/')
            	[len(testDir.split('/'))-2] + ',')
    	cfgNodeUniCount = fe.getBjoernCFGGraphmlNodeUnigramsTF(
        	os.path.join(testDir, file.split('_')[2]+'/'+file), bjoernCFGNodeUnigrams)
    	for cfgNodeUni in cfgNodeUniCount:
        	f.write(str(cfgNodeUniCount[cfgNodeUni]) + ",")
    '''cfgNodeBiCount = fe.getBjoernCFGGraphmlNodeBigramsTF(os.path.join(testDir,file.split('_')[2]+'/'+file) , bjoernCFGNodeBigrams)                          
	for cfgNodeBi in cfgNodeBiCount:
		f.write(str(cfgNodeBiCount[cfgNodeBi]) + ",")'''

    '''wordUniCount = fe.getBjoernDisassemblyInstructionUnigramsTF(str(open(os.path.join(testDir,file.split('_')[2]+'/'+file), errors= 'ignore').readlines()),bjoernDisassemblyUnigrams )
	for  wordUnigram in wordUniCount:
		f.write(str(wordUniCount[wordUnigram]) + ", ")
	wordBigramsCount = fe.getBjoernDisassemblyInstructionBigramsTF(str(open(os.path.join(testDir,file.split('_')[2]+'/'+file), errors= 'ignore').readlines()),bjoernDisassemblyBigrams )
	for  wordBigram in wordBigramsCount:
		f.write(str(wordBigramsCount[wordBigram]) + ", ")
	wordTrigramsCount = fe.getBjoernDisassemblyInstructionTrigramsTF(str(open(os.path.join(testDir,file.split('_')[2]+'/'+file), errors= 'ignore').readlines()),bjoernDisassemblyTrigrams )
	for  wordTrigram in wordTrigramsCount:
		f.write(str(wordTrigramsCount[wordTrigram]) + ", ")'''

    # print (os.path.join(testDir,file.split('_')[2]+'/'+file))

    '''lineUnigramsCount = fe.getBjoernLineUnigramsTF(str(open(os.path.join(testDir,file.split('_')[2]+'/'+file), errors= 'ignore').readlines()),lineUnigrams )
	for  lineUnigram in lineUnigramsCount:
		f.write(str(lineUnigramsCount[lineUnigram]) + ", ")

	lineBigramsCount = fe.getBjoernLineBigramsTF(str(open(os.path.join(testDir,file.split('_')[2]+'/'+file), errors= 'ignore').readlines()),lineBigrams )
	for  lineBigram in lineBigramsCount:
		f.write(str(lineBigramsCount[lineBigram]) + ", ")'''
'''# Related files:
# DECOMPILED CODE AKA SCAA FEATURES START (FROM HEXRAYS)
# 1842485_1486492_a9108_hexrays_decompiled.cpp
# print (os.path.join(testDir,file.split('_')[2]+'/'+file+ "_hexrays_decompiled.cpp"))
featureTextHexraysDecompiledCodeCPP = open(os.path.join(
    testDir, file.split('_')[2]+'/'+file + "_hexrays_decompiled.cpp"))
# 1842485_1486492_a9108_hexrays_decompiled.ast
# featureTextHexraysDecompiledCodeAST = open(authorFileName.getParentFile()+ File.separator + authorFileName.getName()+"_hexrays_decompiled.ast");
# 1842485_1486492_a9108_hexrays_decompiled.dep
featureTextHexraysDecompiledCodeDEP = open(os.path.join(
    testDir, file.split('_')[2]+'/'+file + "_hexrays_decompiled.dep")).read()
# print (featureTextHexraysDecompiledCodeDEP)
# 1842485_1486492_a9108_hexrays_decompiled.txt
# featureTextHexraysDecompiledCodeTXT = Util.readFile(authorFileName.getParentFile()+ File.separator + authorFileName.getName()+"_hexrays_decompiled.txt");

# AST node bigrams
bigramCount = be.getASTNodeBigramsTF(
    featureTextHexraysDecompiledCodeDEP, ASTNodeBigrams)
for bigram in ASTNodeBigrams:
    f.write(str(bigramCount[bigram]) + ",")
f.write(" " + "\n")'''


main()
