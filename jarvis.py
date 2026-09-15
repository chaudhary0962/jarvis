import os
import subprocess
import webbrowser
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Jarvis AI Assistant", page_icon="🤖", layout="centered"
)

st.title("🤖 Jarvis - Your Desktop AI Assistant")
st.write(
    "Main aapka personal AI assistant hoon. Aap yahan command type karein aur main use execute karunga!"
)

# Initialize chat history
if "messages" not in st.session_state:
  st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])


# Function to execute system commands
def execute_command(command):
  cmd = command.lower()
  response = ""

  try:
    if "youtube" in cmd:
      webbrowser.open("https://www.youtube.com")
      response = "YouTube open kar diya hai sir!"
    elif "google" in cmd:
      webbrowser.open("https://www.google.com")
      response = "Google open kar diya hai sir!"
    elif "notepad" in cmd:
      subprocess.Popen(["notepad.exe"])
      response = "Notepad open kar diya hai!"
    elif "calculator" in cmd:
      subprocess.Popen(["calc.exe"])
      response = "Calculator open kar diya hai!"
    elif "chrome" in cmd:
      os.system("start chrome")
      response = "Google Chrome open kar diya hai!"
    else:
      # Default action: Google Search
      url = f"https://www.google.com/search?q={command}"
      webbrowser.open(url)
      response = f"'{command}' ke liye web search open kar diya hai!"
  except Exception as e:
    response = f"Command execute karne mein error aayi: {str(e)}"

  return response


# Accept user input from UI chat box
if prompt := st.chat_input(
    "Aap kya karwana chahte hain? (e.g., 'Open YouTube', 'Open Notepad')"
):
  # Add user message to chat history
  st.session_state.messages.append({"role": "user", "content": prompt})
  with st.chat_message("user"):
    st.markdown(prompt)

  # Generate assistant response
  with st.chat_message("assistant"):
    with st.spinner("Processing..."):
      response_text = execute_command(prompt)
      st.markdown(response_text)

  # Add assistant response to chat history
  st.session_state.messages.append(
      {"role": "assistant", "content": response_text}
  )