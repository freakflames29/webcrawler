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

#iit kanpur import
import iit_kan
import iit_kan_gs

# nit bhopal
import nit_bhop

# nit jaipur
import nit_jaipur
import nit_jaipur_gs



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


def fun_nit_jaipur(name,url):
    print()
    ob = nit_jaipur.NitJaipur()
    ob.scrap()
    print("Finding other profiles of researchers (this may take a while)")

    gs=nit_jaipur_gs.Nit_jaipur_gs()
    gs.start()

    mycursor = mydb.cursor()
    sql = "SELECT * FROM nit_jaipur"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for row in myresult:
        if row[2]==None:
            print("Name: ", row[1])
            print("--------------------------------" * 4)
            with open("../profiles/nit_jaipur_profiles.txt", "a") as f:
                f.write("Name: " + row[1] + '\n')
                f.write("--------------------------------" * 4 + '\n')
                f.write('\n')
                f.close()
        else:
            print("Name: ", row[1])
            print("Google Scholar: ", row[2])
            print("--------------------------------" * 4)
            with open("../profiles/nit_jaipur_profiles.txt", "a") as f:
                f.write("Name: " + row[1] + '\n')
                f.write("Google Scholar: " + row[2] + '\n')
                f.write("--------------------------------" * 4 + '\n')
                f.write('\n')
                f.close()

    print()
    print("[+] Done! all profiles are saved in the directory 'profiles'")



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


def fun_iit_kan(name,url):
    print()
    iit_kan.callurls(url)
    print("Finding other profiles of researchers (this may take a while)")

    iit_kan_gs.gs_start()

    inst_name = name.upper()
    print("[+] Generating profiles for " + inst_name)
    print()
    generate_profile('iit_kan')
    print()
    print("[+] Done! all profiles are saved in the directory 'profiles'")

def fun_nit_bhopal(name,url):
    ob = nit_bhop.NitBhp()
    ob.scrap()
    inst_name = name.upper()
    print("\n[+] Generating profiles for " + inst_name)
    print()
    # generate_profile('nit_bhop')
    mycur=mydb.cursor()
    sql="SELECT * FROM nit_bhop;"
    mycur.execute(sql)
    myresult=mycur.fetchall()
    for row in myresult:
        print("Profile links: ",row[1])
        print("--------------------------------"*4)
        print()
        with open("../profiles/"+"nit_bhop"+"_profiles.txt","a") as f:
            f.write("Profile Links: "+row[1]+'\n')
            f.write("--------------------------------"*4+'\n')
            f.write('\n')
            f.close()

    print()
    print("[+] Done! all profiles are saved in the directory 'profiles'")


def main():
    name = input("Enter the name of the institute: ")
    url = input("Enter the url of the institute: ")

    if len(name) > 0 and (name.casefold() == "iit bombay".casefold() or name.casefold() == "Indian Institute of Technology Bombay".casefold()):
        print("[+] " + name)
        print()
        fun_iit_bombay(name, url[:-1])

    elif len(name) > 0 and (
            name.casefold() == "iit delhi".casefold() or name.casefold() == "Indian Institute of Technology delhi".casefold()):
        print("[+] " + name)
        fun_iit_delhi(name, url[:-1])

    elif len(name) > 0 and (
            name.casefold() == "iit hyderabad".casefold() or name.casefold() == "Indian Institute of Technology hyderabad".casefold()):
        print("[+] " + name)
        fun_iit_hyd(name, url[:-1])

    elif len(name) > 0 and (
            name.casefold() == "iit kanpur".casefold() or name.casefold() == "Indian Institute of Technology kanpur".casefold()):
        print("[+] " + name)
        fun_iit_kan(name, url[:-1])

    elif len(name) > 0 and (
            name.casefold() == "nit bhopal".casefold() or name.casefold() == "Maulana Azad National Institute of Technology Bhopal".casefold()):
        print("[+] " + name)
        fun_nit_bhopal(name, url[:-1])

    elif len(name) > 0 and (
            name.casefold() == "nit jaipur".casefold() or name.casefold() == "Malaviya National Institute of Technology Jaipur".casefold() or name.casefold() == "MNIT".casefold()):
        print("[+] " + name)
        fun_nit_jaipur(name, url[:-1])


    else:
        print("OOps! Check the name please")


main()
