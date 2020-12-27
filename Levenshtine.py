from fuzzywuzzy import fuzz

def sim_score(str1, str2):
	ratio = fuzz.ratio(str1.lower(),str2.lower())
	return ratio
	
	 
	

print("score (", "Muhammed", ",", "Mohamed", ") =" , sim_score("Muhammed", "Mohamed"), "same")
print("score (", "Muhammad", ",", "Mohammed", ") =" , sim_score("Muhammad", "Mohammed"), "same")
print("score (", "Mohamad", ",", "Muhammed", ") =" , sim_score("Mohamad", "Muhammed"), "same")	
print("score (", "Abdel aziz", ",", "Abdul aziz", ") =" , sim_score("Abdel aziz", "Abdul aziz"), "same")
print("score (", "Raqia", ",", "Rakia", ") =" , sim_score("Raqia", "Rakia"), "same")
print("score (", "Hiba", ",", "Heba", ") =" , sim_score("Hiba", "Heba"), "same")
print("score (", "Ahmed", ",", "Ahmad", ") =" , sim_score("Ahmed", "Ahmad"), "same")
print("score (", "Noor", ",", "Nour", ") =" , sim_score("Noor", "Nour"), "same")
print("score (", "Hamid", ",", "Hameed", ") =" , sim_score("Hamid", "Hameed"), "same")
print("score (", "Hamid", ",", "Hamed", ") =" , sim_score("Hamid", "Hamed"), "same")
print("score (", "Fatima", ",", "Fatema", ") =" , sim_score("Fatima", "Fatema"), "same")
print("score (", "Hussam", ",", "Hosam", ") =" , sim_score("Hussam", "Hosam"), "same")
print("score (", "Husam", ",", "Houssam", ") =" , sim_score("Husam", "Houssam"), "same")
print("score (", "Hussam", ",", "Housam", ") =" , sim_score("Hussam", "Housam"), "same")
print("score (", "Hussam", ",", "Houssam", ") =" , sim_score("Hussam", "Houssam"), "same")
print("score (", "Widad", ",", "Widad", ") =" , sim_score("Widad", "Widad"), "same")
print("-----------------")
print("score (", "Widad", ",", "Noor", ") =" , sim_score("Widad", "Noor"), "not same")
print("score (", "Widad", ",", "Wael", ") =" , sim_score("Widad", "Wael"), "not same")
print("score (", "Widad", ",", "Waleed", ") =" , sim_score("Widad", "Waleed"), "not same")
print("score (", "Abdul aziz", ",", "Abdul rahman", ") =" , sim_score("Abdul aziz", "Abdul rahman"), "not same")
print("score (", "Esam", ",", "Husam", ") =" , sim_score("Esam", "Husam"), "not same")
print("score (", "Wesam", ",", "Husam", ") =" , sim_score("Wesam", "Husam"), "not same")
print("score (", "Wesam", ",", "Esam", ") =" , sim_score("Wesam", "Esam"), "not same")
print("score (", "Hussam", ",", "Hassan", ") =" , sim_score("Hussam", "Hassan"), "not same")
print("score (", "Hasan", ",", "Hassan", ") =" , sim_score("Hasan", "Hassan"), "not same")
print("score (", "Eman", ",", "Emad", ") =" , sim_score("Eman", "Emad"), "not same")
print("score (", "Hussam Hallak", ",", "Hussam Masri", ") =" , sim_score("Hussam Hallak", "Hussam Masri"), "not same")
print("score (", "Muhammed", ",", "Muhanned", ") =" , sim_score("Muhammed", "Muhanned"), "not same")
