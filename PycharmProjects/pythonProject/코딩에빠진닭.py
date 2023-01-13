sales_li = []
sales_money = []
sales_days = []
with open('data/chicken.txt', 'r') as f:
    for line in f:
        sales_li = line.strip().split("일: ")
        sales_days.append(sales_li[0])
        sales_money.append(int(sales_li[1])) #숫자니까 int형으로 미리 만들어주기
total_sum = 0
for i in range(0, len(sales_days)):
    total_sum += (sales_money[i])

print(total_sum/(i+1)) #i = 30이므로 12월 마지막날은 31일까지
