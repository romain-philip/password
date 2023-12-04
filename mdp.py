import re

def check_password_strength(password):
  
    if len(password) < 8:
        return "Le mot de passe doit contenir au moins 8 caractères."

  
    if not re.search(r"\d", password):
        return "Le mot de passe doit contenir au moins un chiffre."

  
    if not re.search(r"[a-z]", password):
        return "Le mot de passe doit contenir au moins une lettre minuscule."

   
    if not re.search(r"[A-Z]", password):
        return "Le mot de passe doit contenir au moins une lettre majuscule."

   
    if not re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~""]", password):
        return "Le mot de passe doit contenir au moins un caractère spécial."

    return "Le mot de passe est suffisamment sécurisé."


password = input("Entrez un mot de passe : ")

# Vérifier la force du mot de passe
result = check_password_strength(password)

# Afficher le résultat
print(result)
