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


# Reading the data
def reading_input_file(data):
    if data is not None:
        try:
            for index, row in data.iterrows():
                row_tuple = ('INSERT',) + tuple(row)
                print(row_tuple)

        except Exception as e:
            print(f"The following error occured: {e}")


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

                print("Files in 'Fixed' Directory created successfully")
        except Exception as e:
            print(f"An error occurred while writing to '{directory}' directory: {e}")


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

                print("Files in 'Delimited' created succesfully")

        except Exception as e:
            print(f"An error occurred while writing to '{directory}' directory: {e}")


# Creating files in the directory "Offset"
def create_pages_offset(df, directory, fixed_length_size=2, rows_per_page=500):
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

                    offsets = [(i * fixed_length_size) for i in range(len(row))]

                    combined_values = [f"{value:0>{fixed_length_size}}" for value in row]
                    combined_values += [f"{offset:0>{fixed_length_size}}" for offset in offsets]

                    line = f"{len(row)},{fixed_length_size}\n"
                    line += ''.join(combined_values) + '\n'
                    page_file.write(line)

                print("Files created successfully")

        except Exception as e:
            print(f"An error occurred while writing to '{directory}' directory: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python store_analyze.py <command> <location_of_the_file>")
    else:
        command = sys.argv[1]
        input_file = sys.argv[2]

        if command == "store":
            df = input_and_directories(input_file)
            if df is not None:
                data = create_directories(input_file)
                create_pages_fixed(df, "Fixed")
                create_pages_delimited(df, "Delimited", delimiter='$')
                create_pages_offset(df, "Offset", fixed_length_size=2)
        else:
            print(f"Unknown command: {command}")

# Part 2 - Analysis
import multiprocessing

def read_page(directory, page_num):
    page_path = os.path.join(directory, f"page_{page_num}.txt")
    with open(page_path, 'r') as page_file:
        lines = page_file.readlines()
    return lines

def calculate_average(lines, attribute_index):
    total_sum = 0
    total_count = 0

    for line in lines:
        values = line.split(',')
        try:
            attribute_value = int(values[attribute_index])
            total_sum += attribute_value
            total_count += 1
        except ValueError:
            print(f"Skipping non-numeric value: {values[attribute_index]}")

    return total_sum, total_count

def analyze_directory(directory, attribute_index, num_processes):
    total_sum = 0
    total_count = 0

    page_files = [f"page_{i}.txt" for i in range(len(os.listdir(directory)))]

    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.starmap(
            read_page,
            [(directory, i) for i in range(len(page_files))]
        )

        for result in results:
            sum_page, count_page = calculate_average(result, attribute_index)
            total_sum += sum_page
            total_count += count_page

    if total_count > 0:
        average = total_sum / total_count
        print(f"{attribute_index} average: {average}")
    else:
        print("No numeric values found in the specified attribute.")

if __name__ == "__main__":
    if len(sys.argv) != 5 or sys.argv[1] != "analyze":
        print("Usage: python store_analyze.py analyze <Fixed, Delimited, Offset> <index_of_attribute> <num_processes>")
    else:
        directory = sys.argv[2]
        attribute_index = int(sys.argv[3])
        num_processes = int(sys.argv[4])

        analyze_directory(directory, attribute_index, num_processes)
