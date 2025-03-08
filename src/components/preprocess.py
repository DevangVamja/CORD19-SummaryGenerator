import pandas as pd
from src.utils import processed_df, inverted_index

class Preprocessor:
    def __init__(self):
        self.data_path = 'covid19_Processed.csv' # Path to the dataset
        self.covid_dict = {
                    "COVID-19": ["Coronavirus disease 2019", "SARS-CoV-2", "Novel coronavirus"],
                    "Vaccine": ["COVID vaccine", "Coronavirus vaccine", "SARS-CoV-2 vaccine"],
                    "Face mask": ["Mask", "Surgical mask", "N95 respirator"],
                    "Social distancing": ["Physical distancing", "Social isolation", "Quarantine"],
                    "Hand hygiene": ["Hand washing", "Hand sanitizing", "Hand disinfection"],
                    "Pandemic": ["Global health crisis", "Outbreak", "Epidemic"],
                    "PCR test": ["Polymerase chain reaction test", "COVID-19 test", "Nasal swab test"],
                    "Antibody": ["Immunoglobulin", "Serology test", "Immunity"],
                    "Contact tracing": ["Contact investigation", "Contact monitoring", "Exposure notification"],
                    "Ventilator": ["Mechanical ventilator", "Breathing machine", "Respirator"],
                    "PPE": ["Personal protective equipment", "Protective gear", "Hazmat suit"],
                    "Herd immunity": ["Community immunity", "Population immunity", "Herd protection"],
                    "Lockdown": ["Stay-at-home order", "Quarantine", "Shelter-in-place"],
                    "Asymptomatic": ["Silent carrier", "Without symptoms", "Asymptomatic carrier"],
                    "Isolation": ["Self-quarantine", "Self-isolation", "Medical isolation"],
                    "Mortality rate": ["Death rate", "Fatality rate", "Case fatality rate"],
                    "Incubation period": ["Latency period", "Asymptomatic period", "Symptom-free period"],
                    "Close contact": ["Proximate contact", "Direct contact", "Physical contact"],
                    "Immune response": ["Immunological response", "Antibody response", "Immune system response"],
                    "Essential worker": ["Frontline worker", "Critical worker", "Key worker"],
                    "Superspreader": ["Super-spreading event", "Outbreak amplifier", "Infectious agent"],
                    "Variant": ["COVID variant", "Coronavirus variant", "SARS-CoV-2 variant"],
                    "Booster": ["COVID booster", "Vaccine booster", "Additional dose"],
                    "Long COVID": ["Long-haul COVID", "Post-acute COVID", "Chronic COVID"],
                    "Hybrid work": ["Flexible work", "Remote work", "Virtual work"],
                    "Hazard pay": ["Hero pay", "Essential pay", "Pandemic pay"],
                    "Cytokine storm": ["Cytokine release syndrome", "Systemic inflammatory response", "Hyperinflammation"],
                    "Breakthrough infection": ["Vaccine breakthrough", "Post-vaccination infection", "Vaccine failure"],
                    "Airborne transmission": ["Aerosol transmission", "Droplet transmission", "Respiratory transmission"],
                    "Mental health": ["Psychological well-being", "Emotional health", "Mental wellness"],
                    "Third wave": ["COVID surge", "Outbreak resurgence", "Pandemic rebound"],
                    "Antiviral drug": ["COVID treatment", "Coronavirus medication", "SARS-CoV-2 therapy"],
                    "Digital health pass": ["COVID passport", "Vaccine passport", "Health certificate"]
                }
    
    def load_data(self):
        self.data = pd.read_csv(self.data_path)
        self.data = pd.DataFrame(self.data, columns=['abstract','body_text','title'])

    def preprocess_data(self):
        self.data['processed_title'] = self.data['title'].apply(lambda x: processed_df(x))
        self.document_list = self.data['processed_title'].tolist()
        self.inverted_index = inverted_index(self.document_list)
        return self.document_list,self.inverted_index

