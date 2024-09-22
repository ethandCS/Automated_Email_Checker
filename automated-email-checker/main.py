from email_checker import get_email_services, list_emails_by_date  # Importing functions from email_checker.py

# Main script execution
if __name__ == "__main__":
    # Step 1: Get the Gmail API service
    service = get_email_services()

    # Step 2: Ask the user for the date in YYYY/MM/DD format
    query_date = input("Enter the date to fetch emails from (YYYY/MM/DD): ")

    # Step 3: Ask the user if they want to use GPT for summarization
    use_gpt = input("Do you want to use GPT to summarize and rank the emails? (y/n): ").lower() == 'y'

    # Step 4: Fetch, list, and optionally summarize the emails using GPT
    list_emails_by_date(service, query_date, use_gpt=use_gpt)
