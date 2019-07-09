
import os, re
from  Util import Util
from  pathlib import Path
from array import *

class FeatureExtractorDisassemblyNDISASM():
	#u = Util()
	dirPath = "/home/kejsi/3authors_small"
	hex_reg_ex = re.compile(r'0[xX][0-9a-fA-F]+')
	nr_reg_ex = re.compile(r'\d+')
	multi_sp_reg_ex = re.compile(r'\s+')
	multi_dots_reg_ex = re.compile(r'\..+')	

	def getNDISASMDisassemblyInstructionUnigrams(self, dirPath):
		u = Util()
		unigrams = []
		test_file_paths = u.listFiles(self.dirPath,".dis")			
		for file in test_file_paths:
			f = open(file).readlines()
			for line in f:
				arr = re.split(r'\s+', line, maxsplit=2)
				#arr = line.split("  ",5)
				if (len(arr)>2):
					#print("Here")
					line = arr[2]
					#print (line)	
					line = line.replace("\"", " ")
					line = line.replace(",", " ")
					line = line.replace("'", " ")
					line = line.replace("..+", " ")
					line = line.replace("|", " ")
					line = line.replace("+", " ")
					line = line.replace("-", " ")
					line = line.replace("*", " ")
					line = line.replace(":", " ")
					line = re.sub(self.hex_reg_ex, "hexadecimal", line)
					line = re.sub(self.nr_reg_ex, "number", line)
					line = re.sub(self.multi_sp_reg_ex, " ", line)
					line = re.sub(self.multi_dots_reg_ex, " ", line)
					toAdd  = line.strip().split(" ")
				for add in toAdd: #check if empty
					if add not in unigrams:
						unigrams.append(add)
		return unigrams
		

	def getNDISASMDisassemblyInstructionUnigramsTF(self, featureText, instrUnigrams):
		u = Util()
		unigrams = []
		dict_TF = {}
		featureText = featureText.replace("\"", " ")
		featureText = featureText.replace(",", " ")
		featureText = featureText.replace("'", " ")
		featureText = featureText.replace("..+", " ")
		featureText = featureText.replace("|", " ")
		featureText = featureText.replace("+", " ")
		featureText = featureText.replace("-", " ")
		featureText = featureText.replace("*", " ")
		featureText = featureText.replace(":", " ")
		featureText = re.sub(self.hex_reg_ex, "hexadecimal", featureText)
		featureText = re.sub(self.nr_reg_ex, "number", featureText)
		featureText = re.sub(self.multi_sp_reg_ex, " ", featureText)
		featureText = re.sub(self.multi_dots_reg_ex, " ", featureText)
		for token in  instrUnigrams:
			dict_TF[token] = featureText.count(token)
		return dict_TF
		
	
	def getNDISASMDisassemblyInstructionBigrams(self, dirPath):
		u = Util()
		bigrams = []
		test_file_paths = u.listFiles(dirPath, ".dis")			
		for file in test_file_paths:
			f = open(file).readlines()
			for line in f:
				arr = re.split(r'\s+', line, maxsplit=4)
				#arr = line.split("  ",5)
				if (len(arr)>4):
					#print("Here")
					line = arr[4]
					#print (line)	
					line = line.replace("\"", " ")
					line = line.replace(",", " ")
					line = line.replace("'", " ")
					#line = line.replace("\|", " ")
					line = line.replace("..+", " ")
					line = line.replace("|", " ")
					line = line.replace("'", " ")
					line = line.replace("+", " ")
					line = line.replace("-", " ")
					line = line.replace("*", " ")
					line = line.replace(":", " ")
					line = re.sub(self.hex_reg_ex, "hexadecimal", line)
					line = re.sub(self.nr_reg_ex, "number", line)
					line = re.sub(self.multi_sp_reg_ex, " ", line)
					line = re.sub(self.multi_dots_reg_ex, " ", line)
					toAdd  = line.strip().split(" ")
					#print( toAdd)
					for i in range(1, len(toAdd)): #check if empty
						bigram = toAdd[i-1]+ " " + toAdd[i]
						if (toAdd[i-1] !="number") and i==1:
							continue
						if (bigram not in bigrams):
							bigrams.append(bigram)			
		return bigrams
		
	
	def getNDISASMDisassemblyInstructionBigramsTF(self, featureText, instrBigrams):
		u = Util()	
		bigrams = []
		dict_TF = {}
		featureText = featureText.replace("\"", " ")
		featureText = featureText.replace(",", " ")
		featureText = featureText.replace("'", " ")
		featureText = featureText.replace("..+", " ")
		featureText = featureText.replace("|", " ")
		featureText = featureText.replace("+", " ")
		featureText = featureText.replace("-", " ")
		featureText = featureText.replace("*", " ")
		featureText = featureText.replace(":", " ")
		featureText = re.sub(self.hex_reg_ex, "hexadecimal", featureText)
		featureText = re.sub(self.nr_reg_ex, "number", featureText)
		featureText = re.sub(self.multi_sp_reg_ex, " ", featureText)
		featureText = re.sub(self.multi_dots_reg_ex, " ", featureText)
		for token in  instrBigrams:
			dict_TF[token] = featureText.count(token)
		return dict_TF
                

	def getNDISASMDisassemblyInstructionTrigrams(self, dirPath):
		u = Util()
		trigrams = []
		test_file_paths = u.listFiles(dirPath, ".dis")			
		for file in test_file_paths:
			f = open(file).readlines()
			for line in f:
				arr = re.split(r'\s+', line, maxsplit=4)
				#arr = line.split("  ",5)
				if (len(arr)>4):
					#print("Here")
					line = arr[4]
					#print (line)	
					line = line.replace("\"", " ")
					line = line.replace(",", " ")
					line = line.replace("'", " ")
					line = line.replace("..+", " ")
					line = line.replace("|", " ")
					line = line.replace("+", " ")
					line = line.replace("-", " ")
					line = line.replace("*", " ")
					line = line.replace(":", " ")
					line = re.sub(self.hex_reg_ex, "hexadecimal", line)
					line = re.sub(self.nr_reg_ex, "number", line)
					line = re.sub(self.multi_sp_reg_ex, " ", line)
					line = re.sub(self.multi_dots_reg_ex, " ", line)
					toAdd  = line.strip().split(" ")
					#print( toAdd)
					for i in range(2, len(toAdd)): #check if empty
						trigram = toAdd[i-2]+ " " + toAdd[i-1] + " "+toAdd[i]
						if (toAdd[i-2] !="number") and i==2:
							continue
						if (trigram not in trigrams):
							trigrams.append(trigram)			
		return trigrams
		
	
	def getNDISASMDisassemblyInstructionTrigramsTF(self, featureText, instrTrigrams):
		u = Util()	
		bigrams = []
		dict_TF = {}
		featureText = featureText.replace("\"", " ")
		featureText = featureText.replace(",", " ")
		featureText = featureText.replace("'", " ")
		featureText = featureText.replace("..+", " ")
		featureText = featureText.replace("|", " ")
		featureText = featureText.replace("+", " ")
		featureText = featureText.replace("-", " ")
		featureText = featureText.replace("*", " ")
		featureText = featureText.replace(":", " ")
		featureText = re.sub(self.hex_reg_ex, "hexadecimal", featureText)
		featureText = re.sub(self.nr_reg_ex, "number", featureText)
		featureText = re.sub(self.multi_sp_reg_ex, " ", featureText)
		featureText = re.sub(self.multi_dots_reg_ex, " ", featureText)
		for token in  instrTrigrams:
			dict_TF[token] = featureText.count(token)
		return dict_TF
                
	
	def getNDISASMDisassemblyLineBigrams (self, dirPath):
		u = Util()
		uniqueLineBigrams = []
		lineBigrams = []
		test_file_paths = u.listFiles(dirPath, ".dis")
                #print (test_file_paths)
		for file in test_file_paths:
			f = open(file).readlines()
			tmp = ""
			for line in f:
				arr = re.split(r'\s+', line, maxsplit=2)
				#arr = line.split("  ",5)
				if (len(arr)>2):
					#print("Here")
					line = arr[2]
					#print (line)	
					line = line.replace("\"", " ")
					#line = line.replace("\|", " ")
					line = line.replace("..+", " ")
					line = line.replace("|", " ")
					line = re.sub(self.hex_reg_ex, "hexadecimal", line)
					line = re.sub(self.nr_reg_ex, "number", line)
					line = re.sub(self.multi_sp_reg_ex, " ", line)
					#print (line)
				if (line): #check if empty
					lineBigrams.append(tmp.strip() + " " + line.strip()+" ")			
					tmp = line
		lineBigrams = list(dict.fromkeys(lineBigrams))	
		return lineBigrams

	def getNDISASMLineBigramsTF(self, featureText, lineBigrams):  # this returns 0
		u = Util()
		dict_TF = {}
		featureText = featureText.replace("\"", " ")
		featureText = re.sub(self.hex_reg_ex, "hexadecimal", featureText)
		featureText = re.sub(self.nr_reg_ex, "number", featureText)
		featureText = re.sub(self.multi_sp_reg_ex, " ", featureText)
		for token in lineBigrams:
			dict_TF[token] = featureText.count(token)
		#print (dict_TF)
		return (dict_TF) 		

def main():
	u = Util()
	f = open("/home/kejsi/PythonBda/py_test.arff", 'w+')
	testDir = "/home/kejsi/3authors_small/"
	test_binary_paths = u.listBinaryFiles(testDir)
	print (test_binary_paths)
	f.write("@relation " + testDir + "NDISASMCFGDisassembly" +"\n\n")
	f.write("@attribute instanceID_original {")
	for file in test_binary_paths:
		f.write(str(file) +'_'+testDir.split('/')[len(testDir.split('/'))-2] +',')
	f.write('}' +'\n')
	#authorFileName = ' '
	f.write("@attribute 'authorName_original' {" )
	authors = []
	for file in test_binary_paths:
		authorFileName = (file.split('_')[2])
		#print ("author: " + authorFileName)
		if authorFileName not in authors:
			authors.append(authorFileName)
	for name in authors:
		f.write (name + ',')
	f.write('}' + '\n \n')
	# NDISASM FEATURES START
	# Related files:
	# 1645485_1480492_a9108_NDISASMDisassembly/nodes.csv
	# 1645485_1480492_a9108_NDISASMDisassembly/1645485_1480492_a9108CFG/*.graphml
	# get the basic block node unigrams in NDISASM CFG and write the node unigram features
	fe = FeatureExtractorDisassemblyNDISASM()
	#DISASSEMBLY INSTRUCTION UNIGRAMS
	#CFG NODE UNIGRAMS - REPR
	#get the instruction unigrams in NDISASM disassembly and write the instruction unigram features
	NDISASMDisassemblyUnigrams = fe.getNDISASMDisassemblyInstructionUnigrams(testDir)
	count = 0
	for unigram in NDISASMDisassemblyUnigrams:
                print ( "@attribute 'NDISASMDisassemblyInstructionUnigrams" + str(count) + "=[" + unigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
                f.write( "@attribute 'NDISASMDisassemblyInstructionUnigrams" + str(count) + "=[" + unigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
                count+=1
	NDISASMDisassemblyBigrams = fe.getNDISASMDisassemblyInstructionBigrams(testDir)
	count = 0
	for bigram in NDISASMDisassemblyBigrams:
		print ( "@attribute 'NDISASMDisassemblyInstructionBigrams" + str(count) + "=[" + bigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
		f.write( "@attribute 'NDISASMDisassemblyInstructionBigrams" + str(count) + "=[" + bigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
		count+=1  
	NDISASMDisassemblyTrigrams = fe.getNDISASMDisassemblyInstructionTrigrams(testDir)
	count = 0
	for trigram in NDISASMDisassemblyTrigrams:
		print ( "@attribute 'NDISASMDisassemblyInstructionTrigrams" + str(count) + "=[" + trigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
		f.write( "@attribute 'NDISASMDisassemblyInstructionTrigrams" + str(count) + "=[" + trigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
		count+=1   

	lineBigrams = fe.getNDISASMDisassemblyLineBigrams(testDir)
	count = 0
	for bigram in lineBigrams:
		print ( "@attribute 'NDISASMDisassemblyLineBigrams" + str(count) + "=[" + bigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
		f.write( "@attribute 'NDISASMDisassemblyLineBigrams" + str(count) + "=[" + bigram.replace("'", "apostrophesymbol")+"]' numeric"+ "\n")
		count+=1
	
	f.write ('@data \n')
	for file in test_binary_paths:
		f.write(str(file) +'_'+testDir.split('/')[len(testDir.split('/'))-2] +',') 
		wordUniCount = fe.getNDISASMDisassemblyInstructionUnigramsTF((open(file, errors= 'ignore').read()),NDISASMDisassemblyUnigrams )
		for  wordUnigram in wordUniCount:
			f.write(str(wordUniCount[wordUnigram]) + ", ")
		wordBigramsCount = fe.getNDISASMDisassemblyInstructionBigramsTF(str(open( file, errors= 'ignore').read()),NDISASMDisassemblyBigrams )
		for  wordBigram in wordBigramsCount:
			f.write(str(wordBigramsCount[wordBigram]) + ", ")
		wordTrigramsCount = fe.getNDISASMDisassemblyInstructionTrigramsTF(str(open(file, errors= 'ignore').read()),NDISASMDisassemblyTrigrams )
		for  wordTrigram in wordTrigramsCount:
			f.write(str(wordTrigramsCount[wordTrigram]) + ", ")
		lineBigramsCount = fe.getNDISASMLineBigramsTF(str(open(file, errors= 'ignore').read()),lineBigrams )
		for  lineBigram in lineBigramsCount:
			f.write(str(lineBigramsCount[lineBigram]) + ", ")
main()

