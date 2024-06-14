
alphabet_codes={'A':'$','a':'0','B':'$','b':'%','C':'4','c':'1','D':'!','d':'&','E':'~','e':'^','F':'-','f':'*','G':':','g':'?','H':'!','h':'=','I':'!','i':'>','J':'6','j':'3','K':'9','k':'%','L':'^','l':'@','M':'!','m':'*','N':'<','n':'>','O':'.','o':'?','P':';','p':'-','Q':'0','q':'~','R':'9','r':',','S':'&','s':'$','T':'0','t':'@','U':'*','u':'<','V':'!','v':'9','W':'^','w':'>','X':'&','x':'0','Y':'@','y':'?','Z':'8','z':'~'}


infile=open('info_security-1.txt','r')
line1=infile.readline()
outfile=open('encrypted.txt','w')
for letter in line1:
    if letter in alphabet_codes:
        outfile.write(alphabet_codes[letter])
    else:
        outfile.write('')
outfile.close()