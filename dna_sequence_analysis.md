# Función para convertir una secuencia de ADN en codones
function dna_to_codons(dna_sequence::String)
    dna_sequence = uppercase(dna_sequence)  # Convertir a mayúsculas
    if length(dna_sequence) % 3 != 0
        println("Advertencia: la secuencia no tiene una longitud múltiplo de 3.")
    end
    codons = [dna_sequence[i:i+2] for i in 1:3:length(dna_sequence)]
    return codons
end

# Diccionario de codones a aminoácidos
codon_to_aminoacid = Dict(
    "ATA" => "I", "ATC" => "I", "ATT" => "I", "ATG" => "M",  # I: Isoleucina, M: Metionina
    "ACA" => "T", "ACC" => "T", "ACG" => "T", "ACT" => "T",  # T: Treonina
    "AAC" => "N", "AAT" => "N", "AAA" => "K", "AAG" => "K",  # N: Asparagina, K: Lisina
    "AGC" => "S", "AGT" => "S", "AGA" => "R", "AGG" => "R",  # S: Serina, R: Arginina
    "CTA" => "L", "CTC" => "L", "CTG" => "L", "CTT" => "L",  # L: Leucina
    "CCA" => "P", "CCC" => "P", "CCG" => "P", "CCT" => "P",  # P: Prolina
    "GCA" => "A", "GCC" => "A", "GCG" => "A", "GCT" => "A",  # A: Alanina
    "GAC" => "D", "GAT" => "D", "GAA" => "E", "GAG" => "E",  # D: Ácido aspártico, E: Ácido glutámico
    "GGA" => "G", "GGC" => "G", "GGG" => "G", "GGT" => "G",  # G: Glicina
    "TCA" => "S", "TCC" => "S", "TCG" => "S", "TCT" => "S",  # S: Serina
    "TTC" => "F", "TTT" => "F", "TTA" => "L", "TTG" => "L",  # F: Fenilalanina
    "TAC" => "Y", "TAT" => "Y", "TAA" => "X", "TAG" => "X",  # Y: Tirosina, X: Codón de paro
    "TGC" => "C", "TGT" => "C", "TGA" => "X", "TGG" => "W",  # C: Cisteína, W: Triptófano
    "CGC" => "R", "CGG" => "R", "CGA" => "R", "CGT" => "R"   # R: Arginina
)

# Función para convertir los codones en aminoácidos
function codons_to_aminoacids(codons::Vector{String})
    amino_acids = String[]
    for codon in codons
        if haskey(codon_to_aminoacid, codon)
            push!(amino_acids, codon_to_aminoacid[codon])
        else
            push!(amino_acids, 'X')  # Si el codón no está en el diccionario, marcamos como 'X' (desconocido)
        end
    end
    return amino_acids
end

# Función para contar la frecuencia de nucleótidos en una secuencia de ADN
function nucleotide_frequency(dna_sequence::String)
    dna_sequence = uppercase(dna_sequence)  # Convertir a mayúsculas
    frequency = Dict("A" => 0, "T" => 0, "C" => 0, "G" => 0, "Desconocidos" => 0)
    for nucleotide in dna_sequence
        if haskey(frequency, string(nucleotide))
            frequency[string(nucleotide)] += 1
        else
            frequency["Desconocidos"] += 1  # Contar nucleótidos desconocidos
        end
    end
    return frequency
end

# Función para convertir una secuencia de ADN a ARN
function dna_to_rna(dna_sequence::String)
    dna_sequence = uppercase(dna_sequence)  # Convertir a mayúsculas
    return replace(dna_sequence, "T" => "U")
end

# Función para comparar dos secuencias de ADN
function compare_sequences(dna_sequence1::String, dna_sequence2::String)
    # Convertir las secuencias de ADN a codones y luego a aminoácidos
    codons1 = dna_to_codons(dna_sequence1)
    codons2 = dna_to_codons(dna_sequence2)

    amino_acids1 = codons_to_aminoacids(codons1)
    amino_acids2 = codons_to_aminoacids(codons2)

    # Comparar los aminoácidos
    synonymous = 0
    nonsynonymous = 0
    differences = []

    for (aa1, aa2) in zip(amino_acids1, amino_acids2)
        if aa1 == aa2
            synonymous += 1
        else
            nonsynonymous += 1
            push!(differences, (aa1, aa2))
        end
    end

    # Mostrar resultados
    println("Diferencias sinónimas: $synonymous")
    println("Diferencias no sinónimas: $nonsynonymous")
    println("Diferencias (si las hay):")
    for diff in differences
        println("De $(diff[1]) a $(diff[2])")
    end
end

# Pedir las secuencias de ADN al usuario
println("Escribe la primera secuencia de ADN: ")
dna_sequence1 = readline()
println("Escribe la segunda secuencia de ADN: ")
dna_sequence2 = readline()

# Comparar las secuencias
compare_sequences(dna_sequence1, dna_sequence2)

# Convertir la primera secuencia a codones y luego a aminoácidos
codons1 = dna_to_codons(dna_sequence1)
amino_acids1 = codons_to_aminoacids(codons1)
# Convertir la segunda secuencia a codones y luego a aminoácidos
codons2 = dna_to_codons(dna_sequence2)
amino_acids2 = codons_to_aminoacids(codons2)

# Imprimir los aminoácidos correspondientes a la primera secuencia
println("Aminoácidos correspondientes a la primera secuencia de ADN:")
println(join(amino_acids1, " "))
# Imprimir los aminoácidos correspondientes a la segunda secuencia de ADN
println("Aminoácidos correspondientes a la segunda secuencia de ADN:")
println(join(amino_acids2, " "))

# Contar la frecuencia de nucleótidos en la primera secuencia de ADN
frequency1 = nucleotide_frequency(dna_sequence1)
println("Frecuencia de nucleótidos en la primera secuencia de ADN: ", frequency1)
# Contar la frecuencia de nucleótidos en la segunda secuencia de ADN
frequency2 = nucleotide_frequency(dna_sequence2)
println("Frecuencia de nucleótidos en la segunda secuencia de ADN: ", frequency2)

# Convertir las secuencias de ADN a ARN
rna_sequence1 = dna_to_rna(dna_sequence1)
rna_sequence2 = dna_to_rna(dna_sequence2)
println("Primera secuencia de ADN convertida a ARN: ", rna_sequence1)
println("Segunda secuencia de ADN convertida a ARN: ", rna_sequence2)