'''
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c —
стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой
двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
равнобедренным или равносторонним.
'''

# a = 11
# b = 22
# c = 33

# a = 10
# b = 10
# c = 10

a = 10
b = 5
c = 10

# a = 10
# b = 11
# c = 12

def check_triangle(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        print("Треугольник существует ")
        if a == b and b == c and a == c:
            print("Треугольник - равносторонний")
        elif a == b or b == c or a == c:
            print("Треугольник - равнобедренный")
        else:
            print("Треугольник - разносторонний")
    else:
        print("Треугольник не существует")

check_triangle(a,b,c)