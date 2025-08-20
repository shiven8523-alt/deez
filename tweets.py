import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI as Google
import os
from langchain import PromptTemplate, LLMChain

st.set_page_config(page_title='image Generator', page_icon='🪺', layout="centered", initial_sidebar_state="auto", menu_items=None)
st.title("image Generator")

os.environ['GOOGLE_API_KEY'] = st.secrets['GOOGLE_API_KEY']
model = Google(model = "gemini-1.5-flash-latest")

tweet_template = """
Give me {number} image on {topic} in {language}.
Please follow the below instructions:
1. make a car that has gold rims
2. it should look like a bat 
3. it shouold have a poop emoji.
image_prompt = PromptTemplate(template = image_template, input_variables = ['number', 'topic', 'language'])

with st.form(key = 'images'):
    topic = st.text_input("Topic: ")
    number = st.number_input("Number of images: ", value = 1, step = 1, max_value = 10, min_value = 1)
    language = st.text_input("Language: ")
    submit = st.form_submit_button("Generate")

if submit:
    image_chain = image_prompt | model
    response = image_chain.invoke({"number": number,
                                   "topic": topic,
                                   "language": language,})
    st.write(response.content)
