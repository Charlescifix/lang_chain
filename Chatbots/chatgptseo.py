import streamlit as st
import openai

openai.api_key = ""
st.title("SEO Article Writer with CHATGPT")




def generate_article(keyword, writing_style, word_count):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role":"user", "content": "Write a SEO optimised word article about" + keyword},
            {"role":"user", "content": "This article should be in style" + writing_style},
            {"role":"user", "content": "The article length should be" + str(word_count)}
        ]

    )

    result = ''
    for choice in response.choices:
        result += choice.message.content

    print(result)
    return result

keyword = st.text_input("Enter a keyword")
writing_style = st.selectbox("Select a writing style", ["Sarcastic", "Funny", "Academic"])
word_count = st.slider("Select a word count", min_value=300, max_value=1000, value=300)
submit_button = st.button("Generate Article")

if submit_button:
    message = st.empty()
    message.text("Generating article...")
    article = generate_article(keyword, writing_style, word_count)
    message.text("")
    st.write(article)
    st.download_button(label="Download article", data=article, file_name="article.txt", mime="text/txt")