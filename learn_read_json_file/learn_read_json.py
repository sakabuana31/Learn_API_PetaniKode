#import modules
import json

#open json file
file_json = open("/home/sakabuana31/DEPractice/LEARN_API_PETANIKODE/learn_read_json_file/mydata.json")

#parsing json file
data = json.loads(file_json.read())

#print data
print(data)