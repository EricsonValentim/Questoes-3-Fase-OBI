# Resolução da Questão nivel sênior mesa da 3ª fase da OBI2019
# Autores: Renan e Carlos
a = int(input())
b = int(input())

ana_seat = (1 + a - 1) %3
beatriz_seat = (1 + b - 1) %3

if beatriz_seat == ana_seat:
    beatriz_seat = (beatriz_seat + 1) % 3
else:
    beatriz_seat = beatriz_seat


seats = [0, 1, 2]
seats.remove(ana_seat)
seats.remove(beatriz_seat)
carolina_seat = seats[0]

print(carolina_seat)