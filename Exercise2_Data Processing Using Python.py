import csv

# Question 1, 6
filew = open("FileToRead.csv", 'w')
write = csv.writer(filew)
headers = ["Item", "Value"]
write.writerow(headers)

# Question 2, 6
file = open("FileToRead.txt", 'r')
data = file.read()
Total_Char = ["charCount", str(len(data))]
print(Total_Char)
write.writerow(Total_Char)

# Question 3, 6
print(data.count('\n')+1)
No_Line = ["lineCount", str(data.count('\n')+1)]
write.writerow(No_Line)

# Question 4, 6
word_finance = ["financeCount", str(data.count('finance'))]
print(word_finance)
write.writerow(word_finance)

# Question 5, 6
import re
email = re.findall("[a-zA-Z]\\w*@\\w*.\\w*", data)
for i in range(len(email)):
     print(email[i])

     match = ["matchedEmail", email[i]]
     write.writerow(match)

filew.close()


