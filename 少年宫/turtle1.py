def a(leixing,neirong):

    if leixing=="str":
        print("\"",neirong,"\"")
    try:
        if leixing=="int":
            print(int(neirong))
        if leixing=="float":
            print(neirong/1)
    except Exception as e:
        print('oops, error occurs:',e)

            
# a("float","www")
a("float",2)
