# Formatting a Number with a comma as the thousands separator

my_int = 489985123

# ✅ Format integer with commas as thousands separator
result = f'{my_int:,}'
print(result)  # 👉️ 489,985,123

# ✅ Format integer with spaces as thousands separator
result = f'{my_int:,}'.replace(',', ' ')
print(result) # 👉️ 489 985 123