from csv import reader, writer
import sys

""" 
A quick script to parse the single large edges file by type such that we can
import the edges with appopriate edge types in Neo4j
"""

"""
First, in a single pass get the unique edge types in the consolodated file.
This isn't the most efficient way for super large files - so use with caution
"""

unique_edge_types = []
with open('panama_papers.edges.csv','r') as edges:
    csv_reader = reader(edges)
    header_row = next(csv_reader)
    if header_row != None:
        for row in csv_reader:
            if row[1] not in unique_edge_types:
                unique_edge_types.append(row[1])

        print(f"Here are the unique edge types in the file:")
        print(unique_edge_types)

""" 
Create the Dict that will house the rows for each edge type
"""

by_edge_type = {}
for type in unique_edge_types:
    by_edge_type[type] = []


"""
Now process each row into the dict created above.
Once this is complete this data structure allows us to use csv.writer to output the 
edges in unique files by edge type.
"""

with open('panama_papers.edges.csv', 'r') as edges:
    csv_reader = reader(edges)
    header_row = next(csv_reader)
    if header_row != None:
        for row in csv_reader:
            by_edge_type[row[1]].append(row)

"""
Now create a file per unique edge type. 
"""

for type in unique_edge_types:
    file_name = type + "_edges.csv"
    with open(file_name, 'w') as outfile:
        output = writer(outfile)
        output.writerow(header_row)
        output.writerows(by_edge_type[type])
    outfile.close()
    
    print(f"File: {file_name} written")

# All done!




