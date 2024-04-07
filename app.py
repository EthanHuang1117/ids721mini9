import streamlit as st
from transformers import pipeline

# Load the language model
model = pipeline("text-generation", model="openai-gpt")


# Define Streamlit app with a fresh UI design
def main():
    # Set page title and background color
    st.set_page_config(
        page_title="Text Generation App",
        page_icon=":pencil2:",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    # Add header
    st.header("Text Generation App")

    # Add description
    st.write(
        "Welcome to the Text Generation App powered by Streamlit and Hugging Face Transformers!"
    )
    st.write(
        "This app showcases the capabilities of a state-of-the-art language model for text generation."
    )

    # Add text input area
    with st.form(key="text_form"):
        st.subheader("Enter Text Prompt")
        text_input = st.text_area(label="", height=150)
        submit_button = st.form_submit_button(label="Generate Text")

    # Generate text when button is clicked
    if submit_button and text_input:
        # Generate text with the language model
        generated_text = model(text_input, max_length=50, do_sample=True)[0][
            "generated_text"
        ]

        # Display generated text
        st.subheader("Generated Text")
        st.write(generated_text)


if __name__ == "__main__":
    main()
