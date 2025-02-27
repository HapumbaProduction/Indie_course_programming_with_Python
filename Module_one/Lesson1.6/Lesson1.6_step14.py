number_pencils_bought, number_pens_bought, number_felt_tip_pens_bought = map(int, input().split())
pencil_price = 3
pen_price = 5
felt_tip_pen_price = 12

print((number_pencils_bought * pencil_price) + (number_pens_bought * pen_price) + (number_felt_tip_pens_bought * felt_tip_pen_price))
