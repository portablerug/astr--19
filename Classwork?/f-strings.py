s = "ASTR 19 "
t = "keeps"
u = "getting"
v = "better?"

#use f-strings to print out contents of strings
print(f"{s} {t} {u} {v}")

i = 123908
print(f"{i:12d}")   #prints out i with 12 TOTAL spaces
print(f"{i:012d}")  #prints i with 12 TOTAL spaces with 0 filling in the blanks

x = 38204750.15
print(f"x with 8 digits, 8 after, sci notation = {x:9.8e}")
