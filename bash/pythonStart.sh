#!/bin/bash
line1="#!/usr/bin/python3"
for file in *.py; do
	if [ -f "$file" ]; then
		echo "$line1" >> "$file"
		echo "$line2" >> "$file"
	fi
done

