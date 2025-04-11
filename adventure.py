"""Adventure Game Module

This module contains the functionality to play the Lost Temple of Data adventure game.
It provides options to start the adventure or exit the game, and includes data processing
functions to support archaeological exploration.
"""

import pandas as pd
import re

def load_artifact_data(excel_filepath):
    """
    Reads artifact data from a specific sheet ('Main Chamber') in an Excel file,
    skipping the first 3 rows.

    Args:
        excel_filepath (str): The path to the artifacts Excel file.

    Returns:
        pandas.DataFrame: DataFrame containing the artifact data.
    """
    return pd.read_excel(excel_filepath, sheet_name='Main Chamber', skiprows=3)

def load_location_notes(tsv_filepath):
    """
    Reads location data from a Tab-Separated Value (TSV) file.

    Args:
        tsv_filepath (str): The path to the locations TSV file.

    Returns:
        pandas.DataFrame: DataFrame containing the location data.
    """
    return pd.read_csv(tsv_filepath, sep='\t')

def extract_journal_dates(journal_text):
    """
    Extracts all dates in MM/DD/YYYY format from the journal text.

    Args:
        journal_text (str): The full text content of the journal.

    Returns:
        list[str]: A list of date strings found in the text.
    """
    return re.findall(r"\b\d{2}/\d{2}/\d{4}\b", journal_text)

def extract_secret_codes(journal_text):
    """
    Extracts all secret codes in AZMAR-XXX format (XXX are digits) from the journal text.

    Args:
        journal_text (str): The full text content of the journal.

    Returns:
        list[str]: A list of secret code strings found in the text.
    """
    return re.findall(r"AZMAR-\d{3}", journal_text)

def start_adventure():
    """Starts the adventure game by displaying the introduction and options to the player."""
    print("Welcome to the Lost Temple of Data!")
    print("You are about to embark on an exciting adventure.")
    print("1. Start Adventure")
    print("2. Exit")

def choose_path(choice):
    """
    Chooses the path based on the player's input.

    If the choice is 1, the player takes the adventurous path.
    If the choice is 2, the player chooses to exit the game.
    """
    if choice == 1:
        print("You have chosen the adventurous path!")
    elif choice == 2:
        print("You have chosen to exit the game. Goodbye!")

def main():
    """Main function to run the game."""
    start_adventure()
    try:
        choice = int(input("Enter your choice: "))
        if choice not in [1, 2]:
            raise ValueError("Invalid choice. Please enter 1 or 2.")
    except ValueError as e:
        print(e)
        return
    choose_path(choice)

# --- Optional test/debug block ---
if __name__ == "__main__":
    excel_file = 'artifacts.xlsx'
    tsv_file = 'locations.tsv'
    journal_file = 'journal.txt'

    print(f"--- Loading Artifact Data from {excel_file} ---")
    try:
        artifacts_df = load_artifact_data(excel_file)
        print("Successfully loaded DataFrame. First 5 rows:")
        print(artifacts_df.head())
    except FileNotFoundError:
        print(f"Error: File not found at {excel_file}")

    print(f"\n--- Loading Location Notes from {tsv_file} ---")
    try:
        locations_df = load_location_notes(tsv_file)
        print("Successfully loaded DataFrame. First 5 rows:")
        print(locations_df.head())
    except FileNotFoundError:
        print(f"Error: File not found at {tsv_file}")

    print(f"\n--- Processing Journal from {journal_file} ---")
    try:
        with open(journal_file, 'r', encoding='utf-8') as f:
            journal_content = f.read()

        print("\nExtracting Dates...")
        dates = extract_journal_dates(journal_content)
        print(f"Found dates: {dates}")

        print("\nExtracting Secret Codes...")
        codes = extract_secret_codes(journal_content)
        print(f"Found codes: {codes}")

    except FileNotFoundError:
        print(f"Error: File not found at {journal_file}")
