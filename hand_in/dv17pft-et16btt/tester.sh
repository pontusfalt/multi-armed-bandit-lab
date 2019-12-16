#!/bin/bash
passed='passed'
p=0
for i in {1..100}
do
  t=`python -m pytest`
  if [[ "$t" == *"$passed"* ]]; then
    ((p++))
    echo "Test passed!" $p
  else
    echo "Test failed!"
  fi

done

echo "Passed" $p "/" $i "times!"
