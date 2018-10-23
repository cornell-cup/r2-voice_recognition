#!/bin/bash
trap ctrl_c INT

function ctrl_c() {
  echo "Ended"
}

arecord -d $1 $2
