from django.db import models


class Specialization(models.Model):
    ORGANIZATION_SPECIALIZATIONS = [
        ("cardiology_hospital", "Cardiology Hospital"),
        ("orthopedics_hospital", "Orthopedics Hospital"),
        ("neurology_hospital", "Neurology Hospital"),
        ("pediatrics_hospital", "Pediatrics Hospital"),
        ("oncology_hospital", "Oncology Hospital"),
        ("gastroenterology_hospital", "Gastroenterology Hospital"),
        ("dermatology_hospital", "Dermatology Hospital"),
        ("radiology_hospital", "Radiology Hospital"),
        ("obstetrics_and_gynecology_hospital", "Obstetrics and Gynecology Hospital"),
        ("dental_clinic", "Dental Clinic"),
        ("orthopedic_clinic", "Orthopedic Clinic"),
        ("dermatology_clinic", "Dermatology Clinic"),
        ("pediatric_clinic", "Pediatric Clinic"),
        ("womens_health_clinic", "Women's Health Clinic"),
        ("internal_medicine_clinic", "Internal Medicine Clinic"),
        ("urology_clinic", "Urology Clinic"),
        ("psychiatric_clinic", "Psychiatric Clinic"),
        ("ent_clinic", "ENT Clinic"),
        ("cardiology_clinic", "Cardiology Clinic"),
        ("clinical_pathology_lab", "Clinical Pathology Lab"),
        ("microbiology_lab", "Microbiology Lab"),
        ("chemistry_lab", "Chemistry Lab"),
        ("hematology_lab", "Hematology Lab"),
        ("immunology_lab", "Immunology Lab"),
        ("genetics_lab", "Genetics Lab"),
        ("cytology_lab", "Cytology Lab"),
        ("histopathology_lab", "Histopathology Lab"),
        ("virology_lab", "Virology Lab"),
        ("molecular_diagnostics_lab", "Molecular Diagnostics Lab"),
    ]

    specialization_type = models.CharField(
        max_length=200,
        choices=ORGANIZATION_SPECIALIZATIONS,
        blank=False,
        null=False,
        unique=True,
    )

    def __str__(self) -> str:
        return self.specialization_type


class Organization(models.Model):
    ORGANIZATION_TYPES = [
        ("public_hospital", "Public Hospital"),
        ("private_hospital", "Private Hospital"),
        ("clinic", "Clinic"),
        ("lab", "Laboratory"),
    ]

    organization_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    type = models.CharField(
        max_length=100, choices=ORGANIZATION_TYPES, null=False, blank=False
    )
    specializations = models.ManyToManyField(
        "Specialization", related_name="specializations_of_organisation"
    )

    def __str__(self) -> str:
        return f"{self.organization_id}_{self.name}"


class Degree(models.Model):
    CHOICES = [
        ("MD", "Doctor of Medicine"),
        ("DO", "Doctor of Osteopathic Medicine"),
        ("MBBS", "Bachelor of Medicine, Bachelor of Surgery"),
        ("BDS", "Bachelor of Dental Surgery"),
        ("PhD_Medicine", "Doctor of Philosophy in Medicine"),
        ("DPM", "Doctor of Podiatric Medicine"),
        ("DVM", "Doctor of Veterinary Medicine"),
        ("DPT", "Doctor of Physical Therapy"),
        ("OD", "Doctor of Optometry"),
        ("DDS", "Doctor of Dental Surgery"),
        ("DMD", "Doctor of Dental Medicine"),
        ("DCh", "Doctor of Surgery (Chirurgiae)"),
        ("DM", "Doctor of Medicine (Various Specialties)"),
        ("MBChB", "Bachelor of Medicine and Bachelor of Surgery"),
        ("BChD", "Bachelor of Dental Science"),
        ("BMed", "Bachelor of Medicine"),
        ("BSci (Med)", "Bachelor of Science in Medicine"),
        ("BMBS", "Bachelor of Medicine, Bachelor of Surgery"),
        ("BPT", "Bachelor of Physiotherapy"),
        ("BN", "Bachelor of Nursing"),
        ("BSN", "Bachelor of Science in Nursing"),
        ("BNurs", "Bachelor of Nursing Science"),
        ("PharmD", "Doctor of Pharmacy"),
        ("PsyD", "Doctor of Psychology"),
        ("DSc", "Doctor of Science"),
        ("DSW", "Doctor of Social Work"),
        ("JD", "Juris Doctor (Doctor of Law)"),
        ("DVM", "Doctor of Veterinary Medicine"),
        ("PharmD", "Doctor of Pharmacy"),
        ("DEng", "Doctor of Engineering"),
        ("DFA", "Doctor of Fine Arts"),
        ("DMus", "Doctor of Music"),
        ("DA", "Doctor of Arts"),
    ]

    name = models.CharField(
        max_length=255, choices=CHOICES, unique=True, blank=False, null=False
    )

    def __str__(self):
        return self.name


class Doctor(models.Model):
    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    ]

    SPECIALIZATION_CHOICES = [
        ("cardiology", "Cardiology"),
        ("dermatology", "Dermatology"),
        ("endocrinology", "Endocrinology"),
        ("gastroenterology", "Gastroenterology"),
        ("hematology", "Hematology"),
        ("infectious_diseases", "Infectious Diseases"),
        ("neurology", "Neurology"),
        ("oncology", "Oncology"),
        ("orthopedics", "Orthopedics"),
        ("pediatrics", "Pediatrics"),
        ("psychiatry", "Psychiatry"),
        ("pulmonology", "Pulmonology"),
        ("rheumatology", "Rheumatology"),
        ("urology", "Urology"),
        ("ophthalmology", "Ophthalmology"),
        ("otolaryngology", "Otolaryngology"),
        ("gynecology", "Gynecology"),
        ("obstetrics", "Obstetrics"),
        ("emergency_medicine", "Emergency Medicine"),
        ("family_medicine", "Family Medicine"),
        ("internal_medicine", "Internal Medicine"),
        ("anesthesiology", "Anesthesiology"),
        ("radiology", "Radiology"),
        ("pathology", "Pathology"),
        ("physical_therapy", "Physical Therapy"),
        ("sports_medicine", "Sports Medicine"),
        ("allergy_immunology", "Allergy and Immunology"),
        ("vascular_surgery", "Vascular Surgery"),
        ("plastic_surgery", "Plastic Surgery"),
        ("maxillofacial_surgery", "Maxillofacial Surgery"),
        ("nephrology", "Nephrology"),
        ("reproductive_medicine", "Reproductive Medicine"),
        ("critical_care_medicine", "Critical Care Medicine"),
        ("pain_management", "Pain Management"),
        ("sleep_medicine", "Sleep Medicine"),
    ]

    doctor_id = models.CharField(
        max_length=20, primary_key=True, unique=True, blank=False, null=False
    )
    first_name = models.CharField(max_length=100, blank=False, null=False)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to="images/", default="base/male_doctor.png")
    dob = models.DateField(null=False, blank=False)
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES, null=False, blank=False
    )
    address = models.TextField()
    degrees = models.ManyToManyField(Degree, related_name="degrees_of_doctors")
    specialization = models.CharField(
        max_length=200, choices=SPECIALIZATION_CHOICES, null=False, blank=False
    )
    organization_id = models.ForeignKey(
        Organization,
        on_delete=models.DO_NOTHING,
        null=False,
        blank=False,
    )
    phone_number = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
        return f"{self.doctor_id}_{self.first_name}_{self.last_name}"


class Organization_Staff(models.Model):
    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    ]

    staff_id = models.CharField(
        max_length=20, primary_key=True, unique=True, blank=False, null=False
    )
    first_name = models.CharField(max_length=100, blank=False, null=False)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to="images/", default="base/male_patient.png")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    dob = models.DateField(null=False, blank=False)
    address = models.TextField()
    organization_id = models.ForeignKey(
        Organization,
        on_delete=models.DO_NOTHING,
        null=False,
        blank=False,
    )
    phone_number = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
        return f"{self.staff_id}_{self.first_name}_{self.last_name}"


class Patient(models.Model):
    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    ]

    patient_id = models.CharField(
        max_length=20, primary_key=True, unique=True, blank=False, null=False
    )
    first_name = models.CharField(max_length=100, blank=False, null=False)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to="images/", default="base/male_patient.png")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    dob = models.DateField(null=False, blank=False)
    address = models.TextField()
    phone_number = models.CharField(max_length=15, null=False, blank=False)

    def __str__(self):
        return f"{self.patient_id}_{self.first_name}_{self.last_name}"


class Lab_Report(models.Model):
    file = models.FileField(upload_to="lab_reports/")

    def __str__(self):
        return self.file.name


class Patient_History(models.Model):
    patient_id = models.ForeignKey(
        Patient, on_delete=models.DO_NOTHING, null=False, blank=False
    )
    doctor_id = models.ForeignKey(
        Doctor, on_delete=models.DO_NOTHING, null=False, blank=False
    )
    staff_id = models.ForeignKey(
        Organization_Staff, on_delete=models.DO_NOTHING, null=False, blank=False
    )
    organization_id = models.ForeignKey(
        Organization, on_delete=models.DO_NOTHING, null=False, blank=False
    )
    patient_report_pdf = models.FileField(
        upload_to="patient_reports/", blank=False, null=False
    )
    lab_reports = models.ManyToManyField(Lab_Report, blank=True)

    def __str__(self) -> str:
        return self.patient_id
