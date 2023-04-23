# Benford-s_Law

See if data verifies Benford's Law

This is a web application that allows users to check if the data in csv file satisies Benford's law.

TOOLS USED:
1. Python with Pyramid framework
2. HTML/CSS


The UI is running on address localhost:6543/benford


Files:
1. gen_data.py is used to create csv file with 1 column and 30k rows with random data. Output- benford_data.csv
2. non_benfords.csv does not satisfy Benford's Law.
3. view/home.html contains html code for frontpage UI.
4. backend.py uses pyramid framework which calls check_benford() function from benford_check.py.
5. benford_check.py checks is csv file has data that satisties Benford's law. Saves JSON file in json/ if it does.


For futher details, see documentation-- https://drive.google.com/file/d/196SR3K8bumr_51BXsQtzGgxZwjyuJ0N1/view
