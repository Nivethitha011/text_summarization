
## Text Summarization Using Streamlit and Hugging Face

## Project Overview

AI Text Summarization is a web application developed using Python and Streamlit. It uses a pre-trained Hugging Face Transformer model to convert lengthy English text into concise and meaningful summaries.

The application provides a simple interface where users can enter text, select their preferred summary length, generate a summary, and download the result.

<img width="750" height="173" alt="image" src="https://github.com/user-attachments/assets/5cbc517e-89e6-462e-bdf5-f317c4a5f07f" />


<img width="803" height="398" alt="image" src="https://github.com/user-attachments/assets/03476ee6-d620-4d5a-92b6-ceb7c4116244" />

## Objectives

- To summarize lengthy text automatically using Artificial Intelligence.
- To extract the main ideas from the given text.
- To provide different summary length options.
- To display original and summarized word counts.
- To allow users to download the generated summary.

## Technologies Used

- Python
- Streamlit
- Hugging Face Transformers
- PyTorch
- DistilBART CNN/DailyMail Model

## Features

- Simple and user-friendly web interface.
- Automatic text summarization.
- Short, Balanced, and Detailed summary options.
- Original text word count.
- Summary word count.
- Text reduction percentage.
- Downloadable summary in text format.
- No Hugging Face API key required.

## Project Structure

    TextSummarizerAI/
    |
    |-- app.py
    |-- requirements.txt
    |-- README.md
    |-- .gitignore

## Model Information

The application uses the `sshleifer/distilbart-cnn-12-6` pre-trained model available on Hugging Face.

The model is designed primarily for English text summarization. It generates summaries by identifying and condensing important information from the input text.

## Installation and Setup

### 1. Install Python

Install Python 3.11 or 3.12 and verify the installation.

    python --version

### 2. Create a Virtual Environment

    python -m venv .venv

Activate the environment on Windows PowerShell.

    .\.venv\Scripts\Activate.ps1

### 3. Install Dependencies

    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt

### 4. Run the Application

    python -m streamlit run app.py

The application will open in your default browser. If it does not open automatically, use the local URL displayed in the terminal.

## How to Use

1. Open the AI Text Summarization application.
2. Enter or paste English text into the input area.
3. Select Short, Balanced, or Detailed summary length.
4. Click the Generate Summary button.
5. View the generated summary and word count statistics.
6. Download the summary as a text file if required.

## Requirements

- Python 3.11 or 3.12
- An internet connection for the initial model download
- Sufficient memory and disk space to install and run PyTorch and the pre-trained model
- A modern web browser

## Limitations

- The model is primarily designed for English text.
- Very long input text may be truncated because of the model's input token limit.
- Generated summaries may omit details or contain inaccuracies.
- Processing speed depends on the system hardware and available resources.

## Future Enhancements

- Support for multiple languages.
- Uploading text files and PDF documents.
- Copy-to-clipboard functionality.
- Improved handling of long documents.
- Additional summarization models.
- Deployment as an online web application.

## Conclusion

The AI Text Summarization application demonstrates how pre-trained Transformer models can be integrated with Streamlit to create a practical and user-friendly AI application. It helps users understand lengthy English content more efficiently by generating concise summaries.

## Author

Developed as a Python and Artificial Intelligence project using Streamlit and Hugging Face Transformers.
