# Rubix Cube Structure Data Project
This project obtains different kind of files (images, video, text), classify them, obtain relevant information and metadata and stores the information in a BigQuery table for Analysis. 

## Required tools
1. Code editor. Pycharm or VSCode
2. Git. You can download it from https://git-scm.com/downloads
3. GCP SDK and CLI https://cloud.google.com/sdk?hl=en
4. Open ssh. 
5. check you have access to the project  cia GCP web console https://console.cloud.google.com/welcome/new?project=acn-cloudwars-chatbot-uki

## Environment Setup
Two ways to set up the project, both described below.

### Via SSH Authentication
1. Request for read/write access permission to the repository.
2. Create a SSH key as described [here](https://cloud.google.com/source-repositories/docs/authentication?&_ga=2.241617026.-1422112553.1644353129#generate_a_key_pair). Use *rsa* for *KEY_TYPE*. Thios will create a pair of files, one of the has the *.pub* file.
3. Open the *.pub* file using any tex editor and copy the file content.
4. Register your public key (.pub file) in the [repository keys store](https://source.cloud.google.com/user/ssh_keys). Provide a key name and paste the content of the *.pub* file in the *key* field.
5. Clone the repository via the command `git clone ssh://<YOUR_ACCENTURE_EMAIL>@source.developers.google.com:2022/p/acn-cloudwars-chatbot-uki/r/rubix-cube-structure-data` 

## Via GCloud
1. Request for read/write access permission to the repository.
2. Install the [GCP SDK](https://cloud.google.com/sdk?_ga=2.43845029.-1422112553.1644353129&hl=en) if not installed 
3. In a command line execute `gcloud init` to authenticate with GCP
4. Clone the repository via the command `gcloud source repos clone rubix-cube-structure-data --project=acn-cloudwars-chatbot-uki`

## Commit conventions
We are following the commit conventional messages described in the [conventional commits v1.0.0](https://www.conventionalcommits.org/en/v1.0.0/)