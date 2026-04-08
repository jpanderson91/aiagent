import os
from google import genai  # type: ignore
from dotenv import load_dotenv  # type: ignore
import argparse

def main():
    print("Hello from aiagent!")
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key == None:
        raise RuntimeError("key not found")
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()
    # Now we can access `args.user_prompt`

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(model="gemini-3-flash-preview", contents=args.user_prompt)
    if response.usage_metadata is None:
        raise RuntimeError("usage metadata not found")
    
    print (f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print (f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print (response.text)


if __name__ == "__main__":
    main()

