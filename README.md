# automated-email-checker
Automated Email Checker using Python. Optionally, you can use GPT for summarization and prioritization.

## Overview
The **Automated Email Checker** is a Python-based tool that retrieves emails from your inbox and displays the content. Additionally, it offers an optional feature where GPT is used to summarize the emails and prioritize them based on urgency, helping you efficiently manage your inbox by highlighting important emails.

## Features
- **IMAP Email Access**: Connects to your email account and retrieves unread messages.
- **Basic Email Listing**: Lists email snippets and subjects from your inbox.
- **Optional Email Summarization**: Optionally, use GPT to summarize email content, focusing on key information (this requires setting up OpenAI API access).
- **Optional Priority Sorting**: When GPT is enabled, it organizes emails from most urgent to least based on content analysis.

## Structure Visual
automated-email-checker/
│
├── .env                    # Environment variables (OpenAI API key, Gmail credentials)
├── .gitignore              # Ignore unnecessary files like .env, __pycache__, etc.
├── client_secret.json      # Downloaded OAuth2 credentials file
├── email_checker.py        # Main script for email retrieval and processing
├── gpt_utils.py            # GPT-related functions (summarization, ranking) (optional)
├── main.py                 # Main script that handles user input and calls email checking
├── README.md               # Project overview and instructions
├── requirements.txt        # Python dependencies
├── token.json              # OAuth2 token file
└── __pycache__/            # Compiled Python bytecode files




## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/ethandCS/automated-email-checker.git
    cd automated-email-checker
    ```

2. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Setup OAuth2 (if using Gmail)**:
    - Follow [this guide](https://developers.google.com/identity/protocols/oauth2) to set up OAuth2 for Gmail access.

## Usage

1. **Run the email checker**:
    ```bash
    python main.py
    ```

2. **View the summary**: 
    - The script will output a list of your most urgent emails with a summary of each.
    - Choose whether to use GPT:
            The script will prompt you to decide if you want to use GPT for summarization and ranking. If you choose "n", it will simply list the email subjects and snippets. If you choose "y", GPT will summarize and rank the emails based on urgen

## Roadmap
    - Add notification system for urgent emails.
    - Improve email prioritization algorithm.
    - Create a web-based UI for easy email management.

### Key Information Summary:

    - **Basic Functionality**: By default, the script will fetch and display email snippets.
    - **Optional GPT Integration**: Users can optionally enable GPT summarization by setting up the OpenAI API.
    - **Installation and Usage**: Instructions are clear on how to set up dependencies, use OAuth2, and optionally set up GPT.
    - **Project Structure**: The structure provides a clear view of the files and their roles in the project.

    This version should be ready for your GitHub repository! Let me know if anything else is needed.
