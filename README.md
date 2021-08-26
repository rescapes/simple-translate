# Install gcloud if needed. Then run from the installation directory to initialize the SDK
./google-cloud-sdk/bin/gcloud init
# If needed created a Google API Services project, enable billing, create a service account and download the json key
for it: https://cloud.google.com/translate/docs/setup

# Put credentials somewhere
export GOOGLE_APPLICATION_CREDENTIALS="/Users/andy/.ssh/translation-324107-c4c2d281965d.json"
