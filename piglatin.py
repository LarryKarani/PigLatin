def Piglatin(word):

	if not isinstance(word, str):

		print("please provide an input whith characters")

	else:

		word_list = list(word)

		pop_char = word_list.pop(0)

		word_list.append("{}{}". format(pop_char, 'ay'))

		return ''.join(word_list)



	

