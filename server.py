import sqlite3
conn=sqlite3.connect('books.db')
c=conn.cursor()
name=raw_input("Please Enter UserName : ")
password=raw_input("Please Enter Password : ")
while(True):
    typ=input("Enter Scenario : ")
    if typ==1:
        book_num=input()
        c.execute("SELECT reserved_books,books_left,takenList,reserved_list FROM data WHERE ref_ID=?",(book_num,))
        res,lef,tl,rl=c.fetchall()[0]
        if res < lef :
            lef-=1
            c.execute("UPDATE data SET books_left=? WHERE ref_ID=?",(lef,book_num))
            if tl==None:
                tl=[name]
            else:
                tl=eval(tl)
                if name not in tl:
                    tl.append(name)
                else:
                    print "Already Taken by You"
            c.execute("UPDATE data SET takenList=? WHERE ref_ID=?",(str(tl),book_num))
            conn.commit()
            if rl!=None:
                rl=eval(rl)
                if name in rl:
                    res-=1
                    rl.remove(name)
                    c.execute("UPDATE data SET reserved_books=?,reserved_list=? WHERE ref_ID=?",(res,str(rl),book_num))
                    conn.commit()
                    break
        else:
            check=False
            c.execute("SELECT reserved_books,books_left,takenList,reserved_list FROM data WHERE ref_ID=?",(book_num))
            res,lef,tl,rl=c.fetchall()[0]
            if rl!=None:
                rl=eval(rl)
                if name in rl:
                    check=True
                    res-=1
                    rl.remove(name)
                    c.execute("UPDATE data SET reserved_books=?,reserved_list=? WHERE ref_ID=?",(res,str(rl),book_num))
                    conn.commit()
                    break
            if check:
                print "Sorry All Books Are RESERVED."
        print "Scenario 1 Ends"
    if typ==2:
        n=raw_input()
        if n[0]=='/':
            if n[1]!='/':
                aut=''
                for i in range(1,len(n)):
                    aut+=n[i]
                c.execute("SELECT book_name,ref_ID FROM data WHERE author=?",(aut,))
                a=c.fetchall()
                if a==None:
                    print "Sorry No Book of this Author is Found"
                    print "Scenario 2 Ends"
                    continue
                else:
                    print a
                    proceed=input("Enter the Reference ID : ")
                    c.execute("SELECT reserved_books,books_left,takenList,reserved_list,book_name FROM data WHERE ref_ID=?",(proceed,))
                    res,lef,tl,rl,bookName=c.fetchall()[0]
                    print "Book Name = "+bookName+" No of books left =  "+str(lef)
                    print "People who have Taken : ",tl
                    print "No of books reserved = "+str(res)
                    print "People who have Reserved : ",rl

                    if res < lef :
                        pro=input("Yes : 1 ,No : Any Number  : ")
                        if pro ==1:
                            res+=1
                            lef-=1
                            if rl!=None:
                                rl=eval(rl)
                                rl.append(name)
                            else:
                                rl=[name]
                            c.execute("UPDATE data SET reserved_books=?,reserved_list=?,books_left=? WHERE ref_ID=?",(res,str(rl),lef,proceed))
                            conn.commit()
            else:
                bookName=''
                for i in range(2,len(n)):
                    bookName+=n[i]
                check=False
                c.execute("SELECT reserved_books,books_left,takenList,reserved_list,book_name FROM data WHERE book_name=?",(bookName,))
                res,lef,tl,rl,bookName=c.fetchall()[0]
                if res!=None:
                    check=True
                    print "Book Name = "+bookName+" No of books left =  "+str(lef)
                    print "People who have Taken : ",tl
                    print "No of books reserved = "+str(res)
                    print "People who have Reserved : ",rl
                    if res <lef:
                        pro=input("Yes : 1 else Any Number : ")
                        if pro ==1:
                            res+=1
                            lef-=1
                            if rl!=None:
                                rl=eval(rl)
                                rl.append(name)
                            else:
                                rl=[name]
                            c.execute("UPDATE data SET reserved_books=?,reserved_list=?,books_left=? WHERE ref_ID=?",(res,str(rl),lef,proceed))
                            conn.commit()
                if check:
                    print "No such Book is Present in Library"
        else:
            c.execute("SELECT book_name,ref_ID FROM data WHERE genre=?",(n,))
            a=c.fetchall()
            if a==None:
                print "Sorry No Book of this Genre is Found"
                print "Scenario 2 Ends"
                continue
            else:
                print a
                proceed=input("Enter the Reference ID : ")
                c.execute("SELECT reserved_books,books_left,takenList,reserved_list FROM data WHERE ref_ID=?",(proceed,))
                res,lef,tl,rl=c.fetchall()[0]
                print "Book Name = "+bookName+" No of books left =  "+str(lef)
                print "People who have Taken : ",tl
                print "No of books reserved = "+str(res)
                print "People who have Reserved : ",rl

                if res < lef :
                    pro=input("Yes : 1 ,No : Any Number  : ")
                    if pro ==1:
                        res+=1
                        lef-=1
                        if rl!=None:
                            rl=eval(rl)
                            rl.append(name)
                        else:
                            rl=[name]
                        c.execute("UPDATE data SET reserved_books=?,reserved_list=?,books_left=? WHERE ref_ID=?",(res,str(rl),lef,proceed))
                        conn.commit()
        print "Scenario 2 Ends"
    if typ==3:
        print "Scenario 3 Thanking You... Exiting.."
        break

    











