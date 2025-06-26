import streamlit as st
import numpy as np  # Moved to the top with other imports

sidebar1 = st.sidebar.selectbox("Sidebar", options=["Home", "MyChatbot", "Projects", "Achievements","Contact"])  # Fixed method name

if sidebar1 == "Home":
    st.title("Personal Website for Francesco")
    st.write("Welcome to my personal website! Here you can find information about my projects, skills, and interests.")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.header("About Me")
        st.write("I am a software developer with a passion for building web applications. I love coding and learning new technologies.")
    with col2:
        st.header("Projects")
        st.write("Here are some of my recent projects:")
        st.markdown("- Project 1: A web application for managing tasks.")
        st.markdown("- Project 2: A personal blog built with Streamlit.")
    with col3:
        st.header("Contact")
        st.write("Feel free to reach out to me via email at unknown@gmail.com")  # Fixed email
    with col4:
        st.header("Skills")
        st.write("Python, JavaScript, Streamlit, HTML, CSS, Gaming, Math, and more!")

    tab1, tab2, tab3 = st.tabs(["Home", "Projects", "Contact"])
    with tab1:
        st.write("Welcome to my personal website! Here you can find information about my projects, skills, and interests.")
    with tab2:
        st.write("Here are some of my recent projects:")
        st.markdown("- Project 1: A web application for managing tasks.")
        st.markdown("- Project 2: A personal blog built with Streamlit.")
    with tab3:
        st.write("Feel free to reach out to me via email at unknown@gmail.com")  # Fixed email
        st.write("You can also find me on [LinkedIn](https://www.linkedin.com)")  # Updated link

    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    A = st.slider("Select a value for amplitude", 0.1, 10.0, 1.0)
    st.line_chart(A * y)

    width = st.slider("Select a value for width", 0.1, 10.0, 1.0)
    y2 = np.sin(x / width)
    st.line_chart(A * y2)
    st.write("This is a simple interactive plot using Streamlit.")

elif sidebar1 == "MyChatbot":
    from myAI import tell_response
    st.title("My Chatbot")
    user_input = st.text_input("Ask me anything:")
    if user_input:
        response = tell_response(user_input)
        st.write(f"Chatbot response: {response}")
    else:
        st.write("Please enter a message to get a response.")
elif sidebar1 == "Projects":
    st.title("Projects")
    st.write("Here are some of my recent projects:")
    st.markdown("- Project 1: A web application for managing tasks.")
    from prs import fun_winner
    btn1= st.button("✂️ Scissors")
    btn2= st.button("📄 Paper")
    btn3= st.button("🪨 Rock")
    if btn1:
        result = fun_winner('scissors')
        st.write(result)

    if btn2:
        result = fun_winner('paper')
        st.write(result)    

    if btn3:
        result = fun_winner('rock')
        st.write(result)




    d = st.selectbox("Select an option",[ "✂️", "📄", "🪨"])
    if d == "✂️":
        result = fun_winner('scissors')
        st.write(result)
    elif d == "📄":
        result = fun_winner('paper')
        st.write(result)
    elif d == "🪨":
        result = fun_winner('rock')
        st.write(result)

    

elif sidebar1 == "Achievements":
    st.title("Achievements")
    st.write("Here are some of my achievements:")
    st.markdown("- Achievement 1: Completed a major project successfully.")
    st.markdown("- Achievement 2: Contributed to an open-source project.")

elif sidebar1 == "Contact":
    st.title("Contact")
    st.write("Feel free to reach out to me via email at unknown@gmail.com")  # Fixed email
    st.write("You can also find me on [LinkedIn](https://www.linkedin.com)")  # Updated link

