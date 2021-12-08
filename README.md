# notebook
Notes

## git workflow
- create repo
- clone repo
```
git clone repo_name
```
- cd into repo directory and make changes to the files. Use `git add` to tell git to keep track of the files
```
git add file_name
git add .
```
- Commit changes
```
git commit -m "messages"
```
- Push changes
```
git push origin main
```
## Python 
### Files Read/Write
``` python
with open('EURUSD=X.csv','r') as f:
    lines=f.read()

print(lines)
print(type(lines))

lines_list = lines.split('\n')
print(lines_list)
print(type(lines_list))
```