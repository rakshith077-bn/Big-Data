#Create 3 Directories namely 'Fixed', 'Delimited', 'Offset', and create three pages namely 'Page 0', 'Page 1', 'Page 2'
#Read all the tuples from the dataset you've chosen
#Write the data according to the conditions into the three files sequentially

#Reading the file 
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
#Printing the tuples only for the first 15 tuples in the mentioned format ("INSERT", "Attribute 1", "Attribute 2",......"Attribute N")
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
    
    
#It's working, Now printing it for the whole datasets


# To make sure the dataset has not stored the value "INSERT", I'll print it the first 50 columns of it
with open(file_name, 'r') as file:
    for i in range(50):
        line = file.readline()
        if line:
            print(line)
        else:
            break
# Hence "INSERT" is not stored within the dataset


# Creating 3 directories "Fixed", "Delimited", "Offset" and 3 .txt files within these 3 directories respectively namely "Page 0", "Page 1", "Page 2"
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

txt_names = ["Page 0", "Page 1", "Page 2"]

for i, dir_name in enumerate(dir_names):
    file_path = os.path.join(dir_name, f"{txt_names[i]}.txt")

    try:
        with open(file_path, 'w') as file:
            file.write(f"This is the file's content {txt_names[i]} content")

            print(f"File {txt_names[i]} created successfully in directory {dir_name}")
    
    except Exception as e:
        print(f"An error occured while printing the file: {e}")


        


        
