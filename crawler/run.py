from gen_profile import generate_profile
# iit bombay import

import iit_bomb
import iit_bomb_gs
# iit delhi import
import iit_del
import iit_del_gs




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

    else:
        print("OOps! Check the name please")


main()
