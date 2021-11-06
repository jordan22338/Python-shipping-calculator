weight = 8.4
if weight <= 2:
  cost = weight * 4.50 + 20
elif weight < 2 or weight <= 6:

  cost = weight * 9.00 + 20
elif weight < 6 or weight <= 10 :
  cost = weight * 12.00 + 20
else:
  cost = weight * 14.25 + 20
print(cost)
