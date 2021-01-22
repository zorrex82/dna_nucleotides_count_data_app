# Data App build by: Edinor Junior
# Import libraries
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

image = Image.open('dna-logo.jpg')

st.image(image, use_columnn_width=True)

st.markdown("Project based on Course developed by Chanin Nantasenamat (aka Data Professor).")

st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA!

***

""")

st.header("Enter DNA sequence")

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG" \
                 "\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC" \
                 "\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT "

sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

st.write("""
***
""")

# Prints the input DNA Sequence
st.header("INPUT (DNA Query)")
sequence

# DNA nucleotide Count
st.header("OUTPUT (DNA Nucleotide Count)")

# 1. Print dictionary
st.subheader('1. Print dictionary')


def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count("A")),
        ('T', seq.count("T")),
        ('G', seq.count("G")),
        ('C', seq.count("C"))
    ])
    return d


X = DNA_nucleotide_count(sequence)

X_label = list(X)
X_values = list(X.values())

X

# 2. Print text
st.subheader('2. Print text')
st.write('There are ' + str(X['A']) + ' adenine (A)')
st.write('There are ' + str(X['T']) + ' thymine (T)')
st.write('There are ' + str(X['G']) + ' guanine (G)')
st.write('There are ' + str(X['C']) + ' cytosine (C)')

# 3. Display Dataframe
st.subheader('3. Display Dataframe')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index': 'nucleotide'})
st.write(df)

# 4. Display Bar Char using Altair
st.subheader('4. Display Bar chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80)
)
st.write(p)

bars = alt.Chart(df).mark_bar().encode(
    x='count',
    y="nucleotide"
)

text = bars.mark_text(
    align='left',
    baseline='middle',
    dx=3  # Nudges text to right so it doesn't appear on top of the bar
).encode(
    text='nucleotide'
)

f = (bars + text).properties(height=200, width=400)
st.write(f)
