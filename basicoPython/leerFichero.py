#f = open("demofile.txt", "r")
#print(f.read())

f = open("demofile2.txt", "a")#anadir contenido
f.write("Now the file has more content!")
f.close()


f = open("demofile2.txt", "r")#leo el contenido
print(f.read())

f = open("demofile2.txt", "w")
f.write("Woops! I have deleted the content!")#escribo eliminando todo
f.close()


f = open("demofile2.txt", "r")#leo el contenido
print(f.read())

#os.remove(demofile2.txt) elimino archivo
#os.rmdir(nombrecarpeta) elimino carpeta