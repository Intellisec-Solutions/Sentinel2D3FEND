import json
import requests
import csv


# Add the rquired fields

Azure_AD_Tenant = "Azure_AD_Tenant_HERE"
Client_ID = "Client_ID_HERE"
Client_Secret = "Client_Secret_HERE"
ResourceGroup = "ResourceGroup_HERE"
Workspace = "Workspace_HERE"
Subscription = "Subscription_ID"


# Lists
Sentinel_Techniques = []
Artifacts = []


Url = "https://login.microsoftonline.com/"+Azure_AD_Tenant+"/oauth2/token"
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
payload='grant_type=client_credentials&client_id='+ Client_ID+'&resource=https%3A%2F%2Fmanagement.azure.com&client_secret='+Client_Secret
response = requests.post(Url, headers=headers, data=payload).json()
Access_Token = response["access_token"]
print("[+] Access Token Received Successfully")


# Get Sentinel Alert Rules

Url2= "https://management.azure.com/subscriptions/"+Subscription+"/resourceGroups/"+ResourceGroup+"/providers/Microsoft.OperationalInsights/workspaces/"+Workspace+"/providers/Microsoft.SecurityInsights/alertRules?api-version=2020-01-01"
Auth = 'Bearer '+Access_Token
headers2 = {
  'Authorization': Auth ,
  'Content-Type': 'text/plain'
}

response2 = requests.get(Url2, headers=headers2).json()
print("[+] Alert Rules Details were received Successfully")


for a in range(len(response2["value"])):
    if (str(response2["value"][a]["properties"]["displayName"]).split()[0][0]== "T"):
        Sentinel_Techniques.append((str(response2["value"][a]["properties"]["displayName"]).split()[0]))

print("[+] Technique tags were extracted from Rule Analytics Successfully") 
print(Sentinel_Techniques)


with open('techniques.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    print("[+] D3FEND Techniques and Artifacts were loaded Successfully")
    for i in range(len(Sentinel_Techniques)):
        for row in reader:
            if (str(row["Technique"]).find(str(Sentinel_Techniques[i]))) != -1:
                for j in range(len(row['Accesses'].strip('][').split(', '))):
                    Artifacts.append((row['Accesses'].strip('][').split(', ')[j]).replace("'",""))
                    
                for j in range(len(row['May-Modify'].strip('][').split(', '))):
                    Artifacts.append((row['May-Modify'].strip('][').split(', ')[j]).replace("'",""))
                    
                for j in range(len(row['May-Produce'].strip('][').split(', '))):
                    Artifacts.append((row['May-Produce'].strip('][').split(', ')[j]).replace("'",""))
                
                for j in range(len(row['Produces'].strip('][').split(', '))):
                    Artifacts.append((row['Produces'].strip('][').split(', ')[j]).replace("'",""))
                    
                for j in range(len(row['May-Create'].strip('][').split(', '))):
                    Artifacts.append((row['May-Create'].strip('][').split(', ')[j]).replace("'",""))
                    
                for j in range(len(row['May-Access'].strip('][').split(', '))):
                    Artifacts.append((row['May-Access'].strip('][').split(', ')[j]).replace("'",""))
                    
                for j in range(len(row['Uses'].strip('][').split(', '))):
                    Artifacts.append((row['Uses'].strip('][').split(', ')[j]).replace("'",""))
                    
                for j in range(len(row['Creates'].strip('][').split(', '))):
                    Artifacts.append((row['Creates'].strip('][').split(', ')[j]).replace("'",""))
                    
                for j in range(len(row['Invokes'].strip('][').split(', '))):
                    Artifacts.append((row['Invokes'].strip('][').split(', ')[j]).replace("'",""))
                    
                for j in range(len(row['Modifies'].strip('][').split(', '))):
                    Artifacts.append((row['Modifies'].strip('][').split(', ')[j]).replace("'",""))
                    
                for j in range(len(row['Executes'].strip('][').split(', '))):
                    Artifacts.append((row['Executes'].strip('][').split(', ')[j]).replace("'",""))
                    
                for j in range(len(row['Adds'].strip('][').split(', '))):
                    Artifacts.append((row['Adds'].strip('][').split(', ')[j]).replace("'",""))
                    
                for j in range(len(row['Loads'].strip('][').split(', '))):
                    Artifacts.append((row['Loads'].strip('][').split(', ')[j]).replace("'",""))
                 

while '' in Artifacts:
    Artifacts.remove('')   #Deletes empty elements
    
Artifacts = list(dict.fromkeys(Artifacts)) #Deletes Duplicates

print("[+] Related D3FEND Artifacts were extracted Successfully")                              

#print(Artifacts)

with open('Defenses.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    print("[+] D3FEND Defenses were loaded Successfully")  
    print("[+] Related D3FEND Defenses are the following")      
    for row in reader:
        for i in range(len(Artifacts)):
                ROW = str(row).split("'")
                for elm in ROW:
                    if Artifacts[i] == str(elm):
                        print("-----------------------")
                        print(row['DEFENDid']) 
                        print(row['Defense'])
                        print(row['Definition'])
                        print("Analyzes: ",row['Analyzes'])
                        print("Neutralizes: ",row['Neutralizes'])
                        print("Verifies: ",row['Verifies'])
                        print("Obfuscates: ",row['Obfuscates'])
                        print("Filters: ",row['Filters'])
                        print("Encrypts: ",row['Encrypts'])
                        print("Blocks: ",row['Blocks'])
                        print("Authenticates: ",row['Authenticates'])
                        print("Terminates: ",row['Terminates'])
                        print("Isolates: ",row['Isolates'])
                        print("Spoofs: ",row['Spoofs'])
                        print("Disables: ",row['Disables'])
                        print("Modifies: ",row['Modifies'])
                        									
