#!/usr/bin/env bash

cat ./src/audios_to_fetch.csv | while read -r audio_description; do \
    ./scripts/fetchAudio.sh "$audio_description"; \
done
