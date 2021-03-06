import s01_web_pen
import s02_req
import s03_web_req
import s04_authenticatoin as s04_authentication
import sql_inject
import xss


def main():
    while True:
        print("Available actions:")
        print("1. 01_web_pen")
        print("2. 02_req")
        print("3. 03_web_req")
        print("4. 04_authentication")
        print("5. sql_inject")
        print("6. xss detection")
        print("0. exit")
        choice = int(input("Choose action: "))
        print()
        if choice == 0:
            break
        elif choice == 1:
            s01_web_pen.main()
        elif choice == 2:
            s02_req.main()
        elif choice == 3:
            s03_web_req.main()
        elif choice == 4:
            s04_authentication.main()
        elif choice == 5:
            sql_inject.main()
        elif choice == 6:
            xss.main()
        print()


if __name__ == "__main__":
    main()
