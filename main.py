from Bio import SeqIO

def calculer_frequences_nucleotides(chemin_fichier):
    sequences = SeqIO.parse(chemin_fichier, "fasta")

    for sequence in sequences:
        print(f"Séquence : {sequence.id}")
        counts = { 'A': 0, 'T': 0, 'C': 0, 'G': 0 }

        for nucleotide in sequence.seq:
            counts[nucleotide] += 1

        total = sum(counts.values())
        print(f"Fréquence des nucléotides :")
        for nucleotide, count in counts.items():
            frequency = (count / total) * 100
            print(f"{nucleotide}: {frequency:.2f}%")

# Utilisation de la fonction avec un fichier FASTA spécifique
chemin_fichier = 'votre_fichier.fasta'
calculer_frequences_nucleotides(chemin_fichier)
