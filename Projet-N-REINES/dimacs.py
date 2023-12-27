import sys

def calc_clauses_diag(n):
    diag_cote = n-2
    nb_clauses = 0

    # calcul du nombre de clauses dans les diagonales en dessous de la diagonale principale
    for i in range(1, diag_cote+1):  
        el_diag = n - i
        for el in range(1, el_diag):
            nb_clauses += el

    # nombre de clauses avec les diagonales au dessus de la diag principale
    nb_clauses = nb_clauses*2 

    # nombre de clauses dans la diagonale principale
    for i in range(1, n):
        nb_clauses += i

    # x2 pour les diagonales ascendantes et descendantes
    nb_clauses = nb_clauses*2

    return nb_clauses

def calc_clauses(n):
    nb_clauses = 0

    # maximum 1 reine par ligne
    for i in range(1, n):
        nb_clauses += i
    nb_clauses = nb_clauses*n

    # maximum 1 reine par colonne
    nb_clauses = nb_clauses*2

    # minimum 1 reine par ligne et par colonne
    nb_clauses += 2*n 

    nb_clauses += calc_clauses_diag(n)

    return nb_clauses

def main():
    if len(sys.argv) != 2:
        sys.exit(f"usage: python {sys.argv[0]} <entree.txt>\n")

    file_name = sys.argv[1]
    entree = open(file_name, "r")

    taille = entree.readline().split()
    taille = int(taille[0])

    nb_variables = taille**2

    nb_reines = entree.readline().split()
    nb_reines = int(nb_reines[0])

    nb_clauses = calc_clauses(taille)
    nb_clauses += nb_reines

    reinesL = []

    for n in range(nb_reines):
        position = entree.readline().split()
        position = int(position[0])
        reinesL.append(position)


    dimacs = open("dimacs.txt", "w")
    dimacs.write(f"p cnf {nb_variables} {nb_clauses}\n")

    # Reines déjà en place
    if nb_reines != 0:
        dimacs.write("c reines donnees en entree\n")
    for el in reinesL:
        dimacs.write(f"{el} 0\n")
    
    # Minimum 1 reine par ligne 
    dimacs.write("c minimum une reine par ligne \n")
    for i in range(taille):
        for j in range(1, taille+1):
            variable = i*taille + j
            if j < taille:
                dimacs.write(f"{variable} ")
            else:
                dimacs.write(f"{variable} 0\n")

    # Maximum 1 reine par ligne
    dimacs.write("c maximum une reine par ligne \n")
    for i in range(taille):
        for j in range(1, taille+1):
            for n in range(j+1, taille+1):
                variable1 = i*taille + j
                variable2 = i*taille + n
                dimacs.write(f"-{variable1} -{variable2} 0\n")

    # Minimum 1 reine par colonne
    dimacs.write("c minimum une reine par colonne \n")
    for j in range(1, taille+1):
        for i in range(taille):
            variable = i*taille + j
            if i < taille - 1:
                dimacs.write(f"{variable} ")
            else:
                dimacs.write(f"{variable} 0\n")
    
    # Maximum 1 reine par colonne
    dimacs.write("c maximum une reine par colonne \n")
    for j in range(1, taille+1):
        for i in range(taille):
            for n in range(i+1, taille):
                variable1 = i*taille + j
                variable2 = n*taille + j
                dimacs.write(f"-{variable1} -{variable2} 0\n")
             
    # Maximum 1 reine par diagonale ascendante
    dimacs.write("c maximum une reine par diagonale ascendante \n")   
    for i in range(taille):
        for j in range(taille):
            for k in range(1, taille - max(i, j)):
                variable1 = (i * taille) + j + 1
                variable2 = ((i + k) * taille) + j + k + 1
                dimacs.write(f"-{variable1} -{variable2} 0\n")
    
    # Maximum 1 reine par diagonale descendante
    dimacs.write("c maximum une reine par diagonale descendante \n")
    for i in range(taille):
        for j in range(taille):
            for k in range(1, min(i + 1, taille - j)):
                variable1 = (i * taille) + j + 1
                variable2 = ((i - k) * taille) + j + k + 1
                dimacs.write(f"-{variable1} -{variable2} 0\n")

    dimacs.close()

if __name__ == "__main__":
    main()