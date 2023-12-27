import streamlit as st
import openai
import numpy as np
import docx2txt
import pandas as pd
from PyPDF2 import PdfReader
import textwrap
import time


def generate_notes(textBit):
    openai.api_key = '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'
    text = "Generate notes in bullet format regarding the content of the text that you are provided. Be sure to include important information, key terms and their explanations, and summaries. ALL RESPONSES MUST BE LESS THAN 2000 CHARACTERS. Bold all key terms and paper titles. ONLY GENERATE 1 KEY BULLET POINT. ONLY USE BULLET POINTS TO FORMAT NOT DASHES(Sub-Bullets are allowed). Here is the text: " + textBit
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt = text,
        max_tokens= 444,
        temperature= 0
    )
    # print(response)
    note = response["choices"][0]["text"]
    print(note)
    return note


def control(file):
    reader = PdfReader(file)
    text = ""
    for pageNum in range(len(reader.pages)):
        page = reader.pages[pageNum]
        text += page.extract_text()
    chunks = textwrap.wrap(text, 10000)
    notes = ""
    count = 0
    for chunk in chunks:
        count += 1
        notes += generate_notes(chunk)
        time.sleep(18)
    
    print("FINAL: \n" + notes)
    return notes

with st.form("File Upload"):   
    # st.header('Multiple File Upload')
    uploaded_files = st.file_uploader('Upload your files')
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write(control(uploaded_files))
        
