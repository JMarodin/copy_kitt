import openai
import os
import argparse

MAX_INPUT_LENGTH = 32

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input

    print(f"User input: {user_input}")
    if validate_length(user_input):
        branding_result = generate_branding_snippet(user_input)
        print(branding_result)
    else:
        raise ValueError(f"Input length is too long. Must be under {MAX_INPUT_LENGTH}. Submitted input is: {user_input}")

def validate_length(prompt: str) -> bool:
    return len(prompt) <= MAX_INPUT_LENGTH

def generate_branding_snippet(prompt:str) -> str:
    client = openai.OpenAI()

    client.api_key = os.getenv("OPENAI_API_KEY")

    enriched_prompt = f"Generate upbeat branding snippet with hashtags for {prompt}: "
    print(enriched_prompt)

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": enriched_prompt
            }
        ]
    )

    branding_text = completion.choices[0].message.content
    return branding_text

if __name__ == "__main__":
    main()
