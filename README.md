# spannerimport
command line application that imports a csv file into a cloud spanner table

# Setup

1 Create a cloud spanner table using the SiteRankings.ddl file provided in this repository

2 Open a cloud shell from the google cloud platform console

3 Clone this repository by entering

    git clone https://github.com/hanknac/spannerimport.git

4 Navigate to the spannerimport directory

    cd spannerimport

5 Set the application default login

    gcloud auth application-default login

# Usage

Enter the following to import the 50,000 row csv file into the SiteRankings table

    python import.py --instance_id=[your spanner intance] --database_id=[your spanner database] --table_id=SiteRankings --batchsize=1600 --data_file=50000.csv --format_file=sites.fmt
    
