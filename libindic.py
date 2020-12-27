from libindic.soundex import Soundex
import fuzzy

def isEqual(name1, name2):
	instance = Soundex()
	if instance.soundex(name1) == instance.soundex(name2):
		return 1
	else:
		return 0

def compareNames(name1, name2):
	instance = Soundex()
	if instance.compare(name1, name2) in [0,1, 2]:
		return 1
	else:
		return 0
	
	
#print(isEqual("Hussam", "Hosam"))
#print(isEqual("Hussam", "fsdfsdfsf"))

print(compareNames("Hussam", "Hosam"))
print(compareNames("Jessica", "Joshua"))
print(compareNames("Hasan", "Hasani"))
print(compareNames("Hasan", "Hassan"))
print(compareNames("Ahmad", "Hassan"))

'''
print("soundex")
soundex = fuzzy.Soundex(4)
print(soundex('Hasan'))
print(soundex('Hassan'))

print("dmeta")
dmeta = fuzzy.DMetaphone()
print(dmeta('Hasan'))
print(dmeta('Hassan'))

print("nysiis")
print(fuzzy.nysiis('Hasan'))
print(fuzzy.nysiis('Hassan'))
'''
