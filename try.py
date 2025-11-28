from model import predict_job

# Example: person knows Python + HTML, 1 year experience
job = predict_job(python=1, java=0, html=1, css=1, ml=0, experience=1)
print("Predicted job:", job)
