import os
import random
import names
import xlsxwriter as xlsxwriter
import time
from random import randint
import pandas as pd
import csv
import openpyxl

import Random_date_generator
import Random_cities

def create_data(r):
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, r'Excel_data')
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)
    name = str(time.time())
    workbook = xlsxwriter.Workbook('Excel_data/' + name + '.xlsx')
    worksheet = workbook.add_worksheet()

    worksheet.write('A1', 'User Name')
    worksheet.write('B1', 'Driver Id')
    worksheet.write('C1', 'Policy Number')
    worksheet.write('D1', 'D.O.P')
    worksheet.write('E1', 'Block Id')
    worksheet.write('F1', 'Location')
    worksheet.write('G1', 'Issue')
    worksheet.write('H1', 'D.O.I')
    worksheet.write('I1', 'D.O.R')
    worksheet.write('J1', 'Amount')
    worksheet.write('K1', 'Asset')
    worksheet.write('L1', 'Sybil Attack')
    worksheet.write('M1', 'Claim Id')
    worksheet.write('N1', 'Age')


    n = 0
    driver_id = {}
    policy_id = {}
    to_rand = []

    random_lis = []
    random_dic = {}

    second_claim_lis = []
    second_claim_dic = {}

    third_claim_lis = []
    third_claim_dic = {}

    fourth_claim_lis = []
    fourth_claim_dic = {}


    for i in range (1,int(r/15)):
        random_lis.append(randint(1,r))

    for i in range (1,int(r/3)):
        second_claim_lis.append(randint(1,r))

    for i in range (1,int(r/5)):
        third_claim_lis.append(randint(1,r))

    for i in range (1,int(r/10)):
        fourth_claim_lis.append(randint(1,r))


    for i in range (0,r):
        fraud = False
        luck = randint(1, 10)
        if luck > 1:
            fraud = False
        else:
            fraud = True

        n += 1
        A = names.get_full_name()

        B = randint(1000000, 9999999)
        driver_id[n+1] = B

        C = randint(1000000, 9999999)
        policy_id[n+1] = C

        D = "%d/%d/2020" %(randint(1, 12),randint(1, 28))
        E = randint(10000, 99999)
        F = Random_cities.extract()[randint(0, 28334)]
        G = Random_cities.issues()[randint(0, 4)]
        H = Random_date_generator.random_date(D, Random_date_generator.today(),random.random())
        I = Random_date_generator.random_date(H, Random_date_generator.today(),random.random())
        J = randint(2000, 20000)
        K = randint(5000, 60000)
        L = 0
        M = -1
        N = randint(16,65)
        rand = 0

        while M < 0:
            rand = randint(1000000, 9999999)
            if rand not in to_rand:
                M = rand
                to_rand.append(rand)


        if i in random_lis:
            random_dic[i] = [A,B,C,D,E,F,G,H,I,J,K,L,M,N]

        if i in second_claim_lis:
            second_claim_dic[i] = [A,B,C,D,E,F,G,H,I,J,K,L,M,N]

        if i in third_claim_lis:
            third_claim_dic[i] = [A,B,C,D,E,F,G,H,I,J,K,L,M,N]

        if i in fourth_claim_lis:
            fourth_claim_dic[i] = [A,B,C,D,E,F,G,H,I,J,K,L,M,N]

        worksheet.write('A' + str(n + 1), A)
        worksheet.write('B' + str(n + 1), B)
        worksheet.write('C' + str(n + 1), C)
        worksheet.write('D' + str(n + 1), D)
        worksheet.write('E' + str(n + 1), E)
        worksheet.write('F' + str(n + 1), F)
        worksheet.write('G' + str(n + 1), G)
        worksheet.write('H' + str(n + 1), H)
        worksheet.write('I' + str(n + 1), I)
        worksheet.write('J' + str(n + 1), J)
        worksheet.write('K' + str(n + 1), K)
        worksheet.write('L' + str(n + 1), L)
        worksheet.write('M' + str(n + 1), M)
        worksheet.write('N' + str(n + 1), N)

    i = 0
    while i<= int(r/10):
        a = randint(1,r)
        b = randint(1, r)

        worksheet.write('B' + str(a), driver_id[a])
        worksheet.write('B' + str(r - a), driver_id[a])
        worksheet.write('L' + str(a), 1)
        worksheet.write('L' + str(r-a), 1)

        worksheet.write('C' + str(b), policy_id[b])
        worksheet.write('C' + str(r - b), policy_id[b])
        worksheet.write('L' + str(b), 1)
        worksheet.write('L' + str(r - b), 1)

        i+=1
    n = r
    for key, value in random_dic.items():
        n += 1
        M = -1

        while M < 0:
            rand = randint(1000000, 9999999)
            if rand not in to_rand:
                M = rand
                to_rand.append(rand)
        worksheet.write('A' + str(n + 1), value[0])
        worksheet.write('B' + str(n + 1), value[1])
        worksheet.write('C' + str(n + 1), value[2])
        worksheet.write('D' + str(n + 1), value[3])
        worksheet.write('E' + str(n + 1), value[4])
        worksheet.write('F' + str(n + 1), value[5])
        worksheet.write('G' + str(n + 1), value[6])
        worksheet.write('H' + str(n + 1), value[7])
        worksheet.write('I' + str(n + 1), value[8])
        worksheet.write('J' + str(n + 1), value[9])
        worksheet.write('K' + str(n + 1), value[10])
        worksheet.write('L' + str(n + 1), value[11])
        worksheet.write('M' + str(n + 1), M)
        worksheet.write('N' + str(n + 1), value[13])

    for key, value in second_claim_dic.items():
        n += 1
        E = randint(10000, 99999)
        F = Random_cities.extract()[randint(0, 28334)]
        G = Random_cities.issues()[randint(0, 4)]
        H = Random_date_generator.random_date(D, Random_date_generator.today(), random.random())
        I = Random_date_generator.random_date(H, Random_date_generator.today(), random.random())
        J = randint(2000, 20000)
        L = 0
        M = -1
        while M < 0:
            rand = randint(1000000, 9999999)
            if rand not in to_rand:
                M = rand
                to_rand.append(rand)
        worksheet.write('A' + str(n + 1), value[0])
        worksheet.write('B' + str(n + 1), value[1])
        worksheet.write('C' + str(n + 1), value[2])
        worksheet.write('D' + str(n + 1), value[3])
        worksheet.write('E' + str(n + 1), E)
        worksheet.write('F' + str(n + 1), F)
        worksheet.write('G' + str(n + 1), G)
        worksheet.write('H' + str(n + 1), H)
        worksheet.write('I' + str(n + 1), I)
        worksheet.write('J' + str(n + 1), J)
        worksheet.write('K' + str(n + 1), value[10])
        worksheet.write('L' + str(n + 1), L)
        worksheet.write('M' + str(n + 1), M)
        worksheet.write('N' + str(n + 1), value[13])

    for key, value in third_claim_dic.items():
        n += 1
        E = randint(10000, 99999)
        F = Random_cities.extract()[randint(0, 28334)]
        G = Random_cities.issues()[randint(0, 4)]
        H = Random_date_generator.random_date(D, Random_date_generator.today(), random.random())
        I = Random_date_generator.random_date(H, Random_date_generator.today(), random.random())
        J = randint(2000, 20000)
        L = 0
        M = -1
        while M < 0:
            rand = randint(1000000, 9999999)
            if rand not in to_rand:
                M = rand
                to_rand.append(rand)
        worksheet.write('A' + str(n + 1), value[0])
        worksheet.write('B' + str(n + 1), value[1])
        worksheet.write('C' + str(n + 1), value[2])
        worksheet.write('D' + str(n + 1), value[3])
        worksheet.write('E' + str(n + 1), E)
        worksheet.write('F' + str(n + 1), F)
        worksheet.write('G' + str(n + 1), G)
        worksheet.write('H' + str(n + 1), H)
        worksheet.write('I' + str(n + 1), I)
        worksheet.write('J' + str(n + 1), J)
        worksheet.write('K' + str(n + 1), value[10])
        worksheet.write('L' + str(n + 1), L)
        worksheet.write('M' + str(n + 1), M)
        worksheet.write('N' + str(n + 1), value[13])

    for key, value in fourth_claim_dic.items():
        n += 1
        E = randint(10000, 99999)
        F = Random_cities.extract()[randint(0, 28334)]
        G = Random_cities.issues()[randint(0, 4)]
        H = Random_date_generator.random_date(D, Random_date_generator.today(), random.random())
        I = Random_date_generator.random_date(H, Random_date_generator.today(), random.random())
        J = randint(2000, 20000)
        L = 0
        M = -1
        while M < 0:
            rand = randint(1000000, 9999999)
            if rand not in to_rand:
                M = rand
                to_rand.append(rand)
        worksheet.write('A' + str(n + 1), value[0])
        worksheet.write('B' + str(n + 1), value[1])
        worksheet.write('C' + str(n + 1), value[2])
        worksheet.write('D' + str(n + 1), value[3])
        worksheet.write('E' + str(n + 1), E)
        worksheet.write('F' + str(n + 1), F)
        worksheet.write('G' + str(n + 1), G)
        worksheet.write('H' + str(n + 1), H)
        worksheet.write('I' + str(n + 1), I)
        worksheet.write('J' + str(n + 1), J)
        worksheet.write('K' + str(n + 1), value[10])
        worksheet.write('L' + str(n + 1), L)
        worksheet.write('M' + str(n + 1), M)
        worksheet.write('N' + str(n + 1), value[13])


    workbook.close()

    # open given workbook
    # and store in excel object
    excel = openpyxl.load_workbook("Excel_data/"+name + ".xlsx")

    # select the active sheet
    sheet = excel.active

    # writer object is created
    col = csv.writer(open("Excel_data/"+name+".csv",
                          'w',
                          newline=""))

    # writing the data in csv file
    for r in sheet.rows:
        # row by row write
        # operation is perform
        col.writerow([cell.value for cell in r])

    # read the csv file and
    # covert into dataframe object
    df = pd.DataFrame(pd.read_csv("Excel_data/"+name+".csv", sep='|', encoding='latin-1'))

    return df

create_data(50)
