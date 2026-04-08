import os
from google import genai  # type: ignore
from google.genai import types  # type: ignore
from dotenv import load_dotenv  # type: ignore
import argparse

def create_message(role, text):
    return types.Content(role=role, parts=[types.Part(text=text)])

def main():
    print("Hello from aiagent!")
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key == None:
        raise RuntimeError("key not found")
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    # Now we can access `args.user_prompt`

    client = genai.Client(api_key=api_key)
    
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    response = client.models.generate_content(model="gemini-3-flash-preview", contents=messages)
    
    if response.usage_metadata is None:
        raise RuntimeError("usage metadata not found")
    
    if args.verbose:
        print (f"User prompt: {args.user_prompt}")
        print (f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print (f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print (response.text)
    else:
        print (response.text)

if __name__ == "__main__":
    main()

