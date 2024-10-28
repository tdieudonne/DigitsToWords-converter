
#function to group Entered number into 3 groups
def group_number_into_3(number):
	groups = []
	tmp_group = ""

	while number > 0:
		remainder = number%10
		tmp_group = str(remainder) + tmp_group
		if len(tmp_group) == 3:
			groups.insert(0, [])
			groups[0].append(tmp_group)
			tmp_group = ""
		number //= 10
	if len(tmp_group) != 0:
		groups.insert(0, [])
		groups[0].append(tmp_group)
	return groups

#function to group grouped number into 2
def convert_group(xyz, available_numbers):
	tmp_2_group = ""
	in_words = ""
	tmp_xyz = int(xyz)
	if (int(xyz) in available_numbers):
		if int(xyz) != 0:
			return available_numbers[int(xyz)]
		if int(xyz) == 0:
			return ""
	first_digit = 0
	while tmp_xyz > 0:
		remainder = tmp_xyz%10
		tmp_2_group = str(remainder)+tmp_2_group
		if (len(tmp_2_group) == 2):
			first_digit = tmp_xyz//10
			if int(tmp_2_group) in available_numbers:
				in_words = available_numbers[int(tmp_2_group)]
				if first_digit == 0:
					return in_words
				break
			else:
				word1 = available_numbers[int(tmp_2_group[0])*10]
				word2 = available_numbers[int(tmp_2_group[1])]
				in_words = "{} {}".format(word1, word2)
				if first_digit == 0:
					return in_words
				break
		tmp_xyz = tmp_xyz//10
	first_digit_in_words = "{} {}".format(available_numbers[first_digit], available_numbers[100])
	in_words = "{} {}".format(first_digit_in_words, in_words)
	return in_words

#dictionary containing numbers fundamental to others
available_numbers = {
	0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",
	11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen",20:"Twenty",
	30:"Thirty",40:"Forty",50:"Fifty",60:"Sixty",70:"Seventy",80:"Eighty",90:"Ninenty",100:"Hundred",
	1000:"Thousand",1000000:"Million", 1000000000:"Billion"
}

#get number from user
number = int(input("Enter amount in figures: "))

#get all groups
groups = group_number_into_3(number)

#place value of each group
#calculated using formula 10**(3*place_value) where place balue
#is the index of each group when list is reversed
place_value = len(groups)-1

#variable to hold results
words = ""

#loop throu groups
for group in groups:

	group_in_words = convert_group(group[0], available_numbers)

	#append place value only if it is above ones
	if place_value > 0:
		group_in_words = "{} {}".format(group_in_words,available_numbers[10**(3*place_value)])

	if (place_value == 0) and (groups.index(group)) != 0:
		group_in_words = f"and {group_in_words}"
	words = "{} {}".format(words, group_in_words) 
	place_value -= 1

print(words.strip())