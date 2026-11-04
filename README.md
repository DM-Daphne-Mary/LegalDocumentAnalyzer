# ⚖️ Legal Document Analyzer

## 📌 Project Overview
Legal Document Analyzer is an AI-powered application that helps users understand legal documents easily. It extracts text from PDF files and uses AI to identify important legal information.

## 🎯 Features
- Upload legal documents in PDF format.
- Extract text from PDF files.
- Identify document type and parties involved.
- Analyze key obligations and payment terms.
- Identify termination and confidentiality clauses.
- Extract important dates.
- Generate a simple document summary.

## 🛠️ Technologies Used
- **Python** – Backend programming
- **Streamlit** – User interface
- **Groq API** – AI-powered document analysis
- **PyPDF** – PDF text extraction
- **Python-dotenv** – Environment variable management

## 📂 Project Structure
```text
LegalDocumentAnalyzer/
│
├── app.py
├── ai_engine.py
├── document_processor.py
├── requirements.txt
├── .gitignore
├── README.md
└── data/
```

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/DM-Daphne-Mary/LegalDocumentAnalyzer.git
```

2. Open the project folder:
```bash
cd LegalDocumentAnalyzer
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project folder and add your Groq API key:
```env
GROQ_API_KEY=your_groq_api_key
```

5. Run the application:
```bash
streamlit run app.py
```

## 🔐 Security
- API keys are stored in a local `.env` file.
- Secret keys and private documents should not be uploaded to GitHub.

## ⚠️ Disclaimer
This application is developed for educational purposes. Its output is not a substitute for professional legal advice.

## 👩‍💻 Developed By
Daphne Mary
