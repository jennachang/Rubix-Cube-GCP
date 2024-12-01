import vertexai
from vertexai.preview.generative_models import GenerativeModel
from vertexai.preview.generative_models import Part
#from templates import template_images
from template_standardised import template_images
from google.cloud import storage
import os 
#vertexai.init(project = "acn-cloudwars-chatbot-uki", location = "europe-west2" )

storage_client = storage.Client()
gemini_pro_vision_model = GenerativeModel("gemini-pro-vision")

def generate_output(image):
        api_response = gemini_pro_vision_model.generate_content([template_images, image])
        return api_response.text

def get_image_structure(bucket_name: str, input_bucket_file: str, output_path:str) -> None:

        bucket_list = storage_client.list_blobs(bucket_name, prefix= input_bucket_file)
        output = []

        for counter, file in enumerate(bucket_list):

                try:
                        if counter < 8:  
                                print('trying with image file path {}'.format(str(file).split(',')[1]))
                                file_name = str(file).split(',')[1].strip()
                                source_uri = "gs://{}/{}".format(bucket_name,file_name)
                                image = Part.from_uri(source_uri, mime_type='image/jpeg')
                                api_response = generate_output(image)
                                output.append(api_response)
                                print('#################################################################')
                        else:
                                break

                except Exception as e:
                        print("Issue with image number {} ".format(counter))
                        print("Args for the issue are {}".format(e.args))
                        break
                
        with open(output_path , 'w+',encoding="utf-8") as file:
                for result in output:
                        file.write(result + '\n')
                        file.write("" +'\n')

#output_path = './results/AI_images_results.txt'
output_path = r"C:\Users\jenna.chang\OneDrive - Accenture\Desktop\rubix git\rubix-cube-structure-data\results\mixed image results.txt"  
#output_path = "./results/mixed image results.txt"   
input_bucket_file = 'Modality data/image/mixed_image'
bucket_name = "acn-cloudwars-chatbot-uki-rubix"
get_image_structure(bucket_name, input_bucket_file, output_path)

