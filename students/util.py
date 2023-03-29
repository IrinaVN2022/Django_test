

def format_list_student(students):
    # string = '<br>'.join(str(student) for student in students)
    string = '<table>' \
             '<thead>' \
             '<tr>' \
             '<th>First name</th>' \
             '<th>Last name</th> ' \
             '<th>Email</th>' \
             '<th>Birthday</th>' \
             '<th>City</th>' \
             '<th>Update</th>' \
             '<th>Phone</th>' \
             '</tr>' \
             '<thead>' \
             '<tbody>'
    for student in students:
        string += f'<tr>' \
                  f'<td>{student.first_name}</td>' \
                  f'<td>{student.last_name}</td>' \
                  f'<td>{student.email}</td>' \
                  f'<td>{student.birthday}</td>' \
                  f'<td>{student.city if student.city else ""}</td>' \
                  f'<td><a href="/students/update/{student.pk}/">Edit</a></td>' \
                  f'<td>{student.phone}</td>'\
                  f'</tr>'
    string += '</tbody></table>'
    return string