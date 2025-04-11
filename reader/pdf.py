import pdfplumber
import pandas as pd
import os

# Get the current directory of the script
current_dir = os.path.dirname(os.path.realpath(__file__))

# Specify the path to your PDF file (using the absolute path)
file_path = r"C:\Users\MatthewCottell\OneDrive - Cotton Holdings Inc\Desktop\your_file.pdf"

# Open the PDF file
with pdfplumber.open(file_path) as pdf:
    # Select the first page (you can loop through all pages if needed)
    page = pdf.pages[0]
    
    # Extract the table from the page
    table = page.extract_table()

# Convert the extracted table into a DataFrame
df = pd.DataFrame(table[1:], columns=table[0])

# Save the DataFrame to a CSV file in the same directory as the .py file
output_csv_path = os.path.join(current_dir, "read_data.csv")
df.to_csv(output_csv_path, index=False)

# Inform the user that the file has been saved
print(f"Data has been saved to {output_csv_path}")
