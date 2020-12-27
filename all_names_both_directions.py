from libindic.soundex import Soundex
import fuzzy
import jellyfish
import csv
import itertools

names = [line.strip() for line in open("names.txt", 'r')]

fieldnames = ['Name1', 'Name2', 'Output']

libindic_results_csv = open('2D_libindic_results.csv', 'w', newline='')
libindic_writer = csv.DictWriter(libindic_results_csv, fieldnames=fieldnames)
libindic_writer.writeheader()

jellyfish_match_rating_results_csv = open('2D_jellyfish_match_rating_results.csv', 'w', newline='')
jellyfish_match_rating_writer = csv.DictWriter(jellyfish_match_rating_results_csv, fieldnames=fieldnames)
jellyfish_match_rating_writer.writeheader()

jellyfish_soundex_results_csv = open('2D_jellyfish_soundex_results.csv', 'w', newline='')
jellyfish_soundex_writer = csv.DictWriter(jellyfish_soundex_results_csv, fieldnames=fieldnames)
jellyfish_soundex_writer.writeheader()

fuzzy_nysiis_results_csv = open('2D_fuzzy_nysiis_results.csv', 'w', newline='')
fuzzy_nysiis_writer = csv.DictWriter(fuzzy_nysiis_results_csv, fieldnames=fieldnames)
fuzzy_nysiis_writer.writeheader()

fuzzy_dmeta_results_csv = open('2D_fuzzy_dmeta_results.csv', 'w', newline='')
fuzzy_dmeta_writer = csv.DictWriter(fuzzy_dmeta_results_csv, fieldnames=fieldnames)
fuzzy_dmeta_writer.writeheader()

def reverse(name):
	rvs = ''.join(reversed(name))
	return rvs

def libindic_isEqual(name1, name2):
	instance = Soundex()
	if instance.soundex(name1) == instance.soundex(name2) or instance.soundex(reverse(name1)) == instance.soundex(reverse(name2)):
		return 1
	else:
		return 0

def jellyfish_match_rating_isEqual(name1, name2):
	if jellyfish.match_rating_codex(name1) == jellyfish.match_rating_codex(name2) or jellyfish.match_rating_codex(reverse(name1)) == jellyfish.match_rating_codex(reverse(name2)):
		return 1
	else:
		return 0
		
def jellyfish_soundex_isEqual(name1, name2):
	if jellyfish.soundex(name1) == jellyfish.soundex(name2) or jellyfish.soundex(reverse(name1)) == jellyfish.soundex(reverse(name2)):
		return 1
	else:
		return 0
		
def fuzzy_nysiis_isEqual(name1, name2):
	if fuzzy.nysiis(name1) == fuzzy.nysiis(name2) or fuzzy.nysiis(reverse(name1)) == fuzzy.nysiis(reverse(name2)):
		return 1
	else:
		return 0

def fuzzy_dmeta_isEqual(name1, name2):
	dmeta = fuzzy.DMetaphone()
	if (dmeta(name1)[0] == dmeta(name2)[0] or dmeta(name1)[0] == dmeta(name2)[1] or dmeta(reverse(name1))[1] == dmeta(reverse(name2))[0]) or (dmeta(reverse(name1))[0] == dmeta(reverse(name2))[0] or dmeta(reverse(name1))[0] == dmeta(reverse(name2))[1] or dmeta(reverse(name1))[1] == dmeta(reverse(name2))[0]):
		return 1
	else:
		return 0

		
for name1, name2 in itertools.combinations(names, 2):
	if name1 != name2:
		libindic_writer.writerow({'Name1': name1, 'Name2': name2, 'Output': libindic_isEqual(name1, name2)})
		jellyfish_match_rating_writer.writerow({'Name1': name1, 'Name2': name2, 'Output': jellyfish_match_rating_isEqual(name1, name2)})
		jellyfish_soundex_writer.writerow({'Name1': name1, 'Name2': name2, 'Output': jellyfish_soundex_isEqual(name1, name2)})
		fuzzy_nysiis_writer.writerow({'Name1': name1, 'Name2': name2, 'Output': fuzzy_nysiis_isEqual(name1, name2)})
		fuzzy_dmeta_writer.writerow({'Name1': name1, 'Name2': name2, 'Output': fuzzy_dmeta_isEqual(name1, name2)})
			
libindic_results_csv.close()
jellyfish_match_rating_results_csv.close()
jellyfish_soundex_results_csv.close()
fuzzy_nysiis_results_csv.close()
fuzzy_dmeta_results_csv.close()

'''
print(jellyfish.soundex("nasah"))
print(jellyfish.soundex("ynsuoh"))
print(jellyfish.soundex("massuh"))	
print(jellyfish.soundex("neisuoh"))
print(jellyfish.soundex("nassah"))
print(jellyfish.soundex("ayensuoh"))
print(jellyfish.soundex("anuossah"))

print(jellyfish.match_rating_codex("Hussam"))
print(jellyfish.match_rating_codex("Hussam Hallak"))
print(jellyfish.match_rating_codex("HussamHallak"))	
print(jellyfish.match_rating_codex("Hussam Aldeen"))
print(jellyfish.match_rating_codex("Hussam Aldeen Hallak"))
print(jellyfish.match_rating_codex("Ahmed"))
print(jellyfish.match_rating_codex("Sami"))



print(compareNames("Hussam", "Hasan"))
print(compareNames("Hasan", "Housny"))
print(compareNames("Hasan", "Housien"))
print(compareNames("Hassan", "Housneya"))
print(compareNames("Hasan", "Hassan"))

print("nysiis")
print(fuzzy.nysiis('nasah'))
print(fuzzy.nysiis('ynsuoh'))
print(fuzzy.nysiis('massuh'))
print(fuzzy.nysiis('neisuoh'))
print(fuzzy.nysiis('nassah'))
print(fuzzy.nysiis('ayensuoh'))
print(fuzzy.nysiis('anuossah'))


print("dmeta")
dmeta = fuzzy.DMetaphone(8)
print(dmeta('Hasan'))
print(dmeta('Housny'))
print(dmeta('Hussam'))
print(dmeta('Housien'))
print(dmeta('Hassan'))
print(dmeta('Housneya'))
print(dmeta('Hassouna'))

print("dmeta")
dmeta = fuzzy.DMetaphone(5)
print(dmeta('nasah'))
print(dmeta('ynsuoh'))
print(dmeta('massuh'))
print(dmeta('neisuoh'))
print(dmeta('nassah'))
print(dmeta('ayensuoh'))
print(dmeta('anuossah'))


print("soundex")
soundex = fuzzy.Soundex(4)
print(soundex('Hasan'))
print(soundex('Hassan'))

print("dmeta")
dmeta = fuzzy.DMetaphone()
print(dmeta('Hasan'))
print(dmeta('Hassan'))

print(jellyfish.soundex(u'Jellyfish'))

def libindic_compareNames(name1, name2):
	instance = Soundex()
	if instance.compare(name1, name2) in [0,1, 2]:
		return 1
	else:
		return 0
		
		print("dmeta")
'''
