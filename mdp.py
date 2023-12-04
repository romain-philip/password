import re

def check_password_strength(password):
    # Vérifier la longueur du mot de passe
    if len(password) < 8:
        return "Le mot de passe doit contenir au moins 8 caractères."

    # Vérifier la présence de chiffres
    if not re.search(r"\d", password):
        return "Le mot de passe doit contenir au moins un chiffre."

    # Vérifier la présence de lettres minuscules
    if not re.search(r"[a-z]", password):
        return "Le mot de passe doit contenir au moins une lettre minuscule."

    # Vérifier la présence de lettres majuscules
    if not re.search(r"[A-Z]", password):
        return "Le mot de passe doit contenir au moins une lettre majuscule."

    # Vérifier la présence de caractères spéciaux
    if not re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~""]", password):
        return "Le mot de passe doit contenir au moins un caractère spécial."

    return "Le mot de passe est suffisamment sécurisé."

# Demander à l'utilisateur de saisir un mot de passe
password = input("Entrez un mot de passe : ")

# Vérifier la force du mot de passe
result = check_password_strength(password)

# Afficher le résultat
print(result)