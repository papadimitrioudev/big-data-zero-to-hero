Mini Budget to Excel
--------------------
A Python script that creates an Excel file (mini_budget.xlsx) with a few expenses
and a TOTAL row.

Why I made this
---------------
I'm learning how to generate .xlsx files with Python using openpyxl.

How to run
----------
1) Install:
   pip install -r requirements.txt

2) Run:
   python main.py

Output
------
- mini_budget.xlsx (created in the same folder)

Edit the data
-------------
Open main.py and change the "rows" list (items / categories / costs), then run again.

Notes
-----
The Excel file is only written when the script calls wb.save(...). :contentReference[oaicite:1]{index=1}
