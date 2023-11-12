import os
import sys
import pandas as pd

input_file = 'final_data.xlsx'

# Creating 3 directories ["Fixed", "Delimited", "Offset"]
def create_directories(input_file):

    try:
        data = pd.read_excel(input_file)
    
    except FileNotFoundError:
        print(f"The specified file {input_file} not found")
    
    except Exception as e:
        print(f"The following error occured: {e}")
        return None
    
    directories = ["Fixed", "Delimited", "Offset"]

    for directory in directories:
        try:
            os.mkdir(directory)
            print(f"The Directory {directory} has been successfully created")
        
        except FileExistsError:
            print(f"The directory {directory} already exists")
        
        except Exception as e:
            print(f"The following error occured: {e}")
    return data

data = create_directories(input_file)


# Reading the data
def reading_input_file(data):
    if data is not None:
        try:
            for index, row in data.iterrows():
                row_tuple = ('INSERT',) + tuple(row)
                print(row_tuple)

        except Exception as e:
            print(f"The following error occured: {e}")

reading_input_file(data)

# Creating files in "Fixed" Directories
def create_pages_fixed(data, directory, rows_per_page=500):
    total_rows = len(data)
    total_pages = (total_rows + rows_per_page - 1) // rows_per_page

    for page_num in range(total_pages):
        page_path = os.path.join(directory, f"page_{page_num}.txt")

        try:
            with open(page_path, 'w') as page_file:
                start_index = page_num * rows_per_page
                end_index = min((page_num + 1) * rows_per_page, total_rows)

                for row_index in range(start_index, end_index):
                    row = data.iloc[row_index]
                    formatted_row = [f"{value: <20}" for value in row]
                    line = ''.join(formatted_row) + '\n'
                    page_file.write(line)

        except Exception as e:
            print(f"An error occurred while writing to '{directory}' directory: {e}")

input_file = 'final_data.xlsx'
data = create_directories(input_file)

if data is not None:
    create_pages_fixed(data, "Fixed")


# Creating files in "Delimited" directory
def create_pages_delimited(df, directory, delimiter='$', rows_per_page=500):
    total_rows = len(df)
    total_pages = (total_rows + rows_per_page - 1) // rows_per_page

    for page_num in range(total_pages):
        page_path = os.path.join(directory, f"page_{page_num}.txt")

        try:
            with open(page_path, 'w') as page_file:
                start_index = page_num * rows_per_page
                end_index = min((page_num + 1) * rows_per_page, total_rows)

                for row_index in range(start_index, end_index):
                    row = df.iloc[row_index]
                    formatted_row = delimiter.join(char for value in row for char in str(value))
                    line = f"{formatted_row}{delimiter}\n"
                    page_file.write(line)

        except Exception as e:
            print(f"An error occurred while writing to '{directory}' directory: {e}")

input_file = 'final_data.xlsx'
df = create_directories(input_file)

if df is not None:
    create_pages_delimited(df, "Delimited", delimiter='$')