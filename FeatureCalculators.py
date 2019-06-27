import math
import re
from Util import Util
import os

class FeatureCalculators():
    nr_reg_ex = re.compile(r'\d+\t')
    multi_sp_reg_ex = re.compile(r'\s+')
    multi_dots_reg_ex = re.compile(r'\..+')
    
    def DepASTTypeTF(self,featureText, ASTTypes):
        dict_TF = {}
        for ast in ASTTypes:
            str1 = "("+ast+")"
            str2 = "("+ast+ "("
            str3 = ")"+ast+")"
            str4 = ")"+ast+"("
            dict_TF[ast] = featureText.count(str1) +featureText.count(str2)+featureText.count(str3)+featureText.count(str4)
        return dict_TF

    def DepASTTypeIDF(self, pathDir, ASTType):
        IDFcounter = 0
        directories = os.listdir(pathDir)
        u = Util()
        for authorName in directories:
            counter = 0
            test_file_paths = u.listFiles(os.path.join(pathDir, authorName), '.dep')
            #import pdb; pdb.set_trace()
            for file in test_file_paths:
                featureText = open(file).read()
                termFrequencyAuthor = featureText.count(ASTType)
                if (termFrequencyAuthor > 0):   
                    counter+=1
            if (counter>0):
                IDFcounter +=1
        if IDFcounter==0:
            return 0
        else:
            return math.log2(len(directories)/IDFcounter)

    def DepASTTypeTFIDF(self, featureText, pathDir, DepASTTypes):
        tf = self.DepASTTypeTF(featureText, DepASTTypes)
        dict_tfidf = {}
        idf = 0
        for ast in DepASTTypes:
            if tf[ast]>0 :
                idf = self.DepASTTypeIDF(pathDir, ast)
                dict_tfidf[ast] = int(tf[ast])*idf
            else:
                dict_tfidf[ast]=0
        return dict_tfidf
   
    def uniqueDepASTTypes(self, pathDir):
       u = Util()
       test_file_paths = u.listFiles(pathDir, ".dep")
       uniqueWords = []
       arr = []
       for file in test_file_paths:
           inputText = open(file).read()
           #print (inputText)
           inputText = re.sub(self.nr_reg_ex," ", inputText)
           inputText = inputText.replace("(", "splithere")
           inputText = inputText.replace(")", "splithere")
           inputText = re.sub(self.multi_sp_reg_ex," ", inputText)
           #import pdb; pdb.set_trace()
           arr = set(inputText.split("splithere"))
           if (len(arr)>0):
               for a in arr:
                   if (a) and (a!=" ") and a not in uniqueWords:
                       uniqueWords.append(a.strip())
       return uniqueWords
    
    def getCandCPPKeywordsTF(self, sourceCode):
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
        dict_tf ={}
        for word in cKeywords:
            dict_tf[word] = sourceCode.count(word)
        return dict_tf
   

