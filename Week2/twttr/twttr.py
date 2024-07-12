vowels = "aeiouAEIOU"

tweet = input("Tweet: ")
twt = [char for char in tweet if char not in vowels]
print("".join(twt))