# Big Data Assingnment

This assingnment aimed at performing read, write and analyze operations on a dataset. This repositry contains a single .py file, a dataset which I found on Kaggle and the directories and the .txt folders can be
used as a reference after executing the .py file on your system.

## Getting Started

These instructions will help you set up the pre-requistes for running the .py file successfully. 

### Prerequisites

What things you need to before running the codes

```
Latest version of Python installed.
An IDE such as VS Code or an online compiler such as Replit.
Create a folder in which the both the .py file and the dataset 'final_data.xlsx' are stored
```

### Terminal Command

Open the terminal on your desktop after creating a folder where the .py and the dataset 'final_data.xlsx' is stored.
Navigate your terminal directory to the folder's directory
```
My folder was in Desktop, and was called as Big-Data-master
Navigating to the folder's directory
$ cd Desktop
$ cd Big-Data-master
```

## Running the tests

Ensure the file's name must remain the same: 'store_analyze.py' & 'final_data.xlsx'. 
Run the following command in the terminal
```
python3 store_analyze.py store final_data.xlsx
```
Then run this command in your terminal 
```
python3 store_analyze.py analyze Fixed 1 4
```
'Fixed' represents the new directory created when you ran the first command.
'1' represents the attribute_index
'4' represents the number of processes.

You can play around with which directory you want to perform your analysis in. Note: There are only three directories: 'Fixed', 'Delimited', 'Offset'.
You can also use different attribute_index and the number of processes. 

This aims to define the duration of time taken to complete tasks using parallel processing. This is implemented using the 'Multiprocessing' library in Python.

Check the folder that contains the .py file and the dataset. 
There are three new folders namely 'Fixed', 'Delimited', and 'Offset'

### In casese of NameErrors or TypeErrors

I've already tried to engage most of the errors through exception handling. However, if the problem still persists, double check the python file and the dataset are present in the same folder,
the name of the files remain same as in the time during forking, and the terminal's directory is in the folder that contains the python file and the dataset. 

Contribute, if you think the errors could be handled better than I've done it, or if you have a different approach to it.


### Adding your codes

There is always room for improvments


## Authors

* **Rakshith B N** - *Initial work*

## Acknowledgments

* Professor Mr. Hao Cai, Department of Computer Science, St Francis Xavier University
