#!/bin/bash

for url in $(grep -o '[A-Za-z0-9_\.-]*\.*cisco.com' index.html |sort -u) ;do
host $url|grep "has address"|cut -d" " -f4
done
