#!/usr/bin/env bash

read -p "Ready to Upload Video? (Y/N): " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1

read -p "Enter Video Title: " title
read -p "Enter Video Description: " description
read -p "Enter Video Tags: " tags
read -p "Enter Thumbnail File Name: " thumbnail

youtube-upload \
  --title="$title" \
  --description="$description" \
  --category="Entertainment" \
  --tags="$tags" \
  --default-language="en" \
  --default-audio-language="en" \
  --client-secrets="/Users/asammalik/Desktop/VideoMaker/youtube-upload/client_secrets.json" \
  --thumbnail="$thumbnail" \
  --privacy="unlisted" \
  final.mp4