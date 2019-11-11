import os
import re
from Util import Util
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
    f.write("@relation " + testDir + "ASTFeatures" + "\n\n")
    f.write("@attribute instanceID_original {")
    file_counter = 0
    for file in test_binary_paths:
        #print ("Author" + str(file.split('/')[len(file.split("/"))-2]))
        #print (str(file) + '_'+testDir.split('/')
                #[len(testDir.split('/'))-2] + ',')
        #f.write(str(file) + '_'+testDir.split('/')[len(testDir.split('/'))-2] + ',')
        file_counter+=1
        f.write( str(file_counter) + ",")
    f.write('}' + '\n')
    # authorFileName = ' '
    authors = []
    for file in test_binary_paths:
        authorFileName = file.split('/')[len(file.split("/"))-2]
        # print ("author: " + authorFileName)
        if authorFileName not in authors:
            authors.append(authorFileName)
    fc = FeatureCalculators()
    ASTTypes = fc.uniqueDepASTTypes(testDir)
    count = 0
    '''for ast in ASTTypes:
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
        count += 1'''
    count = 0
    for ast in ASTTypes:
        #print ("@attribute 'ASTNodeTypesAvgDepthASTNode " + str(count) +
        #       "=[" + ast.replace("'", "apostrophesymbol")+"]' numeric" + "\n")
        f.write("@attribute 'ASTNodeTypesAvgDepthASTNode " + str(count) +
                " =[ " + ast.replace("'", "apostrophesymbol")+"]' numeric" + "\n")
        count += 1
    #Write the authors
    f.write("@attribute 'authorName_original' { ")
    for author in authors: 
        f.write (author+"_"+ file.split('/')[-3]+",")
    f.write("} \n")

    f.write('@data \n')
    file_counter=0
    for file in test_binary_paths:
        authorFileName = file.split('/')[-2]
        #f.write(str(file.split('/')[-1]) + '_'+ file.split('/')[-4] +",")
        #f.write(str(file.split('/')[-1].split('_')[-2])  +",")
        file_counter +=1
        f.write(str(file_counter) + ',')
        '''typeCount = fc.DepASTTypeTF((open(file+ "_hexrays_decompiled.dep", errors='ignore').readlines()),ASTTypes)
        for ast in typeCount :
            f.write(str(typeCount[ast]) + ",")
        DepASTTypeTFIDF = fc.DepASTTypeTFIDF((open(file+ "_hexrays_decompiled.dep", errors='ignore').readlines()),testDir,ASTTypes)
        for ast in DepASTTypeTFIDF:
            f.write(str(DepASTTypeTFIDF[ast]) + ",")'''
        dan = DepthASTNode()
        DepFeature = dan.getAvgDepthASTNode((open(file+ "_hexrays_decompiled.dep", errors='ignore').readlines()),ASTTypes)
        for depF in DepFeature:
            f.write(str(DepFeature[depF]) + ",")
        print (file)
        f.write(authorFileName +"_"+ file.split('/')[-3])
        #f.write(authorFileName )
        f.write(" " + "\n")


main()
