print('')
print('☆☆ NAO ZİP FİLE CRACKER ☆☆')
print('')
print('İNSTAGRAM : spynao')
print('')
zipname = input('ZİP DOSYASININ İSMİ (DİZİN) : ')
print('')
txtname = input('PASSWORD WORDLİST İSMİ (DİZİN) : ')
print('')

import zipfile

def extractFile(zfile, password):
    try:
        zfile.extractall(pwd=bytes(password, 'utf-8'))
        return password
    except:
        print('YANLIŞ PASSWORD : ' +password)
        return

def main():
    
    zfile = zipfile.ZipFile(zipname)
    passFile = open(txtname)
    for line in passFile.readlines():
        password = line.strip('\n')
        guess = extractFile(zfile, password)
        if guess:
            print()
            print('PASSWORD BULUNDU : ' +password)
            break

if __name__ == '__main__':
    main()