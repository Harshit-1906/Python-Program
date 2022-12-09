def Check_Vow(string, vowels):

    

    string = string.casefold()

    count = {}.fromkeys(vowels, 0)

    # To count the vowels

    for character in string:

        if character in count:

            count[character] += 1

    return count

# Driver Code

vowels = 'aeiou'

string = "Hi,Introduction about Python World "

print (Check_Vow(string, vowels))