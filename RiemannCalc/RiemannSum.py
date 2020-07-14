from tkinter import *

root = Tk()
root.title("Calculus Calculators")

"""
Class Riemann: Takes user input from tkinter GUI and calculates Left, Right, Midpoint, and Trapezoidal 
Riemann sums for a given function. Riemann cannot currently accept function types log, ln, exponential, sqrt()
because of conflicts with math parsing from user entries. It can calculate delta X and output necessary work to find the 
area given upper and lower bounds.
"""


class Riemann:
    def __init__(self, lower, upper, func, rec):
        self.lower = int(lower)
        self.upper = int(upper)
        self.rec = int(rec)
        self.func = func

    def leftsums(self):
        delta_x = (self.upper - self.lower) / self.rec
        iteration = 0
        ctr = []
        for _ in range(self.rec):
            # print(math.sqrt(iteration))
            print(iteration)
            ctr.append(iteration)
            iteration += delta_x
        # print(*ctr, sep=') + ')
        fof_ctr = []
        for item in ctr:
            fof_ctr.append("f({})".format(item))
        print(*fof_ctr, sep=" + ")

    def rightsums(self):
        delta_x = (self.upper - self.lower) / self.rec
        iteration = delta_x
        ctr = []
        for _ in range(self.rec):
            print(iteration)
            ctr.append(iteration)
            iteration += delta_x
        fof_ctr = []
        for item in ctr:
            fof_ctr.append("f({})".format(item))
        print(*fof_ctr, sep=" + ")

    def midpointsums(self):
        delta_x = (self.upper - self.lower) / self.rec
        iteration_left = 0
        iteration_right = delta_x
        ctr_left = []
        ctr_right = []
        for _ in range(self.rec):
            ctr_left.append(iteration_left)
            ctr_right.append(iteration_right)
            iteration_left += delta_x
            iteration_right += delta_x
        mid_list = [ctr_left[i] + ctr_right[i] for i in range(len(ctr_left))]
        final_fof = []
        for item in mid_list:
            final_fof.append("[f({}) / 2]".format(item))
        print(*final_fof, sep=" + ")


# Create if statements to check for whatever sum the user wished to calculate: Left, Right, Midpoint, or Trapezoid.
# Later make a dictionary with keywords that correspond to class functions
def getvals():
    print(
        f"{function_value.get(), lower_limit_value.get(), upper_limit_entry.get(), rectangles_value.get(), type_of.get()} "
    )
    calculate = Riemann(
        lower_limit_value.get(),
        upper_limit_entry.get(),
        function_value.get(),
        rectangles_value.get(),
    )
    if type_of.get() == "Left":
        calculate.leftsums()
    elif type_of.get() == "Right":
        calculate.rightsums()
    elif type_of.get() == "Midpoint":
        calculate.midpointsums()
    elif type_of.get() == "Trapezoid":
        print("Coming soon...")


root.geometry("500x250")
# Heading
Label(root, text="Riemann Sums", font="TimesNewRoman 16 bold", pady=15).grid(
    row=0, column=3
)
# Text for the form
function = Label(root, text="Function")
lower_limit = Label(root, text="Lower Limit")
upper_limit = Label(root, text="Upper Limit")
rectangles = Label(root, text="# Of Rectangles")


# Pack text for the form
function.grid(row=1, column=2)
lower_limit.grid(row=2, column=2)
upper_limit.grid(row=3, column=2)
rectangles.grid(row=4, column=2)

# Tkinter variable for storing entries
function_value = StringVar()
lower_limit_value = StringVar()
upper_limit_value = StringVar()
rectangles_value = StringVar()

# Tkinter variable for storing entries via drop down menu
type_of = StringVar(root)

# Default value
type_of.set("Left")

w = OptionMenu(root, type_of, "Left", "Right", "Midpoint", "Trapezoid")
w.grid()

# Entries for the form
function_entry = Entry(root, textvariable=function_value)
lower_limit_entry = Entry(root, textvariable=lower_limit_value)
upper_limit_entry = Entry(root, textvariable=upper_limit_value)
rectangles_entry = Entry(root, textvariable=rectangles_value)

# Packing the Entries
function_entry.grid(row=1, column=3)
lower_limit_entry.grid(row=2, column=3)
upper_limit_entry.grid(row=3, column=3)
rectangles_entry.grid(row=4, column=3)

# Submit button that sends user entries to getvals function
Button(text="Calculate", command=getvals).grid(row=10, column=3)
root.mainloop()
