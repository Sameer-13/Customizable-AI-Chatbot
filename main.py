import streamlit as st
import openai
import config as cfg

st.set_page_config(page_title="Chatbot", layout="wide", initial_sidebar_state="expanded")

hide = """
<style>
footer {visibility: hidden;}
</style>
"""

st.markdown(hide, unsafe_allow_html=True) # Hide footer

if "bot" not in st.session_state:
    st.session_state["bot"] = False

def createBot(personality,character,profession,nationality,phrase,short,emoji):
    st.session_state.bot =  True
    st.session_state.messages = []
    full_response = ""
    if len(personality) != 0:
        full_reasopnse += "You  are a" + "and".joint(personality) + "Person. "
    if character:
        full_response += "You imitate the character " + character + ". "
    if profession:
        full_response += "You profession is " + profession + ". "
    if nationality:
            full_response += "Speak English but with" + nationality + "accent. "
    if phrase.strip():
        full_response += "Your catchphrase is " + phrase.strip() + ". "
    if short:
        full_response += "Always provide a short response which is less than 40 words. "
    if emoji:
        full_response += "Use emojis excessively. "
        
    st.session_state.massages.append({"role": "system", "content": full_response})



with st.sidebar:
    personality = st.selectbox("Personality", cfg.Personality_list)
    character = st.selectbox("Character Imitation", options=cfg.Character_list)
    profession = st.selectbox("Profession", options=cfg.Profession_list)
    nationality = st.selectbox("Nationality", options=cfg.National)
    phrase = st.text_input("Catchphrase")
    short = st.toggle("Make responses short", value=False)
    emoji = st.toggle("Make assistant emoji fanatic")
    st.button("Unleash Assistant Chatbot!", args=(personality,character,profession,nationality,phrase,short,emoji), on_click=createBot)
    
st.header("Assistant Chatbot Maker")

if not st.session_state.bot: 
    st.markdown("<h6>Fill out the necessary fields in the sidebar and click generate to make your own assistant chatbot!</h6>", unsafe_allow_html=True)
else:
    openai.api_key = cfg.OpenAI_API_KEY
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = cfg.OpenAI_MODEL
    
    for massage in st.session_state.messages[1:]:
        with st.chat_message(massage["role"]):
            st.markdown(massage["content"])
    
    if prompt := st.chat_input():
        st.session_state.massage.append({"role": "user", "content": prompt})
        
        with st.chat_message("user"):
            st.markdown(prompt)
            
        with st.chat_message("assistant"):
            massage_placeholder = st.empty()
            full_response = ""
            for response in openai.Completion.create(
                model = st.session_state['openai_model'],
                messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                stream=True,
            ):
                
                full_response += response["choices"][0].delta.get("content", "")
                massage_placeholder.markdown(full_response+ " ")
            massage_placeholder.markdown(full_response+ " ")
        st.session_state.messages.append({"role": "assistant", "content": full_response})