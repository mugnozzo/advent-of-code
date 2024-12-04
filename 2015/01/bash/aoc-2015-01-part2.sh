#!/bin/bash

<../input sed -re "s_\(_1\n_g" -re "s_\)_-1\n_g" | \
	awk 'BEGIN{S=0}{S+=$1;print S;if(S==-1){print NR;exit}}'
