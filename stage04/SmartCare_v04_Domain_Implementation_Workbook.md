## 1. UML-to-code Trace
| UML element | Python element                      | Implemented? | Notes                     |
| --- |-------------------------------------| --- |---------------------------|
| Patient class | Patient class                       | yes | Has patient ID, name, DOB |
| Practitioner class | Practitioner class                  | yes | Has practitioner id |
| Appointment class | Appointment class                   | yes | Has appointmentid, datetime, status |
| Patient-Appointment link|patient_id in Appointment|yes| 1 to many|
|Practitioner-Appointment link|doctor_id in Appointment|yes|1 to many|

## 2. Domain Invariants 

| Class        | Invariant / rule                | How protected                      |
|--------------|---------------------------------|------------------------------------|
| Patient      | patientID cannot be empty       | Check in init, if empty give error |
| Practitioner | Practitioner ID cannot be empty | Check in init, if empty give error |
| Appointment  | date Time cannot be empty       | Check in init, if empty give error |
| Appointment  | cannot cancel twice             | Check in cancel()                  |

## 3. Composition / Inheritance Decisions
| Relationship | Decision | Rationale |
| --- | --- | --- |
| Patient-Appointment| Association only|If patient is deleted,appointment history should stay|
| Practitioner-Appointment| Association only|If doctor is deleted, appointment history should stay|
|Patient-Practitioner| No direct link|They connect only through Appointment|
|Inheritance used| No|All three classes are different, no parent-child|

## 4. AI Pair-Programming Record
| AI Contribution | Conforms? | Decision | Reason |Verification|
|---|---|---|---|---|
|Appointment class with status string| Yes|Accepted|Same as stage3 UML|Created object and tested cancel()|
|Appointment class with enum|No|Rejected|Stage 3 UML has no enum,only string|By checking stage 3UML- no enum present|
|Database code to save Appointment|No|Rejected|Design is domain only,no database logic|no database allowed|
|Email/Notification code| No|Rejected|only domain layer|UML has only 3 classes|

## 5. Updated UML
No change needed because v0.3 design is correct. Code works with same 3 classes. No new design needed.

## Reflection
AI added database save and notification logic in Appointment class. I rejected it because approved UML has only 3 classes with no database. Approved design constrained AI to only implement cancel() eith 3 classes.
