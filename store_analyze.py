import os
import sys
import pandas as pd
import argparse
import time
import multiprocessing
import argparse

input_file = 'final_data.xlsx'

# Creating 3 directories ["Fixed", "Delimited", "Offset"]

def create_directories(input_file):
    try:
        df = pd.read_excel(input_file)
    
    except FileNotFoundError:
        print(f"The specified file {input_file} not found")
    
    except Exception as e:
        print(f"The following error occured: {e}")
        return None

    directories = ["Fixed", "Delimited", "Offset"] 

    for directory in directories:
        try:
            os.mkdir(directory)
            print(f"The directory {directory} has been created")
        
        except FileExistsError:
            print("The directory already exists")
        
        except Exception as e:
            print(f"The following error occured: {e}")
        
    return df

# Creating files in "Fixed" Directory

def creating_fixed_pages(df, directory, rows_per_page = 500):
    total_rows = len(df)
    total_pages = (total_rows + rows_per_page - 1) // rows_per_page

    start_time = time.time()

    for number_of_pages in range(total_pages):
        page_path = os.path.join(directory, f"page_{number_of_pages}.txt")

        try:
            with open(page_path, 'w') as file_page:
                start = number_of_pages * rows_per_page
                end = min((number_of_pages + 1) * rows_per_page, total_rows)

                for row_index in range(start, end):
                    row = df.iloc[row_index]
                    formatted_row = [f"{value: <20}" for value in row]
                    line = ''.join(formatted_row) + '\n'
                    file_page.write(line)

            print(f"Page in the 'Fixed' Directory is created successfully")
            end_time = time.time()
                    
        except FileExistsError:
            print("The file already exists")

        except Exception as e:
            print(f"The following error occured: {e}")
    
    end_time = time.time()
    time_taken_fixed = start_time - end_time

    print(f"The time taken create files in the Fixed Directory: {time_taken_fixed} Seconds")

# Creating files in "Delimited" Directory 

def creating_delimited_pages(df, directory, delimiter='$', rows_per_page = 500):
    total_rows = len(df)
    total_pages = (total_rows + rows_per_page - 1) // rows_per_page

    start_time = time.time()

    for page_number in range(total_pages):
        page_path = os.path.join(directory, f"page_{page_number}.txt")

        try:
            with open(page_path, 'w') as page_file:
                start = page_number * rows_per_page
                end = min((page_number + 1) * rows_per_page, total_rows)

                for row_index in range(start, end):
                    row = df.iloc[row_index]
                    row_after_formating = delimiter.join(char for value in row for char in str(value))
                    line = f"{row_after_formating}{delimiter}\n"
                    page_file.write(line)

            print(f"Page in 'Delimited' directory created succesfully")
       
        except FileExistsError:
            print("The files already exists")

        except Exception as e:
            print(f"The following error occured: {e}")
    
    end_time = time.time()
    time_taken_delimited = start_time - end_time

    print(f"Time taken to create files in the Delimited Directory: {time_taken_delimited} Seconds")

# Creating files in the "Offset" Directory

def creating_offset_pages(df, directory, fixed_length_size = 2, rows_in_page = 500):
    total_rows = len(df)
    total_pages = (total_rows + rows_in_page - 1) // rows_in_page

    start_time = time.time()

    for number_of_pages in range(total_pages):        
        page_path = os.path.join(directory, f"page_{number_of_pages}.txt")

        try:
            with open(page_path, 'w') as page_file:
                starting = number_of_pages * rows_in_page
                ending = min((number_of_pages + 1) * rows_in_page, total_rows)

                for row_index in range(starting, ending):
                    row = df.iloc[row_index]

                    offsets = [(i * fixed_length_size) for i in range(len(row))]

                    values_joined = [f"{value:0>{fixed_length_size}}" for value in row]
                    values_joined += [f"{offset:0>{fixed_length_size}}" for offset in offsets]

                    line = f"{len(row)},{fixed_length_size}\n"
                    line += ''.join(values_joined) + '\n'
                    page_file.write(line)

            print(f"Pages in the 'Offset' directory is created successfully")
        
        except FileExistsError:
            print("The files already exists")

        except Exception as e:
            print(f"An error occurred while writing to '{directory}' directory: {e}")

    end_time = time.time()
    time_taken_offset = end_time - start_time

    print(f"Time taken to create files in the Offset directory is: {time_taken_offset} Seconds")


def first_part_command_arguments():
    parse = argparse.ArgumentParser(description='Storing data from the Input File')
    parse.add_argument('operation', help = 'operation type (store)')
    parse.add_argument('dataset', help = 'Location of the dataset file')

    arguments = parse.parse_args()

    output = f'operation: {arguments.operation}, input file: {arguments.dataset}'
    return output

def handling_operation_store(input_file_path):
    df = create_directories(input_file_path)
    
    if df is not None:
        creating_fixed_pages(df, "Fixed", rows_per_page=500)
        creating_delimited_pages(df, "Delimited", delimiter='$', rows_per_page=500)
        creating_offset_pages(df, "Offset", fixed_length_size=2, rows_in_page=500)

def main():
    # Get command line arguments
    given_command = 'python3 store_analyze.py store <location_of_input_file>'
    outcome1 = first_part_command_arguments()

    print(f"This is the example command: {given_command}")
    print(f"Command arguments: {outcome1}")

    if "store" in outcome1:
        input_file_path = outcome1.split()[-1]
        create_directories(input_file_path)
        handling_operation_store(input_file_path)
        creating_fixed_pages(input_file_path)
        creating_delimited_pages(input_file_path)
        creating_offset_pages(input_file_path)

    else:
        print("Invalide operation selected")


if __name__ == "__main__":
    main()

# Analysis - Part 2 

def reading_the_pages(directory, page_num):
    page_path = os.path.join(directory, f"Page {page_num}.txt")

    with open(page_path, 'r') as file:
        data_lines = file.readlines()

    # Parsing each line as values 

    parsed_data = [data_lines(line) for line in data_lines]

    return parsed_data

def converting_to_numeric_values(attribute_indexing):
    tuple_conversion = []
    try:
        number_values = int(attribute_indexing)
        tuple_conversion.append(number_values)
        return tuple(tuple_conversion)
    
    except ValueError:
        print("You have given an invalid attribute index")
        return None
            
attribute_indesxing = 2
tuple_final = converting_to_numeric_values(attribute_indexing=2)


def calculation_of_average(lines, attribute_indexing):
    total_sum = 0
    total_count = 0

    for line in lines:
        try:
            attribute_value = int(line[attribute_indexing])
            total_sum += attribute_value
            total_count += 1

        except (ValueError, IndexError):
            print(f"Skipping invalid or non-numeric value in line: {line}")

    return total_sum, total_count

def analyze_page(page_args):
    # This function is used by each process to analyze a specific page
    directory, page_num, attribute_index = page_args
    lines = reading_the_pages(directory, page_num)
    return calculation_of_average(lines, attribute_index)

def part2_analysis(directory, attribute_index, number_of_processes):
    # Generating a list of pages
    page_files = [i for i in range(len(os.listdir(directory)))]

    start_time = time.time()

    # Creating a pool of processes
    with multiprocessing.Pool(processes=number_of_processes) as pool:
        # Mapping the analyze_page function to each page
        results = pool.map(analyze_page, [(directory, page, attribute_index) for page in page_files])

    # Calculate the overall average from the results
    total_sum = sum(result[0] for result in results)
    total_count = sum(result[1] for result in results)

    if total_count > 0:
        average_cal = total_sum / total_count
        print(f"{attribute_index} average: {average_cal}")
    else:
        print("No numeric attributes found")
    
    end_time = time.time()
    time_taken_analysis = end_time - start_time

    print(f"Time taken to process: {time_taken_analysis}")

def second_part_command_arguments():
    parse = argparse.ArgumentParser(description='Part 2 analysis')
    parse.add_argument('operation', help='operation type (analyze)')
    parse.add_argument('directory', help='Location of the directory file')
    parse.add_argument('attribute_index', type=int, help='Attribute index for calculating the average of')
    parse.add_argument('number_of_processes', type=int, help='Number of processes for part-2')

    arguments = parse.parse_args()

    output = {
        'operation': arguments.operation,
        'directory': arguments.directory,
        'attribute_index': arguments.attribute_index,
        'number_of_processes': arguments.number_of_processes
    }
    
    return output

def main():
    # Get command line arguments
    given_command = 'python3 store_analyze.py store <location_of_input_file> <attribute_index> <number_of_processes>'
    output = second_part_command_arguments()

    print(f"This is the example command: {given_command}")
    print(f"Command arguments: {output}")

    if "analyze" in output['operation']:
        attribute_index = output['attribute_index']
        num_processes = output['number_of_processes']
        directory = output['directory']
        part2_analysis(directory, attribute_index, num_processes)
    else:
        print("Invalid operation selected")

if __name__ == "__main__":
    main()