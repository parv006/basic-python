import pickle
while True:
    print('''enter choice
       1. add record 
       2. diplay record
       3. search record
       4. exit 
    ''')
    l=[]
    ch=int(input('enter your choice'))
    if ch==1:
        f=open('file1.dat','ab')
        id1=int(input('enter your id'))
        name=input('enter your name')
        roll_no=int(input('enter your roll no'))
        l=[id1,name,roll_no]
        pickle.dump(l,f)
        print('data sucessfully stored')
        f.close()
    elif ch==2:
        f=open('file1.dat','rb')
        while True:
            try:
                dt=pickle.load(f)
                print(dt)
            except EOFError:
                break
        f.close()
    elif ch==3:
        s=int(input('enter roll no to search'))
        f=open('file1.dat','rb')
        fl=False
        while True:
            try:
                dt=pickle.load(f)
                for i in dt:
                    if i==s:
                        fl=True
                        print('record found')
                        print('id no. ',dt[0])
                        print('name ',dt[1])
                        print('roll no ',dt[2])
            except EOFError:
                break  
        if fl==False:
            print('record not found')     
            break    
        f.close()
                
    elif ch==4:
        break
    else :
        print('invalid choice')