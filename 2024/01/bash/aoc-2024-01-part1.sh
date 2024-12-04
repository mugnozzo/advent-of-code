#!/bin/bash

<../input awk -F"   " '{print $1 >>"./inputL"; print $2 >>"./inputR";}'

<inputL
