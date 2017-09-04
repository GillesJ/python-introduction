import syns_and_ants
import translation

def SP_NL(filename):
	syns_and_ants.syns_and_ants(filename)
	translation.translate_mijnwoordenboek(filename)

filename = input("Give the filename: ")
SP_NL(filename)