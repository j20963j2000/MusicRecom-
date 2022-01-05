
import streamlit as st
from SPARQLWrapper import SPARQLWrapper
from streamlit_agraph import agraph, Node, Edge, Config, TripleStore


graph = Graph()
graph.parse("http://www.w3.org/People/Berners-Lee/card")
store = TripleStore()

for subj, pred, obj in graph:
    store.add_triple(subj, pred, obj, "")
    
agraph(list(store.getNodes()), list(store.getEdges()), config)