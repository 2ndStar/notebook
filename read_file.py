with open('EURUSD=X.csv','r') as f:
    lines=f.read()

print(lines)
print(type(lines))

lines_list = lines.split('\n')
print(lines_list)
print(type(lines_list))