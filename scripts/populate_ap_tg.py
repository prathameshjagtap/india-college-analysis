import json, os

def load_db():
    if os.path.exists('data/private_colleges_ownership.json'):
        with open('data/private_colleges_ownership.json', 'r') as f:
            own = json.load(f)
    else:
        own = []
    if os.path.exists('data/private_college_sources.json'):
        with open('data/private_college_sources.json', 'r') as f:
            src = json.load(f)
    else:
        src = []
    return own, src

def save_db(own, src):
    # Ensure unique by SlNo
    own_dict = {str(x['SlNo']): x for x in own}
    src_dict = {str(x['SlNo']): x for x in src}
    
    sorted_own = sorted(own_dict.values(), key=lambda x: int(x['SlNo']))
    sorted_src = sorted(src_dict.values(), key=lambda x: int(x['SlNo']))
    
    with open('data/private_colleges_ownership.json', 'w') as f:
        json.dump(sorted_own, f, indent=2)
    with open('data/private_college_sources.json', 'w') as f:
        json.dump(sorted_src, f, indent=2)
    print(f"Saved {len(sorted_own)} records to private_colleges_ownership.json and private_college_sources.json")

own, src = load_db()

ap_tg_records = [
  # --- ANDHRA PRADESH ---
  {
    "SlNo": "6",
    "CollegeName": "Alluri Sitharam Raju Academy of Medical Sciences Eluru",
    "State": "Andhra Pradesh",
    "District": "Eluru",
    "University": "Dr. YSR University of Health Sciences",
    "Management": "Trust",
    "ParentOrganization": "Alluri Sitarama Raju Educational Society",
    "KeyPeople": [
      {"Name": "Dr. Gokaraju Ganga Raju", "Role": "Founder & Chairman", "Details": "Industrialist (Laila Group) and former Member of Parliament"}
    ],
    "PoliticalAffiliation": "Dr. Gokaraju Ganga Raju served as Member of Parliament (BJP, Narsapuram constituency, 2014-2019).",
    "FundingSource": "Student tuition fees, super-specialty hospital operational revenues, promoter capital from Laila Group.",
    "SummaryReport": "Established in 1999 by Alluri Sitarama Raju Educational Society under the leadership of industrialist and former BJP MP Dr. Gokaraju Ganga Raju. Funded via self-financing medical college fee structure and hospital operations."
  },
  {
    "SlNo": "8",
    "CollegeName": "Apollo Institute of Medical Sciences and Research Chittoor",
    "State": "Andhra Pradesh",
    "District": "Chittoor",
    "University": "Dr. YSR University of Health Sciences",
    "Management": "Society",
    "ParentOrganization": "Apollo Hospitals Educational Trust / Apollo Hospitals Group",
    "KeyPeople": [
      {"Name": "Dr. Prathap C. Reddy", "Role": "Founder & Chairman", "Details": "Founder-Chairman of Apollo Hospitals Group"},
      {"Name": "Ms. Preetha Reddy", "Role": "Executive Vice Chairperson", "Details": "Apollo Hospitals Enterprise Ltd"}
    ],
    "PoliticalAffiliation": "None identified / Corporate healthcare conglomerate (Apollo Hospitals Group).",
    "FundingSource": "Apollo Hospitals Enterprise Ltd corporate backing, clinical hospital earnings, student tuition fees.",
    "SummaryReport": "Founded by Apollo Hospitals Group chairman Dr. Prathap C. Reddy under Apollo Hospitals Educational Trust. Funded primarily through Apollo corporate healthcare group resources and student fees."
  },
  {
    "SlNo": "9",
    "CollegeName": "Dr. P.S.I. Medical College Chinoutpalli",
    "State": "Andhra Pradesh",
    "District": "Krishna",
    "University": "Dr. YSR University of Health Sciences",
    "Management": "Trust",
    "ParentOrganization": "Siddhartha Academy of General and Technical Education (SAGTE)",
    "KeyPeople": [
      {"Name": "Dr. C. Nageswara Rao", "Role": "President", "Details": "Siddhartha Academy of General & Technical Education"},
      {"Name": "Dr. Pinnamaneni Venkateswara Rao", "Role": "Chief Promoter / Benefactor", "Details": "Renowned surgeon and philanthropist"}
    ],
    "PoliticalAffiliation": "None direct / Prominent educational academy managed by Vijayawada philanthropic and business leaders.",
    "FundingSource": "Trust endowment, tuition fees, Siddhartha Academy institutional funds, hospital income.",
    "SummaryReport": "Operated by Siddhartha Academy (SAGTE), a premier educational society in Vijayawada. Named after donor Dr. Pinnamaneni Siddhartha Rao. Self-financed through academy endowments and student fees."
  },
  {
    "SlNo": "10",
    "CollegeName": "Fathima Instt. of Medical Sciences Kadapa",
    "State": "Andhra Pradesh",
    "District": "Kadapa",
    "University": "Dr. YSR University of Health Sciences",
    "Management": "Trust",
    "ParentOrganization": "Mohammadiya Educational Society",
    "KeyPeople": [
      {"Name": "Mr. Mohiuddin Cox", "Role": "Chairman", "Details": "Mohammadiya Educational Society"}
    ],
    "PoliticalAffiliation": "None identified / Muslim Minority Educational Institution.",
    "FundingSource": "Muslim minority trust funding, student tuition fees, hospital service charges.",
    "SummaryReport": "Established in 2010 as a Muslim minority medical college managed by Mohammadiya Educational Society in Kadapa. Financed through student fees and trust funding."
  },
  {
    "SlNo": "11",
    "CollegeName": "Gayathri Vidya Parishad Institute of Health Care & Medical Technology Visakhapatnam",
    "State": "Andhra Pradesh",
    "District": "Visakhapatnam",
    "University": "Dr. YSR University of Health Sciences",
    "Management": "Society",
    "ParentOrganization": "Gayatri Vidya Parishad (GVP Society)",
    "KeyPeople": [
      {"Name": "Prof. Dr. P. Srinivasa Rao", "Role": "President", "Details": "Gayatri Vidya Parishad"},
      {"Name": "Prof. P. Soma Raju", "Role": "Secretary", "Details": "Former academician & GVP founder member"}
    ],
    "PoliticalAffiliation": "None identified / Academician-led non-profit educational society.",
    "FundingSource": "GVP Society funds, student tuition fees, clinical hospital income.",
    "SummaryReport": "Founded in 2016 by Gayatri Vidya Parishad, an esteemed society of academicians and philanthropists in Vizag. Funded via self-financing academic trust model."
  },
  {
    "SlNo": "12",
    "CollegeName": "GITAM Institute of Medical Sciences and Research Visakhapatnam",
    "State": "Andhra Pradesh",
    "District": "Visakhapatnam",
    "University": "GITAM Deemed University Visakhapatnam",
    "Management": "Private",
    "ParentOrganization": "GITAM (Gandhi Institute of Technology and Management) Deemed University",
    "KeyPeople": [
      {"Name": "M. Sribharat", "Role": "President", "Details": "President of GITAM Deemed University and current Member of Parliament (TDP, Visakhapatnam)"},
      {"Name": "Late Dr. M. V. V. S. Murthi", "Role": "Founder", "Details": "Former Member of Parliament (TDP) and prominent industrialist"}
    ],
    "PoliticalAffiliation": "Strong Telugu Desam Party (TDP) affiliation. Founded by late TDP MP Dr. M.V.V.S. Murthi; currently headed by M. Sribharat, TDP MP for Visakhapatnam.",
    "FundingSource": "Deemed university tuition fees, research grants, hospital patient fees, NRI student seat revenues.",
    "SummaryReport": "Constituent medical college of GITAM Deemed University, established by late TDP MP Dr. M.V.V.S. Murthi. Governed by GITAM Trust headed by MP M. Sribharat."
  },
  {
    "SlNo": "19",
    "CollegeName": "Great Eastern Medical School and Hospital Srikakulam",
    "State": "Andhra Pradesh",
    "District": "Srikakulam",
    "University": "Dr. YSR University of Health Sciences",
    "Management": "Trust",
    "ParentOrganization": "Aditya Educational Society",
    "KeyPeople": [
      {"Name": "Dr. K. Bhaskara Rao", "Role": "Chairman", "Details": "Aditya Educational Society"}
    ],
    "PoliticalAffiliation": "None identified / Private medical educational society.",
    "FundingSource": "Self-financing student tuition, hospital outpatient and clinical service fees.",
    "SummaryReport": "Established in 2010 by Aditya Educational Society to provide medical education and healthcare in North Coastal Andhra Pradesh. Self-funded institution."
  },
  {
    "SlNo": "20",
    "CollegeName": "GSL Medical College Rajahmundry",
    "State": "Andhra Pradesh",
    "District": "Rajahmundry",
    "University": "Dr. YSR University of Health Sciences",
    "Management": "Trust",
    "ParentOrganization": "GSL Educational Society",
    "KeyPeople": [
      {"Name": "Dr. Ganni Bhaskara Rao", "Role": "Chairman & Founder", "Details": "Surgeon, healthcare entrepreneur"},
      {"Name": "Dr. Ganni Rama Devi", "Role": "Managing Trustee", "Details": "GSL Educational Society"}
    ],
    "PoliticalAffiliation": "Local political connections in East Godavari region; non-partisan institutional leadership.",
    "FundingSource": "Student tuition fees, multi-specialty hospital revenue, diagnostic services earnings.",
    "SummaryReport": "Founded in 2002 by Dr. Ganni Bhaskara Rao under GSL Educational Society. Funded through self-financing medical college tuition structure and hospital revenues."
  },
  {
    "SlNo": "22",
    "CollegeName": "Katuri Medical College Guntur",
    "State": "Andhra Pradesh",
    "District": "Guntur",
    "University": "Dr. YSR University of Health Sciences",
    "Management": "Trust",
    "ParentOrganization": "Katuri Health Foundation / Katuri Educational Society",
    "KeyPeople": [
      {"Name": "Mr. Katuri Subba Rao", "Role": "Chairman", "Details": "Founder promoter of Katuri Health Foundation"}
    ],
    "PoliticalAffiliation": "None identified / Private health trust.",
    "FundingSource": "Tuition fees, hospital earnings, promoter endowment.",
    "SummaryReport": "Established in 2002 under Katuri Health Foundation near Guntur. Operated on a self-financing model using fee revenues and hospital services."
  },
  {
    "SlNo": "23",
    "CollegeName": "Konaseema Institute of Medical Sciences & Research Foundation Amalapuram",
    "State": "Andhra Pradesh",
    "District": "Amalapuram",
    "University": "Kaloji Narayana Rao University of Health Sciences Warangal",
    "Management": "Trust",
    "ParentOrganization": "V.S.L. Educational Society",
    "KeyPeople": [
      {"Name": "Dr. K. V. V. Satyanarayana Raju (Chaitanya Raju)", "Role": "Chairman & Founder", "Details": "Former Member of Legislative Council (MLC, Andhra Pradesh)"}
    ],
    "PoliticalAffiliation": "Founder Dr. K. V. V. Satyanarayana Raju (Chaitanya Raju) was a Member of the Legislative Council (MLC) in Andhra Pradesh.",
    "FundingSource": "Self-financing student tuition, hospital health scheme receipts, NRI quota seat revenues.",
    "SummaryReport": "Founded in 2005 in Konaseema region by former MLC Dr. K.V.V. Satyanarayana Raju under VSL Educational Society. Self-funded private trust institution."
  },
  {
    "SlNo": "25",
    "CollegeName": "Maharajah Institute of Medical Sciences Vizianagaram",
    "State": "Andhra Pradesh",
    "District": "Vizianagaram",
    "University": "Dr. YSR University of Health Sciences",
    "Management": "Trust",
    "ParentOrganization": "Maharajah Alak Narayan Society of Arts and Science (MANSAS Trust) / MIMS Society",
    "KeyPeople": [
      {"Name": "P. Ashok Gajapathi Raju", "Role": "Trustee / Royal Family Head", "Details": "Former Union Cabinet Minister for Civil Aviation (TDP) and hereditary trustee of MANSAS Trust"},
      {"Name": "Dr. Rama Rao", "Role": "Director/Management", "Details": "MIMS Vizianagaram"}
    ],
    "PoliticalAffiliation": "TDP Leadership. Associated with the Royal Family of Vizianagaram and P. Ashok Gajapathi Raju (former Union Minister, TDP).",
    "FundingSource": "MANSAS Trust royal endowments, student fees, teaching hospital revenue.",
    "SummaryReport": "Established in 2002 in Vizianagaram, tied to the historic MANSAS Trust created by the Vizianagaram royal family (headed by TDP leader P. Ashok Gajapathi Raju). Self-financing trust institution."
  },
  {
    "SlNo": "26",
    "CollegeName": "Narayana Medical College Nellore",
    "State": "Andhra Pradesh",
    "District": "Nellore",
    "University": "Dr. YSR University of Health Sciences",
    "Management": "Trust",
    "ParentOrganization": "Narayana Educational Society / Narayana Group",
    "KeyPeople": [
      {"Name": "Dr. Ponguru Narayana", "Role": "Founder & Chairman", "Details": "Cabinet Minister for Municipal Administration & Urban Development (Andhra Pradesh, TDP) and founder of Narayana Educational Group"}
    ],
    "PoliticalAffiliation": "Strong TDP Affiliation. Founder Dr. P. Narayana is an MLA (Nellore City) and senior Cabinet Minister in the TDP government.",
    "FundingSource": "Narayana Educational Group revenues, student tuition fees, NRI seat quota fees, super-specialty hospital earnings.",
    "SummaryReport": "Founded in 2000 by TDP Cabinet Minister Dr. P. Narayana. Key asset of Narayana Educational Group, funded through student fees and group revenues."
  },
  {
    "SlNo": "27",
    "CollegeName": "Nimra Institute of Medical Sciences Krishna Dist.",
    "State": "Andhra Pradesh",
    "District": "Krishna",
    "University": "Dr. YSR University of Health Sciences",
    "Management": "Society",
    "ParentOrganization": "Nimra Educational Society",
    "KeyPeople": [
      {"Name": "Dr. Md. Viquaruddin", "Role": "Chairman", "Details": "Founder of Nimra Group of Institutions"}
    ],
    "PoliticalAffiliation": "None identified / Muslim Minority Educational Society.",
    "FundingSource": "Tuition fees, Muslim minority trust funds, hospital operational income.",
    "SummaryReport": "Established in 2016 near Vijayawada as a Muslim minority medical college operated by Nimra Educational Society. Self-funded."
  },
  {
    "SlNo": "28",
    "CollegeName": "NRI Institute of Medical Sciences Visakhapatnam",
    "State": "Andhra Pradesh",
    "District": "Visakhapatnam",
    "University": "Dr. YSR University of Health Sciences",
    "Management": "Trust",
    "ParentOrganization": "Anil Neerukonda Educational Society (ANES)",
    "KeyPeople": [
      {"Name": "V. Rajan Neerukonda", "Role": "Chairman", "Details": "NRI entrepreneur and philanthropist"},
      {"Name": "Dr. V. B. J. O. Chelikani", "Role": "Trustee / Director", "Details": "ANES Society"}
    ],
    "PoliticalAffiliation": "None direct / NRI physician and entrepreneur educational trust.",
    "FundingSource": "NRI promoter capital, tuition fees, hospital revenue, ANITSE educational group funds.",
    "SummaryReport": "Founded in 2012 by Anil Neerukonda Educational Society (ANES) established by non-resident Indian entrepreneurs. Self-financing trust model."
  },
  {
    "SlNo": "29",
    "CollegeName": "NRI Medical College Guntur",
    "State": "Andhra Pradesh",
    "District": "Guntur",
    "University": "Dr. YSR University of Health Sciences",
    "Management": "Trust",
    "ParentOrganization": "Academy of Regional Medical Sciences (ARMS) / NRI Educational Society",
    "KeyPeople": [
      {"Name": "Dr. N. Nageswara Rao", "Role": "President / Promoter", "Details": "Senior physician and NRI group representative"},
      {"Name": "Dr. K. Rajendra Prasad", "Role": "Management Member", "Details": "ARMS Society"}
    ],
    "PoliticalAffiliation": "None direct / Consortium of Non-Resident Indian doctors and medical professionals.",
    "FundingSource": "NRI physician syndicate equity, tuition fees, hospital clinical earnings.",
    "SummaryReport": "Established in 2003 at Chinakani, Guntur by a group of NRI doctors under Academy of Regional Medical Sciences (ARMS). Funded by NRI capital and self-financing fee model."
  },
  {
    "SlNo": "30",
    "CollegeName": "P E S Institute Of Medical Sciences and Research Kuppam",
    "State": "Andhra Pradesh",
    "District": "Chittoor",
    "University": "Dr. YSR University of Health Sciences",
    "Management": "Trust",
    "ParentOrganization": "People's Education Society (PES Trust)",
    "KeyPeople": [
      {"Name": "Dr. M. R. Doreswamy", "Role": "Founder Chairman", "Details": "Former Member of Legislative Council (MLC, Karnataka, BJP) and former Advisor on Education to Govt of Karnataka"},
      {"Name": "Prof. D. Jawahar", "Role": "Pro-Chancellor / CEO", "Details": "PES Group"}
    ],
    "PoliticalAffiliation": "BJP Affiliation. Founder Dr. M. R. Doreswamy served as MLC (BJP) in Karnataka and Education Advisor to the Karnataka state government.",
    "FundingSource": "PES Educational Trust reserves, student tuition fees, hospital treatment fees.",
    "SummaryReport": "Established in 2001 in Kuppam by PES Trust founder Dr. M.R. Doreswamy (BJP former MLC). Self-funded through PES educational network resources."
  },
  {
    "SlNo": "36",
    "CollegeName": "Santhiram Medical College Nandyal",
    "State": "Andhra Pradesh",
    "District": "Nandyal",
    "University": "Dr. YSR University of Health Sciences",
    "Management": "Trust",
    "ParentOrganization": "Santhiram Educational Society / RGM Group",
    "KeyPeople": [
      {"Name": "Dr. M. Santhiramudu", "Role": "Chairman", "Details": "Industrialist and founder of RGM & Santhiram Educational Institutions"}
    ],
    "PoliticalAffiliation": "Prominent local business leadership with strong regional political influence in Rayalaseema region.",
    "FundingSource": "RGM Group industrial revenue, tuition fees, hospital operational income.",
    "SummaryReport": "Founded in 2005 near Nandyal by industrialist Dr. M. Santhiramudu under Santhiram Educational Society. Self-financed."
  },
  {
    "SlNo": "37",
    "CollegeName": "Sri Balaji Medical College Hospital and Research Institute Chittoor",
    "State": "Andhra Pradesh",
    "District": "Chittoor",
    "University": "Dr. YSR University of Health Sciences",
    "Management": "Trust",
    "ParentOrganization": "Sri Balaji Educational Trust",
    "KeyPeople": [
      {"Name": "Dr. R. Venkataswamy", "Role": "Founder Chairman", "Details": "Educational trustee"}
    ],
    "PoliticalAffiliation": "None identified / Independent educational trust.",
    "FundingSource": "Trust capital, student fees, hospital revenue.",
    "SummaryReport": "Private medical college established in Chittoor district under Sri Balaji Educational Trust. Self-funded."
  },
  {
    "SlNo": "39",
    "CollegeName": "Viswabharathi Medical College Kurnool",
    "State": "Andhra Pradesh",
    "District": "Kurnool",
    "University": "Dr. YSR University of Health Sciences",
    "Management": "Society",
    "ParentOrganization": "Viswabharathi Educational Society",
    "KeyPeople": [
      {"Name": "Dr. M. V. Subba Reddy", "Role": "Chairman", "Details": "Viswabharathi Educational Institutions"}
    ],
    "PoliticalAffiliation": "None identified / Private educational society.",
    "FundingSource": "Tuition fees, hospital earnings, promoter investments.",
    "SummaryReport": "Established in 2014 in Kurnool by Viswabharathi Educational Society. Financed through student fee structure and hospital clinical services."
  }
]

ap_tg_sources = [
  {"SlNo": "6", "CollegeName": "Alluri Sitharam Raju Academy of Medical Sciences Eluru", "Sources": ["http://asram.in/", "https://en.wikipedia.org/wiki/Gokaraju_Ganga_Raju", "https://myneta.info/ls2014/candidate.php?candidate_id=2273"]},
  {"SlNo": "8", "CollegeName": "Apollo Institute of Medical Sciences and Research Chittoor", "Sources": ["https://aimsrchittoor.edu.in/", "https://www.apollohospitals.com/corporate/about-us/leadership/dr-prathap-c-reddy/"]},
  {"SlNo": "9", "CollegeName": "Dr. P.S.I. Medical College Chinoutpalli", "Sources": ["https://psims.org.in/", "https://siddharthaacademy.ac.in/"]},
  {"SlNo": "10", "CollegeName": "Fathima Instt. of Medical Sciences Kadapa", "Sources": ["https://fims.ac.in/", "https://www.nmc.org.in/information-desk/college-and-course-search/"]},
  {"SlNo": "11", "CollegeName": "Gayathri Vidya Parishad Institute of Health Care & Medical Technology Visakhapatnam", "Sources": ["https://gvpht.in/", "https://gvpce.ac.in/aboutgvp.html"]},
  {"SlNo": "12", "CollegeName": "GITAM Institute of Medical Sciences and Research Visakhapatnam", "Sources": ["https://gimsr.gitam.edu/", "https://en.wikipedia.org/wiki/M._V._V._S._Murthi", "https://en.wikipedia.org/wiki/M._Sribharat"]},
  {"SlNo": "19", "CollegeName": "Great Eastern Medical School and Hospital Srikakulam", "Sources": ["https://gems.edu.in/", "https://www.medicalcouncilindia.org/"]},
  {"SlNo": "20", "CollegeName": "GSL Medical College Rajahmundry", "Sources": ["https://gslmc.com/", "https://gslmed.edu.in/"]},
  {"SlNo": "22", "CollegeName": "Katuri Medical College Guntur", "Sources": ["http://katurimedicalcollege.org/"]},
  {"SlNo": "23", "CollegeName": "Konaseema Institute of Medical Sciences & Research Foundation Amalapuram", "Sources": ["https://kims.in/", "https://en.wikipedia.org/wiki/Konaseema_Institute_of_Medical_Sciences_and_Research_Foundation"]},
  {"SlNo": "25", "CollegeName": "Maharajah Institute of Medical Sciences Vizianagaram", "Sources": ["http://mims.edu.in/", "https://en.wikipedia.org/wiki/Pusapati_Ashok_Gajapathi_Raju"]},
  {"SlNo": "26", "CollegeName": "Narayana Medical College Nellore", "Sources": ["https://narayanamedicalcollege.com/", "https://en.wikipedia.org/wiki/P._Narayana"]},
  {"SlNo": "27", "CollegeName": "Nimra Institute of Medical Sciences Krishna Dist.", "Sources": ["http://nims.in/", "https://nimra.in/"]},
  {"SlNo": "28", "CollegeName": "NRI Institute of Medical Sciences Visakhapatnam", "Sources": ["https://nriims.com/", "https://anits.edu.in/"]},
  {"SlNo": "29", "CollegeName": "NRI Medical College Guntur", "Sources": ["http://nrimc.edu.in/"]},
  {"SlNo": "30", "CollegeName": "P E S Institute Of Medical Sciences and Research Kuppam", "Sources": ["https://pesimsr.pes.edu/", "https://en.wikipedia.org/wiki/M._R._Doreswamy"]},
  {"SlNo": "36", "CollegeName": "Santhiram Medical College Nandyal", "Sources": ["https://santhirammedicals.org/", "https://rgmcet.edu.in/"]},
  {"SlNo": "37", "CollegeName": "Sri Balaji Medical College Hospital and Research Institute Chittoor", "Sources": ["https://sribalajimedicalcollege.com/"]},
  {"SlNo": "39", "CollegeName": "Viswabharathi Medical College Kurnool", "Sources": ["https://vmcknl.or.in/"]}
]

own.extend(ap_tg_records)
src.extend(ap_tg_sources)

save_db(own, src)
