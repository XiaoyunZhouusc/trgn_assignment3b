# extract_phonenum.py
## Usage
>
> python3 extract_phonenum.py [file]
>
## Description
This script can extract phone numbers from the [file]. The script only recognize a phone numbers if it has dashes ("-") that segment portions (i.e: first-second-third). You can add optional country code at the front with or without "+" sign.
## Know Issues
The script assumes each portion can have no more than 4 digits. if there are more than 4 digits then the extracted number may not be correct.

# ensg2hugo.py
## Usage
>
> python3 ensg2hugo.py -f[1-9] [file]
>
## Description
It can translate from Ensembl name to HUGO name! Please specify which column by inputting -f[column number]. (1-based numbering) 
If there is no “-f” then the first column is used.
## Dependency 
It requires ***Homo_sapiens.GRCh37.75.gtf*** to be able to correctly compile. Please do the following before running the script:
>
> cd [to the location where the script is at]
> 
> wget http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens/Homo_sapiens.GRCh37.75.gtf.gz
>
> gzip -d Homo_sapiens.GRCh37.75.gtf.gz  
>
## Know Issues
* It supports up to 9 columns. If you have more columns than that and your data is at one of these, then this script cannot help you translating the names. 
* It is 1-based, but if you select the 0th column it will try translating names on the last column.
* If names are not in the ***Homo_sapiens.GRCh37.75.gtf***, then it will translate nothing. 

# histogram.py
## Usage
>
> python3 histogram.py -f[1-9] [file]
>
## Description
It can create a histogram (**histogram.png**) as a png from a file using the specified column in a tab delimited file.
## Know Issues
* It supports up to 9 columns. If you have more columns than that and your data is at one of these, then this script cannot help you plotting the histogram.
* It is 1-based, but if you select the 0th column it will plot what is on the last column.
* User cannot adjust the size or other attributes of the generated figure.
## Unit tests
There are files have unit test input data in the folder **histogramUnitTestData**
