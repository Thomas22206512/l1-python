#projet == Création d'un programme qui es un fast finger mais version pokémon
import random

caract_maj = "AZERTYUIOPQSDFGHJKLMWXCVBN"
caract_min = "azertyuiopqsdfghjklmwxcvbn"
caract_chif = "1234567890"
caract_spe = "!#*%:"

caractere = caract_chif + caract_maj + caract_min + caract_spe
length_for_pass = 12

passwords = "".join(random.sample(caractere, length_for_pass))
print(f"Le mots de passe est : {passwords}")
