if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        
    grades = sorted(list(set([score for name, score in records])))
    second_lowest_grade = grades[1]
    

    result_names = sorted([name for name, score in records if score == second_lowest_grade])
    
    for name in result_names:
        print(name)