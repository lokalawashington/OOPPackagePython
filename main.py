"""GO TO PyPI PYTHON PACKAGE INDEX"""
"""SEARCH Prettytable and go to doc"""
"""Go to setting ,project ,python intepreter then plus + sign and search for Prettytable"""
from prettytable import PrettyTable
table = PrettyTable()
print(table)
"""use documentation to add column and row"""

table.add_column("Taka safi", ["youth empowerment","agency","networks","leadership"])
table.add_column("type",["community seminar","seminars", "unity","good leaders"])

table.align = "l"

print(table)