filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames =[file.replace('.hpp', '.h')for file in filenames]  

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]