import csv
import numpy as np

file_name = "nationwidechildrens.org_clinical_follow_up_v4.0_brca.txt"


form_completion_date = 4
followup_lost_to = 5
radiation_treatment_adjuvant = 6
pharmaceutical_tx_adjuvant = 7
tumor_status = 8
person_neoplasm_cancer_status = 8
vital_status = 9
last_contact_days_to = 10
days_to_last_followup = 10
death_days_to = 11
days_to_death = 11
new_tumor_event_dx_indicator = 12



with open(file_name) as f:
    reader = csv.reader(f, delimiter = "\t")
    master_list = list(reader)
    master_array = np.asarray(master_list)
number_of_cases = len(master_list) - 3


print "Total Number of patients in this clinical data set = ",number_of_cases

number_of_alive_patients = np.where(master_array[2:718,vital_status] == 'Alive')
print "Number of Alive patients = ", len(number_of_alive_patients[0])

number_of_radiation_treatment_patients = np.where(master_array[2:718,radiation_treatment_adjuvant] == 'YES')
print "Number of patients with radiation treatment", len(number_of_radiation_treatment_patients[0])


number_of_pharmaceutical_patients = np.where(master_array[2:718,pharmaceutical_tx_adjuvant] == 'YES')
print "Number of patients with Pharmacuitical Treatment = ", len(number_of_pharmaceutical_patients[0])


number_of_patients_with_tumor = np.where(master_array[2:718,tumor_status] == 'WITH TUMOR')
print "Number of patients with Tumor = ", len(number_of_patients_with_tumor[0])

number_of_patients_with_no_tumor_event =np.where(master_array[2:718,new_tumor_event_dx_indicator] == 'NO')
print "Number of patients with no new Tumor after initial treatment = ", len(number_of_patients_with_no_tumor_event[0])


number_of_Patients_no_returning_turmor = np.where((master_array[2:718,tumor_status] == 'WITH TUMOR')&(master_array[2:718,new_tumor_event_dx_indicator] == 'NO'))
print "Number of patients with tumor who had no new Tumor = ", len(number_of_Patients_no_returning_turmor[0])

number_of_patients_with_no_tumor_pharma = np.where((master_array[2:718,new_tumor_event_dx_indicator] == 'NO')&(master_array[2:718,pharmaceutical_tx_adjuvant] == 'YES'))
print "Number of patients with no new tumor who were treated pharmacuitical = ", len(number_of_patients_with_no_tumor_pharma[0])

number_of_patients_with_no_tumor_rad = np.where((master_array[2:718,new_tumor_event_dx_indicator] == 'NO')&(master_array[2:718,radiation_treatment_adjuvant] == 'YES'))

print "Number of patients with no new tumor who were treated radiation = ", len(number_of_patients_with_no_tumor_rad[0])

number_of_patients_with_no_tumor_pharma_and_rad =np.where((master_array[2:718,new_tumor_event_dx_indicator] == 'NO')&(master_array[2:718,radiation_treatment_adjuvant] == 'YES')&(master_array[2:718,pharmaceutical_tx_adjuvant] == 'YES'))
print "Number of patients with no new tumor who were treated both pharmacuitical and radiation = ", len(number_of_patients_with_no_tumor_pharma_and_rad[0])

number_of_patients_with_no_tumor_alive = np.where((master_array[2:718,new_tumor_event_dx_indicator] == 'NO')&(master_array[2:718,vital_status] == 'Alive'))

print "Number of patients with no new tumor who are alive = ", len(number_of_patients_with_no_tumor_alive[0])


print "Percentage of Alive patients after no Tumor event = ", (float(len(number_of_patients_with_no_tumor_alive[0]))/(float(len(number_of_patients_with_no_tumor_event[0]))))*100.0, "%"

print "Percentage of Alive patients with no new tumor = ", (float(len(number_of_patients_with_no_tumor_alive[0]))/(number_of_cases))*100.0, "%"


