country = ["india", "spain", "france", "germany", "norway"]
capital = ["delhi", "madrid", "paris", "berlin", "oslo"]
a = {key: val for(key, val) in zip(country, capital)}
x = input()
print(a[x])
