from tkinter import*
import socket 
pen = Tk()
pen.geometry("330x500")
pen.title("PORT SCANNER - H4WK OFCX")
def tarama():
    s1=str(enturl.get())
    liste=[21,22,23,25,80,139,443,445,3389]
    try:
        for port in liste:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result=sock.connect_ex((s1,port))
            if result== 0 :
                listsonuc.insert(1, "Port{} -> Açık".format(port))
            else:
                listsonuc.insert(1, "Port{} -> Kapalı   ".format(port))
                sock.close()
    except sock.error:
        print("Bilgisayar Yok")

lburl = Label(pen, text="URL veya İP Adresi", font="Verdana 12 ", fg="black",bg="white")
lburl.place(x=60, y=20)
listsonuc = Listbox(pen, font="Verdana 12 bold", width="25", height="17",fg="white", bg="black")
listsonuc.place(x=27, y=140)
enturl = Entry(pen, font="Verdana 12 bold", fg="blue")
enturl.place(x=50 ,y=50)
btntara=Button(pen, text="Portları Tara ", font="Verdana 12 bold",fg="white" ,bg="black", command=tarama)
btntara.place(x=80, y=90)

pen.mainloop()