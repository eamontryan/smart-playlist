import os
import sys
import openai
from datetime import datetime



client = openai.OpenAI(
    api_key=os.getenv('API_KEY'),
    organization='org-yVptBVbE45uqNqJ0HWV0BByo',
)


def process_markdown(file_path):
    print("Processing markdown...")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        # Rewrite content using GPT API and store it in a variable
        new_content = gpt(content)

        # Write the new content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)


    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        sys.exit(1)

def gpt(content):
    print("Contacting API...")
    with open("prompt.txt", "r", encoding='utf-8') as f:
        prompt_content = f.read()

    combination = "Apply the following PROMPT to the specified TEXT and give me" + \
    " only the output. Do not comment or add anything extra, just the solution. PROMPT=" + prompt_content + " TEXT=" + content

    print(os.getenv('API_KEY'))
    
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": combination,
            }
        ],
        model="gpt-3.5-turbo",
    )

    # Correctly accessing the response data
    if response.choices:
        return response.choices[0].message.content
    else:
        return "No response from API."
    
if __name__ == "__main__":
    if len(sys.argv) > 1:
        markdown_file = sys.argv[1]
        process_markdown(markdown_file)
    else:
        print("No file specified.")