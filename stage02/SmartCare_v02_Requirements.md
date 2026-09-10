# SmartCare v0.2_ Requirements 
## 1. Problem and Scope
Current SmartCare clinic use paper and excel. Duplicate booking same doctor same time, difficult to find patient info, appointment status incorrect, no history of canceled appointments. Management want small system that is maintainable, easy to use, for patient, doctor and appointment only.

In Scope: patient add/search, doctor add/search, booking appointments, canceling appointments, viewing appointments by date/doctor, keeping canceled history.                          
Out of Scope: SMS reminders, online payment, facial recognition login, AI treatment suggestion, mobile app.
Small system is for a small clinic only.

## 2. Stakeholders
| Stakeholder | Need | Evidence |                  
| Patient | no double booking | client brief says duplicate bookings problem |                            
| Receptionist | Need to create, cancel, search quickly | Primary users of system, every day tasks |                    
| Practitioner / Doctor | Need to see my daily appointments | Need schedule to see patients |                                    
| Clinic Manager | need to keep history and reports | Management doesn't want any duplicate |               
| IT Admin | Need system secure and easy to fix | Brief says maintainable system |

## 3. Functional Requirements
FR-01: Add new patient with ID, name, phone.                             
FR-02: System should search for patient using ID.                  
FR-03: System should locate a patient by name (partial).                
FR-04: System should add new doctor with ID and name.                 
FR-05: System should create appointment with patient ID, doctor ID, date time.                 
FR-06: No double bookings for doctor same time.   
FR-07: System should cancel appointment with reason.       
FR-08: System should maintain canceled appointments in canceled status.    
FR-09: The system should display appointments by date.      
FR-10: System should show appointments by doctor.             
FR-11: System should display status - booked, canceled, completed.        
FR-12: System should not accept appointment if patient ID or doctor ID invalid.

## 4. Non-Functional Requirements
NFR-01: Search 10,000 patients in 2 seconds.                 
NFR-02: No data loss, save to file after every change.               
NFR-03: main logic (booking check) is separate from UI, can be tested independently.              
NFR-04: New receptionist can make appointment in 2 minutes with small training.             
NFR-05: System requires to work without slow on small clinic data.           
NFR-06: Patient data can only be accessed by staff with logins.

## 5. User Stories
US-01: As a receptionist, I want to create appointment, so that patient can meet doctor.               
US-02: As a receptionist, I want to search patient by ID, so that I can book fast.            
US-03: As a receptionist, I want to cancel appointment, so that slot become free.            
US-04: As a doctor, I want to see my today appointments, so that I know my work.         
US-05: As a manager, I want to see canceled history, so that I know what happened.          
US-06: As a receptionist, I want to see appointments by date, so that I can plan.      

## 6. Acceptance Criteria
US-01:          
GIVEN patient P001 and doctor D01 exist.             
When I make appointment for P001 with D01 on 2026-09-10 10:00.          
Then system marks appointment as booked.

US-01 Failure:     
GIVEN doctor D01 already booked on 2026-09-10 10:00.        
When I attempt to book same doctor, same time again.        
The error shown is double booking not allowed.

US-02:             
GIVEN there is a patient named P001.          
When I search for the ID, "P001"
Then system shows patient details.         
And when I search "P999" not exist then show "not found".    

US-03:  
GIVEN appointment A001 is booked.             
When I cancel A001 with reason "patient sick".    
Then status is canceled and remains in the history. 

## 7. Assumptions and Open Questions
Assumption: Clinic has less than 10,000 patients.              
Assumption: Only one receptionist at a time uses system.

Open Q1: How long do we keep with canceled history? Forever or 1 year?                        
Open Q2: Who may cancel? Only receptionist or doctor?              
Open Q3: Need separate login for roles or one login is ok?            
Open Q4: How many hours are spent on appointments?        

## 8. AI Requirements Review Record
| AI suggestion | Evidence? | Decision | Reason | Verification |                   
| Facial recognition login | No evidence | Rejected | Out of scope,small clinic,no need,privacy risk | No evidence in brief |                 
| Online payment | No evidence | Rejected | Brief says only patient/doctor/appointment system | Client never said payment |                                              
| Keep canceled appointments history | Yes evidence | Accepted | Client said limited appointment history is problem | Confirmed from brief |        
| Data should be secure with login | Question need validation | Accepted with change | Patient data sensitive, but need to ask what security | Check with manager |



