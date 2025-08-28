# topclass-data-pipeline

Goal: creating content database for the topclass app 

Data:
- sourcing data from txt, pdf files 
- cleaning data
- create .csv file ready for upload to Bubble App

Tech Stack:
Python 

🧰 Core Libraries by Functionality

📄 Reading TXT and PDF Files

PyMuPDF (fitz) – Fast and accurate PDF text extraction.
pdfminer.six – More detailed PDF parsing (e.g., layout, metadata).
PyPDF2 – Good for basic PDF manipulation (merging, splitting).
Built-in open() – For reading .txt files.

🧼 Text Cleaning and Preprocessing

re – Regular expressions for pattern matching and cleaning.
nltk – Tokenization, stopword removal, stemming, etc.
spaCy – Fast and modern NLP library (great for named entity recognition, lemmatization).
unidecode – For removing accents and normalizing text.
beautifulsoup4 – If you ever need to clean HTML content.

📊 Writing to CSV and Data Handling

pandas – For structured data manipulation and CSV I/O.
csv – Python’s built-in CSV module (lightweight alternative).

🧠 Optional but Powerful Add-ons

🔍 Text Mining & NLP

scikit-learn – For feature extraction (e.g., TF-IDF), clustering, classification.
gensim – Topic modeling (e.g., LDA), word embeddings.
textblob – Simple sentiment analysis and text processing.
langdetect – Language detection if you're working with multilingual data.

🧪 Testing & Logging

pytest – For writing unit tests.
logging – For tracking pipeline execution and debugging.

⚙️ Configuration & CLI

PyYAML – For reading configuration files.
argparse or click – For building command-line interfaces.

-----------------------------------------------------------------------------

💡 Further Suggestions

1. Pipeline Design: Consider using a pipeline pattern (e.g., with classes or functions chained together) to make your process modular and testable.

2. Parallel Processing: If you’re processing many files, look into concurrent.futures or joblib to speed things up.

3. Metadata Tracking: Store metadata (e.g., filename, date processed, source) alongside your cleaned data for traceability.

4. Visualization (optional): Use matplotlib, seaborn, or wordcloud to visualize word frequencies or patterns.
