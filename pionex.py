# -*- coding: utf-8 -*-
"""Pionex

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Kv4SmD_RyG5OoouNElqH0eOYQbjd9cFX
"""

# prompt: using "/content/241k-Singapore-pionex.com-Crypto-Trading-Bots-UsersDB-csv-2023.csv" write a code that prints head(10) tail (10) info and description

import pandas as pd

# Load the CSV file into a pandas DataFrame.
try:
  df = pd.read_csv("/content/241k-Singapore-pionex.com-Crypto-Trading-Bots-UsersDB-csv-2023.csv")
except FileNotFoundError:
  print("Error: File not found. Please make sure the file path is correct.")
  exit()


# Print the first 10 rows.
print("Head (10 rows):")
print(df.head(10))

# Print the last 10 rows.
print("\nTail (10 rows):")
print(df.tail(10))

# Print information about the DataFrame.
print("\nInfo:")
print(df.info())

# Print a description of the DataFrame (summary statistics).
print("\nDescription:")
print(df.describe())

# prompt: using "/content/241k-Singapore-pionex.com-Crypto-Trading-Bots-UsersDB-csv-2023.csv" Merge the columns "First Name" "Last Name" into  column called Full Name and export as a new csv Called Singapore Pionex Cleaning

import pandas as pd


# Load the CSV file into a pandas DataFrame.
try:
  df = pd.read_csv("/content/241k-Singapore-pionex.com-Crypto-Trading-Bots-UsersDB-csv-2023.csv")
except FileNotFoundError:
  print("Error: File not found. Please make sure the file path is correct.")
  exit()

# Merge "First Name" and "Last Name" into "Full Name"
df["Full Name"] = df["First Name"].astype(str) + " " + df["Last Name"].astype(str)

# Export the modified DataFrame to a new CSV file
df.to_csv("Singapore_Pionex_Cleaning.csv", index=False)

# Print the first 10 rows.
print("Head (10 rows):")
print(df.head(10))

# Print the last 10 rows.
print("\nTail (10 rows):")
print(df.tail(10))

# Print information about the DataFrame.
print("\nInfo:")
print(df.info())

# Print a description of the DataFrame (summary statistics).
print("\nDescription:")
print(df.describe())

# prompt: using  "/content/Singapore_Pionex_Cleaning.csv" update the csv by removing duplicates from "Email" "Phone" and placing thm in a csv called duplicates

import pandas as pd

# Load the CSV file into a pandas DataFrame.
try:
    df = pd.read_csv("/content/Singapore_Pionex_Cleaning.csv")
except FileNotFoundError:
    print("Error: File not found. Please make sure the file path is correct.")
    exit()

# Find duplicate rows based on 'Email' and 'Phone' columns
duplicates = df[df.duplicated(subset=['Email', 'Phone'], keep=False)]

# Remove duplicates from the original DataFrame, keeping the first occurrence
df_no_duplicates = df.drop_duplicates(subset=['Email', 'Phone'], keep='first')

# Save the de-duplicated data to a new CSV file
df_no_duplicates.to_csv("Singapore_Pionex_cleaned.csv", index=False)

# Save the duplicate rows to a separate CSV file
duplicates.to_csv("duplicates.csv", index=False)

print("Duplicates removed and saved to 'duplicates.csv'")
print("Cleaned data saved to 'Singapore_Pionex_cleaned.csv'")

# prompt: using "/content/Singapore_Pionex_cleaned.csv" update the csv and drop the columns "First Name" "Last Name" "BrandCode" and put them in a csv and called "dropped columns"

import pandas as pd

try:
    df = pd.read_csv("/content/Singapore_Pionex_cleaned.csv")
except FileNotFoundError:
    print("Error: File not found. Please make sure the file path is correct.")
    exit()

# Create a new DataFrame with the dropped columns
dropped_columns_df = df[["First Name", "Last Name", "BrandCode"]]

# Drop the specified columns from the original DataFrame
df = df.drop(["First Name", "Last Name", "BrandCode"], axis=1)

# Save the updated DataFrame to the original file
df.to_csv("/content/Singapore_Pionex_cleaned.csv", index=False)

# Save the dropped columns to a new CSV file
dropped_columns_df.to_csv("dropped_columns.csv", index=False)

print("Columns 'First Name', 'Last Name', and 'BrandCode' dropped and saved to 'dropped_columns.csv'")
print("Updated CSV saved to '/content/Singapore_Pionex_cleaned.csv'")

# prompt: using "/content/Singapore_Pionex_cleaned.csv" update the csv and Seperate The column "RegistrationDate" but putting time formatted content into a column called time as well as removing time formatted content from "RegistrationDate"

import pandas as pd

try:
    df = pd.read_csv("/content/Singapore_Pionex_cleaned.csv")
except FileNotFoundError:
    print("Error: File not found. Please make sure the file path is correct.")
    exit()

# Convert 'RegistrationDate' to datetime objects
df['RegistrationDate'] = pd.to_datetime(df['RegistrationDate'], errors='coerce')

# Extract time component into a new column 'time'
df['time'] = df['RegistrationDate'].dt.time

# Remove the time component from 'RegistrationDate', leaving only the date
df['RegistrationDate'] = df['RegistrationDate'].dt.date

# Save the updated DataFrame back to the CSV file
df.to_csv("/content/Singapore_Pionex_cleaned.csv", index=False)

print("Updated CSV saved to '/content/Singapore_Pionex_cleaned.csv'")

# prompt: using "/content/Singapore_Pionex_cleaned.csv" drop the time column and add it to the "/content/dropped_columns.csv"

import pandas as pd

try:
    df = pd.read_csv("/content/Singapore_Pionex_cleaned.csv")
except FileNotFoundError:
    print("Error: File not found. Please make sure the file path is correct.")
    exit()

# Check if the 'time' column exists before attempting to drop it
if 'time' in df.columns:
    # Extract the 'time' column
    time_column = df['time']

    # Drop the 'time' column from the DataFrame
    df = df.drop('time', axis=1)

    # Save the updated DataFrame
    df.to_csv("/content/Singapore_Pionex_cleaned.csv", index=False)

    # Append the 'time' column to the 'dropped_columns.csv' file
    try:
        dropped_df = pd.read_csv("dropped_columns.csv")
        dropped_df['time'] = time_column  # Add the 'time' column
        dropped_df.to_csv("dropped_columns.csv", index=False)
    except FileNotFoundError:
        time_column.to_csv("dropped_columns.csv", index=False) # Create the file if it doesn't exist
    print("Time column dropped and appended to 'dropped_columns.csv'")
    print("Updated CSV saved to '/content/Singapore_Pionex_cleaned.csv'")
else:
    print("The 'time' column does not exist in the DataFrame.")

# prompt: using "/content/Singapore_Pionex_cleaned.csv" make "Full Name" the first column as well as let content in that column fit on one line

import pandas as pd

try:
    df = pd.read_csv("/content/Singapore_Pionex_cleaned.csv")
except FileNotFoundError:
    print("Error: File not found. Please make sure the file path is correct.")
    exit()

# Move 'Full Name' to the first column
cols = list(df.columns)
cols.insert(0, cols.pop(cols.index('Full Name')))
df = df[cols]

# Ensure "Full Name" fits on one line (assuming it might have newlines)
df["Full Name"] = df["Full Name"].str.replace('\n', ' ')


# Save the updated DataFrame
df.to_csv("/content/Singapore_Pionex_cleaned.csv", index=False)

print("Updated CSV saved to '/content/Singapore_Pionex_cleaned.csv'")

# prompt: using "/content/Singapore_Pionex_cleaned.csv" update the csv by checking the columns "Email" for invalid emails "Phone" for invalid phone numbers and place them in a file called invalid entries if one of the two columns has valid values then keep the entry

import pandas as pd
import re

def is_valid_email(email):
    # Basic email validation using regular expression
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.fullmatch(pattern, email))

def is_valid_phone(phone):
    # Basic phone number validation (can be customized)
    # This example allows numbers with or without + and spaces/dashes
    pattern = r"^\+?\d[\d\s-]*$"
    return bool(re.fullmatch(pattern, str(phone)))


try:
    df = pd.read_csv("/content/Singapore_Pionex_cleaned.csv")
except FileNotFoundError:
    print("Error: File not found. Please make sure the file path is correct.")
    exit()

invalid_entries = []
valid_entries = []

for index, row in df.iterrows():
    email = str(row['Email'])
    phone = str(row['Phone'])

    if not is_valid_email(email) and not is_valid_phone(phone):
        invalid_entries.append(row)
    else:
        valid_entries.append(row)

invalid_df = pd.DataFrame(invalid_entries)
invalid_df.to_csv("invalid_entries.csv", index=False)

valid_df = pd.DataFrame(valid_entries)
valid_df.to_csv("/content/Singapore_Pionex_cleaned.csv", index=False)

print("Invalid entries saved to 'invalid_entries.csv'")
print("Updated CSV with valid entries saved to '/content/Singapore_Pionex_cleaned.csv'")

# prompt: using "/content/Singapore_Pionex_cleaned.csv" update the csv  update the csv by checking the columns "Email" for invalid emails "Phone" for invalid phone numbers, extract them and place them in the "/content/invalid_entries.csv" path and change removed invalid entries to NULL

import pandas as pd
import re

def is_valid_email(email):
    # Basic email validation using regular expression
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.fullmatch(pattern, email))

def is_valid_phone(phone):
    # Basic phone number validation (can be customized)
    # This example allows numbers with or without + and spaces/dashes
    pattern = r"^\+?\d[\d\s-]*$"
    return bool(re.fullmatch(pattern, str(phone)))

try:
    df = pd.read_csv("/content/Singapore_Pionex_cleaned.csv")
except FileNotFoundError:
    print("Error: File not found. Please make sure the file path is correct.")
    exit()

invalid_entries = []

for index, row in df.iterrows():
    email_valid = is_valid_email(str(row['Email']))
    phone_valid = is_valid_phone(str(row['Phone']))

    if not email_valid or not phone_valid:
        invalid_entries.append(row)
        # Change invalid entries to NULL in the original DataFrame
        if not email_valid:
            df.loc[index, 'Email'] = 'NULL'
        if not phone_valid:
            df.loc[index, 'Phone'] = 'NULL'

invalid_df = pd.DataFrame(invalid_entries)
invalid_df.to_csv("/content/invalid_entries.csv", index=False)

df.to_csv("/content/Singapore_Pionex_cleaned.csv", index=False)

print("Invalid entries saved to '/content/invalid_entries.csv'")
print("Updated CSV with invalid entries set to NULL saved to '/content/Singapore_Pionex_cleaned.csv'")

# prompt: remove row entries with the value NULL but contain valid values in "Email" or "Phone from "/content/invalid_entries.csv" and add them to "/content/Singapore_Pionex_cleaned.csv"

import pandas as pd

try:
    invalid_df = pd.read_csv("/content/invalid_entries.csv")
    cleaned_df = pd.read_csv("/content/Singapore_Pionex_cleaned.csv")
except FileNotFoundError:
    print("Error: One or both of the input files not found.")
    exit()

# Filter out rows where all columns except 'Email' and 'Phone' are NULL and either 'Email' or 'Phone' is valid
rows_to_add = invalid_df[
    (invalid_df.drop(columns=['Email', 'Phone']).isnull().all(axis=1)) &
    ((invalid_df['Email'] != 'NULL') | (invalid_df['Phone'] != 'NULL'))
]

# Concatenate the filtered rows to the cleaned DataFrame
updated_cleaned_df = pd.concat([cleaned_df, rows_to_add], ignore_index=True)

# Save the updated DataFrame
updated_cleaned_df.to_csv("/content/Singapore_Pionex_cleaned.csv", index=False)

print(f"Added {len(rows_to_add)} rows from 'invalid_entries.csv' to 'Singapore_Pionex_cleaned.csv'")

# prompt: using "/content/Singapore_Pionex_cleaned.csv" check "Email" "Phone" for *** and if they occur remove the *** value only and add them to :/content/invalid_entries.csv" in a new column called unwanted symbols

import pandas as pd

try:
    df = pd.read_csv("/content/Singapore_Pionex_cleaned.csv")
except FileNotFoundError:
    print("Error: File not found. Please make sure the file path is correct.")
    exit()

# Create an empty list to store invalid entries
invalid_entries = []

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    email = str(row['Email'])
    phone = str(row['Phone'])

    # Check for "***" in Email and Phone columns
    if "***" in email or "***" in phone:
        # Append the row with unwanted symbols to the invalid_entries list
        invalid_entries.append(row)

        # Remove the "***" from Email and Phone columns in the original DataFrame
        df.loc[index, 'Email'] = email.replace("***", "")
        df.loc[index, 'Phone'] = phone.replace("***", "")


# Create a DataFrame for invalid entries
invalid_df = pd.DataFrame(invalid_entries)

# Add a new column 'unwanted symbols' to the invalid entries DataFrame
invalid_df['unwanted symbols'] = '***'


# Save the updated DataFrame to a new CSV file
invalid_df.to_csv("/content/invalid_entries.csv", mode='a', header=not pd.io.common.file_exists("/content/invalid_entries.csv"), index=False)


# Save the cleaned DataFrame back to the original file
df.to_csv("/content/Singapore_Pionex_cleaned.csv", index=False)

print("Invalid entries with '***' saved to '/content/invalid_entries.csv'")
print("Updated CSV saved to '/content/Singapore_Pionex_cleaned.csv'")