import openai

# Set your OpenAI API key
openai.api_key = ''

def ask_chatgpt(prompt):
    # Send prompt to ChatGPT
    response = openai.ChatCompletion.create(
        model="text-davinci-003",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    # Return the generated text from ChatGPT
    return response['choices'][0]['message']['content']

def main():
    # Get user input
    user_input = input("Enter your prompt: ")

    # Pass user input to ChatGPT and get response
    response = ask_chatgpt(user_input)

    # Display the response
    print("ChatGPT response:", response)

if __name__ == "__main__":
    main()
