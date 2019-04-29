#!/usr/bin/env sh
# This scripts downloads the cifar data and unzips it.

DIR="$( cd "$(dirname "$0")" ; pwd -P )"
cd "$DIR"

echo "Downloading..."

for fname in images.tar.gz
do
    if [ ! -e $fname ]; then
        wget --no-check-certificate https://www.kaggle.com/zippyz/cats-and-dogs-breeds-classification-oxford-dataset/downloads/cats-and-dogs-breeds-classification-oxford-dataset.zip/1
        gunzip ${fname}
    fi
done
