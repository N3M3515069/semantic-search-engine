import streamlit as st
from search import search

st.title("Semantic Search Engine")
st.write("Search though documents using meanings not just words")

query = st.text_input("Enter your search query: ")

if query:
    results = search(query)
    st.subheader(f"Top {len(results)} Results:")
    for i, result in enumerate(results):
        st.markdown(f"**Result  {i + 1}:**")
        st.write(result['text'])
        st.caption(f"Distance score: {result['distance']:.4f}")
        st.divider()