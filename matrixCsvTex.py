import pandas as pd

def main():
#     input_file = input("enter .csv file : ")
#     output_file = input("enter output file name : ")

    input_file = pd.read_csv("./A.csv", header = None)
    output_file = open("a.txt", "a")


    for row_index in range(0, len(input_file)):
        for column_index in range(0, len(input_file[row_index])):
            current_value = input_file[row_index][column_index]
            if (column_index != (len(input_file[row_index]) - 1)):
                current_value = round(current_value, 4)
                output_file.write(str(current_value) + " & ")
            else:
                current_value = round(current_value, 4)
                output_file.write(str(current_value))
        if (row_index != (len(input_file) - 1)):
            output_file.write(" \\\ ")
    
    output_file.close()



if __name__ == "__main__":
    main()