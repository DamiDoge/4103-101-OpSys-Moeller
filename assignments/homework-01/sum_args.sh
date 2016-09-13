#!/bin/bash

for var;
do
	let total=$total+$var
	expr=$expr$var'+'
done
expr=${expr:0:-1}
echo $expr'='$total;