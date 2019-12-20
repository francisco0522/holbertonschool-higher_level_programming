#!/usr/bin/python3
def complex_delete(a_dictionary, value):
	for i in range(len(a_dictionary)):
		for key, v in a_dictionary.items():
			if v == value:
				del a_dictionary[key]
				break;
	return a_dictionary
