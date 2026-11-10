#!/usr/bin/env bash

TEST_DIR="$HOME/test-directory"

rm -rf "$TEST_DIR"

mkdir -p "$TEST_DIR/Images"

cd "$TEST_DIR" || exit 1

touch screenshot.PNG meme.gif resume.pdf notes.txt budget.xlsx \
      song.mp3 clip.mp4 backup.zip project.tar.gz \
      google-chrome.rpm Obsidian.AppImage script.py index.html \
      mystery_file random.xyz .hidden-config big-download.iso.part

echo "Old Photo" > Images/photo.jpg
echo "New Photo" > photo.jpg

echo "Test directory is Ready Freddy: $TEST_DIR"