import streamlit as st
from transformers import pipeline

# use t5 in tf
summarizer = pipeline("summarization", model="google-t5/t5-base", tokenizer="google-t5/t5-base", framework="tf")



def main():

    st.title("Automated Text Summarizer App")

    min = st.sidebar.slider('Minimum words',min_value = 10,max_value = 50)  
    max = st.sidebar.slider('Maximum words',min_value = 50,max_value = 100) 

    # Text Input
    input_text = st.text_area("Enter text here",height=200)

    if st.button('summarize'):
        if input_text:
            with st.spinner("Generating summary..."):
                summary = summarizer(input_text,min_length= min, max_length= max)
                st.write(summary[0]['summary_text'])
        
        else:
            st.warning("Please enter some text to summarize.")



if __name__ == "__main__":
    main()


