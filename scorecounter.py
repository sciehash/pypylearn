# Simple score counter to count olympiad participant's score

correct = 4
wrong = -1
unanswered = 0
anna_score = correct * 30 + wrong * 8
dean_score = correct * 25 + wrong * 15
grace_score = correct * 10 + wrong * 15
score_comparison = anna_score > grace_score > dean_score
print(f"Anna's score is {anna_score}")
print(f"Dean's score is {dean_score}")
print(f"Grace's score is {grace_score}")
print(f"Score Prediction: {score_comparison}")
