
start_dir = "D:/desktop/3Dmodelle/gcode_mpcnc/"  //choose your working directory here
filename = input("filename>->")
filename = start_dir + filename

src_file = open(filename + ".nc", "r")
out_file = open(filename + ".gcode", "w")

for src_line in src_file:
    fc = str(src_line)[0]

    if fc=="X" or fc=="Y" or fc=="Z":
        out_file.write("G0 ")

    out_file.write(src_line)

src_file.close()
out_file.close()
