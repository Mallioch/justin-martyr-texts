from unicodedata import normalize
import sys

f = open("texts/" + sys.argv[1], "r")    
contents = f.read();
normalized_contents = normalize('NFC', contents)

print(normalized_contents);

