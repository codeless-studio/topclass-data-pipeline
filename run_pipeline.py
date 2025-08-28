# Main script to run the full pipeline

from src.reader import txt_reader, pdf_reader
from src.cleaner import text_cleaner
from src.extractor import data_extractor
from src.writer import csv_writer

def run_pipeline():
    # Step 1: Read files
    raw_texts = txt_reader.read_txt_files("data/raw") + pdf_reader.read_pdf_files("data/raw")

    # Step 2: Clean text
    cleaned_texts = [text_cleaner.clean(text) for text in raw_texts]

    # Step 3: Extract data
    extracted_data = [data_extractor.extract(text) for text in cleaned_texts]

    # Step 4: Write to CSV
    csv_writer.write_to_csv(extracted_data, "data/output/cleaned_data.csv")

if __name__ == "__main__":
    run_pipeline()
