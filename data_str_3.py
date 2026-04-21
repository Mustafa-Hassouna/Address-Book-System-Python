web_page = []
for i in range(1,4):
    web_page.append("web"+str(i))
print(web_page)
# back 
web_page.pop()
# ['web1', 'web2']
print("redirect",web_page[-1]) # web_page(-1) == web2
# back 
web_page.pop()
# ['web1']
print("redirect",web_page[-1])
print(bool([0]))
