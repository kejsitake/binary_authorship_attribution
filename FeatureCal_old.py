import re
from Util import Util
class FeatureCalculators():
	hex_reg_ex = re.compile(r'0[xX][0-9a-fA-F]+')
	nr_reg_ex = re.compile(r'\d+\t+')
	multi_sp_reg_ex = re.compile(r'\s+')
	multi_dots_reg_ex = re.compile(r'\..+') 
	def uniqueDepASTTypes(self, dirPath):
		u = Util()
		test_file_paths =u.listFiles(dirPath, ".dep")
		uniqueWords = []
		for file in test_file_paths:
			f = open(file).readlines()		
			for line in f:
				inputText = line.replace("(", "splitthere")
				inputText = inputText.replace(")", "splithere")
				inputText = re.sub(self.nr_reg_ex, " ", inputText)		
				inputText = re.sub(self.multi_sp_reg_ex, " ", inputText)
				arr = inputText.split("splitthere")
				if (len(arr)>0):
					for a in arr:
						if (a):
							uniqueWords.append(a.strip("splithere"))
		#print(uniqueWords)
		return uniqueWords
	

	def DepASTTypeTF(featureText, ASTTypes):	
		#symbolCount = len(ASTTypes)
		counter = []
		for i in range(0,len(ASTTypes)):
			str = ASTTypes[i]
			str1 = "(" + str + ")"
			str2 = "(" + str + "("
			str3 = ")" + str + ")"
			str4 = ")" + str + "("
		#if case insensitive, make lowercase
			counter[i] = featureText.count(str1) + featureText.count(str2)+featureText.count(str3)+featureText.count(str4) 
		return counter

	def DepASTTypeTFIDF(featureText, pathDir, DepASTTypes):
		symbolCount = len(DepASTTypes)
		tf = self.DepASTTypeTF(featureText, DepASTTypes)
		idf = 0
		counter = []
		for i in range (0, len(ASTTypes)):
			if (tf[i]>0):
				idf = DepASTTypeIDF(pathDir, DepASTTypes)
				counter.append(tf[i]*idf)	
		return counter

	def getCandCPPKeywordsTF(sourceCode):
		counter = [] 
		cKeywords = ["auto", 	"break", 	"case", 	"char", 	"const", 	
				  "continue", 	"default", 	"do", 	"double", 	"else", 	"enum", 	
				  "extern", 	"float", 	"for", 	"goto", 	"if", 	"inline", 	
				  "int", 	"long", 	"register", 	"restrict", 	"return", 	"short", 	
				  "signed", 	"sizeof", 	"static", 	"struct", 	"switch", 	"typedef", 	
				  "union", 	"unsigned", 	"void", 	"volatile", 	"while", 	"_Alignas", 	
				  "_Alignof", 	"_Atomic", 	"_Bool", 	"_Complex", 	"_Generic", 	"_Imaginary",
				  "_Noreturn", 	"_Static_assert", 	"_Thread_local","alignas",	"alignof",	"and",	"and_eq",	"asm",	
				  "bitand",	"bitor",	"bool",	"catch",	"char",	"char16_t",	"char32_t",
				  "class",	"compl",	"const",	"constexpr",	"const_cast",	"decltype",	
				  "delete",	"dynamic_cast",	"explicit",	"export",	
				  "FALSE",		"friend",		
				  "mutable",	"namespace",	"new",	"noexcept",	"not",	"not_eq",	"nullptr",	"operator",	"or",
				  "or_eq"	,"private"	,"protected"	,"public"	,	"reinterpret_cast",	
				  "static_assert",	"static_cast",	
				  	"template",	"this"	,"thread_local",	"throw",	"TRUE",	"try",		"typeid",
				  "typename",		"using",	"virtual",		"wchar_t",
				  "xor",	"xor_eq", "override", "final"] 
		#counter = []	
		for i in symbolCount:
			counter.append(sourceCode.count(i))
		return counter
def main():
	testDir = "/home/sahil/3authors_small"
	fc = FeatureCalculators()
	print (fc.uniqueDepASTTypes(testDir))	
	print ("here")
main()
