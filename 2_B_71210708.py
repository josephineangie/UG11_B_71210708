str = "string"
int = 12345

def check_data_type(kata,tebakan):
    tebakan = tebakan.lower()
    if (type(kata) == type(str)) and (tebakan == "str"):
        print("Jawaban anda benar")
        return "True"
    elif (type(kata) == type(int)) and (tebakan == "int"):
        print("Jawaban anda benar")
        return "True"
    elif (type(kata) == type(int)) and (tebakan == "str"):
        print("Jawaban anda salah, seharusnya adalah: int")
        return "False"
    elif (type(kata) == type(str)) and (tebakan == "int"):
        print("Jawaban anda salah, seharusnya adalah: str")
        return "False"
    else:
        print("Jawaban anda tidak valid")
        return "False"

print(check_data_type("Kevin","STr"))
print(check_data_type("Kevin","str"))
print(check_data_type(12345,"str"))
print(check_data_type("9347","int"))
print(check_data_type(9876,"int"))