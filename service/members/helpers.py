import tablib

members = [
  {
    "about": " ",
    "age": 29,
    "avatar": "https://avatars.githubusercontent.com/",
    "birth": [
      "1987-03-23",
      "00:00:00"
    ],
    "confirmed": True,
    "course": {
      "id": 9,
      "name": "Engenharia de computação"
    },
    "education": {
      "id": 1,
      "name": "Ensino Superior completo"
    },
    "email": " lffsantos@gmail.com",
    "experience_time": {
      "id": 3,
      "name": "1 - 2 years"
    },
    "full_name": " Lucas Farias Ferreira Santos",
    "gender": {
      "id": 1,
      "name": "Male"
    },
    "github": " https://github.com/lffsantos/",
    "id": 1,
    "is_working": False,
    "linkedin": " https://www.linkedin.com/in/lucasfariassantos",
    "occupation_area": {
      "id": 4,
      "name": "Back-end Developer"
    },
    "phone": "",
    "short_name": " Lucas Farias",
    "technologies": [
      {
        "id": 1,
        "name": "Java"
      },
      {
        "id": 2,
        "name": "Python"
      },
      {
        "id": 3,
        "name": "C"
      },
      {
        "id": 4,
        "name": "C++"
      },
      {
        "id": 5,
        "name": ".NET"
      },
      {
        "id": 6,
        "name": "C#"
      },
      {
        "id": 7,
        "name": "ASP"
      },
      {
        "id": 8,
        "name": "PHP"
      },
      {
        "id": 9,
        "name": "COBOL"
      }
    ],
    "update_at": [
      "2016-10-21",
      "13:49:37"
    ],
    "visa": {
      "description": " Visto de estudante com permissão de trabalho",
      "id": 4,
      "name": "Stamp 2"
    }
  },
  {
    "about": " ",
    "age": 29,
    "avatar": "https://avatars.githubusercontent.com/",
    "birth": [
      "1987-03-23",
      "00:00:00"
    ],
    "confirmed": True,
    "course": {
      "id": 9,
      "name": "Engenharia de computação"
    },
    "education": {
      "id": 1,
      "name": "Ensino Superior completo"
    },
    "email": " lffsantos@gmail.com",
    "experience_time": {
      "id": 3,
      "name": "1 - 2 years"
    },
    "full_name": " Lucas Farias Ferreira Santos",
    "gender": {
      "id": 1,
      "name": "Male"
    },
    "github": " https://github.com/lffsantos/",
    "id": 1,
    "is_working": False,
    "linkedin": " https://www.linkedin.com/in/lucasfariassantos",
    "occupation_area": {
      "id": 4,
      "name": "Back-end Developer"
    },
    "phone": "",
    "short_name": " Lucas Farias",
    "technologies": [
      {
        "id": 1,
        "name": "Java"
      },
      {
        "id": 2,
        "name": "Python"
      },
      {
        "id": 3,
        "name": "C"
      },
      {
        "id": 4,
        "name": "C++"
      },
      {
        "id": 5,
        "name": ".NET"
      },
      {
        "id": 6,
        "name": "C#"
      },
      {
        "id": 7,
        "name": "ASP"
      },
      {
        "id": 8,
        "name": "PHP"
      },
      {
        "id": 9,
        "name": "COBOL"
      }
    ],
    "update_at": [
      "2016-10-21",
      "13:49:37"
    ],
    "visa": {
      "description": " Visto de estudante com permissão de trabalho",
      "id": 4,
      "name": "Stamp 2"
    }
  },
  {
    "about": " ",
    "age": 29,
    "avatar": "https://avatars.githubusercontent.com/",
    "birth": [
      "1987-03-23",
      "00:00:00"
    ],
    "confirmed": True,
    "course": {
      "id": 9,
      "name": "Engenharia de computação"
    },
    "education": {
      "id": 1,
      "name": "Ensino Superior completo"
    },
    "email": " lffsantos@gmail.com",
    "experience_time": {
      "id": 3,
      "name": "1 - 2 years"
    },
    "full_name": " Lucas Farias Ferreira Santos",
    "gender": {
      "id": 1,
      "name": "Male"
    },
    "github": " https://github.com/lffsantos/",
    "id": 1,
    "is_working": False,
    "linkedin": " https://www.linkedin.com/in/lucasfariassantos",
    "occupation_area": {
      "id": 4,
      "name": "Back-end Developer"
    },
    "phone": "",
    "short_name": " Lucas Farias",
    "technologies": [
      {
        "id": 1,
        "name": "Java"
      },
      {
        "id": 2,
        "name": "Python"
      },
      {
        "id": 3,
        "name": "C"
      },
      {
        "id": 4,
        "name": "C++"
      },
      {
        "id": 5,
        "name": ".NET"
      },
      {
        "id": 6,
        "name": "C#"
      },
      {
        "id": 7,
        "name": "ASP"
      },
      {
        "id": 8,
        "name": "PHP"
      },
      {
        "id": 9,
        "name": "COBOL"
      }
    ],
    "update_at": [
      "2016-10-21",
      "13:49:37"
    ],
    "visa": {
      "description": " Visto de estudante com permissão de trabalho",
      "id": 4,
      "name": "Stamp 2"
    }
  }
]


def get_fields_and_label():
    fields = ['full_name', 'age', 'visa', 'occupation_area', 'experience_time', 'gender',
              'is_working', 'education', 'course', 'email', 'technologies', 'phone',
              'about', 'linkedin', 'github']
    label = (
        'Name', 'Age', 'Visa', 'Occupation', 'Experience', 'Gender', 'Is Working',
        'Education', 'Course', 'Email', 'Technologies', 'Phone', 'About', 'Linkedin',
        'Github',
    )
    return fields, label


def format_member_to_export(member, fields):
    data = ()
    for f in ["course", "education", "experience_time", "occupation_area", "gender",
              "visa", "technologies"]:
        if member.get(f):
            if isinstance(member[f], list):
                technologies = []
                for tech in member[f]:
                    technologies.append(tech['name'])
                member[f] = ", ".join(technologies)
            else:
                member[f] = member[f]['name']

    for field in fields:
        data = data + (member.get(field), )

    return data


def export_members(members, export_to='xls'):
    data = []
    fields, headers = get_fields_and_label()
    for member in members:
        data.append(format_member_to_export(member, fields))

    data = tablib.Dataset(*data, headers=headers)
    open('people.xls', 'wb').write(data.xls)
    return data


# def export_to_csv(data):
#     format_data_to_export(data)
#     data = tablib.Dataset(*data, headers=headers)
#     return data


if __name__ == '__main__':
    export_members(members)
    # import xlwt
    # from datetime import datetime
    #
    # style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
    #     num_format_str='#,##0.00')
    # style1 = xlwt.easyxf(num_format_str='D-MMM-YY')
    #
    # wb = xlwt.Workbook()
    # ws = wb.add_sheet('A Test Sheet')
    #
    # ws.write(0, 0, 1234.56, style0)
    # ws.write(1, 0, datetime.now(), style1)
    # ws.write(2, 0, 1)
    # ws.write(2, 1, 1)
    # ws.write(2, 2, xlwt.Formula("A3+B3"))
    #
    # wb.save('example.xls')
    # pass