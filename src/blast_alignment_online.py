from Bio.Blast import NCBIWWW, NCBIXML

# Detect sequence type (DNA, RNA, or Protein)
def detect_sequence_type(seq):
    seq = seq.upper()
    if set(seq) <= {"A", "T", "G", "C"}:
        return "DNA"
    elif set(seq) <= {"A", "U", "G", "C"}:
        return "RNA"
    elif set(seq) <= {"A","R","N","D","C","E","Q","G","H","I","L","K","M","F","P","S","T","W","Y","V"}:
        return "PROTEIN"
    else:
        return "UNKNOWN"

# Input sequence
sequence = input("Enter your sequence: ").strip().upper()

# Identify type
seq_type = detect_sequence_type(sequence)
print(f"Detected sequence type: {seq_type}")

# Select BLAST program and database
if seq_type == "DNA":
    program, database = "blastn", "nt"
elif seq_type == "RNA":
    program, database = "blastn", "nt"
elif seq_type == "PROTEIN":
    program, database = "blastp", "nr"
else:
    print("Unknown sequence type.")
    exit()

# Run BLAST online
print(f"Running {program} against {database} database... please wait")
result_handle = NCBIWWW.qblast(program=program, database=database, sequence=sequence)

# Parse XML result
blast_record = NCBIXML.read(result_handle)

# Write output to file
with open("blast_output.txt", "w", encoding="utf-8") as out_file:
    if not blast_record.alignments:
        print("No matches found.")
        out_file.write("No matches found.\n")
    else:
        print("\nMatched Sequences and Scores:\n")
        out_file.write("Matched Sequences and Scores:\n\n")
        for alignment in blast_record.alignments[:5]:
            for hsp in alignment.hsps:
                line = (
                    f"Matched Sequence Title: {alignment.title}\n"
                    f"Score: {hsp.score}\n"
                    f"E-value: {hsp.expect}\n"
                    + "-" * 70 + "\n"
                )
                print(line)
                out_file.write(line)

print("\nResults saved in 'blast_output.txt'")
