# BLAST Alignment Tool (BioPython)

## 🧬 Overview
This project performs alignment for an input sequence using BLAST via BioPython.  
It automatically detects the biological type of a sequence (DNA, RNA, or Protein)  
and runs the appropriate BLAST program against NCBI’s databases.

The program sends the query sequence online to NCBI servers, retrieves the best matches,  
and reports detailed alignment results including matched sequence titles, scores, and E-values.  
All results are saved locally for reference and analysis.

---

## ⚙️ Key Features
- Automatic sequence type detection (DNA, RNA, or Protein)
- Dynamic BLAST selection — uses `blastn` for nucleotides and `blastp` for proteins
- Online integration with NCBI’s BLAST servers using `Bio.Blast.NCBIWWW`
- Automated XML parsing with `Bio.Blast.NCBIXML` to extract alignment data
- Clean output showing matched sequence titles, scores, and E-values
- Top 5 alignments displayed in both console and saved in a `.txt` file
- Lightweight implementation — single Python script, easy to run and modify

---

## 📦 Requirements
Install the required libraries before running the script:
```bash
pip install biopython requests

---

🚀 How to Use
1. Clone the repository
git clone https://github.com/your-username/your-repo-name.git        (هظبطها)

2. Run the script
python blast_alignment_online.py

3. Enter your sequence when prompted
4. The alignment results will be saved in blast_results.txt


---
🧪 Example

Input:
ATGCGTACGTAGCTAG


Output:
Detected sequence type: DNA
Running blastn against nt database... please wait

Matched Sequences and Scores:

Matched Sequence Title: gi|123456| Example Sequence
Score: 180
E-value: 2e-50
----------------------------------------------------------------------

Results saved in 'blast_output.txt'


---

📁 Project Structure
.
├── src/
│   └── blast_alignment_online.py     # Main script
├── blast_results.txt                 # Output file
├── README.md                         # Project documentation
└── requirements.txt                  # Dependencies

---

🔮 Future Improvements:
Add graphical interface for easier use
Include multiple input sequences in one run
Support for local BLAST databases
Add summary statistics for matches

---


👩‍💻 Author
  Fatma Elnbawy 
[LinkedIn Profile](https://www.linkedin.com/in/fatma-elnbawy)