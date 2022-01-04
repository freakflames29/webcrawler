from gen_profile import generate_profile
import requests as rq
from bs4 import BeautifulSoup as bs

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

# iit kanpur import
import iit_kan
import iit_kan_gs

# nit bhopal
import nit_bhop

# nit jaipur
import nit_jaipur
import nit_jaipur_gs

# nit jalandhar
import nit_jalandhar

# nit karnataka
import nit_karnat
import nit_karanatak_gs
# nit kurukshetra
import nit_kurks
import nit_kuruks_gs
# nit nagpur
import nit_nagpur
import nit_nagpur_gs
# IIIT gwalior
import trip_iit_gwalior
import trip_gwalior_gs


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


def fun_nit_kuruk(name, url):
    print()
    ob = nit_kurks.NitKuruk()
    ob.scrap()
    print("Finding other profiles of researchers (this may take a while)")
    gs = nit_kuruks_gs.NitKurk()
    gs.start()

    inst_name = name.upper()
    print("[+] Generating profiles for " + inst_name)
    generate_profile('nit_kuruk')
    print()
    print("[+] Done! all profiles are saved in the directory 'profiles'")


def fun_nit_nagpur(name, url):
    print()
    ob = nit_nagpur.NitNag()
    ob.scrap()
    print("Finding other profiles of researchers (this may take a while)")
    gs = nit_nagpur_gs.NitNagGs()
    gs.start()
    inst_name = name.upper()
    print("[+] Generating profiles for " + inst_name)
    generate_profile('nit_nagpur')
    print()
    print("[+] Done! all profiles are saved in the directory 'profiles'")


def fun_trip_gwalior(name, url):
    print()
    ob = trip_iit_gwalior.IITGwa()
    ob.scrapdata()
    ob.start()
    print("Finding other profiles of researchers (this may take a while)\n")
    gs = trip_gwalior_gs.TripGwaGs()
    gs.start()
    inst_name = name.upper()
    print("[+] Generating profiles for " + inst_name)
    generate_profile('trip_gwalior')
    print()
    print("[+] Done! all profiles are saved in the directory 'profiles'")


def fun_nit_karnatak(name, url):
    print()
    ob = nit_karnat.NitKarnatk()
    ob.find_dept_links()
    print("Finding other profiles of researchers (this may take a while)\n")

    gs = nit_karanatak_gs.NitKarnatakGS()
    gs.start()
    inst_name = name.upper()
    print("[+] Generating profiles for " + inst_name)
    generate_profile('nit_karnatak')
    print()
    print("[+] Done! all profiles are saved in the directory 'profiles'")


def fun_nit_jaipur(name, url):
    print()
    ob = nit_jaipur.NitJaipur()
    ob.scrap()
    print("Finding other profiles of researchers (this may take a while)")

    gs = nit_jaipur_gs.Nit_jaipur_gs()
    gs.start()

    mycursor = mydb.cursor()
    sql = "SELECT * FROM nit_jaipur"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for row in myresult:
        if row[2] == None:
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


def fun_nit_jalandhar(name, url):
    print()
    ob = nit_jalandhar.NitJala()
    ob.scrap()
    print("Finding other profiles of researchers (this may take a while)\n")
    inst_name = name.upper()
    print("[+] Generating profiles for " + inst_name)
    print()
    file_name = "../profiles/" + "nit_jalandhar" + "_profiles.txt"

    mycursor = mydb.cursor()
    sql = "SELECT * FROM nit_jal"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for row in myresult:
        print("Profiles: ", row[1])
        print("--------------------------------" * 4 + '\n')
        with open(file_name, "a") as f:
            f.write("Profiles: " + row[1] + '\n')
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


def fun_iit_kan(name, url):
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


def fun_nit_bhopal(name, url):
    ob = nit_bhop.NitBhp()
    ob.scrap()
    inst_name = name.upper()
    print("\n[+] Generating profiles for " + inst_name)
    print()
    # generate_profile('nit_bhop')
    mycur = mydb.cursor()
    sql = "SELECT * FROM nit_bhop;"
    mycur.execute(sql)
    myresult = mycur.fetchall()
    for row in myresult:
        print("Profile links: ", row[1])
        print("--------------------------------" * 4)
        print()
        with open("../profiles/" + "nit_bhop" + "_profiles.txt", "a") as f:
            f.write("Profile Links: " + row[1] + '\n')
            f.write("--------------------------------" * 4 + '\n')
            f.write('\n')
            f.close()

    print()
    print("[+] Done! all profiles are saved in the directory 'profiles'")


def find_res_links(name, urlname):
    filename = "../profiles/" + name + "_profiles.txt"
    user_url = urlname
    print("[+] Finding potential urls for researchers info...\n")
    orUrl = user_url
    reqs = rq.get(urlname)
    soup = bs(reqs.text, 'html.parser')
    urls = []
    for link in soup.find_all('a'):
        urls.append(link.get('href'))
    # print(len(urls))
    for i in urls:
        # print(i)
        if i == "{ul}/".format(ul=user_url) or i == "/":
            continue
        elif urls.count(i) == 0:
            find_res_links(orUrl + i)

    newurls = list(set(urls))
    research_urls = []
    for i in newurls:
        if i is not None and i.find("research") != -1:
            # print(i)
            if i.find(urlname) == -1:

                if i.startswith(''):
                    research_urls.append(orUrl+"/"+i)
            else:
                research_urls.append(i)
    if len(research_urls) > 0:
        for i in research_urls:
            print(i)
            print("--------------------------------" * 4)
            with open(filename, "a") as f:
                f.write("Links: " + i + '\n')
                f.write("--------------------------------" * 4 + '\n')
                f.write('\n')
                f.close()
        print()
        print("[+] "+str(len(research_urls))+" potential links found and saved to the directory named 'profiles'")
    else:
        print("[+] No potential links found")


def main():
    name = input("Enter the name of the institute: ")
    url = input("Enter the url of the institute: ")

    if len(name) > 0 and (
            name.casefold() == "iit bombay".casefold() or name.casefold() == "Indian Institute of Technology Bombay".casefold()):
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

    elif len(name) > 0 and (
            name.casefold() == "nit jalandhar".casefold() or name.casefold() == "Dr. B. R. Ambedkar National Institute of Technology Jalandhar".casefold()):
        print("[+] " + name)
        fun_nit_jalandhar(name, url[:-1])
    elif len(name) > 0 and (
            name.casefold() == "nit karnataka".casefold() or name.casefold() == "National Institute of Technology Karnataka".casefold() or name.casefold() == "NITK".casefold()):
        print("[+] " + name)
        fun_nit_karnatak(name, url[:-1])

    elif len(name) > 0 and (
            name.casefold() == "nit kurukshetra".casefold() or name.casefold() == "National Institute of Technology Kurukshetra".casefold()):
        print("[+] " + name)
        fun_nit_kuruk(name, url[:-1])

    elif len(name) > 0 and (
            name.casefold() == "nit nagpur".casefold() or name.casefold() == "Visvesvaraya National Institute of Technology Nagpur".casefold() or name.casefold() == "vnit nagpur".casefold()):
        print("[+] " + name)
        fun_nit_nagpur(name, url[:-1])
    elif len(name) > 0 and (
            name.casefold() == "iiit gwalior".casefold() or name.casefold() == "Atal Bihari Vajpayee Indian Institute of Information Technology and Management Gwalior".casefold() or name.casefold() == "Indian Institute of Information Technology and Management Gwalior".casefold()):
        print("[+] " + name)
        fun_trip_gwalior(name, url[:-1])


    else:
        find_res_links(name,url[:-1])


main()
# find_res_links(url[:-1])
