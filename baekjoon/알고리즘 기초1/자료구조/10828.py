def solution(today, terms, privacies):

    answer = []

    # today
    today_total = today.split(".")

    # 총 terms 나누기
    terms_total = len(terms)
    terms_first = []  # A B C
    terms_second = []  # 6 12 3

    for i in range(terms_total):
        terms_split = terms[i].split()       # ["A","6"]
        terms_first.append(terms_split[0])   # ["A"]
        terms_second.append(terms_split[1])  # 6

    # 총 pricvacies 나누기
    privacies_total = len(privacies)
    privacies_first = []  # 2021.05.02, 2021.07.01 ...
    privacies_second = []  # A B C C

    for i in range(privacies_total):
        privacies_split = privacies[i].split()  # ["2021.05.02" , "A"]
        privacies_first.append(privacies_split[0])    # 2021.05.02
        privacies_second.append(privacies_split[1])   # A

        for j in range(terms_total):
            if terms_first[j] == privacies_second[i]:
                month = privacies_second[i].split(".")
                print("==================", month)
                after_year = int(month[0])
                after_month = int(month[1]) + int(terms_second[j])
                after_date = int(month[2])-1
                if(after_month > 12):
                    after_month = after_month % 12
                    after_year += (after_month % 12)

                    if(after_date == 0):
                        after_month -= 1
                        after_date = 28
                    if(after_month < 10):
                        after_month = "0" + str(after_month)
                    if(after_date < 10):
                        after_date = "0" + str(after_date)

                    after = str(after_year) + "." + \
                        str(after_month) + "." + str(after_date)
                else:
                    if(after_date == 0):
                        after_month -= 1
                        after_date = 28
                    if(after_month < 10):
                        after_month = "0" + str(after_month)
                    if(after_date < 10):
                        after_date = "0" + str(after_date)
                    after = str(after_year) + "." + \
                        str(after_month) + "." + str(after_date)

                after_days = month[0] + after_month + month[2]
                if today >= after:
                    answer.append(i+1)

    return answer


solution("2022.05.19", ["A 6", "B 12", "C 3"],
         ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])
