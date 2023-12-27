import sys

def main():
    if len(sys.argv) != 2:
        sys.exit(f"usage: python {sys.argv[0]} <solution.txt>\n")

    file_name = sys.argv[1]
    f = open(file_name, "r")

    taille = f.readline().split()
    taille = int(taille[0])

    liste = f.readline().split()
    solutions = []

    for el in liste:
        el = int(el)
        if el > 0:
            solutions.append(el)

    interface = open("interface.txt", "w")

    n = 1
    for i in range(taille):
        for j in range(taille):
            interface.write("+ -- ")
        interface.write("+\n")
        for j in range(taille):
            interface.write("|")
            if n in solutions:
                interface.write(" RR ")
            else:
                interface.write("    ")
            n += 1
        interface.write("|\n")
    for i in range(taille):
        interface.write("+ -- ")
    interface.write("+\n")

    interface.close()

if __name__ == "__main__":
    main()