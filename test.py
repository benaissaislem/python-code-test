def check_number_in_line(ch):
    com=['0','1','2','3','4','5','6','7','8','9']
    num=0
    for i in ch :
        #check the first number
        if i in com:
            #print ("first number =" ,i)
            num =num + 10* (int(i))  
            break

    for i in reversed(ch) :
        #check the first number
        if i in com:
            #print ("last number =" ,i)
            num =num + int(i)
            break
    return num

def process_text_file(file_path):
    somme=0
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line_number, line in enumerate(lines, start=1):
                line = line.strip()  
                result = check_number_in_line(line)
                somme=result+somme
                print(f"la valeur d'étalonnage n°  {line_number}: {result}")
            print ("En les ajoutant, on obtient ", somme)     
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = r"document.txt"


process_text_file(file_path)
