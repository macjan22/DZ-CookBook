cook_book = {}
with open("recipes.txt", "r", encoding="utf-8") as f:
    n = 0
    fl = -1
    current_dish = "" 
    
    for line in f:
        line = line.strip() 
        
        if n > 0: 
            parts = line.split("|")  
            if len(parts) >= 3: 
                cook_book[current_dish].append({
                    "ingredient_name": parts[0].strip(),
                    "quantity": parts[1].strip(),
                    "measure": parts[2].strip()
                })
                n -= 1
            continue
            
        if not line:  
            continue
            
        if line.isdigit():  
            n = int(line)
            continue
            
        if not any(char.isdigit() for char in line) and '|' not in line and len(line) > 1:
            current_dish = line.strip()
            cook_book[current_dish] = []
            fl = 1

print(cook_book)

for dish in cook_book:
    print("\n" + dish + ":\n")
    print("##########")
    for ingredient in cook_book[dish]:
        print(f"{ingredient['ingredient_name']} | {ingredient['quantity']} | {ingredient['measure']}")
        print("##########")