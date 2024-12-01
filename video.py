import vertexai
from vertexai.preview.generative_models import GenerativeModel
from vertexai.preview.generative_models import Part
from templates import template_images
from google.cloud import storage
import os 
import json



vertexai.init(project = "acn-cloudwars-chatbot-uki", location = "europe-west2" )
storage_client = storage.Client()
gemini_pro_vision_model = GenerativeModel("gemini-1.0-pro-vision")


def get_config(temperature: int, top_p: int):
        return {
                "temperature": temperature, 
                "top_p": top_p
        }

def process_output(output, output_path):

        process_output = []

        for counter, result in enumerate(output):

                try:
                        if type(result) == str:
                                process_output.append(result)
                        else:
                                output_string = result.text
                                process_output.append(output_string)

                except Exception as e:
                        print('Issue with retrieving text from output for {}'.format(counter))
                        print('The issue is {}'.format(e))
                        break

        with open(output_path , 'w+', encoding='utf-8') as file:

                for counter_1, result in enumerate(process_output):

                        try:
                                file.write(result + '\n')
                                file.write("" +'\n')
                        except Exception as r:
                                print('Could not write result for image number {}'.format(counter_1))
                                print('the Issue is {}'.format(r))
                                break

def generate_output(image):
        model = gemini_pro_vision_model.start_chat()
        api_response = model.send_message([template_images, image], generation_config= get_config(temperature= 0.2, top_p= 0.7)) 
        return api_response

def get_image_structure(bucket_name: str, input_bucket_file: str, output_path:str) -> None:

        bucket_list = storage_client.list_blobs(bucket_name, prefix= input_bucket_file)
        output = []

        for counter, file in enumerate(bucket_list):
                try:
                        if counter < 8:  
                                print('trying with image file path {}'.format(str(file).split(',')[1]))
                                file_name = str(file).split(',')[1].strip()
                                source_uri = "gs://{}/{}".format(bucket_name,file_name)
                                image = Part.from_uri(source_uri, mime_type='video/mp4')
                                api_response = generate_output(image)
                                output.append(api_response)
                                print('#################################################################')
                        else:
                                break

                except Exception as e:
                        print("Issue with image number {} ".format(counter))
                        print("Args for the issue are {}".format(e.args))
                        break

        return output

output_path = './results/video_results.txt'
input_bucket_file = 'Modality data/video/Aggressive_behaviour/files/aggressive'
bucket_name = "acn-cloudwars-chatbot-uki-rubix"
output = get_image_structure(bucket_name, input_bucket_file, output_path)
process_output(output, output_path)