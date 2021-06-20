import os

import names
import xlsxwriter as xlsxwriter
import time
from random import randint
import Read_Excel

def create_data(r):
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, r'Excel_data')
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)
    workbook = xlsxwriter.Workbook('Excel_data/' + str(time.time()) + '.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', 'User Name')
    worksheet.write('B1', 'Driver\'s Id')
    worksheet.write('C1', 'Policy Number')
    worksheet.write('D1', 'D.O.I')
    worksheet.write('E1', 'Block Id')
    worksheet.write('F1', 'Location')
    worksheet.write('G1', 'Issue')
    worksheet.write('H1', 'Fraud')

    n = 0
    driver_id = {}
    policy_id = {}
    for i in range (0,r):

        n += 1
        A = names.get_full_name()

        B = randint(1000000, 9999999)
        driver_id[n+1] = B

        C = randint(1000000, 9999999)
        policy_id[n+1] = C

        D = "%d/%d/20" %(randint(1, 12),randint(1, 28))
        E = randint(10000, 99999)
        F = Read_Excel.extract()[randint(0, 28334)]
        G = Read_Excel.issues()[randint(0,4)]
        H = 0
        worksheet.write('A' + str(n + 1), A)
        worksheet.write('B' + str(n + 1), B)
        worksheet.write('C' + str(n + 1), C)
        worksheet.write('D' + str(n + 1), D)
        worksheet.write('E' + str(n + 1), E)
        worksheet.write('F' + str(n + 1), F)
        worksheet.write('G' + str(n + 1), G)
        worksheet.write('H' + str(n + 1), H)

    i = 0
    while i<= int(r/10):
        a = randint(1,r)
        b = randint(1, r)

        worksheet.write('B' + str(a), driver_id[a])
        worksheet.write('B' + str(r - a), driver_id[a])
        worksheet.write('H' + str(a), 1)
        worksheet.write('H' + str(r-a), 1)

        worksheet.write('C' + str(b), policy_id[b])
        worksheet.write('C' + str(r - b), policy_id[b])
        worksheet.write('H' + str(b), 1)
        worksheet.write('H' + str(r - b), 1)

        i+=1

    workbook.close()

create_data(5000)