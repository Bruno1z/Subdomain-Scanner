#Python 3.11.1
import requests # De-facto python library for HTTP request. 

domain = input("Enter the domain you want to find subdomains to: ")  #target domain 

with open("subdomains.txt", "r") as file: 

    for subdomain in file.readlines():
        # define subdomain url
        subdomain_url = f"https://{subdomain.strip()}.{domain}" 

        try:
            # the get request is sent to the prospect subdomain URLs to check if the subdomain for the domain exists or not and is stored in the response variable.
            response = requests.get(subdomain_url) 
            f= open("result.txt","a+") #creates a file (result.txt) to write the found subdomains to

            # 200 success code
            if response.status_code == 200 :
                f.write(f"Subdomain Found [+]: {subdomain_url} \n") #writes the the newly created file with the found subdomains.

        except:
            pass

 
