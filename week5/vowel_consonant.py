"""
Read multiple lines of text from the user and store it in a file called “INPUT.txt”. Read
each character one by one from the file and store vowel characters in “VOWEL.txt’
and consonant in “CONSONANT.txt”. Print all the file contents.
"""

# Getting number of lines and text
n=int(input("Enter the number of lines:"))
txt =''
print("Enter the lines:")
for i in range(n):
    txt+=input()
#write the txt into Input.txt
with open('Input.txt','w') as fw:
    fw.write(txt)

#Opening Files to write the output
vow = open("VOWEL.txt",'w')
con = open("CONSONANT.txt","w")

#Read the text from Input.txt
rtxt = ''
with open('Input.txt') as fr:
    rtxt=fr.read()
for i in rtxt:
    if i.lower() in ['a','e','i','o','u']:
        vow.write(i)
    else:
        con.write(i)

vow.close()
con.close()
