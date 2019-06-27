import os
import re
from Util import Util
from FeatureExtractorBjoern import FeatureExtractorBjoern
from BigramExtractor import BigramExtractor
from FeatureCalculators import FeatureCalculators
from DepthASTNode import DepthASTNode
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
    authors = []
    for file in test_binary_paths:
        authorFileName = (file.split('_')[2])
        # print ("author: " + authorFileName)
        if authorFileName not in authors:
            authors.append(authorFileName)
    '''for name in authors:
        f.write(name + ',')
    f.write('}' + '\n \n')'''
    # BJOERN FEATURES START
    # Related files:
    # 1645485_1480492_a9108_bjoernDisassembly/nodes.csv
    # 1645485_1480492_a9108_bjoernDisassembly/1645485_1480492_a9108CFG/*.graphml
    # get the basic block node unigrams in bjoern CFG and write the node unigram features
    fe = FeatureExtractorBjoern()
    '''# CFG NODE UNIGRAMS
    bjoernCFGNodeUnigrams = fe.getBjoernCFGGraphmlNodeUnigrams()
    count = 0
    for unigram in bjoernCFGNodeUnigrams:
        print ("@attribute 'bjoernCFGNodeUnigrams" + str(count) + " " + unigram)
        f.write("@attribute 'BjoernCFGGraphmlNodeUnigrams " + str(count) +
                "=[" + unigram.replace("'", "apostrophesymbol")+"]' numeric" + "\n")
        count += 1
    # CFG NODE BIGRAMS AKA EDGES - REPR
       # get the cflow edges in bjoern CFG and write the node bigram features
    bjoernCFGNodeBigrams = fe.getBjoernCFGGraphmlNodeBigrams()
    count = 0
    for bigram in bjoernCFGNodeBigrams:
        print ("@attribute 'bjoernCFGNodeBigrams" +
               str(count) + " " + str(bigram))
        f.write("@attribute 'BjoernCFGGraphmlNodeBigrams " + str(count) +
                "=[" + bigram.replace("'", "apostrophesymbol")+"]' numeric" + "\n")
        count += 1
    bjoernDisassemblyUnigrams = fe.getBjoernDisassemblyInstructionUnigrams(
        testDir)
    count = 0
    for unigram in bjoernDisassemblyUnigrams:
        print ("@attribute 'bjoernDisassemblyInstructionUnigrams" + str(count) +
               "=[" + unigram.replace("'", "apostrophesymbol")+"]' numeric" + "\n")
        f.write("@attribute 'bjoernDisassemblyInstructionUnigrams" + str(count) +
                "=[" + unigram.replace("'", "apostrophesymbol")+"]' numeric" + "\n")
        count += 1
    bjoernDisassemblyBigrams = fe.getBjoernDisassemblyInstructionBigrams(
        testDir)
    count = 0
    for bigram in bjoernDisassemblyBigrams:
        print ("@attribute 'bjoernDisassemblyInstructionBigrams" + str(count) +
               "=[" + bigram.replace("'", "apostrophesymbol")+"]' numeric" + "\n")
        f.write("@attribute 'bjoernDisassemblyInstructionBigrams" + str(count) +
                "=[" + bigram.replace("'", "apostrophesymbol")+"]' numeric" + "\n")
        count += 1
    bjoernDisassemblyTrigrams = fe.getBjoernDisassemblyInstructionTrigrams(
        testDir)
    count = 0
    for trigram in bjoernDisassemblyTrigrams:
        print ("@attribute 'bjoernDisassemblyInstructionTrigrams" + str(count) +
               "=[" + trigram.replace("'", "apostrophesymbol")+"]' numeric" + "\n")
        f.write("@attribute 'bjoernDisassemblyInstructionTrigrams" + str(count) +
                "=[" + trigram.replace("'", "apostrophesymbol")+"]' numeric" + "\n")
        count += 1'''
    '''lineUnigrams = fe.getBjoernLineUnigrams()
    count = 0
    for unigram in lineUnigrams:
        print ("@attribute 'bjoernLineUnigrams" + str(count) +
               "=[" + unigram.replace("'", "apostrophesymbol")+"]' numeric" + "\n")
        f.write("@attribute 'bjoernLineUnigrams" + str(count) +
                "=[" + unigram.replace("'", "apostrophesymbol")+"]' numeric" + "\n")
        count += 1
    lineBigrams = fe.getBjoernLineBigrams()
    count = 0
    for bigram in lineBigrams:
        print ("@attribute 'bjoernLineBigrams" + str(count) +
               "=[" + bigram.replace("'", "apostrophesymbol")+"]' numeric" + "\n")
        f.write("@attribute 'bjoernLineBigrams" + str(count) +
                "=[" + bigram.replace("'", "apostrophesymbol")+"]' numeric" + "\n")
        count += 1'''
    fc = FeatureCalculators()
    ASTTypes = fc.uniqueDepASTTypes(testDir)
    count = 0
    '''for ast in ASTTypes:
        print ("@attribute 'ASTNodeTypesTF" + str(count) +
               "=[" + ast.replace("'", "apostrophesymbol")+"]' numeric" + "\n")
        f.write("@attribute 'ASTNodeTypesTF" + str(count) +
                "=[" + ast.replace("'", "apostrophesymbol")+"]' numeric" + "\n")
        count += 1'''
    count = 0
    for ast in ASTTypes:
        print ("@attribute 'ASTNodeTypesTFIDF" + str(count) +
               "=[" + ast.replace("'", "apostrophesymbol")+"]' numeric" + "\n")
        f.write("@attribute 'ASTNodeTypesTFIDF" + str(count) +
                "=[" + ast.replace("'", "apostrophesymbol")+"]' numeric" + "\n")
        count += 1
    #Keyword Features from HexRays
    cKeywords = ["auto",     "break",        "case",         "char",         "const",
              "continue",       "default",      "do",   "double",       "else",         "enum",
              "extern",         "float",        "for",  "goto",         "if",   "inline",
              "int",    "long",         "register",     "restrict",     "return",       "short",
              "signed",         "sizeof",       "static",       "struct",       "switch",       "typedef",
              "union",  "unsigned",     "void",         "volatile",     "while",        "_Alignas",
              "_Alignof",       "_Atomic",      "_Bool",        "_Complex",     "_Generic",     "_Imaginary",
              "_Noreturn",      "_Static_assert",       "_Thread_local","alignas",      "alignof",      "and",  "and_eq",       "asm",
              "bitand", "bitor",        "bool", "catch",        "char", "char16_t",     "char32_t",
              "class",  "compl",        "const",        "constexpr",    "const_cast",   "decltype",
              "delete", "dynamic_cast", "explicit",     "export",
              "FALSE",          "friend",
              "mutable",        "namespace",    "new",  "noexcept",     "not",  "not_eq",       "nullptr",      "operator",     "or",
              "or_eq"   ,"private"      ,"protected"    ,"public"       ,       "reinterpret_cast",
              "static_assert",  "static_cast",
                    "template", "this"  ,"thread_local",        "throw",        "TRUE", "try",          "typeid",
              "typename",               "using",        "virtual",              "wchar_t",
              "xor",    "xor_eq", "override", "final"]
    count = 0
    for word in cKeywords:
        f.write("@attribute 'cppKeyword "+ str(count)+"=["+word+"]' numeric"+"\n")
        count +=1

    #Write the authors
    f.write("@attribute 'authorName_original' { ")
    for author in authors: 
        f.write (author+"_"+testDir.split('/')
                            [len(testDir.split('/'))-2] + ", ")
    f.write("} \n")

    f.write('@data \n')
    for file in test_binary_paths:
        authorFileName = (file.split('_')[2])
        f.write(str(file) + '_'+testDir.split('/')
                [len(testDir.split('/'))-2] + ',')
        '''cfgNodeUniCount = fe.getBjoernCFGGraphmlNodeUnigramsTF(os.path.join(testDir, file.split('_')[2]+'/'+file), bjoernCFGNodeUnigrams)
        # print (cfgNodeUniCount)
        for cfgNodeUni in cfgNodeUniCount:
            f.write(str(cfgNodeUniCount[cfgNodeUni]) + ",")
        f.write(" " + "\n")
        cfgNodeBiCount = fe.getBjoernCFGGraphmlNodeBigramsTF(os.path.join(
            testDir, file.split('_')[2]+'/'+file), bjoernCFGNodeBigrams)
        for cfgNodeBi in cfgNodeBiCount:
            f.write(str(cfgNodeBiCount[cfgNodeBi]) + ",")

        wordUniCount = fe.getBjoernDisassemblyInstructionUnigramsTF(str(open(os.path.join(testDir,file.split(
            '_')[2]+'/'+file+ "_bjoernDisassembly/nodes.csv"), errors= 'ignore').readlines()),bjoernDisassemblyUnigrams)
        for  wordUnigram in wordUniCount:
                f.write(str(wordUniCount[wordUnigram]) + ", ")
        wordBiCount = fe.getBjoernDisassemblyInstructionBigramsTF(str(open(os.path.join(testDir, file.split(
            '_')[2]+'/'+file + "_bjoernDisassembly/nodes.csv"), errors='ignore').readlines()), bjoernDisassemblyBigrams)
        for wordBigram in wordBiCount:
            f.write(str(wordBiCount[wordBigram]) + ", ")
        wordTriCount = fe.getBjoernDisassemblyInstructionTrigramsTF(str(open(os.path.join(testDir, file.split(
            '_')[2]+'/'+file + "_bjoernDisassembly/nodes.csv"), errors='ignore').readlines()), bjoernDisassemblyTrigrams)
        for wordTrigram in wordTriCount:
            f.write(str(wordTriCount[wordTrigram]) + ", ")'''
        '''lineBigramsCount = fe.getBjoernLineBigramsTF(str(open(os.path.join(
            testDir, file.split('_')[2]+'/'+file +"_bjoernDisassembly/nodes.csv"), errors='ignore').readlines()), lineBigrams)
        for lineBigram in lineBigramsCount:
            f.write(str(lineBigramsCount[lineBigram]) + ", ")'''
        '''lineUnigramsCount = fe.getBjoernLineUnigramsTF(str(open(os.path.join(
            testDir, file.split('_')[2]+'/'+file+ "_bjoernDisassembly/nodes.csv"), errors='ignore').readlines()), lineUnigrams)
        for lineUnigram in lineUnigramsCount:
            f.write(str(lineUnigramsCount[lineUnigram]) + ", ")'''
        '''typeCount = fc.DepASTTypeTF(str(open(os.path.join(
            testDir, file.split('_')[2]+'/'+file+ "_hexrays_decompiled.dep"), errors='ignore').readlines()),ASTTypes)
        for ast in typeCount :
            f.write(str(typeCount[ast]) + ",")
        DepASTTypeTFIDF = fc.DepASTTypeTFIDF(str(open(os.path.join(
            testDir, file.split('_')[2]+'/'+file+ "_hexrays_decompiled.dep"), errors='ignore').readlines()),testDir,ASTTypes)
        for ast in DepASTTypeTFIDF:
            f.write(str(DepASTTypeTFIDF[ast]) + ",")
        f.write(authorFileName+"_"+testDir.split('/')
                            [len(testDir.split('/'))-2])'''
        '''dan = DepthASTNode()
        DepFeature = dan.getAvgDepthASTNode(open(os.path.join(
            testDir, file.split('_')[2]+'/'+file+ "_hexrays_decompiled.dep"), errors='ignore').readlines(),ASTTypes)
        print (os.path.join(
            testDir, file.split('_')[2]+'/'+file+ "_hexrays_decompiled.dep"))
        for depF in DepFeature:
            f.write(str(DepFeature[depF]) + ",")
            print (str(DepFeature[depF]) + ",")'''
        print (file)
        cKeywordsTF = fc.getCandCPPKeywordsTF(open(os.path.join(
            testDir, file.split('_')[2]+'/'+file+ "_hexrays_decompiled.cpp"), errors='ignore').read())
        for word in cKeywords:
            f.write(str(cKeywordsTF[word])+ ",")
        f.write(authorFileName+"_"+testDir.split('/')
                            [len(testDir.split('/'))-2])
        
        f.write(" " + "\n")


main()
