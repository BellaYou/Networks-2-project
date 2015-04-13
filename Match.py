# Implement the main algorithm for matching students
numStudents = 0
numQuestions = 0
matchFactor = 0

# First, process the students' preferences:
# Each student will be represented by an array representing the student's answers
# to the preference survey. For each question, the student will have a number 0 to 4 (if 5 choices)
# at the question's position in the student's array. arrays will then be stored in another array.
# Each student is assigned a unique ID number in our system; this number identifies the position
# of the student's answers in the outer array.
studentArray = []

# For each student, compare answer array with every other student. Generate a score for a given matching,
# based on how many different answers they two students have (and how different the answers are).
# From these scores, generate a preference list for each student. 
compareMatrix = []
for i in range(0, numStudents):
	compareMatrix[i] = []
for i in range(0, numStudents):
	for j in range(i, numStudents):
		compareMatrix[i][j] = compare(i, j)
		compareMatrix[j][i] = compareMatrix[i][j]

def compare(s1, s2):
	totalDiff = 0
	for i in range(0, numQuestions):
		if studentArray[s1][i] != studentArray[s2][i]:
			totalDiff += # calculate exact difference, sum diff
	return totalDiff

# Use one of the matching algorithms studied to match the students together. If the given project/class 
# only needs to match groups of 2, use Gale-Shapley, if more than 2, use serial dictator (or something else), etc.

#implement matching algorithms