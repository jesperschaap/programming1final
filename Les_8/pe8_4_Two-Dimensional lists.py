# studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]
#
# def gemiddelde_per_student(studentencijfers):
#     x = 0
#     for myList in studentencijfers:
#         print(myList)
#         x = 0
#         for item in myList:
#             for i in range(0,1,1):
#                 x = x + item
#         print(x)
#
# # def gemiddelde_van_alle_studenten(studentencijfers):
# #
# #    return antw
#
# gemiddelde_per_student(studentencijfers)
#
# # print(gemiddelde_van_alle_studenten(studentencijfers))

studentencijfers = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]];

def gemiddelde_per_student(studentencijfers):
    gemiddelden = [];

    for student in studentencijfers:
        gemiddelden.append(sum(student) / len(student));

    return gemiddelden;

def gemiddelde_van_alle_studenten(studentencijfers):
    som = 0;
    aantal = 0;

    for student in studentencijfers:
        som += sum(student);
        aantal += len(student);

    return som / aantal;

print(gemiddelde_per_student(studentencijfers));
print(gemiddelde_van_alle_studenten(studentencijfers));