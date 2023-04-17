# Python program for the above approach

# Returns the maximum length


def maxLen(arr):

	# NOTE: Dictionary in python is
	# implemented as Hash Maps
	# Create an empty hash map (dictionary)
	hash_map = {}

	# Initialize result
	max_len = 0

	# Initialize sum of elements
	curr_sum = 0

	# Traverse through the given array
	for i in range(len(arr)):

		# Add the current element to the sum
		curr_sum += arr[i]

		if curr_sum == 0:
			max_len = i + 1

		# NOTE: 'in' operation in dictionary
		# to search key takes O(1). Look if
		# current sum is seen before
		if curr_sum in hash_map:
			max_len = max(max_len, i - hash_map[curr_sum])
		else:

			# else put this sum in dictionary
			hash_map[curr_sum] = i

	return max_len


# Driver's code
if __name__ == "__main__":

	# test array
	arr = [15, -2, 2, -8, 1, 7, 10, 13]

	# Function call
	print("Length of the longest 0 sum subarray is % d" % maxLen(arr))
