import os
import openai
import tkinter as tk
from tkinter import ttk, simpledialog


class ChatbotApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Chatbot App")
        self.master.geometry("600x500")
        self.master.config(bg="#d9d9d9")
        self.master.protocol("WM_DELETE_WINDOW", self.on_close)

        self.selected_agent = tk.StringVar()

        self.conversation_history = []
        self.selected_agent = tk.StringVar()

        self.check_and_set_openai_api_key()

    def on_close(self):
        self.master.destroy()

    def init_widgets(self):
        agents_frame = ttk.Frame(self.master)
        agents_frame.pack(pady=10)

        chat_frame = ttk.Frame(self.master)
        chat_frame.pack(pady=10)

        self.chat_text = tk.Text(chat_frame, width=70, height=20, state="disabled")
        self.chat_text.grid(column=0, row=0)

        input_frame = ttk.Frame(self.master)
        input_frame.pack(pady=10)

        chat_frame.grid_rowconfigure(0, weight=1)
        chat_frame.grid_columnconfigure(0, weight=1)

        self.user_input = ttk.Entry(input_frame, width=70)
        self.user_input.grid(column=0, row=0)

        # Bind the Enter key to the send_message function
        self.user_input.bind("<Return>", lambda event: self.send_message())

        input_frame.grid_columnconfigure(0, weight=1)

        ttk.Button(input_frame, text="Send", command=self.send_message).grid(column=1, row=0)

    def check_and_set_openai_api_key(self):
        api_key = os.getenv("OPENAI_API_KEY")

        if api_key:
            openai.api_key = api_key
            self.init_agent_selection()
        else:
            api_key = self.prompt_for_api_key()
            self.save_api_key(api_key)
            openai.api_key = api_key
            self.init_agent_selection()

    def prompt_for_api_key(self):
        api_key = simpledialog.askstring("API Key", "Enter your OpenAI API key:", parent=self.master)
        return api_key

    def save_api_key(self, api_key):
        with open("config.txt", "w") as f:
            f.write(f"OPENAI_API_KEY={api_key}")

    def init_agent_selection(self):
        self.agent_selection_frame = ttk.Frame(self.master)
        self.agent_selection_frame.pack(pady=10)

        ttk.Label(self.agent_selection_frame, text="Choose an agent:").grid(column=0, row=0)

        ttk.Button(self.agent_selection_frame, text="Mathematics Expert", command=lambda: self.init_chat("math")).grid(
            column=1, row=0)
        ttk.Button(self.agent_selection_frame, text="Database Expert", command=lambda: self.init_chat("database")).grid(
            column=2, row=0)

    def init_chat(self, agent_type):
        self.selected_agent.set(agent_type)
        self.master.winfo_children()[0].destroy()
        self.init_widgets()

        # Greeting message
        # self.update_chat("Agent", "Hello! How can I help you today?")

        # Add context message based on selected agent
        if agent_type == "math":
            context_message = "You are Mr. Smith, a mathematics expert. After greeting the user, your job is to exam them in mathematics by sending them 10 questions. Wait for their response to each question, grade their answer from 1 to 10 and send them the perfect answer. Do not send all the questions in one go, wait for their response before sending the next one."
        else:
            context_message = "You are Mr. Joe, a database expert. After greeting the user, your job is to give them a database test. You will provide 10 questions, one at a time, and wait for the user to answer. You will grade the submitted answer from 1 to 10 and give feedback with the correct answer. Your goal is to help the user improve their knowledge about the database."

        self.conversation_history.append({"role": "system", "content": context_message})

    def send_message(self):
        user_message = self.user_input.get()
        if not user_message:
            return

        self.update_chat("User", user_message)
        self.user_input.delete(0, tk.END)

        if len(self.conversation_history) == 0:
            system_message = f"You are an {self.selected_agent.get()} expert."
            self.conversation_history.append({"role": "system", "content": system_message})

        openai_response = self.chat_with_agent(user_message)
        self.update_chat("Agent", openai_response)

    def chat_with_agent(self, user_message):
        self.conversation_history.append({"role": "user", "content": user_message})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.conversation_history
        )

        assistant_message = response['choices'][0]['message']['content']
        self.conversation_history.append({"role": "assistant", "content": assistant_message})

        return assistant_message

    def update_chat(self, role, message):
        self.chat_text.config(state="normal")
        if role == "User":
            self.chat_text.insert(tk.END, f"{role}: {message}\n", "user")
            self.chat_text.tag_config("user", foreground="#0000ff")
        else:
            self.chat_text.insert(tk.END, f"{role}: {message}\n", "agent")
            self.chat_text.tag_config("agent", foreground="#008000")
        self.chat_text.config(state="disabled")
        self.chat_text.see(tk.END)


def load_api_key():
    if os.path.exists("config.txt"):
        with open("config.txt", "r") as f:
            for line in f:
                key, value = line.strip().split("=")
                if key == "OPENAI_API_KEY":
                    return value
    return None


api_key = load_api_key()
if api_key:
    os.environ["OPENAI_API_KEY"] = api_key

root = tk.Tk()
app = ChatbotApp(root)
root.mainloop()
