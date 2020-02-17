city_file=["delhi","nagpur","mumbai","bihar","bhopal"]
cities=open("different cities.html","w+")
cities.write("<html>\n")
cities.write("<head>\n")
cities.write("<title> cities </title>\n")
cities.write("</head>\n")
cities.write("<body>\n")
cities.write("<ul>\n")
for city in city_file:
    cities.write("<li>"+city+"</li>\n")
cities.write("</ul>\n")
cities.write("</body>\n")
cities.write("</html>")
cities.close()

cities1=open("different cities.html","r+")
city=cities1.read()
print city
cities1.close()



