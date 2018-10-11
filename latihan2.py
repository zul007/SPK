lampu = [
    {"lampu": 1, "value":""},
    {"lampu": 2, "value":""},
    {"lampu": 3, "value":""},
    {"lampu": 4, "value":""},
]
nyalahijau = 3
for i in range(0, len(lampu)):
	if lampu[i]["lampu"]==nyalahijau:
		lampu[i]["value"]="hijau"
	else:
		lampu[i]["value"] = "merah"
print(lampu)
	