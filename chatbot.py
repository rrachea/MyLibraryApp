"""
Chatbot script for prompting using ChatGPT; using pn for GUI
"""

# Installing dependencies
import os
import openai
from dotenv import load_dotenv, find_dotenv

# read local .env file
_ = load_dotenv(find_dotenv('keys.env')) 
# load api key
openai.api_key  = os.getenv('OPENAI_API_KEY')

###### Useful Functions ######

def get_completion(prompt, model="gpt-3.5-turbo"):
    """
    Function:
        - Retrieve response from ChatGPT based off singular prompt
    Args:
        - prompt: message to be sent
        - model: GPT model to use
    Output:
        - response as a string
    """
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.2, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    """
    Function:
        - Retrieve response from ChatGPT based on history i.e. messages
    Args:
        - messages: string object containing context and history
        - model: GPT model to use
        - temperature: determine variability in response from GPT
    Output:
        - response as a JSON object
    """
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]

def collect_messages(_):
    """
    Function:
        - Retrieve responses from GPT prompt
    Output:
        - response as a string object
    """
    prompt = inp.value_input
    # append user prompt
    inp.value = ''
    context.append({'role': 'user', 'content': f"{prompt}"})
    # append response from system
    response = get_completion_from_messages(context)
    context.append({'role': 'assistant', 'content': f"{response}"})
    # store as context
    panels.append(pn.Row('User:', pn.pane.Markdown(prompt, width=600)))
    pannels.append(pn.Row('Assistant:', pn.pane.Markdown(response, width=600, style={'background-color': '#F6F6F6'})))
    return pn.Column(*panels)

import panel as pn
pn.extension()

panels = []

# context for bot
context = [ {'role':'system', 'content':"""
You are SmooBot, an automated ChatBot meant to serve as a interactive Library Management service. \ You will follow the steps accordingly whenever you meet a customer: \
1. Find the current time. \
2. You must greet the customer according to the time and introduce yourself in a kind and polite manner. \
3. Ask the customer for their name and always refer to them by their name. \
4. Ask them what they would like to do. \
"""} ]  # accumulate messages

inp = pn.widgets.TextInput(value="Hi", placeholder='Enter text here…')
button_conversation = pn.widgets.Button(name="Chat!")

interactive_conversation = pn.bind(collect_messages, button_conversation)

dashboard = pn.Column(
    inp,
    pn.Row(button_conversation),
    pn.panel(interactive_conversation, loading_indicator=True, height=300),
)

dashboard