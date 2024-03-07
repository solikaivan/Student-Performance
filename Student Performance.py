def rate_performance(marks):

 if   70<= marks <=80:
        return  "Distinction"
 elif 60 <= marks <= 70:
        return "Credit"
 elif 50 <= marks <= 60:
        return "Pass"
 elif 40 <= marks <= 50:
        return "Fair"
 else:
        return "Fail"
scores = [63, 51, 40, 29, 80, 77]

for score in scores:
    print(f"Score: {score}, Performance: {rate_performance(score)}")