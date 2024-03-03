def get_hamming_distance(dna1, dna2):
    
    if len(dna1) != len(dna2):
        hamming_distance = 0
        for i in range(len(dna1)):
            if dna1[i] != dna2[i]:
                hamming_distance += 1        
        return hamming_distance

def get_dna_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    dna = ''
    for base in reversed(dna):
        if base in complement:
            complement_dna += complement[base]
        else:
            dna += base

    return complement_dna

#dna1 = "GAGCCTACTAACGGGAT"
#dna2 = "CATCGTAATGACGGCCT"

#print("Hamming distance:", get_hamming_distance(dna1, dna2))
#print("Reverse complement of dna1:", get_dna_complement(dna1))
#print("Reverse complement of dna2:", get_dna_complement(dna2))
def menu():
    print("Menu:")
    print("1-Hamming Distance")
    print("2-DNA Complement")
    print("3-Exit")
    choice = input("Enter your choice (1, 2, or 3): ")
    return choice

def Hamming_Distance_1():
    dna1 = input("Enter the first DNA string: ")
    dna2 = input("Enter the second DNA string: ")
    distance = get_hamming_distance(dna1, dna2)
    print(f"The Hamming distance between {dna1} and {dna2} is: {distance}")

def DNA_Complement_2():
    dna = input("Enter the DNA string: ")
    complement = get_dna_complement(dna)
    print(f"The DNA complement of {dna} is: {complement}")

while True:
    choice = menu()
    if choice == '1':
        Hamming_Distance_1()
    elif choice == '2':
        pass
    elif choice == '3':
        print("Exiting")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")