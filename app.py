import streamlit as st #for web dev
from aitextgen import aitextgen #for ai text gen

st.title("TEXTGEN App")

# instantiate the model / download
ai = aitextgen()

# create a prompt text for the text generation 
col1,col2 = st.beta_columns(2)
with col1:
    prompt_text = st.text_input(label = "Enter your prompt text...", value = "The point is")
with col2:
    m_length = st.number_input("Length", min_value=1, step=1)               

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
