#!/usr/bin/env sh
# This script converts the mnist data into lmdb/leveldb format,
# depending on the value assigned to $BACKEND.
set -e

EXAMPLE=/home/ubuntu/final_project/FinalProject
DATA=/home/ubuntu/final_project/FinalProject
BUILD=/home/ubuntu/caffe/build/examples/oxford


BACKEND="lmdb"

echo "Creating ${BACKEND}..."

rm -rf $EXAMPLE/oxford_train_${BACKEND}
rm -rf $EXAMPLE/oxford_test_${BACKEND}

$BUILD/convert_oxford_data.bin $DATA/train \
  $EXAMPLE/oxford_train_${BACKEND} --backend=${BACKEND}
$BUILD/convert_oxford_data.bin $DATA/validation \
  $EXAMPLE/oxford_test_${BACKEND} --backend=${BACKEND}

echo "Done."
