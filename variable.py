# creating a list of amis 
ami_list = ["ami- 0d729d2846a86a9e7","ami-0c1bc246476a5572b","ami-0022f774911c1d690"]
pass
print(ami_list)

# creating a for loop through ami_list variable
for item in ami_list:
    print("instance ami id")
    print(item)

#  creating a turple of amis
regions_tuple = ("ami- 0d729d2846a86a9e7","ami-0c1bc246476a5572b","ami-0022f774911c1d690")   
for ami in regions_tuple:
     print(ami)
if ami == "ami-0022f774911c1d690":
       print("us-east-1")

# A key-value pair of region to ami dictionry  
region_ami_dict = {"eu-west-2" : "ami- 0d729d2846a86a9e7", "eu-west-1" : "ami-0c1bc246476a5572b","us-east-1" : "ami-0022f774911c1d690"}

for k,v in region_ami_dict.items():
    print(k,v) 
    
# import aws library
import boto3

# specify region
region = "eu-west-2"

# the the aws set up
session = boto3.Session()

# get some available resources from our aws account
availalable_resources = session.get_available_resources()
print(availalable_resources)