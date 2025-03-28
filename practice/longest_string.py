string = 'ttrctrcuuyuioyuiorprd' 

string = 'adccfirtyuift'

res = ''
result = ''
for i in range(len(string)-1):
    if string[i] != string[i+1]:
        if string[i] in res or string[i] == string[i+1]:
            if len(result)< len(res):
                result = res
                res = ''
    res+=string[i]

print(result)
