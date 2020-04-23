from backend_final import execute_sentiment

negative_reasons = execute_sentiment.get_data("default_students_responses.json")

print(negative_reasons)
