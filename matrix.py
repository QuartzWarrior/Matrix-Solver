from numpy import array, linalg, matmul, sum, newaxis
from questionary import select, text
"""
#4x + 3y + 2z = 25
#-2x + 2y + 3z = -10
#3x -5y + 2z = -4

# Using the inv() and dot() Methods
A = array([[4, 3, 2], [-2, 2, 3], [3, -5, 2]])
B = array([25, -10, -4])
X = linalg.inv(A).dot(B)

print(X)

# Using the solve() Method
A = array([[4, 3, 2], [-2, 2, 3], [3, -5, 2]])
B = array([25, -10, -4])
X2 = linalg.solve(A,B)

print(X2)

"""


def init():
    inp = select("Choose an option",choices=["Solve a matrix", "Add matricies", "Multiply two matricies", "Calculate cofactor of matrix", "Calculate determinant of matrix"],qmark="->", pointer="-->",instruction="(Use arrow keys)").ask()
    if inp is None:return
    if "Solve" in inp:solve()
    elif "Add" in inp:add()
    elif "cofactor" in inp:cofactor()
    elif "determinant" in inp:determinant()
    else:multiply()


def check_int(inp):
    try:inp = int(inp)
    except:return False
    else:return True


def rc(before=""):
    return int(text(f"{before}How many rows are there?\n--> ", qmark="->",validate=check_int).ask()), int(text(f"{before}How many columns are there?\n--> ", qmark="->",validate=check_int).ask())


def solve():
    rows, columns = rc("[MATRIX] ")
    try:print(linalg.solve(array([[float(num)for num in text(f"[CONSTANTS (XYZ)] Input {columns} number(s) seperated by a comma. No Spaces.\n--> ",qmark="->").ask().split(",")]for row in range(rows)]),array([float(num)for num in text(f"[ANSWERS] Input {columns} number(s) spereated by comma. No Spaces.\n--> ",qmark="->").ask().split(",")])))
    except linalg.LinAlgError:
        print("\nLast 2 dimensions of the array must be square.\n")
        init()


def add():
    rows, columns = rc("[BOTH MATRICIES] ")
    print(sum([array([[float(num)for num in text(f"Matrix: ({i+1}), Row: ({row+1}) [CONSTANTS (XYZ)] Input {columns} number(s) seperated by a comma. No Spaces.\n--> ",qmark="->").ask().split(",")]for row in range(rows)])for i in range(float(text("How many matricies do you want to add?\n--> ",qmark="->").ask()))],axis=0))


def multiply():
    rows, columns = rc("[FIRST MATRIX] ")
    full_one = array([[float(num)for num in text(f"(1) ({row+1}) [CONSTANTS (XYZ)] Input {columns} number(s) seperated by a comma. No Spaces.\n--> ",qmark="->").ask().split(",")] for row in range(rows)])
    rows, columns = rc("[SECOND MATRIX] ")
    full_two = array([[float(num)for num in text(f"(2) ({row+1}) [CONSTANTS (XYZ)] Input {columns} number(s) seperated by a comma. No Spaces.\n--> ",qmark="->").ask().split(",")] for row in range(rows)])
    print(matmul(full_one, full_two))

def determinant():
    rows, columns = rc("[MATRIX] ")
    print(linalg.det(array([[float(num)for num in text(f"[CONSTANTS (XYZ)] Input {columns} number(s) seperated by a comma. No Spaces.\n--> ",qmark="->").ask().split(",")]for row in range(rows)])))

def cofactor():
    rows, columns = rc("[MATRIX] ")
    matrix = array([[float(num)for num in text(f"[CONSTANTS (XYZ)] Input {columns} number(s) seperated by a comma. No Spaces.\n--> ",qmark="->").ask().split(",")]for row in range(rows)])
    print(linalg.inv(matrix).T * linalg.det(matrix))

# Minor not finished yet.
def minor():
    rows, columns = rc("[MATRIX] ")
    arr = array([[float(num)for num in text(f"[CONSTANTS (XYZ)] Input {columns} number(s) seperated by a comma. No Spaces.\n--> ",qmark="->").ask().split(",")]for row in range(rows)])
    
    print([arr[array(list(range(i))+list(range(i+1,arr.shape[0])))[:,newaxis],array(list(range(j))+list(range(j+1,arr.shape[1])))] for i,j in arr])

init()
