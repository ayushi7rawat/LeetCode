a = ["bella","label","roller"]
res = ''
for i in a[0]:
  if i in a[1] and a[2]:
    res += i
ans = ''
for i in a[2]:
    if i in res:
        ans += i

print(ans)
print(res)
print(a[0])
print(a[1])