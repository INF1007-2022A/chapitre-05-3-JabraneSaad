#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def get_num_letters(text):
	return 0

def get_word_length_histogram(text):

	maxcount = 0
	histo = []
	for word in text:
		if len(word) > maxcount:
			maxcount = len(word)

	for i in range(maxcount + 1):
		histo.append(0)

	for word in text:
		histo[len(word)] += 1

	return histo





	return [0]

def format_histogram(histogram):
	ROW_CHAR = "*"

	return ""

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"

	return ""


if __name__ == "__main__":
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
