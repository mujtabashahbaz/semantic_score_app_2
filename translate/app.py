import openai
from striprtf.striprtf import rtf_to_text
import time

def read_rtf_file(file_path):
    """Read and extract text from an RTF file"""
    with open(file_path, 'r', encoding='utf-8') as file:
        rtf_text = file.read()
    plain_text = rtf_to_text(rtf_text)
    return plain_text

def translate_with_openai(text, api_key, model="gpt-4", max_retries=3):
    """Translate Hindi text to English using OpenAI API"""
    openai.api_key = api_key
    
    prompt = f"""
    Translate the following Hindi text to proper, grammatical English. 
    Maintain the original meaning while ensuring the English translation is natural and fluent.
    Do not add any additional explanations or notes, just provide the translation.
    
    Hindi text:
    {text}
    """
    
    for attempt in range(max_retries):
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are a skilled translator fluent in both Hindi and English."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3  # Lower temperature for more consistent translations
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            if attempt == max_retries - 1:
                raise e
            time.sleep(2 ** attempt)  # Exponential backoff

def save_translation(translated_text, output_path):
    """Save the translated text to a file"""
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(translated_text)

def main():
    # Configuration
    input_rtf_path = 'hindi_content.rtf'  # Path to your Hindi RTF file
    output_txt_path = 'english_translation.txt'  # Output file path
    openai_api_key = 'your-api-key-here'  # Replace with your OpenAI API key
    
    try:
        # Step 1: Read the RTF file
        print("Reading Hindi content from RTF file...")
        hindi_text = read_rtf_file(input_rtf_path)
        print(f"Original Hindi text sample: {hindi_text[:200]}...")
        
        # Step 2: Translate using OpenAI
        print("Translating to English...")
        english_translation = translate_with_openai(hindi_text, openai_api_key)
        
        # Step 3: Save the translation
        save_translation(english_translation, output_txt_path)
        print(f"Translation successfully saved to {output_txt_path}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()