from minizinc import Instance, Model, Solver

# Load model from file
nqueens = Model("./19_1.mzn")
# Find the MiniZinc solver configuration for Gecode
gecode = Solver.lookup("gecode")
# Create an Instance of the model for Gecode
instance = Instance(gecode, nqueens)

# Assign 4 to n
result = instance.solve()
# Output the array q
print(result)
