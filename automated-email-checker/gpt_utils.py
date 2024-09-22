from dotenv import load_dotenv
import os
import openai

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key from the .env file
openai.api_key = os.getenv('OPENAI_API_KEY')


def summarize_and_rank_emails(emails):
    """Use GPT to summarize and rank emails based on urgency."""
    
    # Combine email subjects and snippets into a single message to pass to GPT
    email_text = "\n".join([f"Subject: {email['subject']}\nSnippet: {email['snippet']}" for email in emails])
    
    # The prompt structure for the Chat API: role-based interaction
    messages = [
        {"role": "system", "content": "You are a helpful assistant that summarizes and ranks emails based on urgency."},
        {"role": "user", "content": f"I have a list of emails with their subjects and snippets. Please summarize the content and rank them based on urgency, from most urgent to least urgent.\n\n{email_text}"}
    ]
    
    # Call OpenAI GPT for summarization and ranking using the new API
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # Use the GPT-3.5-turbo model (best for chat-based tasks like summarization and reasoning)
        messages=messages,
        max_tokens=500,
        temperature=0.5
    )
    
    # Extract and return the generated response from GPT
    return response['choices'][0]['message']['content'].strip()
