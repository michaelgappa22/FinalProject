import pandas as pd;
import numpy as np;
import requests;
import io;

def downloadDbprFile():
    dbpr_file_url = "http://www.myfloridalicense.com/dbpr/sto/file_download/extracts//REALESTATE2501LICENSE_1.csv";
    data_request = requests.get(dbpr_file_url).content;
    read_data_request = pd.read_csv(io.StringIO(data_request.decode('utf-8')));
    dbpr_columns = ["License Type","Name","DBA License Type Name","Rank","Mailing Address 1","Mailing Address 2"
                    ,"Mailing Address 3","City","State","Zip Code","County","License Number","Primary Status",
                    "Secondary Status","Licensure Date","Relation Date","Expires","License Number","Sole Proprietor DBA",
                    "Related Party","Office License Number",];
    df_dbpr = pd.DataFrame(read_data_request.values,columns=dbpr_columns);
    df_dbpr.to_csv("DbprFile.csv",index=False);

# downloadDbprFile();
df = pd.DataFrame(pd.read_csv('DbprFile.csv'));
pd.set_option('display.max_rows', None)

print(df["County"].value_counts());
print(df["Zip Code"].value_counts());
print(df["Primary Status"].value_counts());
print(df["Secondary Status"].value_counts());