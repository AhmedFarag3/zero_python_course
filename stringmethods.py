#strip function 
a = " ahmed mahmoud"
print(a.strip("a")) #in this method it is supposed to remove the letter a but due to the space before the a it didnt
print(a.lstrip())

#title()  this function takes the string and convert the first letter into capital 
b = "ahmed mahmoud mohamed farag"
print(b.title())

#capitalize function the difference between it and the title function that the letters after the numbers are not affected and this function affects the first word in the string
c  = "ahmed mahmoud mahemd farag"
print(c.capitalize())
# lower and upper case function 
namesmale = "aHmEd"
namecapital = "AhmED"
print(namesmale.upper())
print(namecapital.lower())