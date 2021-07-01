# importing csv module
import csv
import xlrd
import pandas as pd
import openpyxl

class Claim_block(object):
    def __init__(self, username, d_id, p_id, d_policy, b_id,location,issue, d_incident,d_report,amount,asset):
        self.p_id = p_id
        self.username = username
        self.d_id = d_id
        self.b_id = b_id
        self.d_incident = d_incident
        self.d_policy = d_policy
        self.d_report = d_report
        self.issue = issue
        self.amount = amount
        self.location = location
        self.asset = asset
    def get_username(self):
        return self.username
    def get_p_id(self):
        return self.p_id
    def get_d_id(self):
        return self.d_id
    def get_b_id(self):
        return self.b_id
    def get_d_incident(self):
        return self.d_incident
    def get_d_policy(self):
        return self.d_policy
    def get_d_report(self):
        return self.d_report
    def get_issue(self):
        return self.issue
    def get_amount(self):
        return self.amount
    def get_location(self):
        return self.location
    def get_asset(self):
        return self.asset
    def toDictionary(self):
        dic = {}
        dic["Username"] = self.username
        dic["Driver ID"] = self.d_id
        dic["Policy ID"] = self.p_id
        dic["Date of Policy"] = self.d_policy
        dic["Block ID"] = self.b_id
        dic["Location"] = self.location
        dic["Reason for Claim"] = self.issue
        dic["Date of Incident"] = self.d_incident
        dic["Date of Report"] = self.d_report
        dic["Claimed mount"] = self.amount
        dic["Insured Asset Value"] = self.asset

        return dic

    def toList(self):
        lis = []
        lis.append(self.username)
        lis.append(self.d_id)
        lis.append(self.p_id)
        lis.append(self.d_policy)
        lis.append( self.b_id)
        lis.append(self.location)
        lis.append(self.issue)
        lis.append(self.d_incident)
        lis.append(self.d_report)
        lis.append( self.amount)
        lis.append(self.asset)

        return lis
