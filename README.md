# *Chatbot App* 

A responsive chatbot application built using Python's **Tkinter** library and **OpenAI's GPT-3.5-turbo** model. The chatbot can act as a mathematics expert or a database expert, based on the user's selection.

## Features

On launch, the app checks if it has an OpenAI API key saved. If not, it will prompt the user for the API key.

The user can choose to chat with either a *mathematics expert* or a *database expert*.

The chatbot conducts an examination, asking the user a question and waiting for a response.

The chatbot asks up to 10 questions, with each answer graded on a scale of 1 to 10.

The user's response should be the answer to the question. If the response is not relevant, the chatbot will reply with "it's not relevant, please answer the question."
The user's answers and grades are recorded.

At the end of the 10 questions, the user will see their answers, correct answers (if they were wrong), and their grade.

The chat interface is designed using light colors.

## Installation and Running

+ Clone the repository or download the source code.

+ Install the required libraries: openai (**pip install openai**) and tkinter.

+ Run the examBot.py file. This will launch the chatbot app.

## Usage

When the app starts, choose the agent you want to chat with by clicking the "Mathematics Expert" or "Database Expert" button.

The chatbox will be initialized based on the agent's specialty.

Type your message in the input box and press Enter or click the "Send" button to send the message.

The agent will respond based on its specialty.

## Code Structure

ChatbotApp: The examBot class responsible for managing the user interface and interaction with the GPT-3.5-turbo model.

+ **__init__**: Initializes the chatbot app and checks for an OpenAI API key.

+ **on_close**: Handles the closing event of the application.

+ **init_widgets**: Initializes the user interface widgets.

+ **check_and_set_openai_api_key**: Checks if an OpenAI API key is saved, prompts the user for the key if needed, and sets the key.

+ **prompt_for_api_key**: Prompts the user for an OpenAI API key.

+ **save_api_key**: Saves the OpenAI API key to a configuration file.

+ **init_agent_selection**: Initializes the agent selection interface.

+ **init_chat**: Initializes the chat interface based on the selected agent's specialty and sets the conversation context.

+ **send_message**: Sends the user's message and receives the chatbot's response.

+ **chat_with_agent**: Interacts with the GPT-3.5-turbo model and receives the chatbot's response.

+ **update_chat**: Updates the chat text box with the messages from the user and the chatbot.

+ **load_api_key**: Loads the OpenAI API key from the configuration file if it exists.

+ **main.py**: The main script that initializes and runs the chatbot app.

+ **load_api_key**: Loads the OpenAI API key from a configuration file, if it exists.

Initializes the Tkinter root window and creates an instance of the ChatbotApp class.

Runs the Tkinter main loop to start the application.

## Requirements

Python 3.6 or higher

openai library (can be installed using *pip install openai*)

tkinter library (usually comes pre-installed with Python)

## Limitations

+ The chatbot app currently supports only two agent specialties: Mathematics and Database.

- The grading system is based on the GPT-3.5-turbo model's responses and may not always be accurate.

- The app relies on the OpenAI API key, which requires an internet connection.

## Future Improvements

- Add more agent specialties to expand the app's capabilities.

- Implement a more advanced grading system for better accuracy.

- Provide an option to save the chat history to a file.

- Improve error handling and user experience.