#!/bin/bash

# Isolate mul(num*num) in their own lines
<input sed -re "s/(mul\([0-9]{1,3},[0-9]{1,3}\))/\n\1\n/g" | \
	# Remove useless lines
	sed -rne "/^mul\([^)]*\)$/ p" | \
	# Do the Math
	awk -F"[\(\),]" 'BEGIN{S=0}{print $0;S+=$2*$3}END{print S}'
