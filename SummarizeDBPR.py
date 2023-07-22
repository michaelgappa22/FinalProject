import pandas as pd;
import requests;
import io;
import matplotlib.pyplot as plt;


def downloadDbprFile():
    # url we are using.  
    dbpr_file_url = "http://www.myfloridalicense.com/dbpr/sto/file_download/extracts//REALESTATE2501LICENSE_1.csv";
    # get content from URL
    data_request = requests.get(dbpr_file_url).content;
    # decode the data request using utf-8, pass it into the io.StringIO function, and pass the result into panda's 
    # read_csv function.
    read_data_request = pd.read_csv(io.StringIO(data_request.decode('utf-8')));
    # Create the dbpr columns for the csv file that you will convert into a Dataframe.
    dbpr_columns = ["License Type","Name","DBA License Type Name","Rank","Mailing Address 1","Mailing Address 2"
                    ,"Mailing Address 3","City","State","Zip Code","County","License Number","Primary Status",
                    "Secondary Status","Licensure Date","Relation Date","Expires","License Number","Sole Proprietor DBA",
                    "Related Party","Office License Number",];
    # Pass pandas read_csv object values into pandas DataFrame function first argument, while passing the dbpr_columns as columns.
    df_dbpr = pd.DataFrame(read_data_request.values,columns=dbpr_columns);
    # Take the returned DataFrame object and write into CSV using pandas to_csv function. We don't need index, so set as False.
    df_dbpr.to_csv("DbprFile.csv",index=False);

# downloadDbprFile();

df = pd.DataFrame(pd.read_csv('DbprFile.csv'));
pd.set_option('display.max_rows', None)

licenseByPrimaryStatus = df["Primary Status"].value_counts();
licenseBySecondaryStatus = df["Secondary Status"].value_counts();
licenseByZipCode = df["Zip Code"].value_counts();
licenseByCounty = df["County"].value_counts();
licenseByState = df["State"].value_counts();

licenseByPrimaryStatus.to_csv("DbprStatistics.csv",index=True,index_label="Status", mode="w");
licenseBySecondaryStatus.to_csv("DbprStatistics.csv",index=True, mode="a");
licenseByZipCode[0:5].to_csv("DbprStatistics.csv",index=True, mode="a");
licenseByCounty[0:5].to_csv("DbprStatistics.csv",index=True, mode="a");
licenseByState[0:5].to_csv("DbprStatistics.csv",index=True, mode="a");

licenseStatus = list(licenseByCounty[0:5].keys());
numberOfLicenseStatus = list(licenseByCounty[0:5].values);
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(licenseStatus, numberOfLicenseStatus, color ='maroon',
        width = 0.4)
 
plt.xlabel("County")
plt.ylabel("No. of Licenses per County")
plt.title("Total Licenses in Each County in Florida")
plt.show()

df["Relation Date"] = pd.to_datetime(df["Relation Date"],format='%d-%b-%y');
currentActiveDataFrame = df[(df['Relation Date'] > '2023-06-08') & (df['Primary Status'] == 'Current') 
                            * (df['Secondary Status'] == 'Active')];
licenseByRelationDate = currentActiveDataFrame["Relation Date"].value_counts();

licenseStatus = list(licenseByRelationDate.keys());
numberOfLicenseStatus = list(licenseByRelationDate.values);
fig = plt.figure(figsize = (15, 8))
 
# creating the bar plot
plt.bar(licenseStatus, numberOfLicenseStatus, color ='blue',
        width = 0.8)
 
plt.xlabel("Date License Activated")
plt.ylabel("No. of Licenses Activated")
plt.title("Total Licenses Current Active per Day")
plt.show()

# print("Finished!")