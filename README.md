# Agent Labs

## Setup

### Google Cloud Authentication

To use Google Cloud services, you need to install the gcloud CLI and set up authentication:

1. Install gcloud CLI: `brew install --cask google-cloud-sdk`
2. Authenticate with Application Default Credentials: `gcloud auth application-default login`

**Application Default Credentials (ADC)** are a strategy used by Google client libraries to automatically find credentials. When you run `gcloud auth application-default login`, it stores your user credentials in a well-known location that Google client libraries can automatically discover and use for API calls. This eliminates the need to explicitly pass credentials in your code.