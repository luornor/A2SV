def average(salary: list[int]) -> float:
    salary.remove(min(salary))
    salary.remove(max(salary))

    return float((sum(salary)/len(salary)))


print(average([1000,2000,3000]))