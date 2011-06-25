#!/usr/bin/env python
# encoding: utf-8
"""
Split words with respect to quotes etc.

About
---------------------------

I needed this for my DSL parser

"""
def safe_split(line):
	word = ""
	out = []
	char_position = 0

	try:
		''' Iterate Char by Char fast forward in double quotes'''
		while char_position < len(line):
			if line[char_position] == " ":
				out.append(word); word = ""
			'''
			'' REFACTOR HERE as a method so that we can also by pass
			'' other special chars such as ( ' 
			''	Handling quotes '''
			if line[char_position] == "\"":
			
				begins = char_position
				char_position = char_position + 1
			
				''' fast forward until we reach another double quote '''
				''' allowing \" type escaping '''
			
				escaped = False
				while escaped or line[char_position] != "\"" :
					if line[char_position] == "\\" : 
						escaped = True
					else:
						escaped = False
					
					char_position = char_position + 1
				
				char_position = char_position + 1
				out.append(line[begins + 1:char_position -1])
			
			word = word + line[char_position]
			char_position = char_position + 1
		
	except IndexError:
		''' we have reached the end while chasing the end of a quote '''
		out.append(word)
	finally:
		out.append(word)
	
	return [x for x in out if x.strip() != '']
