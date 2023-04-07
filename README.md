
# Payroll System 

This system calculates a payroll out from work a record input file.

An input file format can be found at

```
payroll_calculator_project/data/work_record.txt
```

As well as the output file

```
payroll_calculator_project/data/payroll.csv
```

## Approach

I had the alternative to write a solution in a single python script that would have solved the problem stated, with
no scale up option, or build a more robust solution applying the factory pattern to allow the system to be extensible
in reading input files from different sources or writing output files to different targets. I chose tha latter approach.

It has two main modules:

- **data_handler**: to manage the data load and saving (extensible part)
- **payroll**: to perform the salary calculations.

**data_handler** -- reads --> **payroll** -- saves --> **data_handler**

The main.py module clearly reflects the system logic.

I have tried to follow as much as possible Clean Code an SOLID Principles.

The working methodology was TDD. All the tests are include under the folder:

```
payroll_calculator_project/tests
```
If you want to run the tests, you need to have installed pytest and positioned in the 
above folder you can run pytest.

DISCLAIMER:

* I have built only happy path tests
* I'm not expert in docker, so the method described below to run the solution from Docker
probably could be improved.

  
## Run from docker 

You can run the project from a docker image at the cost of the time that takes 
building the image, 30 minutes approximately.

### Pre-requisites:

1. Docker installed 

### Procedure 
Run the following sequence of commands: 

``` shell
sudo docker build --tag payroll . 
```

Once the image is built run the command:
``` 
sudo docker run -it --mount src=$(pwd)/data,target=/data,type=bind payroll
```

This option will take as input the file _work_record.txt_, which is placed in the folder:

```
payroll_calculator_project/data
```

You can change the input file at will, replacing the existing one.

## Run using a local python or a virtual environment (Linux)

Using a local installation of python:

1. Open a terminal
2. Position yourself at root folder: payroll_calculator_project.
3. Paste and run the following set of commands
```shell
sudo chmod ugo+wr ./data/; # make sure have right permissions
sudo chmod ugo+wr ./data/*; # make sure have right permissions
export PYTHONPATH=$PWD;
python3 ./payroll_calculator/main.py ./data/work_record.txt ./data/payroll.csv;
```
You will se the result in the file payroll.csv

## Run using a local python or a virtual environment (MACOSX)

1. Open a terminal
2. Position yourself at root folder: payroll_calculator_project.
3. Paste and run the following set of commands

```shell
export PYTHONPATH=$PWD;
python3 ./payroll_calculator/main.py ./data/work_record.txt ./data/payroll.csv;
```

NOTES:

1. You can change the input data file by replacing the file placed in ./data/ folder work_record.txt
2. You can run the previous sequence oif commands by running the shell command ./run_payroll.sh






