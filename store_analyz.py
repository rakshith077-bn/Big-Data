# Reading the input data file
file_name = 'cryptotoken_full.csv'

try:
    with open(file_name, 'r') as file:
        data = file.read()

    dataset_lenght = len(data)

    print(f"The lenght of the dataset is {dataset_lenght}")

except FileNotFoundError:
    print(f"The file {file_name} not found")

except Exception as e:
    print(f"An error occured: {e}")
    
#Processing the Dataset
import csv 
    
try:
    with open(file_name, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            row_tuple = ('INSERT',) + tuple(row)
            print(row_tuple)  # This will print each row as a tuple with 'INSERT' at the start
except FileNotFoundError:
    print(f"File {file_name} not found.")
except Exception as e:
    print(f"An error occurred: {e}")


# To make sure the dataset has not stored the value "INSERT", I'll print it the first 50 columns of it
with open(file_name, 'r') as file:
    for i in range(50):
        line = file.readline()
        if line:
            print(line)
        else:
            break
# Hence we can see that the value "INSERT" is not stored in the dataset


# Creating 3 directories
import os 

dir_names = ["Fixed", "Delimeted", "Offset"]

for dir_name in dir_names:
    try:
        os.mkdir(dir_name)
        print(f"Directory {dir_name} created successfully")

    except FileExistsError:
        print(f"Directory {dir_name} already exists")
   
    except Exception as e:
        print(f"An Error occured: {e}")

rows_per_file = 200

total_files = dataset_lenght // rows_per_file

for i in range(total_files):
    file_path = os.path.join(dir_name, f"Page_{i}.txt")
    start_index = i * rows_per_file
    end_index = (i + 1) * rows_per_file
    with open(file_path, 'w') as text_file:
        text_file.writelines(map(str, file_name[start_index:end_index]))


        
