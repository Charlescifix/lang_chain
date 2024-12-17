import streamlit as st
import asyncio
from streamlit_chat import message


st.set_page_config(
    page_title = "Enhanced PDFChat",
    layout = "wide",
    initial_sidebar_state = "expanded",
)

async def main():
    st.title("PDFChat: ")

    option = st.selectbox("Select Option", ("PDF", "Blog", "Database"))

    if option == "PDF":
        uploaded_file = st.file_uploader("Choose a file", type="pdf")
        if uploaded_file is not None:
            with st.spinner("Processing..."):
                uploaded_file.seek(0)
                file = uploaded_file.read()

            st.session_state["ready"] = True

    elif option == "Blog":
        url = st.text_input("Enter the URL of the blog")

        if url:
            st.session_state["ready"] = True

    elif option == "Database":
        uploaded_file = st.file_uploader("Choose a Database file", type="db")
        if uploaded_file is not None:
            with st.spinner("Processing..."):
                uploaded_file.seek(0)

            st.session_state["ready"] = True

    if st.session_state.get("ready", False):
        if 'generated' not in st.session_state:
            st.session_state["generated"] = ["Welcome! You can ask questions"]

        if 'past' not in st.session_state:
            st.session_state["past"] = ["Hey"]

        container = st.container()
        response_container = st.container()

        with container:
            with st.form(key="my form", clear_on_submit=True):
                user_input = st.text_input("Query", placeholder = "e.g: Summarise The Document", key = "input")
                submit_button = st.form_submit_button(label = "Send")

            if submit_button and user_input:
                output = "Your message has been received"
                st.session_state["past"].append(user_input)
                st.session_state["generated"].append(output)

        if st.session_state["generated"]:
            with response_container:
                for i in range(len(st.session_state["generated"])):
                    if i < len(st.session_state["past"]):
                        st.markdown(
                            "<div style='background-color: #90caf9; color: black; padding: 10px; border-radius: 5px; width: 70%; float: right; margin: 5px;'>"+ st.session_state["past"][i] + "</div>",
                            unsafe_allow_html=True,
                        )
                    message(st.session_state["generated"][i], key = str(i), avatar_style="fun-emoji")




if __name__ == "__main__":
    asyncio.run(main())