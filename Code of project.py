from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result
from cloudant.result import Result, ResultByKey


# IBM Cloudant Legacy authentication
client = Cloudant("apikey-v2-1g7tj4xulwlrroyh29chec014k4gviohl80g7himpt33", "3cff79c3fe501830264565beac3e3793",
                  url="https://apikey-v2-1g7tj4xulwlrroyh29chec014k4gviohl80g7himpt33:3cff79c3fe501830264565beac3e3793@0bcba821-607c-40f9-9c92-262a84f9742e-bluemix.cloudantnosqldb.appdomain.cloud")
client.connect()

database_name = "smartdata"

my_database = client.create_database(database_name)

if my_database.exists():
    print(f"'{database_name}' successfully created.")
    json_document = {
                    "_id": "18430",
                    "name":"Bindu"
                    }
    new_document = my_database.create_document(json_document)
    if new_document.exists():
        print("Document '{new_document}' successfully created.")

result_collection = Result(my_database.all_docs, include_docs=True)
# Get the result for matching a key
result = result_collection['18430']  #search by id, if id=1001   

print("---------------")
print("the data with id =18430 is")
print (result)
print("---------------")
# Iterate over the result collection
for result in result_collection:
    print(result)# it will print all the records

# First retrieve the document
for document in my_database:
    my_document = my_database['18430'] 

# Update the document content
# This can be done as you would any other dictionary
my_document['temperature'] = 29
my_document['gas Level'] = 20
my_document['flame'] = 50


# You must save the document in order to update it on the database
my_document.save()

result_collection = Result(my_database.all_docs, include_docs=True)
# Get the result for matching a key
result = result_collection['18430']     
# Iterate over the result collection
print (result)


