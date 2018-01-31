from def_scap_tagging import tagging 
import os
import codecs
c=0
while c<5:
	c+=1 
	for file in ".\\tag_docs\\":
		file = ".\\tag_docs\\article" + str(c) + ".txt"
		tagging(file)