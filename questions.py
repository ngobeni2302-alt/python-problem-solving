
def daily_sales(sales):
    return sum(sales)
print(daily_sales([12,8,5,10]))

def total_goals(goals):
    return sum(goals)
print(total_goals([2,3,1,4]))

def class_attendance(students):
    total = 0 
    for i in students:
        total += i
    return total
print(class_attendance([25,24,26,23]))

def total_distance(distances):
    total = 0
    for i in distances:
        total += i
    return total
print(total_distance([5,3,6,4]))

def warehouse_items(items):
    return sum(items)
print(warehouse_items([20,15,30]))

# ----- DISCOUNT TYPE QUESTIONS -----

def half_price(prices):
    ls = []
    for i in prices:
        a = i // 2
        ls.append(f"R {a}")
    return ls
print(half_price([80,120,200]))

def student_discount(prices):
    price = []
    for i in prices:
        x = i // 2
        price.append(f"R {x}")
    return price
print(student_discount([60, 100, 40]))

def movie_special(prices):
    price = []
    for i in prices:
        x = i // 2
        price.append(f"R {x}")
    return price
print(movie_special([20, 30, 50]))

def gym_promo(prices):
    price = []
    for i in prices:
        x = i // 2
        price.append(f"R {x}")
    return price
print(gym_promo([500,800]))

def tech_sale(prices):
    price = []
    for i in prices:
        x = i // 2
        price.append(f"R {x}")
    return price
print(tech_sale([1000,600,200]))