#!/bin/bash

# Q&D Script to create 100 directories. One for each of the exersices in the UDEMY course:
# 
# Python Workbook 100 Exercises
#
for i in {1..100}
do 
	if [[ $i -le 10 ]]
  then
	  mkdir ex-0"${i}"
	elif [[ $i -lt 101 ]] 
	then
		mkdir ex-"${i}"
	fi	
done
		

