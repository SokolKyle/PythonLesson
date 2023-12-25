months = ["January", "February", "March"]
total_sales = [52000.00, 51000.00, 48000.00]
prod_cost = [46800.00, 45900.00, 43200.00]

for sales, costs, mon in zip(total_sales, prod_cost, months):
    prof = sales - costs
    print("Чистая прибыль в", mon, "=", prof)