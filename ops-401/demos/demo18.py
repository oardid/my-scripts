import zipfile 

zip_file = input("Input path to zipped file: ")
password = input("Input pass:")

with zipfile.ZipFile(zip_file) as zf:
    zf.extractall(pwd=bytes(password,'utf-8'))