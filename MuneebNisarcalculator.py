import streamlit as st

# Set page config
st.set_page_config(layout="centered")

# Initialize session state
if "expression" not in st.session_state:
    st.session_state.expression = ""

st.title("Muneeb Nisar Calculator")

# Display bar
st.text_input("Calculation", value=st.session_state.expression, key="display", disabled=True)

# Functions
def press(val):
    st.session_state.expression += str(val)

def calculate():
    try:
        expression = st.session_state.expression.replace("×", "*").replace("÷", "/")
        result = eval(expression)
        st.session_state.expression = str(result)
    except:
        st.session_state.expression = "Error"

def clear():
    st.session_state.expression = ""

# Button Layout
buttons = [
    ['7', '8', '9', '÷'],
    ['4', '5', '6', '×'],
    ['1', '2', '3', '-'],
    ['0', 'C', '=', '+']
]

for row in buttons:
    cols = st.columns([1, 1, 1, 1])  # Equal width columns
    for i, btn in enumerate(row):
        with cols[i]:
            if btn == "=":
                st.button(btn, on_click=calculate)
            elif btn == "C":
                st.button(btn, on_click=clear)
            else:
                st.button(btn, on_click=press, args=(btn,))
