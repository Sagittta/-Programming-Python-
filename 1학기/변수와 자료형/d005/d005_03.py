d = {}
urls = {"google":"google.com", 18:"unesco.org"}
print(urls)

urls["z"] = "zzz"
print(urls)

urls["x"] = 2560
print(urls)

urls["x"] = 1920
print(urls)

del urls["x"]
print(urls)

urls.pop(18)
print(urls)

urls.clear()
print(urls)

urls = {"NCT":"윈윈, 도영, 재현, 텐", "방탄소년단":"RM, 뷔, 슈가, 지민"}
print(urls)
print(urls['NCT'])
urls['exo'] = ["백현", "수호", "경수", "카이"]
urls.get('방탄소년단')
'NCT' in urls       #true

'윈윈, 도영, 재현, 텐' in urls         #false
'윈윈, 도영, 재현, 텐' in urls.values()        #true

len(urls)
urls.keys()
urls.values()       #리스트 찾기 가능. 리스트 안에 하나를 찾기는 불가능
urls.items()        #키값 1, 내용 1, 키값1, 내용 1 ---

#dict ~~~

#list는 [] tuple은 () dictionary는 {} set(집합)은 
