import os
import sys
import openai
from datetime import datetime

openai.api_key = os.getenv('API_KEY')
prompt = "prompt.txt"

def process_markdown(file_path):
    # Open the Markdown file
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        
        # Rewrite content using GPT API and store it in a variable
        new_content = gpt(content)

        # Write the new content back to the file
        with open(file_path, 'w') as file:
            file.write(new_content)

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        sys.exit(1)  # Exit with error status

if __name__ == "__main__":
    markdown_file = sys.argv[1]
    process_markdown(markdown_file)

def gpt(content):
    with open(prompt, "r") as f:
        promptContent = f.read()

    combination = "Apply the following PROMPT to the specified TEXT and give me" + \
    " only the output. Do not comment or add anything extra, just the solution. PROMPT=" + promptContent + " TEXT=" + content

    response = openai.Completion.create(
            engine="text-davinci-003",  # or use another model version
            prompt=combination,  # sets the prompt based on text input from prompt.txt
            max_tokens=150
        )
    
    return response
    

