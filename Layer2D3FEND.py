import json
import csv
import sys

# Lists
Techs = []
Artifacts = []

LayerPath = str(sys.argv[1])

with open(LayerPath,"r") as f:
    layer_data = json.load(f)
    

for i in range(len(layer_data["techniques"])):
    Techs.append(layer_data["techniques"][i]["techniqueID"])
print("[+] Layer Techniques were extracted Successfully")
print("[+] These are the extracted techniques")
Techs = list(dict.fromkeys(Techs))
print(Techs)

with open('techniques.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    print("[+] D3FEND Techniques and Artifacts were loaded Successfully")
    for i in range(len(Techs)):
        for row in reader:
            #print(row['ATTACKid'])
            if (str(row["Technique"]).find(str(Techs[i]))) != -1:
                #print(row['ATTACKid'])
                
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
print(Artifacts)

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
                        									

