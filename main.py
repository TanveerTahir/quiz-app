import streamlit as st
import random
import time

# Title of the app
st.title("📝 Quiz Application")

# List of questions
questions = [
    {
        "question": "What is Python, and what is it commonly used for?",
        "options": [
            "A programming language for web development only",
            "A general-purpose programming language used for web development, data analysis, AI, and more",
            "A type of snake",
            "A database management system"
        ],
        "answer": "A general-purpose programming language used for web development, data analysis, AI, and more"
    },
    {
        "question": "How do you print 'Hello, World!' in Python?",
        "options": [
            "print('Hello, World!')",
            "echo 'Hello, World!'",
            "console.log('Hello, World!')",
            "printf('Hello, World!')"
        ],
        "answer": "print('Hello, World!')"
    },
    {
        "question": "Which of the following is the correct way to create a variable in Python?",
        "options": [
            "var x = 10",
            "int x = 10",
            "x = 10",
            "x := 10"
        ],
        "answer": "x = 10"
    },
    {
        "question": "What is the output of `2 ** 3` in Python?",
        "options": ["6", "8", "9", "5"],
        "answer": "8"
    },
    {
        "question": "Which of the following is used to define a function in Python?",
        "options": [
            "function my_function():",
            "def my_function():",
            "func my_function():",
            "define my_function():"
        ],
        "answer": "def my_function():"
    },
    {
        "question": "What is the output of `'Hello' + 'World'` in Python?",
        "options": [
            "HelloWorld",
            "Hello World",
            "Hello+World",
            "Error"
        ],
        "answer": "HelloWorld"
    },
    {
        "question": "Which of the following is a valid Python list?",
        "options": [
            "[1, 2, 3, 4]",
            "{1, 2, 3, 4}",
            "(1, 2, 3, 4)",
            "1 2 3 4"
        ],
        "answer": "[1, 2, 3, 4]"
    },
    {
        "question": "What does the `len()` function do in Python?",
        "options": [
            "Returns the length of an object",
            "Converts a string to lowercase",
            "Adds two numbers",
            "Sorts a list"
        ],
        "answer": "Returns the length of an object"
    },
    {
        "question": "What is the output of `'Python'.lower()`?",
        "options": [
            "PYTHON",
            "python",
            "Python",
            "Error"
        ],
        "answer": "python"
    },
    {
        "question": "Which of the following is used to comment a single line in Python?",
        "options": [
            "// This is a comment",
            "# This is a comment",
            "/* This is a comment */",
            "<!-- This is a comment -->"
        ],
        "answer": "# This is a comment"
    },
    {
        "question": "What is the output of `10 / 2` in Python?",
        "options": ["5.0", "5", "2", "Error"],
        "answer": "5.0"
    },
    {
        "question": "Which of the following is a valid Python dictionary?",
        "options": [
            "{'name': 'Alice', 'age': 25}",
            "['name', 'Alice', 'age', 25]",
            "('name', 'Alice', 'age', 25)",
            "{'name', 'Alice', 'age', 25}"
        ],
        "answer": "{'name': 'Alice', 'age': 25}"
    },
    {
        "question": "What is the output of `'Python'[1]`?",
        "options": ["P", "y", "t", "h"],
        "answer": "y"
    },
    {
        "question": "What does the `range(5)` function generate?",
        "options": [
            "[0, 1, 2, 3, 4]",
            "[1, 2, 3, 4, 5]",
            "[5, 6, 7, 8, 9]",
            "[0, 1, 2, 3, 4, 5]"
        ],
        "answer": "[0, 1, 2, 3, 4]"
    },
    {
        "question": "What is the output of `'Python'.upper()`?",
        "options": [
            "PYTHON",
            "python",
            "Python",
            "Error"
        ],
        "answer": "PYTHON"
    },
    {
        "question": "Which of the following is used to check if a key exists in a dictionary?",
        "options": [
            "if key in dictionary:",
            "if dictionary.has_key(key):",
            "if dictionary[key]:",
            "if key.exists(dictionary):"
        ],
        "answer": "if key in dictionary:"
    },
    {
        "question": "What is the output of `3 * 'a'` in Python?",
        "options": [
            "aaa",
            "3a",
            "a3",
            "Error"
        ],
        "answer": "aaa"
    },
    {
        "question": "What is the output of `bool(0)` in Python?",
        "options": ["True", "False", "0", "Error"],
        "answer": "False"
    },
    {
        "question": "Which of the following is used to remove whitespace from the beginning and end of a string?",
        "options": [
            "trim()",
            "strip()",
            "remove()",
            "clean()"
        ],
        "answer": "strip()"
    },
    {
        "question": "What is the output of `'Python'.replace('P', 'J')`?",
        "options": [
            "Jython",
            "Python",
            "JythonP",
            "Error"
        ],
        "answer": "Jython"
    }
]

# Initialize session state for the current question
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

# Display the current question
question = st.session_state.current_question
st.subheader(question["question"])

# Display options as radio buttons
selected_option = st.radio("Choose your answer:", question["options"], key="answer")

# Submit button
if st.button("Submit Answer"):
    if selected_option == question["answer"]:
        st.success("✔ Correct Answer!")

        time.sleep(5)
        # Select a new random question
        st.session_state.current_question = random.choice(questions)
        st.rerun()  # Refresh the app to show the next question
    else:
        st.error(f"❌ Incorrect answer! The correct answer is: {question['answer']}")