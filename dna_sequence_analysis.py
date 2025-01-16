# Función para convertir una secuencia de ADN en codones
def dna_to_codons(dna_sequence):
    dna_sequence = dna_sequence.upper()  # Convertir a mayúsculas
    if len(dna_sequence) % 3 != 0:
        print("Advertencia: la secuencia no tiene una longitud múltiplo de 3.")
    codons = [dna_sequence[i:i+3] for i in range(0, len(dna_sequence), 3)]
    return codons

# Diccionario de codones a aminoácidos
codon_to_aminoacid = {
    "ATA": "I", "ATC": "I", "ATT": "I", "ATG": "M",  # I: Isoleucina, M: Metionina
    "ACA": "T", "ACC": "T", "ACG": "T", "ACT": "T",  # T: Treonina
    "AAC": "N", "AAT": "N", "AAA": "K", "AAG": "K",  # N: Asparagina, K: Lisina
    "AGC": "S", "AGT": "S", "AGA": "R", "AGG": "R",  # S: Serina, R: Arginina
    "CTA": "L", "CTC": "L", "CTG": "L", "CTT": "L",  # L: Leucina
    "CCA": "P", "CCC": "P", "CCG": "P", "CCT": "P",  # P: Prolina
    "GCA": "A", "GCC": "A", "GCG": "A", "GCT": "A",  # A: Alanina
    "GAC": "D", "GAT": "D", "GAA": "E", "GAG": "E",  # D: Ácido aspártico, E: Ácido glutámico
    "GGA": "G", "GGC": "G", "GGG": "G", "GGT": "G",  # G: Glicina
    "TCA": "S", "TCC": "S", "TCG": "S", "TCT": "S",  # S: Serina
    "TTC": "F", "TTT": "F", "TTA": "L", "TTG": "L",  # F: Fenilalanina
    "TAC": "Y", "TAT": "Y", "TAA": "X", "TAG": "X",  # Y: Tirosina, X: Codón de paro
    "TGC": "C", "TGT": "C", "TGA": "X", "TGG": "W",  # C: Cisteína, W: Triptófano
    "CGC": "R", "CGG": "R", "CGA": "R", "CGT": "R",  # R: Arginina
}

# Función para convertir los codones en aminoácidos
def codons_to_aminoacids(codons):
    amino_acids = []
    for codon in codons:
        if codon in codon_to_aminoacid:
            amino_acids.append(codon_to_aminoacid[codon])
        else:
            amino_acids.append('X')  # Si el codón no está en el diccionario, marcamos como 'X' (desconocido)
    return amino_acids

# Función para contar la frecuencia de nucleótidos en una secuencia de ADN
def nucleotide_frequency(dna_sequence):
    dna_sequence = dna_sequence.upper()  # Convertir a mayúsculas
    frequency = {"A": 0, "T": 0, "C": 0, "G": 0, "Desconocidos": 0}
    for nucleotide in dna_sequence:
        if nucleotide in frequency:
            frequency[nucleotide] += 1
        else:
            frequency["Desconocidos"] += 1  # Contar nucleótidos desconocidos
    return frequency

# Función para convertir una secuencia de ADN a ARN
def dna_to_rna(dna_sequence):
    dna_sequence = dna_sequence.upper()  # Convertir a mayúsculas
    return dna_sequence.replace("T", "U")

# Función para comparar dos secuencias de ADN
def compare_sequences(dna_sequence1, dna_sequence2):
    # Convertir las secuencias de ADN a codones y luego a aminoácidos
    codons1 = dna_to_codons(dna_sequence1)
    codons2 = dna_to_codons(dna_sequence2)

    amino_acids1 = codons_to_aminoacids(codons1)
    amino_acids2 = codons_to_aminoacids(codons2)

    # Comparar los aminoácidos
    synonymous = 0
    nonsynonymous = 0
    differences = []

    for aa1, aa2 in zip(amino_acids1, amino_acids2):
        if aa1 == aa2:
            synonymous += 1
        else:
            nonsynonymous += 1
            differences.append((aa1, aa2))

    # Mostrar resultados
    print(f"Diferencias sinónimas: {synonymous}")
    print(f"Diferencias no sinónimas: {nonsynonymous}")
    print("Diferencias (si las hay):")
    for diff in differences:
        print(f"De {diff[0]} a {diff[1]}")

# Pedir las secuencias de ADN al usuario
dna_sequence1 = input("Escribe la primera secuencia de ADN: ")
dna_sequence2 = input("Escribe la segunda secuencia de ADN: ")

# Comparar las secuencias
compare_sequences(dna_sequence1, dna_sequence2)

# Convertir la primera secuencia a codones y luego a aminoácidos
codons1 = dna_to_codons(dna_sequence1)
amino_acids1 = codons_to_aminoacids(codons1)
# Convertir la segunda secuencia a codones y luego a aminoácidos
codons2 = dna_to_codons(dna_sequence2)
amino_acids2 = codons_to_aminoacids(codons2)

# Imprimir los aminoácidos correspondientes a la primera secuencia
print("Aminoácidos correspondientes a la primera secuencia de ADN:")
print(' '.join(amino_acids1))
# Imprimir los aminoácidos correspondientes a la segunda secuencia de ADN
print("Aminoácidos correspondientes a la segunda secuencia de ADN:")
print(' '.join(amino_acids2))

# Contar la frecuencia de nucleótidos en la primera secuencia de ADN
frequency1 = nucleotide_frequency(dna_sequence1)
print("Frecuencia de nucleótidos en la primera secuencia de ADN:", frequency1)
# Contar la frecuencia de nucleótidos en la segunda secuencia de ADN
frequency2 = nucleotide_frequency(dna_sequence2)
print("Frecuencia de nucleótidos en la segunda secuencia de ADN:", frequency2)

# Convertir las secuencias de ADN a ARN
rna_sequence1 = dna_to_rna(dna_sequence1)
rna_sequence2 = dna_to_rna(dna_sequence2)
print("Primera secuencia de ADN convertida a ARN:", rna_sequence1)
print("Segunda secuencia de ADN convertida a ARN:", rna_sequence2)