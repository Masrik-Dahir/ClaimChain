import csv
import os
import Claim_2

def read_csv(dir: str) -> tuple:
    # csv file name
    filename = dir

    # initializing the titles and rows list
    fields = []
    rows = []

    # reading csv file
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)

        # get total number of rows
        print("Total no. of rows: %d" % (csvreader.line_num))

    # printing the field names
    print('Field names are:' + ', '.join(field for field in fields))

    #  printing first 5 rows
    print('\nFirst %d rows are:\n'%(csvreader.line_num))

    dic = {}
    n = 1
    p_id_lis = []
    result = []
    fraud_result = []
    legit_result = []

    for row in rows[:]:
        # parsing each column of a row
        lis = []
        for col in row:
            lis.append(col)
        p_id_lis.append(lis[2])
        claim_block = Claim_2.Claim_block(lis[0],lis[1],lis[2],lis[3],lis[4],lis[5],lis[6],lis[7],lis[8],lis[9],
                                          lis[10],lis[11],lis[12],lis[13],lis[14],lis[15],lis[16],lis[17],lis[18],
                                          lis[19],lis[20],lis[21],lis[22],lis[23],lis[24],lis[25],lis[26],lis[27],
                                          lis[28],lis[29],lis[30],lis[31],lis[32])


        if int(claim_block.getFraudFound_P()) == 1:
            fraud_claim_block = Claim_2.Claim_block(lis[0],lis[1],lis[2],lis[3],lis[4],lis[5],lis[6],lis[7],lis[8],lis[9],
                                          lis[10],lis[11],lis[12],lis[13],lis[14],lis[15],lis[16],lis[17],lis[18],
                                          lis[19],lis[20],lis[21],lis[22],lis[23],lis[24],lis[25],lis[26],lis[27],
                                          lis[28],lis[29],lis[30],lis[31],lis[32])
            fraud_result.append(fraud_claim_block)

        elif int(claim_block.getFraudFound_P()) == 0:
            legit_claim_block = Claim_2.Claim_block(lis[0],lis[1],lis[2],lis[3],lis[4],lis[5],lis[6],lis[7],lis[8],lis[9],
                                          lis[10],lis[11],lis[12],lis[13],lis[14],lis[15],lis[16],lis[17],lis[18],
                                          lis[19],lis[20],lis[21],lis[22],lis[23],lis[24],lis[25],lis[26],lis[27],
                                          lis[28],lis[29],lis[30],lis[31],lis[32])
            legit_result.append(legit_claim_block)

        result.append(claim_block)

        n += 1

    return result, fraud_result, legit_result

# print(read_csv("claims_modified.csv"))