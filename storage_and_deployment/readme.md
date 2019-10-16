
# Storage And Deployment

Participants: Ysé

## DB storage

Storage of the Microfaune DB (alternatives with prices).

- For the Bird Audio Detection Challenge, data are stored on Figshare and Archive.
- suggestions made by other: BlackBlaze
- AWS bucket (TODO: check for pricing)
- GCP storage (TODO: check for pricing)

## Model storage

Back-end hosting for deployment. Choose tech etc.

### GRPC Service
gRPC application is a Backend Service created by Google. 
Very efficient. With a typed protocol, we can exchange bytes data  (audio, a wav files) and streaming data (microphone)
For more info. See https://gRPC.io/

## Model Deployment

Several alternatives are considered:
- in local, use a Makefile and bash script
- if complexe data proprecssing, use Airflow
- use circleci or travis for automation 

Model is stored in the repository (if small enough or in a storage)

### Upload audio file

A short audio file is uploaded and the label (bird/no bird) is returned.

### Extract bird segments

The user upload an audio file and audio segments containing bird sounds are returned. This can be good first step for bird identification.

### Real-time bird detection

Users turn on their microphone and a visual cue indicate when there is a bird.
