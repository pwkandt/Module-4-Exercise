def computeGrade(score):
    try:
        score = float(score)

        if score > 1.0:
            return 'Bad score'
        elif score >= 0.9 and score <= 1.0:
            return 'A'
        elif score >= 0.8 and score < 0.9:
            return 'B'
        elif score >= 0.7 and score < 0.8:
            return 'C'
        elif score >= 0.6 and score < 0.7:
            return 'D'
        elif score > 0.0 and score < 0.6:
            return 'F'
        elif score < 0.0:
            return 'Bad Score'
    except:
        return 'Bad score'


score = input("Enter Score Between 0.0 and 1.0: ")
score = computeGrade(score)
print(score)
