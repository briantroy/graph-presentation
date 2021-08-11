This repository is a collection of tools to recreate the presented
Panama Papers use case in Neo4j Desktop.

Requirements:
Neo4j Desktop
  APOC library installed

Your system will need a reasonable amount of free memory to import the
graph data from the sample set. The instructions call for 3GB of memory
for Neo4j (max heap size).

TL;DR
Install Neo4j Desktop: https://neo4j.com/download-neo4j-now/
Create a project and a database: https://neo4j.com/developer/neo4j-desktop/
Install APOC in the Project: https://neo4j.com/labs/apoc/4.1/installation/

Prepare the data for Import:
Unzip the files found in this repository at:
Panama Papers/csv_panama_papers.2018-02-14
  Each zip file is needed.
  NOTE: The primary edges file has been split by edge type.
Move the CSV files to the Neo4j Desktop Import Directory:
https://neo4j.com/developer/desktop-csv-import/


Import the Data:
Open the file: Panama Papers/Scripts Queries and Notes/PanamaPapersImportCypher.txt
Read the document.

You will need to run each cypher USING PERIODIC COMMIT LOAD CSV WITH HEADERS
query **except** the all edges query. It is there for reference only.

You will also note that some Neo4j Desktop settings have to be adjusted
to allow enough memory to be available for the import of edges.
https://neo4j.com/developer/neo4j-desktop/#desktop-DBMS-settings

Sample queries:
The sample queries are located in the file:
Panama Papers/Scripts Queries and Notes/Interesting queries

Enjoy!
