import streamlit as st #for web dev
from aitextgen import aitextgen #for ai text gen
import googletrans
#from pprint import pprint

st.title("TEXT GEN")

# instantiate the model / download
ai = aitextgen()

# Initial
translator = googletrans.Translator()

# create a prompt text for the text generation 
col1,col2 = st.beta_columns(2)
with col1:
    prompt_text = st.text_input(label = "Enter your Chinese prompt text...", value = "哈利波特")
with col2:
    m_length = st.number_input("Length", min_value=1, step=1)        

if st.button('Generate'):
    with st.spinner("AI is Working~"):
        e_results = translator.translate(prompt_text, dest='us').text
        gpt_text = ai.generate_one(prompt=e_results,
            max_length = m_length )
#st.success("AI Successfully generated the below text ")
    st.success(gpt_text)
   

    # Basic Translate
    #results = translator.translate('我覺得今天天氣不好。')
    results = translator.translate(gpt_text, dest='zh-tw').text
    st.text(results)
    #st.balloons()
    # print ai generated text
    #print(gpt_text)

    #st.text(gpt_text)





