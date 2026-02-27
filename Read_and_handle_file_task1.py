try:
    file_handler=open('sample1.txt','rt')
    line_1=file_handler.readline()
    line_2=file_handler.readline()
    file_handler.close()
    print("Reding file content\n")
    print(f'line 1 :{line_1}\n')
    print(f'line 2 : {line_2}\n')

except FileNotFoundError as file_error:
    print(file_error)

