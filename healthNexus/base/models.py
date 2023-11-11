from django.db import models

# ALL ENTITIES
class Specialization(models.Model):
    ORGANIZATION_SPECIALIZATIONS=[
        ('cardiology_hospital','Cardiology Hospital'),
        ('orthopedics_hospital','Orthopedics Hospital'),
        ('neurology_hospital','Neurology Hospital'),
        ('pediatrics_hospital','Pediatrics Hospital'),
        ('oncology_hospital','Oncology Hospital'),
        ('gastroenterology_hospital','Gastroenterology Hospital'),
        ('dermatology_hospital','Dermatology Hospital'),
        ('radiology_hospital','Radiology Hospital'),
        ('obstetrics_and_gynecology_hospital','Obstetrics and Gynecology Hospital'),

        ('dental_clinic', 'Dental Clinic'),
        ('orthopedic_clinic', 'Orthopedic Clinic'),
        ('dermatology_clinic', 'Dermatology Clinic'),
        ('pediatric_clinic', 'Pediatric Clinic'),
        ('womens_health_clinic', "Women's Health Clinic"),
        ('internal_medicine_clinic', 'Internal Medicine Clinic'),
        ('urology_clinic', 'Urology Clinic'),
        ('psychiatric_clinic', 'Psychiatric Clinic'),
        ('ent_clinic', 'ENT Clinic'),
        ('cardiology_clinic', 'Cardiology Clinic'),

        ('clinical_pathology_lab', 'Clinical Pathology'),
        ('microbiology_lab', 'Microbiology'),
        ('chemistry_lab', 'Chemistry'),
        ('hematology_lab', 'Hematology'),
        ('immunology_lab', 'Immunology'),
        ('genetics_lab', 'Genetics'),
        ('cytology_lab', 'Cytology'),
        ('histopathology_lab', 'Histopathology'),
        ('virology_lab', 'Virology'),
        ('molecular_diagnostics_lab', 'Molecular Diagnostics')
    ]

    specialization_type = models.CharField(max_length=200, choices=ORGANIZATION_SPECIALIZATIONS,blank=False,null=False,unique=True)

    def __str__(self) -> str:
        return self.specialization_type

class Organization(models.Model):
    ORGANIZATION_TYPES=[
        ('public_hospital','Public Hospital'),
        ('private_hospital','Private Hospital'),
        ('clinic','Clinic'),
        ('lab','Laboratory')
    ]

    organization_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=False,blank=False)
    type = models.CharField(max_length=100, choices=ORGANIZATION_TYPES,null=False,blank=False)
    specializations = models.ManyToManyField('Specialization', related_name='specializations_of_organisation')

    def __str__(self) -> str:
        return f"{self.organization_id}_{self.name}"

class Degree(models.Model):
    CHOICES = [
        ('MD', 'Doctor of Medicine'),
        ('DO', 'Doctor of Osteopathic Medicine'),
        ('MBBS', 'Bachelor of Medicine, Bachelor of Surgery'),
        ('BDS', 'Bachelor of Dental Surgery'),
        ('PhD_Medicine', 'Doctor of Philosophy in Medicine'),
        ('DPM', 'Doctor of Podiatric Medicine'),
        ('DVM', 'Doctor of Veterinary Medicine'),
        ('DPT', 'Doctor of Physical Therapy'),
        ('OD', 'Doctor of Optometry'),
        ('DDS', 'Doctor of Dental Surgery'),
        ('DMD', 'Doctor of Dental Medicine'),
        ('DCh', 'Doctor of Surgery (Chirurgiae)'),
        ('DM', 'Doctor of Medicine (Various Specialties)'),
        ('MBChB', 'Bachelor of Medicine and Bachelor of Surgery'),
        ('BChD', 'Bachelor of Dental Science'),
        ('BMed', 'Bachelor of Medicine'),
        ('BSci (Med)', 'Bachelor of Science in Medicine'),
        ('BMBS', 'Bachelor of Medicine, Bachelor of Surgery'),
        ('BPT', 'Bachelor of Physiotherapy'),
        ('BN', 'Bachelor of Nursing'),
        ('BSN', 'Bachelor of Science in Nursing'),
        ('BNurs', 'Bachelor of Nursing Science'),
        ('PharmD', 'Doctor of Pharmacy'),
        ('PsyD', 'Doctor of Psychology'),
        ('DSc', 'Doctor of Science'),
        ('DSW', 'Doctor of Social Work'),
        ('JD', 'Juris Doctor (Doctor of Law)'),
        ('DVM', 'Doctor of Veterinary Medicine'),
        ('PharmD', 'Doctor of Pharmacy'),
        ('DEng', 'Doctor of Engineering'),
        ('DFA', 'Doctor of Fine Arts'),
        ('DMus', 'Doctor of Music'),
        ('DA', 'Doctor of Arts'),
    ]

    name = models.CharField(max_length=255, choices=CHOICES, unique=True,blank=False,null=False)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    SPECIALIZATION_CHOICES = [
        ('cardiology', 'Cardiology'),
        ('dermatology', 'Dermatology'),
        ('endocrinology', 'Endocrinology'),
        ('gastroenterology', 'Gastroenterology'),
        ('hematology', 'Hematology'),
        ('infectious_diseases', 'Infectious Diseases'),
        ('neurology', 'Neurology'),
        ('oncology', 'Oncology'),
        ('orthopedics', 'Orthopedics'),
        ('pediatrics', 'Pediatrics'),
        ('psychiatry', 'Psychiatry'),
        ('pulmonology', 'Pulmonology'),
        ('rheumatology', 'Rheumatology'),
        ('urology', 'Urology'),
        ('ophthalmology', 'Ophthalmology'),
        ('otolaryngology', 'Otolaryngology'),
        ('gynecology', 'Gynecology'),
        ('obstetrics', 'Obstetrics'),
        ('emergency_medicine', 'Emergency Medicine'),
        ('family_medicine', 'Family Medicine'),
        ('internal_medicine', 'Internal Medicine'),
        ('anesthesiology', 'Anesthesiology'),
        ('radiology', 'Radiology'),
        ('pathology', 'Pathology'),
        ('physical_therapy', 'Physical Therapy'),
        ('sports_medicine', 'Sports Medicine'),
        ('allergy_immunology', 'Allergy and Immunology'),
        ('vascular_surgery', 'Vascular Surgery'),
        ('plastic_surgery', 'Plastic Surgery'),
        ('maxillofacial_surgery', 'Maxillofacial Surgery'),
        ('nephrology', 'Nephrology'),
        ('reproductive_medicine', 'Reproductive Medicine'),
        ('critical_care_medicine', 'Critical Care Medicine'),
        ('pain_management', 'Pain Management'),
        ('sleep_medicine', 'Sleep Medicine'),
    ]

    doctor_id = models.CharField(max_length=20, primary_key=True, unique=True,blank=False,null=False)
    first_name = models.CharField(max_length=100,blank=False,null=False)
    middle_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=False,null=False)
    dob = models.DateField(null=False,blank=False)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES,null=False,blank=False)
    address = models.TextField()
    degrees = models.ManyToManyField(Degree, related_name='degrees_of_doctors')
    specialization = models.CharField(max_length=200,choices=SPECIALIZATION_CHOICES,null=False,blank=False)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True, blank=True, related_name='doctors')
    phone_number = models.CharField(max_length=15,null=False,blank=False)

    def __str__(self):
        return f"{self.doctor_id}_{self.first_name}_{self.last_name}"

class Patient(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    patient_id = models.CharField(max_length=30, unique=True,null=False,blank=False)
    first_name = models.CharField(max_length=100,blank=False,null=False)
    middle_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=False,null=False)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    dob = models.DateField(null=False,blank=False)
    address = models.TextField()
    symptoms = models.TextField()
    doctors = models.ManyToManyField(Doctor,related_name='doctors_of_patients')
    organizations = models.ManyToManyField(Organization, related_name='organizations_of_patient')
    phone_number = models.CharField(max_length=15,null=False,blank=False)

    def __str__(self):
        return f"{self.patient_id}_{self.first_name}_{self.last_name}"
    