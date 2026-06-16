import csv

num_attributes = 6
a = []

print("\nThe Given Training Data Set\n")

with open('enjoysport.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)
    a = data[1:]   # Skip header row

    for row in a:
        print(row)

print("\nThe initial value of hypothesis:")
hypothesis = a[0][:num_attributes]
print(hypothesis)

print("\nFind S: Finding a Maximally Specific Hypothesis\n")

for i in range(len(a)):
    if a[i][-1].strip().lower() == 'yes':   # Checking last column
        for j in range(num_attributes):
            if a[i][j] != hypothesis[j]:
                hypothesis[j] = '?'

        print("For Training instance No:", i+1,
              "the hypothesis is:", hypothesis)

print("\nThe Maximally Specific Hypothesis for the given Training Examples:\n")
print(hypothesis)