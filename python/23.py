table=''.maketrans('abcdef123','uvwxyz@#$')
s="Python is a greate programming language. I like it!"
print(s.translate(table))