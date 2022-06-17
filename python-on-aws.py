# import aws library
import boto3

# specify region
region = "eu-west-2"

# the the aws set up
session = boto3.Session()

# get some available resources from our aws account
availalable_resources = session.get_available_resources()

print("the resources I have in my account are:")
for resources in availalable_resources:
    if resources == "glacier":
        print("yes project, we actually have glacier")

# # provision resources
# # create s3
s3_client = boto3.client("s3")
print(s3_client.list_buckets())

listofbuckets = s3_client.list_buckets()
pass

for key, value in listofbuckets.items():
    pass
    #  print(f"key is: {key} and value: {value}")


for bucket in listofbuckets["Buckets"]:
    print(bucket)
    for name, value in bucket.items():
        pass
        print(f"buckek: {value}")

# # create s3
location = {'LocationConstraint': region}
s3_client.create_bucket(Bucket="python-project4",CreateBucketConfiguration=location)

# # create ec2 =====
import boto3
ec2 = boto3.resource('ec2')

instances = ec2.create_instances(
        ImageId="ami-05a8c865b4de3b127",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="au131"
    )
