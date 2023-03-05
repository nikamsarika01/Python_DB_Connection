from python_DB import DBHlper

def main():
    db=DBHlper()
    while True:
        print("press 1 to insert new user")
        print("press 2 to display new user")
        print("press 3 to delete new user")
        print("press 4 to update new user")
        print("press 5 to exit new user")
        print()

        try:
            choice=int(input())
            if choice==1:

                uid=int(input("enter user id"))
                uname = input("enter user name")
                uphone = int(input("enter user phone"))
                db.insert_user(uid,uname,uphone)

            elif choice == 2:
                db.fech_user()


            elif choice == 3:
                userid=int(input("enter yser id which you want to delete"))
                db.delete_user(userid)


            elif choice == 4:
                uid = int(input("enter user id"))
                uname = input("enter user new_name")
                uphone = int(input("enter user new_phone"))
                db.update_user(uid,uname,uphone)


            elif choice == 5:
                break
            else:
                print('Invalid input try again ')
        except Exception as e:
            print(e)
            print("inalid detail plx try again")
if __name__=="__main__":
    main()
