from DB_CON import mydb


def generate_profile(name_of_the_table):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM " + name_of_the_table + ";"
    file_name = "../profiles/" + name_of_the_table + "_profiles.txt"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    # print()
    # print(len(myresult[0]))
    if len(myresult[0]) == 4:
        for x in myresult:
            if x[3] == None:
                print("Name: " + x[1])
                print("Description: " + x[2])
                print("--------------------------------" * 4)
                with open(file_name, "a") as f:
                    f.write("Name: " + x[1] + '\n')
                    f.write("Description: " + x[2] + '\n')
                    f.write("--------------------------------" * 4 + '\n')
                    f.write('\n')
                    f.close()
            else:
                print("Name: " + x[1])
                print("Description: " + x[2])
                print("Google scholar: " + x[3])
                print("--------------------------------" * 4)
                with open(file_name, "a") as f:
                    f.write("Name: " + x[1] + '\n')
                    f.write("Description: " + x[2] + '\n')
                    f.write("Google scholar: " + x[3] + '\n')
                    f.write("--------------------------------" * 4 + '\n')
                    f.write('\n')
                    f.close()
    elif len(myresult[0]) == 3:
        for x in myresult:
            if x[2] is None:
                print("Name: " + x[1])
                print("--------------------------------" * 4)
                with open(file_name, "a") as f:
                    f.write("Name: " + x[1] + '\n')
                    f.write("--------------------------------" * 4 + '\n')
                    f.write('\n')
                    f.close()
            else:
                print("Name: " + x[1])
                print("Description/Google Scholar: " + x[2])
                print("--------------------------------" * 4)
                with open(file_name, "a") as f:
                    f.write("Name: " + x[1] + '\n')
                    f.write("Description: " + x[2] + '\n')
                    f.write("--------------------------------" * 4 + '\n')
                    f.write('\n')
                    f.close()

# generate_profile('trip_gwalior')