# Customizable-AI-Chatbot

## Introduction
This project allows you to create and interact with a custom-tailored AI chatbot using Streamlit and OpenAI.

## Key Features:

* Customization: Build a chatbot with a unique personality, character imitation (optional), profession (optional), and even a catchphrase!
* User-friendly Interface: A Streamlit web app provides an intuitive interface for configuring and interacting with your custom chatbot.
* OpenAI Integration: Leverage OpenAI's powerful language models to generate responses for your chatbot.
* Interactive Chat: Engage in a conversation with your chatbot by entering prompts and receiving responses.

## Overveiw
![image_2024-06-27_05-10-38](https://github.com/Sameer-13/Customizable-AI-Chatbot/assets/106761486/5a9ef01f-436b-40d8-9f3f-8ee77a540ea7)

## Installation
* Setup conda environment (recommended):
```bash
# Create a conda environment
conda create --name streamlit python=3.10
# Activate the environment
conda activate streamlit
# Install requirements:
pip install -r requirements.txt
```
* Setup OpenAI Key:
```
1. Create an account in OpenAI
2. Go to API Keys. Now 
3. Create a new secret key, and save it somewhere so you don't lose it.
4. Go to config.py and write in it your OpenAI key
```

## Getting Started
After successfully installing and activating the streamlit env, go to the ```config.py``` and fill the Nationality, Profession, Character, and Personality list with your personal preference and needs. 
Lastly, run the following command in the cmd:
```bash
streamlit run main.py
```
Enjoy chatting with personal AI assistance!

## Authors
Sameer Alsabei (Sameer-13) [Twitter](https://mobile.twitter.com/Sameer_Alsabei), [Linked in](https://www.linkedin.com/in/sameer-alsabea-610291239/)
