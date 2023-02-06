import os
import json

print ("Enter gene: ", sep = "", end = "")
orig_gene = input()
gene = orig_gene.lower()

# Opening file
fname = 'TF-Target-information.txt'
while not os.path.isfile(fname):
    print ("file", fname, "wasn't found, please enter filename: ", end="")
    fname = input()

file1 = open(fname, 'r')
count = 0
count_tf = 0
    
# Array for TF details
res_tfs_details = []

# Array for TFs
res = []

# Open json file with info about TFs
with open('datasets_all.json', 'r') as fcc_file:
    fcc_data = json.load(fcc_file)
# put list of dictionaries into list. Each dictionary in this list is TF
tfs_list = fcc_data["datasets"]    

# Loop to print results
for line in file1:
    count += 1
#   t is target gene (one which was entered by user)
    t = line.strip("\n ").split ("\t") [1].lower()
#   tf is transition factor, connected to t 
    tf = line.strip("\n ").split ("\t") [0].upper()
    if gene == t :
        res.append(line)
        for tf_dict in tfs_list:
            count_tf += 1
            if tf_dict["factor"] == tf :
                res_tfs_details.append(tf_dict)

tf_to_print = []
        
if len(res) > 0 :
    print("For the gene: ", orig_gene, ", ", len(res), " TFs were found")
    print("----------------------------------------")
    print("TF", "Target", "Tissue", sep="\t")
    print("----------------------------------------")
    for line in res:
        print(line,end = "")
    print("----------------------------------------")    
    print("More details about found TFs :")
    print("--------------------------------------------------------------")

    print("TF", "cell_line", "cell_type", "disease", "tissue", sep="\t|")
    print("--------------------------------------------------------------")
    for record in res_tfs_details:
        flexible = [record["factor"], "==|==", record["cell_line"], "==|==",
                    record["cell_type"], "==|==", record["disease"], "==|==", record["tissue"]]
        tf_to_print.append(" ".join(flexible))
    tf_to_print[:] = list(set(tf_to_print))
    tf_to_print.sort()
    for el in tf_to_print:
        words = el.split("==|==")
        print(words[0].strip(), words[1].strip(), words[2].strip(), words[3].strip(), words[4].strip(), sep="\t|")
else:
    print("No TFs found for the gene", orig_gene)

# Closing files
file1.close()
