# Automatic-detection-of-fieldbus-protocols
Automatic detection of fieldbus protocols and recognition of the data structure - IuK - Universität Rostock

# Installation Guide

## MySQL Installation

If you don't have apache and MySQL , then you need to download and install them. you and install and configure  them separately from `https://httpd.apache.org/download.cgi` and `https://www.mysql.com/downloads/`  or as one package using this link `https://sourceforge.net/projects/xampp/`

## Install mysql connector 
run `pip install mysql-connector-python`

## Python Installation

Download and install python from `https://www.python.org/downloads/` 

## Database Migration
cd database and Run `python migrate.py`.
This will create the database and the table for you if you have installed and configured mysql will.


## Adding test telegram messages

In the data folder, you will find a file named `knx.txt`. This file contains a list of KNX telegrams we want to use to generate our sequence. you can make use of it or copy and replace your own telegrams in the file.

## Generating Sequences

cd to the root directory and run `python sequence_alignment.py`
This will generate and add a list of sequences to the database using the telegrams in the file `data/knx.txt`.

## Identifying a new telegram 

For a new message you want to know the sequence it belongs to, copy and paste the message in the line `test = "BCE0362E094C000080" ` (i.e. replace `BCE0362E094C000080` with your own telegram). this line can be found in `identify.py`.

Finally you can run `python identify.py`
The output will be a list of all the sequences related to the message you replaced in the variable `test`