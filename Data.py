import pandas as pd

drinks_data_from_csv = pd.read_csv('Copia_de_datos_bebidas.csv', sep=';')
drinks_data = pd.DataFrame(drinks_data_from_csv)

fetch_data_csv = pd.read_csv("datos_proyecto_de_aula.csv", sep=";")
columns = list(fetch_data_csv)
data_base = []

student_data = {
        "gender": "",
        "height": 0,
        "weight": 0,
        "studyHours": 0.0,
        "age": 0,
        "timeBackingHouse": 0,
        "lastSemesterAvg": 0.0,
        "enrollmentValue": 0,
        "stratum": 0,
        "isWorking": False
    }


for j in range(0, len(fetch_data_csv)):
    current_student = []
    student_data = {}
    for i in columns:
        current_student.append(fetch_data_csv[i][j])

    if current_student[0] == "MUJER":
        student_data["gender"] = True
    elif current_student[0] == "HOMBRE":
        student_data["gender"] = False

    student_data["height"] = current_student[1]
    student_data["weight"] = current_student[2]
    student_data["studyHours"] = current_student[3]
    student_data["age"] = current_student[4]
    student_data["timeBackingHouse"] = current_student[5]
    student_data["lastSemesterAvg"] = current_student[6]
    student_data["enrollmentValue"] = current_student[7]
    student_data["stratum"] = current_student[8]
    if current_student[9] == "SI":
        student_data["isWorking"] = True
    elif current_student[9] == "NO":
        student_data["isWorking"] = False
    data_base.append(student_data)



"""data_base = [
    {
        "gender": "Male",
        "height": 151,
        "weight": 62,
        "studyHours": 0.3954,
        "age": 24,
        "timeBackingHouse": 63,
        "lastSemesterAvg": 2.4,
        "enrollmentValue": 3061445,
        "stratum": 3,
        "isWorking": False
    },
    {
        "gender": "Male",
        "height": 150,
        "weight": 90,
        "studyHours": 2.2838,
        "age": 23,
        "timeBackingHouse": 93,
        "lastSemesterAvg": 3.2,
        "enrollmentValue": 4375655,
        "stratum": 3,
        "isWorking": False
    },
    {
        "gender": "Female",
        "height": 169,
        "weight": 88,
        "studyHours": 2.0699,
        "age": 21,
        "timeBackingHouse": 71,
        "lastSemesterAvg": 5,
        "enrollmentValue": 2914072,
        "stratum": 4,
        "isWorking": True
    },
    {
        "gender": "Female",
        "height": 156,
        "weight": 79,
        "studyHours": 0.4046,
        "age": 25,
        "timeBackingHouse": 114,
        "lastSemesterAvg": 1.8,
        "enrollmentValue": 2694273,
        "stratum": 3,
        "isWorking": True
    },
    {
        "gender": "Male",
        "height": 178,
        "weight": 86,
        "studyHours": 1.8601,
        "age": 19,
        "timeBackingHouse": 107,
        "lastSemesterAvg": 5,
        "enrollmentValue": 4815397,
        "stratum": 3,
        "isWorking": True
    },
    {
        "gender": "Male",
        "height": 157,
        "weight": 67,
        "studyHours": 2.1555,
        "age": 18,
        "timeBackingHouse": 89,
        "lastSemesterAvg": 3.9,
        "enrollmentValue": 2831263,
        "stratum": 4,
        "isWorking": True
    },
    {
        "gender": "Male",
        "height": 158,
        "weight": 89,
        "studyHours": 2.8153,
        "age": 18,
        "timeBackingHouse": 118,
        "lastSemesterAvg": 0.6,
        "enrollmentValue": 4579876,
        "stratum": 5,
        "isWorking": True
    },
    {
        "gender": "Male",
        "height": 156,
        "weight": 71,
        "studyHours": 2.5079,
        "age": 24,
        "timeBackingHouse": 46,
        "lastSemesterAvg": 2.7,
        "enrollmentValue": 4647774,
        "stratum": 2,
        "isWorking": False
    },
    {
        "gender": "Female",
        "height": 158,
        "weight": 63,
        "studyHours": 2.6828,
        "age": 19,
        "timeBackingHouse": 44,
        "lastSemesterAvg": 3.1,
        "enrollmentValue": 2544661,
        "stratum": 2,
        "isWorking": True
    },
    {
        "gender": "Male",
        "height": 153,
        "weight": 74,
        "studyHours": 0.6683,
        "age": 23,
        "timeBackingHouse": 80,
        "lastSemesterAvg": 5,
        "enrollmentValue": 2409702,
        "stratum": 4,
        "isWorking": True
    },
    {
        "gender": "Female",
        "height": 169,
        "weight": 92,
        "studyHours": 2.2245,
        "age": 22,
        "timeBackingHouse": 54,
        "lastSemesterAvg": 1.3,
        "enrollmentValue": 2190523,
        "stratum": 5,
        "isWorking": False
    },
    {
        "gender": "Male",
        "height": 162,
        "weight": 91,
        "studyHours": 1.4741,
        "age": 18,
        "timeBackingHouse": 48,
        "lastSemesterAvg": 0.5,
        "enrollmentValue": 2948830,
        "stratum": 3,
        "isWorking": False
    },
    {
        "gender": "Female",
        "height": 160,
        "weight": 73,
        "studyHours": 2.8505,
        "age": 24,
        "timeBackingHouse": 85,
        "lastSemesterAvg": 0.8,
        "enrollmentValue": 4349089,
        "stratum": 2,
        "isWorking": False
    },
    {
        "gender": "Female",
        "height": 170,
        "weight": 82,
        "studyHours": 0.5024,
        "age": 22,
        "timeBackingHouse": 72,
        "lastSemesterAvg": 4.1,
        "enrollmentValue": 2605021,
        "stratum": 2,
        "isWorking": False
    },
    {
        "gender": "Male",
        "height": 182,
        "weight": 68,
        "studyHours": 1.3757,
        "age": 25,
        "timeBackingHouse": 55,
        "lastSemesterAvg": 1.8,
        "enrollmentValue": 2573234,
        "stratum": 2,
        "isWorking": False
    },
    {
        "gender": "Male",
        "height": 155,
        "weight": 60,
        "studyHours": 2.1252,
        "age": 18,
        "timeBackingHouse": 80,
        "lastSemesterAvg": 4.1,
        "enrollmentValue": 4112908,
        "stratum": 2,
        "isWorking": False
    },
    {
        "gender": "Female",
        "height": 175,
        "weight": 80,
        "studyHours": 0.5563,
        "age": 25,
        "timeBackingHouse": 110,
        "lastSemesterAvg": 2.6,
        "enrollmentValue": 2736336,
        "stratum": 5,
        "isWorking": True
    },
    {
        "gender": "Male",
        "height": 189,
        "weight": 95,
        "studyHours": 1.3714,
        "age": 21,
        "timeBackingHouse": 110,
        "lastSemesterAvg": 2.1,
        "enrollmentValue": 4502072,
        "stratum": 4,
        "isWorking": True
    },
    {
        "gender": "Male",
        "height": 155,
        "weight": 74,
        "studyHours": 1.5228,
        "age": 23,
        "timeBackingHouse": 113,
        "lastSemesterAvg": 3.6,
        "enrollmentValue": 4790231,
        "stratum": 5,
        "isWorking": False
    },
    {
        "gender": "Female",
        "height": 178,
        "weight": 64,
        "studyHours": 2.6828,
        "age": 23,
        "timeBackingHouse": 63,
        "lastSemesterAvg": 4.2,
        "enrollmentValue": 3240928,
        "stratum": 5,
        "isWorking": True
    },
    {
        "gender": "Male",
        "height": 183,
        "weight": 72,
        "studyHours": 2.0699,
        "age": 21,
        "timeBackingHouse": 10,
        "lastSemesterAvg": 5,
        "enrollmentValue": 3389833,
        "stratum": 5,
        "isWorking": True
    },
    {
        "gender": "Female",
        "height": 161,
        "weight": 75,
        "studyHours": 2.6828,
        "age": 25,
        "timeBackingHouse": 62,
        "lastSemesterAvg": 3.7,
        "enrollmentValue": 2236915,
        "stratum": 5,
        "isWorking": True
    },
    {
        "gender": "Male",
        "height": 173,
        "weight": 83,
        "studyHours": 0.797,
        "age": 24,
        "timeBackingHouse": 42,
        "lastSemesterAvg": 2.2,
        "enrollmentValue": 2343793,
        "stratum": 5,
        "isWorking": True
    },
    {
        "gender": "Female",
        "height": 182,
        "weight": 82,
        "studyHours": 1.0636,
        "age": 21,
        "timeBackingHouse": 26,
        "lastSemesterAvg": 2.9,
        "enrollmentValue": 2426760,
        "stratum": 4,
        "isWorking": True
    },
    {
        "gender": "Female",
        "height": 172,
        "weight": 95,
        "studyHours": 2.0699,
        "age": 25,
        "timeBackingHouse": 47,
        "lastSemesterAvg": 5,
        "enrollmentValue": 3958715,
        "stratum": 2,
        "isWorking": False
    },
    {
        "gender": "Male",
        "height": 176,
        "weight": 84,
        "studyHours": 2.8153,
        "age": 20,
        "timeBackingHouse": 96,
        "lastSemesterAvg": 2.7,
        "enrollmentValue": 3539378,
        "stratum": 2,
        "isWorking": False
    },
    {
        "gender": "Male",
        "height": 174,
        "weight": 63,
        "studyHours": 2.0699,
        "age": 24,
        "timeBackingHouse": 44,
        "lastSemesterAvg": 4.1,
        "enrollmentValue": 4928892,
        "stratum": 2,
        "isWorking": False
    },
    {
        "gender": "Female",
        "height": 163,
        "weight": 69,
        "studyHours": 0.1979,
        "age": 21,
        "timeBackingHouse": 120,
        "lastSemesterAvg": 2.4,
        "enrollmentValue": 4574943,
        "stratum": 3,
        "isWorking": False
    },
    {
        "gender": "Male",
        "height": 189,
        "weight": 78,
        "studyHours": 0.4046,
        "age": 18,
        "timeBackingHouse": 96,
        "lastSemesterAvg": 2.2,
        "enrollmentValue": 4641719,
        "stratum": 4,
        "isWorking": True
    },
    {
        "gender": "Male",
        "height": 188,
        "weight": 63,
        "studyHours": 0.6523,
        "age": 24,
        "timeBackingHouse": 34,
        "lastSemesterAvg": 2.9,
        "enrollmentValue": 4930990,
        "stratum": 5,
        "isWorking": True
    },
    {
        "gender": "Female",
        "height": 187,
        "weight": 73,
        "studyHours": 1.0636,
        "age": 18,
        "timeBackingHouse": 111,
        "lastSemesterAvg": 4.1,
        "enrollmentValue": 3531875,
        "stratum": 5,
        "isWorking": True
    },
    {
        "gender": "Male",
        "height": 175,
        "weight": 79,
        "studyHours": 2.8505,
        "age": 18,
        "timeBackingHouse": 62,
        "lastSemesterAvg": 0.9,
        "enrollmentValue": 3910944,
        "stratum": 4,
        "isWorking": True
    },
    {
        "gender": "Female",
        "height": 152,
        "weight": 70,
        "studyHours":  0.5563,
        "age": 22,
        "timeBackingHouse": 18,
        "lastSemesterAvg": 0.7,
        "enrollmentValue": 2322197,
        "stratum": 5,
        "isWorking": False
    },
    {
        "gender": "Male",
        "height": 155,
        "weight": 61,
        "studyHours": 1.1431,
        "age": 18,
        "timeBackingHouse": 64,
        "lastSemesterAvg": 1.5,
        "enrollmentValue": 2491675,
        "stratum": 3,
        "isWorking": True
    },
    {
        "gender": "Female",
        "height": 152,
        "weight": 75,
        "studyHours": 2.5079,
        "age": 21,
        "timeBackingHouse": 11,
        "lastSemesterAvg": 5,
        "enrollmentValue": 4592355,
        "stratum": 2,
        "isWorking": False
    },
    {
        "gender": "Male",
        "height": 179,
        "weight": 61,
        "studyHours": 2.0699,
        "age": 24,
        "timeBackingHouse": 46,
        "lastSemesterAvg": 1.2,
        "enrollmentValue": 2857477,
        "stratum": 3,
        "isWorking": True
    },
    {
        "gender": "Male",
        "height": 189,
        "weight": 82,
        "studyHours": 2.5079,
        "age": 21,
        "timeBackingHouse": 46,
        "lastSemesterAvg": 2.9,
        "enrollmentValue": 3886406,
        "stratum": 2,
        "isWorking": True
    },
    {
        "gender": "Male",
        "height": 182,
        "weight": 74,
        "studyHours": 2.1555,
        "age": 24,
        "timeBackingHouse": 71,
        "lastSemesterAvg": 5,
        "enrollmentValue": 2502761,
        "stratum": 4,
        "isWorking": True
    },
    {
        "gender": "Male",
        "height": 165,
        "weight": 69,
        "studyHours": 0.4153,
        "age": 23,
        "timeBackingHouse": 109,
        "lastSemesterAvg": 5,
        "enrollmentValue": 2889386,
        "stratum": 5,
        "isWorking": False
    },
    {
        "gender": "Female",
        "height": 164,
        "weight": 69,
        "studyHours": 2.4899,
        "age": 19,
        "timeBackingHouse": 89,
        "lastSemesterAvg": 2.9,
        "enrollmentValue": 2758812,
        "stratum": 5,
        "isWorking": True
    },
    {
        "gender": "Female",
        "height": 160,
        "weight": 90,
        "studyHours": 0.6523,
        "age": 21,
        "timeBackingHouse": 30,
        "lastSemesterAvg": 5,
        "enrollmentValue": 3135303,
        "stratum": 2,
        "isWorking": False
    },
    {
        "gender": "Male",
        "height": 173,
        "weight": 95,
        "studyHours": 2.4899,
        "age": 20,
        "timeBackingHouse": 90,
        "lastSemesterAvg": 1.1,
        "enrollmentValue": 2717393,
        "stratum": 3,
        "isWorking": False
    },
    {
        "gender": "Female",
        "height": 150,
        "weight": 64,
        "studyHours": 1.4741,
        "age": 18,
        "timeBackingHouse": 23,
        "lastSemesterAvg": 3,
        "enrollmentValue": 4910746,
        "stratum": 4,
        "isWorking": True
    },
    {
        "gender": "Male",
        "height": 174,
        "weight": 85,
        "studyHours": 2.2245,
        "age": 20,
        "timeBackingHouse": 64,
        "lastSemesterAvg": 1,
        "enrollmentValue": 3860838,
        "stratum": 2,
        "isWorking": True
    },
    {
        "gender": "Female",
        "height": 190,
        "weight": 90,
        "studyHours": 0.5113,
        "age": 22,
        "timeBackingHouse": 35,
        "lastSemesterAvg": 5,
        "enrollmentValue": 2013253,
        "stratum": 5,
        "isWorking": True
    },
    {
        "gender": "Male",
        "height": 171,
        "weight": 65,
        "studyHours": 0.8181,
        "age": 21,
        "timeBackingHouse": 64,
        "lastSemesterAvg": 3.2,
        "enrollmentValue": 3916597,
        "stratum": 5,
        "isWorking": True
    },
    {
        "gender": "Male",
        "height": 182,
        "weight": 64,
        "studyHours": 1.1826,
        "age": 19,
        "timeBackingHouse": 59,
        "lastSemesterAvg": 1.7,
        "enrollmentValue": 3661401,
        "stratum": 3,
        "isWorking": False
    },
    {
        "gender": "Male",
        "height": 154,
        "weight": 64,
        "studyHours": 2.8153,
        "age": 21,
        "timeBackingHouse": 34,
        "lastSemesterAvg": 0.1,
        "enrollmentValue": 2588667,
        "stratum": 5,
        "isWorking": True
    },
    {
        "gender": "Female",
        "height": 185,
        "weight": 93,
        "studyHours": 1.5192,
        "age": 25,
        "timeBackingHouse": 62,
        "lastSemesterAvg": 3.8,
        "enrollmentValue": 2990454,
        "stratum": 4,
        "isWorking": True
    },
    {
        "gender": "Female",
        "height": 171,
        "weight": 78,
        "studyHours": 1.2663,
        "age": 25,
        "timeBackingHouse": 29,
        "lastSemesterAvg": 3,
        "enrollmentValue": 3529970,
        "stratum": 3,
        "isWorking": False
    }
]"""
