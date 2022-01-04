from gen_profile import generate_profile
from DB_CON import mydb
# iit bombay import

import iit_bomb
import iit_bomb_gs
# iit delhi import
import iit_del
import iit_del_gs

# iit hyderabad import
import iit_hyd
import iit_hyd_gs


def hyd_profile():
    file_name = "../profiles/" + "iit_hyd" + "_profiles.txt"
    mycur = mydb.cursor()
    sql = "SELECT * FROM iit_hyd;"
    mycur.execute(sql)
    myresult = mycur.fetchall()
    for row in myresult:
        if row[3] == None:
            print("Name: ", row[1])
            print("Description: ", row[2])
            print("Project: ", row[4])
            print("--------------------------------" * 4)
            print()
            with open(file_name, "a") as f:
                f.write("Name: " + row[1] + '\n')
                f.write("Description: " + row[2] + '\n')
                f.write("Project: " + row[4] + '\n')
                f.write("--------------------------------" * 4 + '\n')
                f.write('\n')
                f.close()
        else:
            print("Name: ", row[1])
            print("Description: ", row[2])
            print("Google Scholar: ", row[3])
            print("Project: ", row[4])
            print("--------------------------------" * 4)
            print()
            with open(file_name, "a") as f:
                f.write("Name: " + row[1] + '\n')
                f.write("Description: " + row[2] + '\n')
                f.write("Google Scholar: " + row[3] + '\n')
                f.write("Project: " + row[4] + '\n')
                f.write("--------------------------------" * 4 + '\n')
                f.write('\n')
                f.close()


def fun_iit_bombay(name, url):
    print()
    ob = iit_bomb.IIT_BOMB()
    ob.scrap()

    print("Finding other profiles of researchers (this may take a while)")

    gs = iit_bomb_gs.IIT_BOMB_GS()
    gs.run()

    inst_name = name.upper()
    print("[+] Generating profiles for " + inst_name)
    print()
    generate_profile('iit_bomb')
    print()
    print("[+] Done! all profiles are saved in the directory 'profiles'")


def fun_iit_delhi(name, url):
    # pass
    print()
    obj = iit_del.Delhi()
    print("Finding researchers...")
    obj = obj.scrap_info()
    print("Finding other profiles of researchers (this may take a while)")

    gs = iit_del_gs.IIT_DEL_GS()
    gs.run()

    inst_name = name.upper()
    print("[+] Generating profiles for " + inst_name)
    generate_profile('iit_delhi')
    print()
    print("[+] Done! all profiles are saved in the directory 'profiles'")


def fun_iit_hyd(name, url):
    print()
    ob = iit_hyd.IIT_HYD()
    ob.run()

    print("Finding other profiles of researchers (this may take a while)")

    gs = iit_hyd_gs.IIT_HYD_GS()
    gs.run()

    inst_name = name.upper()
    print("[+] Generating profiles for " + inst_name)
    print()
    hyd_profile()
    print("[+] Done! all profiles are saved in the directory 'profiles'")



def main():
    name = input("Enter the name of the institute: ")
    url = input("Enter the url of the institute: ")
    if len(name) > 0 and (
            name.casefold() == "iit bombay".casefold() or name.casefold() == "Indian Institute of Technology Bombay".casefold()):
        print("[+] " + name)
        print()
        fun_iit_bombay(name, url)

    elif len(name) > 0 and (
            name.casefold() == "iit delhi".casefold() or name.casefold() == "Indian Institute of Technology delhi".casefold()):
        print("[+] " + name)
        fun_iit_delhi(name, url)
    elif len(name) > 0 and (
            name.casefold() == "iit hyderabad".casefold() or name.casefold() == "Indian Institute of Technology hyderabad".casefold()):
        print("[+] " + name)
        fun_iit_hyd(name, url)


    else:
        print("OOps! Check the name please")


main()
