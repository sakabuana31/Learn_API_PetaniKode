#import modules
import json

#open json file
file_json = open("/home/sakabuana31/DEPractice/LEARN_API_PETANIKODE/learn_read_json_file/mydata.json")

#parsing json file
data = json.loads(file_json.read())

#print data
print("")
print(f"Nama: {data['name']}")
print(f"Website: {data['web']}")
print("")
print("Sosial Media:")
print(f"- Facebook: {data['social_media']['facebook']}")
print(f"- Twitter: {data['social_media']['twitter']}")
print(f"- Instagram: {data['social_media']['instagram']}")
print("")
print(f"Read by: {data['readby']}")
print(f"Github: {data['github']}")