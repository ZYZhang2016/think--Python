def print_head():
	four_minus = "- "*4
	print("+ " + four_minus + "+ " + four_minus + "+")

def print_body():
	print_head()
	section = "|"+" "*9
	row = section*2 + "|"
	print_fourtimes(row)

def print_fourtimes(s):
	print(s)
	print(s)
	print(s)
	print(s)

def print_grid():
	print_body()
	print_body()
	print_head()

print_grid()