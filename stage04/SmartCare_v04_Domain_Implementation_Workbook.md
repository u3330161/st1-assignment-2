## 1. UML-to-code Trace
| UML element | Python element | Implemented? | Notes                     |
| --- | --- | --- |---------------------------|
| Patient class | class patient | yes | Has patient ID, name, DOB |
| Practitioner class | class practitioner | yes | Has practitioner id |
| Appointment class | class appointment | yes | Has appointmentid, datetime, status |
| MedicalRecord class | class MedicalRecord | yes | Has recordid,diagnosis |
| Prescription class | class prescription | yes | Has prescriptionid, medication |
|Patient 1 -- 0..* Appointment |appointments list in Patient|Yes|One patient has many appointments|
|Practitioner 1 -- 0..* Appointment|appointments list in Practitioner|Yes|One doctor has many appointments|
|Appointment 1 -- 0..1 MedicalRecord|medicalRecord object in Appointment|Yes|One appointment has one record|
|MedicalRecord 1 -- 0..* Prescription|prescriptions list in MedicalRecord|Yes|One record has many prescriptions|
|Patient - register()|def register(self)|Yes|Register method|
|Appointment - checkAvailability()|def checkAvailability(self)|Yes|Check free time|

## 2. Domain Invariants 
| Class | Invariant / rule | How protected |
| --- | --- | --- |
| Patient | patientID cannot be empty | Check in init, if empty give error |
| Appointment | date Time must be future | Check data in checkAvailability()|
|Appointment | status must be booked,confirmed, or canceled only | Allow only 3values |
| MedicalRecord | diagnosis cannot be empty  | Check in init |

## 3. Composition / Inheritance Decisions
| Relationship | Decision | Rationale |
| --- | --- | --- |
| Patient--Appointment| Composition with list | Patient has many appointments, list is simple|
| Practitioner--Appointment| Composition with list | Doctor manages many appointments, list is best |
| Appointment--MedicalRecord | Composition single object | One appointment has one record, use None if empty|
| MedicalRecord--Prescription | Composition with list | One record has many prescriptions |

## 4. AI Pair-Programming Record
| AI Contribution | Conforms? | Decision | Reason |Verification|
|---|---|---|---|---|
|Suggested patient and practitioner class| yes| Accepted|matches UML|Checked with diagram|
|Suggested list for 1 to many relation| yes| Accepted|Simple and correct|Tested manually|
|Suggested cancel() and finalize() methods| yes|Accepted| In UML| Code runs ok|

## 5. Updated UML
No change needed because v0.3 design is correct. Code works with same 5 classes. No new design needed.
