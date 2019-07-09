import os
import re
from Util import Util
from FeatureExtractorBjoern import FeatureExtractorBjoern
from FeatureExtractorDisassemblyNDISASM import FeatureExtractorDisassemblyNDISASM
from BigramExtractor import BigramExtractor
from FeatureCalculators import FeatureCalculators
from DepthASTNode import DepthASTNode
from pathlib import Path
from array import *

def config():
    f = open('binary_project.conf')
    conf = {}
    for line in f.readlines():
        key = line.split('=')[0].strip()
        value = line.split('=')[1].strip()
        conf[key] = value
    return conf

def main():
    conf = config()
    u = Util()
    f = open(conf['featureFile'], 'w+')
    testDir = conf['testFolder']
    test_binary_paths = u.listBinaryFiles(testDir)
    print (test_binary_paths)
    f.write("@relation " + testDir + "BjoernCFGDisassembly" + "\n\n")
    f.write("@attribute instanceID_original {")
    for file in test_binary_paths:
        #print (file)
        print(Path(file))
        print ("Author" + str(file.split('/')[len(file.split("/"))-3]))
        #print (str(file) + '_'+testDir.split('/')
                #[len(testDir.split('/'))-2] + ',')
        f.write(str(file) + '_'+testDir.split('/')
                [len(testDir.split('/'))-2] + ',')
    f.write('}' + '\n')
    # authorFileName = ' '
    authors = []
    for file in test_binary_paths:
        authorFileName = file.split('/')[len(file.split("/"))-3]
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
    # CFG NODE UNIGRAMS
    '''bjoernCFGNodeUnigrams = fe.getBjoernCFGGraphmlNodeUnigrams(testDir)
    count = 0
    for unigram in bjoernCFGNodeUnigrams:
        print ("@attribute 'bjoernCFGNodeUnigrams" + str(count) + " " + unigram)
        f.write("@attribute 'BjoernCFGGraphmlNodeUnigrams " + str(count) +
                "=[" + unigram.replace("'", "apostrophesymbol")+"]' numeric" + "\n")
        count += 1
    # CFG NODE BIGRAMS AKA EDGES - REPR
       # get the cflow edges in bjoern CFG and write the node bigram features
    bjoernCFGNodeBigrams = fe.getBjoernCFGGraphmlNodeBigrams(testDir)
    count = 0
    for bigram in bjoernCFGNodeBigrams:
        print ("@attribute 'bjoernCFGNodeBigrams" +
               str(count) + " " + str(bigram))
        f.write("@attribute 'BjoernCFGGraphmlNodeBigrams " + str(count) +
                "=[" + bigram.replace("'", "apostrophesymbol")+"]' numeric" + "\n")
        count += 1'''
    '''bjoernDisassemblyUnigrams = fe.getBjoernDisassemblyInstructionUnigrams(
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
    lineUnigrams = fe.getBjoernLineUnigrams(testDir)
    count = 0
    for unigram in lineUnigrams:
        print ("@attribute 'bjoernLineUnigrams" + str(count) +
               "=[" + unigram.replace("'", "apostrophesymbol")+"]' numeric" + "\n")
        f.write("@attribute 'bjoernLineUnigrams" + str(count) +
                "=[" + unigram.replace("'", "apostrophesymbol")+"]' numeric" + "\n")
        count += 1
    lineBigrams = fe.getBjoernLineBigrams(testDir)
    count = 0
    for bigram in lineBigrams:
        print ("@attribute 'bjoernLineBigrams" + str(count) +
               "=[" + bigram.replace("'", "apostrophesymbol")+"]' numeric" + "\n")
        f.write("@attribute 'bjoernLineBigrams" + str(count) +
                "=[" + bigram.replace("'", "apostrophesymbol")+"]' numeric" + "\n")
        count += 1
    # NDISASM FEATURES START
    # Related files:
    # 1645485_1480492_a9108_NDISASMDisassembly/nodes.csv
    # 1645485_1480492_a9108_NDISASMDisassembly/1645485_1480492_a9108CFG/*.graphml
    # get the basic block node unigrams in NDISASM CFG and write the node unigram features
    fedn = FeatureExtractorDisassemblyNDISASM()
    #DISASSEMBLY INSTRUCTION UNIGRAMS
    #CFG NODE UNIGRAMS - REPR
    #get the instruction unigrams in NDISASM disassembly and write the instruction unigram features
    NDISASMDisassemblyUnigrams = fedn.getNDISASMDisassemblyInstructionUnigrams(testDir)
    count = 0
    for unigram in NDISASMDisassemblyUnigrams:
            print ( "@attribute 'NDISASMDisassemblyInstructionUnigrams" + str(count) + "=[" + unigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
            f.write( "@attribute 'NDISASMDisassemblyInstructionUnigrams" + str(count) + "=[" + unigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
            count+=1
    NDISASMDisassemblyBigrams = fedn.getNDISASMDisassemblyInstructionBigrams(testDir)
    count = 0
    for bigram in NDISASMDisassemblyBigrams:
            print ( "@attribute 'NDISASMDisassemblyInstructionBigrams" + str(count) + "=[" + bigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
            f.write( "@attribute 'NDISASMDisassemblyInstructionBigrams" + str(count) + "=[" + bigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
            count+=1  
    NDISASMDisassemblyTrigrams = fedn.getNDISASMDisassemblyInstructionTrigrams(testDir)
    count = 0
    for trigram in NDISASMDisassemblyTrigrams:
            print ( "@attribute 'NDISASMDisassemblyInstructionTrigrams" + str(count) + "=[" + trigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
            f.write( "@attribute 'NDISASMDisassemblyInstructionTrigrams" + str(count) + "=[" + trigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
            count+=1   

    lineBigrams = fedn.getNDISASMDisassemblyLineBigrams(testDir)
    count = 0
    for bigram in lineBigrams:
            print ( "@attribute 'NDISASMDisassemblyLineBigrams" + str(count) + "=[" + bigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
            f.write( "@attribute 'NDISASMDisassemblyLineBigrams" + str(count) + "=[" + bigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
            count+=1
    
    fc = FeatureCalculators()
    ASTTypes = fc.uniqueDepASTTypes(testDir)
    count = 0
    for ast in ASTTypes:
        print ("@attribute 'ASTNodeTypesTF" + str(count) +
               "=[" + ast.replace("'", "apostrophesymbol")+"]' numeric" + "\n")
        f.write("@attribute 'ASTNodeTypesTF" + str(count) +
                "=[" + ast.replace("'", "apostrophesymbol")+"]' numeric" + "\n")
        count += 1
    count = 0
    for ast in ASTTypes:
        print ("@attribute 'ASTNodeTypesTFIDF" + str(count) +
               "=[" + ast.replace("'", "apostrophesymbol")+"]' numeric" + "\n")
        f.write("@attribute 'ASTNodeTypesTFIDF" + str(count) +
                "=[" + ast.replace("'", "apostrophesymbol")+"]' numeric" + "\n")
        count += 1
    count = 0
    for ast in ASTTypes:
        print ("@attribute 'ASTNodeTypesAvgDepthASTNode" + str(count) +
               "=[" + ast.replace("'", "apostrophesymbol")+"]' numeric" + "\n")
        f.write("@attribute 'ASTNodeTypesAvgDepthASTNode" + str(count) +
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
    ''' count = 0
    for word in cKeywords:
        f.write("@attribute 'cppKeyword "+ str(count)+"=["+word+"]' numeric"+"\n")
        count +=1'''

    #Write the authors
    f.write("@attribute 'authorName_original' { ")
    for author in authors: 
        f.write (author+"_"+ file.split('/')[-4]+",")
    f.write("} \n")

    f.write('@data \n')
    for file in test_binary_paths:
        authorFileName = file.split('/')[-3]
        f.write(str(file.split('/')[-1]) + '_'+ file.split('/')[-4] +",")
        '''cfgNodeUniCount = fe.getBjoernCFGGraphmlNodeUnigramsTF(file, bjoernCFGNodeUnigrams)
        # print (cfgNodeUniCount)
        for cfgNodeUni in cfgNodeUniCount:
            f.write(str(cfgNodeUniCount[cfgNodeUni]) + ",")
        f.write(" " + "\n")'''
        '''cfgNodeBiCount = fe.getBjoernCFGGraphmlNodeBigramsTF(os.path.join(
            testDir, file.split('_')[2]+'/'+file), bjoernCFGNodeBigrams)
        for cfgNodeBi in cfgNodeBiCount:
            f.write(str(cfgNodeBiCount[cfgNodeBi]) + ",")'''

        '''wordUniCount = fe.getBjoernDisassemblyInstructionUnigramsTF((open(file+ "_bjoernDisassembly/nodes.csv", errors= 'ignore').read()),bjoernDisassemblyUnigrams)
        for  wordUnigram in wordUniCount:
            f.write(str(wordUniCount[wordUnigram]) + ", ")
        wordBiCount = fe.getBjoernDisassemblyInstructionBigramsTF((open(file + "_bjoernDisassembly/nodes.csv", errors='ignore').read()), bjoernDisassemblyBigrams)
        for wordBigram in wordBiCount:
            f.write(str(wordBiCount[wordBigram]) + ", ")
        wordTriCount = fe.getBjoernDisassemblyInstructionTrigramsTF((open(file + "_bjoernDisassembly/nodes.csv", errors='ignore').read()), bjoernDisassemblyTrigrams)
        for wordTrigram in wordTriCount:
            f.write(str(wordTriCount[wordTrigram]) + ", ")'''
        lineUnigramsCount = fe.getBjoernLineUnigramsTF((open(file+ "_bjoernDisassembly/nodes.csv", errors='ignore').read()), lineUnigrams)
        for lineUnigram in lineUnigramsCount:
            f.write(str(lineUnigramsCount[lineUnigram]) + ", ")
        lineBigramsCount = fe.getBjoernLineBigramsTF((open(file +"_bjoernDisassembly/nodes.csv", errors='ignore').read()), lineBigrams)
        for lineBigram in lineBigramsCount:
            f.write(str(lineBigramsCount[lineBigram]) + ", ")
        wordUniCount = fedn.getNDISASMDisassemblyInstructionUnigramsTF((open(file, errors= 'ignore').read()),NDISASMDisassemblyUnigrams )
        for  wordUnigram in wordUniCount:
                f.write(str(wordUniCount[wordUnigram]) + ", ")
        wordBigramsCount = fedn.getNDISASMDisassemblyInstructionBigramsTF(str(open( file, errors= 'ignore').read()),NDISASMDisassemblyBigrams )
        for  wordBigram in wordBigramsCount:
                f.write(str(wordBigramsCount[wordBigram]) + ", ")
        wordTrigramsCount = fedn.getNDISASMDisassemblyInstructionTrigramsTF(str(open(file, errors= 'ignore').read()),NDISASMDisassemblyTrigrams )
        for  wordTrigram in wordTrigramsCount:
                f.write(str(wordTrigramsCount[wordTrigram]) + ", ")
        lineBigramsCount = fedn.getNDISASMLineBigramsTF(str(open(file, errors= 'ignore').read()),lineBigrams )
        for  lineBigram in lineBigramsCount:
                f.write(str(lineBigramsCount[lineBigram]) + ", ")
        typeCount = fc.DepASTTypeTF((open(file+ "_hexrays_decompiled.dep", errors='ignore').readlines()),ASTTypes)
        for ast in typeCount :
            f.write(str(typeCount[ast]) + ",")
        DepASTTypeTFIDF = fc.DepASTTypeTFIDF((open(file+ "_hexrays_decompiled.dep", errors='ignore').readlines()),testDir,ASTTypes)
        for ast in DepASTTypeTFIDF:
            f.write(str(DepASTTypeTFIDF[ast]) + ",")
        dan = DepthASTNode()
        DepFeature = dan.getAvgDepthASTNode((open(file+ "_hexrays_decompiled.dep", errors='ignore').readlines()),ASTTypes)
        for depF in DepFeature:
            f.write(str(DepFeature[depF]) + ",")
            #print (str(DepFeature[depF]) + ",")
        print (file)
        '''cKeywordsTF = fc.getCandCPPKeywordsTF(open(file+ "_hexrays_decompiled.cpp", errors='ignore').read())
        for word in cKeywords:
            f.write(str(cKeywordsTF[word])+ ",")'''
        f.write(authorFileName +"_"+ file.split('/')[-4])
        
        
        f.write(" " + "\n")


main()
