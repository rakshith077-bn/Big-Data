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


#Creating files respective to the above directories    
file_names = ["Page 0", "Page 1", "Page 2"]



for name in file_names:
    try:
        for name in file_names:
            path_file = os.path.join(dir_names, name)
        if not os.path.exists(dir_names):
            os.mkdir(dir_names)
        print("File Created successfully")
    
    except FileExistsError:
        print(f"File {name} already exists")
    
    except FileNotFoundError:
        print(f"Directory {dir_names} not found")
    
    except Exception as e:
        print(f"An error occured: {e}")
    
    
    
    try:
        with open(file_path, 'w') as file:
            file.write(f"This is a file in {dir_name}")
        print(f"File created successfully in {dir_name}")
    except Exception as e:
        print(f"An error occured: {e}")
        


        
