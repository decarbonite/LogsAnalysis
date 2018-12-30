# LogsAnalysis

A reporting tool that prints out reports (in plain text) based on the data in a database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

## Design

The project consists of two source files, main.py which calls the functions and prints the output and newsdb.py which consist of the methods that grabs the data from the database.

The query statements were done one for each question.

## How to Run

You have to be in the same directory level as main.py and new.db in Vagrant virtual machine. Then type:

```bash
python main.py
```
