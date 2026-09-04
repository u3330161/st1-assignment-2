print("Welcome to SmartCare:Community Clinic Appointment Booking System!")
appointments = []
def book_appointment(patient_name,practitioner_name,appointment_time):
    if not patient_name:
        raise ValueError("patient name cannot be empty")
    if not practitioner_name:
        raise ValueError("practitioner_name cannot be empty")
    if not appointment_time:
        raise ValueError("appointment_time cannot be empty")
    if "2024" not in appointment_time:
        raise ValueError("appointment year must be 2024")
    appointment = {
       "patient": patient_name,
       "practitioner": practitioner_name,
       "time": appointment_time
    }
    appointments.append(appointment)
def display_appointments():
    if not appointments:
     print("No appointments recorded.")
     return
    for appointment in appointments:
     print(f"patient: {appointment['patient']}| practitioner: {appointment['practitioner']}| time: {appointment['time']}")
book_appointment('Alice Smith','Dr.John Doe ','2024-07-20 10:00AM')
book_appointment('Bob Johnson', 'Dr.John Doe',  '2024-07-20 11:30 AM')
display_appointments()



