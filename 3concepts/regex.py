import re #module for regular expressions
regex = re.compile(r'\d\d\d-\d\d\d')  #\d matches a digit between 0 to 9
matchregex=regex.search("contact this num 123-456")
print(matchregex.group())

#adding a number in curly braces tells the python to match the pattern multiple times.
regex = re.compile(r'\d{3}-\d{3}')
matchregex = regex.search("contact this num 123-456")
print(matchregex.group())

#we can make the regex patterns into groups by using parenthesis.
regex = re.compile(r'(\d{3})-(\d{3})')
matchregex = regex.search("contact this num 123-456")
print(matchregex.group(1), matchregex.group(2))

#matching multiple regex patterns with pipe character.
regex = re.compile(r'sai|yaswanth|vendra|yaswanth sai')
matchregex = regex.search("hello yaswanth")
print(matchregex.group())

#optional regex instances matching
regex = re.compile(r'yaswanth (sai)?')
matchregex = regex.search("hello yaswanth sai")
print(matchregex.group())

regex = re.compile(r'yaswanth(sai)?')
matchregex = regex.search("hello yaswanth")
print(matchregex.group())
