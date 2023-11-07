# Reading the input data file
file_name = 'cryptotoken_full.csv'

try:
    with open(file_name, 'r') as file:
        data = file.read()

except FileNotFoundError:
    print(f"The file {file_name} not found")

except Exception as e:
    print(f"An error occured: {e}")
    
#Processing the Dataset
import csv 

#Since it is 50,000 rows, I will print it only for the first 10 rows
#Reading the CSV file and printing the tuple in the format ["INSERT", "Attribute_1", "Attribute_2",...., "Attribute_n"]
try:
    with open(file_name, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader) #Skipping the first heading line in the dataset
        row_count = 0
        for row in reader:
            if row_count < 10:
                row_tuple = ('INSERT',) + tuple(row)
                print(row_tuple)  # Without storing the "INSERT" value in the tuple I'm printing it here
                row_count += 1
            else:
                break

except Exception as e:
    print(f"An error occurred: {e}")
    
    
# Since it's working, I'll print it for the whole dataset and then move on to writing those into different values
try:
    with open(file_name, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader) #Skipping the first heading line in the dataset
        row_count = 0
        for row in reader:
            row_tuple = ("INSERT",) + tuple(row_tuple)
            print(row_tuple)

except Exception as e:
    print(f"An error occurred: {e}")



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
        print("An Error occured")

for dir_name in dir_names:
    file_path = os.path.join(dir_name, 'example.txt')
    
    try:
        with open(file_path, 'w') as file:
            file.write(f"This is an example file in {dir_name}")
        print(f"File created successfully in {dir_name}")
    except Exception as e:
        print(f"An error occured: {e}")
        


        
