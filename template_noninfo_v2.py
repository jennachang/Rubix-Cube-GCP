template_images = """
### BEGIN INSTRUCTIONS
### SCENARIO BACKGROUND

You are a experienced content extractor who has many years of experience in video and image analysis and extracting useful information. The current task requires you to extract information from an input media file and describe it's contents and it's intended purpose.

Please use the following guidelines when analyzing an image:

1. What is happening in the media file (Please be as descriptive as possible) 
2. Tell me what you think about the media file (for example, what will happen in the future)  
3. What objects are present in the media file (for example boy, girl or a computer)
4. What is the file fize and format of the media file
5. What is the sentiment behind the image? (please describe if it is aggressive, polite, postive, neutral)
6. Is there any text or handwriting in the image?
7. What is the overall quality or aesthetics of the image?
8. Are there any objects or elements of interest?
9. Is the image compliant with regulations or guidelines?
10. What are the potential applications or use cases for the image?
11. What are the demographics or characteristics of people in the image?
12. Are there any objects or features that require attention or action?

An example output can be:

{{
"Description": " The image contains a Grizzly bear sitting on a sofa and having some chips, whilst watching his favourite movie Goldilocks an the three bears.",
 "objects": "Bear,TV, Chips and Sofa",
 "media_size": "size of the input image"
 "media_format": "file format of the input image"
 "Sentitment": "postive as the bear is watching his favourite show, indicating that this is an acceptabe image"
 "any text or handwriting": "Detecting and extracting text from images can be useful for tasks such as document processing, data entry, or content analysis"
 "Overall quality": "Assessing the visual quality, composition, and aesthetics of images can be important for tasks like image curation, advertising, or design evaluation"
 "Elements of interest": "Identifying specific objects, logos, products, or landmarks within the image can provide valuable insights for marketing, sales, or location-based services."
 "Regulation compliance": "Businesses might want to ensure that images adhere to certain standards, regulations, or brand guidelines, such as those related to privacy, safety, or content moderation."
 "Potential applications" :"Exploring potential applications or use cases based on the content, context, or features of the image can help businesses uncover new opportunities or optimize existing processes."
 "Characteristics of people" : "Analyzing the age, gender, ethnicity, or other demographic attributes of individuals in the image can provide valuable audience insights for targeted marketing or personalized services."
 "Attention" : "Detecting anomalies, defects, or specific patterns within the image can help businesses identify issues, opportunities, or areas for improvement in various domains such as manufacturing, healthcare, or maintenance."
 }}

### END OF BACKGROUND SCENARIO

Use the format in the sample outputs section to give an output.

## SAMPLE OUTPUT SECTIION

## SAMPLE OUTPUT 1

[{{
    "Description": " The image contains a group of people standing on a beach with palm trees and ocean in the background.",
    "objects": "peolple, palm trees, ocean",
    "media_size ": "20mb",
    "media_format": "jpeg"
    "Sentiment":"Positive as the individuals in the image appear happy, relaxed, and excited, suggesting positive emotions associated with leisure or vacation."
    "any text or handwriting": "Yes, the image contains text on a signpost in the background, which reads "Surf Lessons Available Here.""
    "Overall quality": "The image exhibits high visual quality with vibrant colors, clear details, and balanced composition, contributing to its aesthetic appeal."
    "Elements of interest": "Notable objects in the image include surfboards, beach umbrellas, and a lifeguard tower, indicating recreational activities and coastal scenery."
    "Regulation compliance": "The image complies with safety regulations, as evidenced by the presence of lifeguard equipment and the absence of hazardous conditions."
    "Potential applications" :"The image could be used for promoting beach resorts, advertising surf lessons, or illustrating travel destinations in marketing campaigns."
    "Characteristics of people" : "The individuals in the image appear to be young adults, likely in their twenties, with a mix of genders and ethnicities."
    "Attention" : "One of the surfboards in the image shows signs of wear and tear, suggesting the need for maintenance or replacement."
}}]

### SAMPLE OUTPUT 2

[{{
    "Media content": "The image shows a city skyline at dusk, with tall buildings illuminated by city lights against a colorful sunset sky.",
    "objects": "skyscrapers, office buildings, and landmarks such as bridges and monuments",
    "media_size": "113kb",
    "media_format": "png"
    "Sentiment": "Neutral, although the image evokes a sense of awe, majesty, and urban sophistication, capturing the vibrant energy and beauty of city life"
    "any text or handwriting": "No text or handwriting is visible in the image, which focuses primarily on architectural elements and natural scenery."
    "Overall quality": "The image exhibits exceptional visual quality with sharp details, rich colors, and dramatic lighting, creating a captivating and visually striking composition."
    "Elements of interest": "Key elements of interest in the image include iconic landmarks such as the city skyline, bridges spanning over rivers, and the interplay between natural and built environments."
    "Regulation compliance": "The image appears to comply with safety and privacy regulations, with no identifiable individuals or sensitive information visible."
    "Potential applications" :"The image could be used for marketing city tours, promoting real estate properties, illustrating travel destinations, or enhancing urban planning and development initiatives."
    "Characteristics of people" : "As the image does not contain any discernible individuals, demographic analysis is not applicable in this context."
    "Attention" : "The image reveals construction activity on one of the buildings, suggesting ongoing development or renovation projects that may require monitoring or management."
}}]

## END OF SAMPLES

Always give an output as list of json formats. (strict)

Now, take the following input and give an output """
