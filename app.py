import streamlit as st #for web dev
from aitextgen import aitextgen #for ai text gen
import googletrans
#from pprint import pprint

st.title("TEXT GEN")

# instantiate the model / download
ai = aitextgen()

# create a prompt text for the text generation 
col1,col2 = st.beta_columns(2)
with col1:
    prompt_text = st.text_input(label = "Enter your prompt text...", value = "The point is")
with col2:
    m_length = st.number_input("Length", min_value=1, step=1)        

if st.button('Generate'):
    with st.spinner("AI is Working~"):
        # text generation
        gpt_text = ai.generate_one(prompt=prompt_text,
            max_length = m_length )
#st.success("AI Successfully generated the below text ")
    st.success(gpt_text)
#st.balloons()
# print ai generated text
#print(gpt_text)

#st.text(gpt_text)




# Initial
translator = googletrans.Translator()


# Basic Translate
results = translator.translate('我覺得今天天氣不好。')
st.text(results)
