#!/bin/bash
#echo "---------------------------------"
#env
echo "---------------------------------"
echo -n "moj hostname "
hostname 
echo -n "moja nazwa: "
echo $0
echo -n "moje parametry: "
echo $*
/usr/sbin/httpd -DFOREGROUND

