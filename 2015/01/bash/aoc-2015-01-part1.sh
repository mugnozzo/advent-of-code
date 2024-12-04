#!/bin/bash

<../input sed -re "s/([\(\)])/\1\n/g" | sort | uniq -c | \
	sed -zre "s/[^0-9]+/,/g" | awk -F"," '{print $2-$3}'
