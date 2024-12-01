template_images = """
### SCENARIO BACKGROUND
Your job is to extracting information from a graph or a picture, as well as from any tables and charts within documents, to do image analysis and extract useful information. 

The current task requires you to extract information from an input media file and describe it's contents and it's intended purpose.

This is a difficult task as the details need to be exact and concise. Please do not be creative or speculative with your responses. 

Please ensure that the results with accurate spelling and no special characters, to facilitate easy understanding by humans.


Please use the following metrics below when you read and extract and analyse information from a single file

"Description": You will need to tell a detailed description of the content, elements, and context of the image. It includes information about what is depicted in the image, such as objects, people, scenes, or text.

"Possible_source": You will need to tell the potential origin or where the image may have been sourced from. It could include sources such as a website, social media platform, digital publication, stock photo library, or personal collection.

"Media_size": You will need to tell the size of the image file, typically measured in kilobytes (KB) or megabytes (MB). It provides information about the digital storage space required for the image.

"Media_format": You will need to identify the file format of the image, such as JPEG, PNG, GIF, TIFF, or BMP. It describes how the image data is encoded and stored.

"Word_count": You will need to count the number of words, special characters and emojis presented within the image. It provides insight into the textual content or amount of information contained in the image.

"Purpose_or_application: You will need to describe the intended use or application of the image. It could include purposes such as informational, educational, promotional, illustrative, or decorative. It also highlights the context in which the image is intended to be used.

"Image_quality": You will need to evaluate the overall quality of the image, considering factors such as resolution, clarity, sharpness, color accuracy, and absence of distortion or artifacts. It assesses how well the image visually represents the content and conveys information effectively.
 
### END OF SCENARIO BACKGROUND

### BEGIN OF SAMPLE OUTPUT SECTION

Please use the format in the example sample outputs section (below) to give an output. (strict)

## SAMPLE OUTPUT 1

{{
    "Description": "The image serves as a summary, presenting multiple tables illustrating the distribution of Apple employee salaries.",
    "Possible_source": " The possible source of this image could be a company's internal report or presentation, a financial analysis article or report, or a data visualization platform showcasing salary distribution data. Alternatively, it could be sourced from a business news website or a research publication discussing trends in employee compensation.",
    "Media_size": "8.73kb",
    "Media_format": "png",
    "Word_count": "There are one bar chart, two pie charts and one Geographical Distribution Chart. The total word count extracted from this image is 50 English words, 3 spanish words, along with 5 special characters and 10 emojis."
    "Purpose_or_application": "The purpose or application of this image could be to provide insights into the salary distribution among Apple employees, aiding in financial analysis, workforce planning, or benchmarking against industry standards.",
    "image_quality": "The image quality appears to be high-definition, with clear and sharp details that allow for easy readability of the text and accurate interpretation of the visual elements."
    
}}


### END OF SAMPLE OUTPUT

Always give an output as list of json formats(strict)

Now, take the following input and give an output 

## End OF INSTRUCTIONS 

"""


