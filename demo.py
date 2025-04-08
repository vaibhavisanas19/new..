import streamlit as st
from Bio import AlignIO, Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
import matplotlib.pyplot as plt
from io import StringIO

# Streamlit App Title
st.title("Phylogenetic Tree Generator")

# Sequence Input
st.header("Enter Sequences in FASTA Format")
sequences_input = st.text_area("Input your aligned DNA/protein sequences below:",
""">Seq1
ATCGTACGATCG
>Seq2
ATGGTACGATCA
>Seq3
ATCGTACGCTCG
""", height=200)

# Generate Tree Button
if st.button("Generate Phylogenetic Tree"):
    try:
        # Convert input string to a file-like object
        fasta_io = StringIO(sequences_input)

        # Read sequences into alignment object
        alignment = AlignIO.read(fasta_io, "fasta")

        # Compute distance matrix
        calculator = DistanceCalculator('identity')
        distance_matrix = calculator.get_distance(alignment)

        # Construct tree using Neighbor-Joining method
        constructor = DistanceTreeConstructor()
        tree = constructor.nj(distance_matrix)

        # Plot the tree
        fig, ax = plt.subplots(figsize=(6, 6))
        Phylo.draw(tree, axes=ax)

        # Display in Streamlit
        st.pyplot(fig)

    except Exception as e:
        st.error(f"An error occurred: {e}")
