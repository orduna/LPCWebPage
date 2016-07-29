import os, sys, re, subprocess

file = open("temp.txt", 'r')

for line in file:
	name = line.split("-")[-1].replace("\n", '')
	date = line.split("-")[0].split(" ")

	string = ('\n' +
			  '\t<tr>\n' +
			  '\t\t<td class="day">'+ date[5] +' ' + date[4] +'</td>\n' +
			  '\t\t<td class="speaker"><a href="">' + name +'</a></td>\n' +
			  '\t\t<td class="topic">TBD</td>\n' +
			  '\t\t<td class="where">WH11 NE (Sunrise)</td>\n' +
			  '\t</tr>')
		
	
	print string
