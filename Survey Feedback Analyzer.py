feedback_data = {
 'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
 'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
 'Feedback': [
 ' Very GOOD Service!!!',
 'poor support, not happy ',
 'GREAT experience! will come again.',
 'okay okay...',
 ' not BAD',
 'Excellent care, excellent staff!',
 'good food and good ambience!',
 'Poor response and poor handling of issue',
 'Satisfied. But could be better.',
 'Good support... quick service.'
 ],
 'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}
print(feedback_data)



n = int(input("How many more feedbacks do you want to add? "))
sno=11

for i in range(n):

    name = input("Enter your name: ")
    feedback = input("Enter your feedback: ")
    rating = int(input("Enter your rating (1-5): "))
    feedback_data['S_No'].append(sno) 
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(feedback)
    feedback_data['Rating'].append(rating)
    sno +=1

print(feedback_data)


for i in range(len(feedback_data['Feedback'])):

    feedback = feedback_data['Feedback'][i]
    feedback = feedback.replace(".", "")
    feedback = feedback.replace(",", "")
    feedback = feedback.replace("!", "")
    feedback = feedback.replace("?", "")
    feedback = ' '.join(feedback.split())
    feedback = feedback.lower()
    feedback_data['Feedback'][i] = feedback

print(feedback_data['Feedback'])


def count_word_in_feedbacks(word):
    count = 0
    for feedback in feedback_data['Feedback']:
        if word.lower() in feedback.lower():
            count += 1
            return count

print("Feedbacks containing good:", count_word_in_feedbacks("good"))
print("Feedbacks containing poor:", count_word_in_feedbacks("poor"))
print("Feedbacks containing excellent:", count_word_in_feedbacks("excellent"))
print("Final Cleaned Feedback Data:")
print(feedback_data)

total_rating = sum(feedback_data['Rating'])
total_feedbacks = len(feedback_data['Rating'])
average_rating = total_rating / total_feedbacks

print("Average Rating:", average_rating)

max_words = 0
longest_feedback = ""

for feedback in feedback_data['Feedback']:
    word_count = len(feedback.split())
    if word_count > max_words:
        max_words = word_count
        longest_feedback = feedback

print("Number of Words:", max_words)

unique_words = set()
for feedback in feedback_data['Feedback']:
    words = feedback.split()
    for word in words:
        unique_words.add(word)

print("Unique Words:")
print(unique_words)



feedback_entries = zip(
    feedback_data["Rating"],
    feedback_data["S_No"],
    feedback_data["Name"],
    feedback_data["Feedback"]
)
sorted_feedbacks = sorted(feedback_entries, reverse=True)
print("Feedbacks sorted by rating:")
for Rating, S_No, Name, Feedback in sorted_feedbacks:
    print(Rating,S_No,Name,Feedback)
