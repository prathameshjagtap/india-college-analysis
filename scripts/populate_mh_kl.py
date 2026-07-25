import json, os

def load_db():
    with open('data/private_colleges_ownership.json', 'r') as f:
        own = json.load(f)
    with open('data/private_college_sources.json', 'r') as f:
        src = json.load(f)
    return own, src

def save_db(own, src):
    own_dict = {str(x['SlNo']): x for x in own}
    src_dict = {str(x['SlNo']): x for x in src}
    
    sorted_own = sorted(own_dict.values(), key=lambda x: int(x['SlNo']))
    sorted_src = sorted(src_dict.values(), key=lambda x: int(x['SlNo']))
    
    with open('data/private_colleges_ownership.json', 'w') as f:
        json.dump(sorted_own, f, indent=2)
    with open('data/private_college_sources.json', 'w') as f:
        json.dump(sorted_src, f, indent=2)
    print(f"Total updated: {len(sorted_own)} records")

own, src = load_db()

mh_kl_records = [
  # --- MAHARASHTRA ---
  {
    "SlNo": "331",
    "CollegeName": "Mahatma Gandhi Missions Medical College Navi Mumbai",
    "State": "Maharashtra",
    "District": "Navi Mumbai",
    "University": "MGM Institute of Health Sciences",
    "Management": "Private",
    "ParentOrganization": "Mahatma Gandhi Mission Trust (MGM Trust) / MGM Institute of Health Sciences Deemed University",
    "KeyPeople": [
      {"Name": "Kamalkishor Kadam", "Role": "Chairman & Founder", "Details": "Former Cabinet Minister for Education (Maharashtra, NCP/Congress)"},
      {"Name": "Dr. N. N. Kadam", "Role": "Trustee", "Details": "MGM Trust"}
    ],
    "PoliticalAffiliation": "NCP / Congress Leader. Founder Kamalkishor Kadam is a former Maharashtra Education Minister.",
    "FundingSource": "MGM Deemed University fees, super-specialty hospital clinical earnings, trust endowments.",
    "SummaryReport": "Established in 1989 in Kamothe, Navi Mumbai by former Education Minister Kamalkishor Kadam under MGM Trust. Constituent of MGM Deemed University. Self-financed."
  },
  {
    "SlNo": "332",
    "CollegeName": "Shri Ramchandra Institute of Medical Sciences Aurangabad",
    "State": "Maharashtra",
    "District": "Chhatrapati Sambhajinagar",
    "University": "Maharashtra University of Health Sciences Nashik",
    "Management": "Private",
    "ParentOrganization": "Shri Ramchandra Educational Trust",
    "KeyPeople": [{"Name": "Dr. Ramchandra", "Role": "Chairman", "Details": "Trustee"}],
    "PoliticalAffiliation": "None identified / Educational trust.",
    "FundingSource": "Tuition fees, hospital operational income.",
    "SummaryReport": "Medical college at Sambhajinagar (Aurangabad) operated by Shri Ramchandra Trust. Self-financed."
  },
  {
    "SlNo": "342",
    "CollegeName": "Mahatma Gandhi Mission Medical College Vashi",
    "State": "Maharashtra",
    "District": "Thane",
    "University": "Maharashtra University of Health Sciences Nashik",
    "Management": "Trust",
    "ParentOrganization": "Mahatma Gandhi Mission Trust (MGM Trust)",
    "KeyPeople": [{"Name": "Kamalkishor Kadam", "Role": "Chairman", "Details": "Former Maharashtra Cabinet Minister"}],
    "PoliticalAffiliation": "NCP / Congress Leader. Founded by Kamalkishor Kadam.",
    "FundingSource": "MGM Trust reserves, tuition fees, hospital clinical income.",
    "SummaryReport": "Established at Vashi, Navi Mumbai under MGM Trust by former Minister Kamalkishor Kadam. Self-financed."
  },
  {
    "SlNo": "344",
    "CollegeName": "Parbhani Medical College",
    "State": "Maharashtra",
    "District": "Parbhani",
    "University": "Maharashtra University of Health Sciences Nashik",
    "Management": "Society",
    "ParentOrganization": "Godavari Foundation / Parbhani Education Society",
    "KeyPeople": [{"Name": "Dr. Ulhas Patil", "Role": "Chairman", "Details": "Former Member of Parliament"}],
    "PoliticalAffiliation": "Former MP Connection. Associated with Godavari Foundation (Dr. Ulhas Patil, former MP).",
    "FundingSource": "Tuition fees, hospital earnings.",
    "SummaryReport": "Medical college in Parbhani managed under educational society ecosystem. Self-financed."
  },
  {
    "SlNo": "348",
    "CollegeName": "ACPM Medical College Dhule",
    "State": "Maharashtra",
    "District": "Dhule",
    "University": "Maharashtra University of Health Sciences Nashik",
    "Management": "Trust",
    "ParentOrganization": "Jawahar Medical Foundation",
    "KeyPeople": [
      {"Name": "Kunal Rohidas Patil", "Role": "Chairman", "Details": "Member of Legislative Assembly (Congress, Dhule Rural)"},
      {"Name": "Late Annasaheb D. B. Patil", "Role": "Founder", "Details": "Veteran Maratha leader and former Minister"}
    ],
    "PoliticalAffiliation": "Congress Leader. Governed by sitting Congress MLA Kunal Patil.",
    "FundingSource": "Jawahar Foundation funds, tuition fees, hospital operational income.",
    "SummaryReport": "Established in 1990 in Dhule by Jawahar Medical Foundation, founded by Annasaheb D.B. Patil and led by Congress MLA Kunal Patil. Self-financed."
  },
  {
    "SlNo": "350",
    "CollegeName": "Dr. D Y Patil Medical College Hospital and Research Centre Pimpri Pune",
    "State": "Maharashtra",
    "District": "Pune",
    "University": "Dr. D Y Patil University Deemed Pimpri Pune",
    "Management": "Trust",
    "ParentOrganization": "Dr. D. Y. Patil Educational Society / Dr. D. Y. Patil Unitech Society",
    "KeyPeople": [
      {"Name": "Dr. D. Y. Patil", "Role": "Founder & Chancellor Emeritus", "Details": "Padma Shri awardee, former Governor of Bihar & Tripura, senior Congress leader"},
      {"Name": "Dr. P. D. Patil", "Role": "Chancellor", "Details": "Dr. D. Y. Patil Vidyapeeth Pune"}
    ],
    "PoliticalAffiliation": "Congress Leader Family. Founded by former Governor and senior Congress leader Dr. D. Y. Patil.",
    "FundingSource": "Deemed university tuition fees, 2000-bed super-specialty hospital clinical income, international student fees.",
    "SummaryReport": "Established in 1996 in Pimpri, Pune. Flagship constituent college of Dr. D. Y. Patil Vidyapeeth Deemed University. Self-financed."
  },
  {
    "SlNo": "352",
    "CollegeName": "Krishna Institute of Medical Sciences Karad",
    "State": "Maharashtra",
    "District": "Satara",
    "University": "Krishna Institute of Medical Sciences University Deemed Karad",
    "Management": "Trust",
    "ParentOrganization": "Shetkari Shikshan Mandal / KIMS Deemed University",
    "KeyPeople": [
      {"Name": "Late Jaywantrao Bhosale", "Role": "Founder", "Details": "Cooperative leader and educationist"},
      {"Name": "Dr. Suresh Bhosale", "Role": "Chancellor & Chairman", "Details": "BJP candidate (Karad South) and prominent western Maharashtra leader"}
    ],
    "PoliticalAffiliation": "BJP Leader. Chancellor Dr. Suresh Bhosale is a prominent BJP political leader in Satara.",
    "FundingSource": "KIMS Deemed University fees, super-specialty hospital earnings, trust reserves.",
    "SummaryReport": "Established in 1984 in Karad, Satara by Jaywantrao Bhosale. Constituent of KIMS Deemed University led by BJP leader Dr. Suresh Bhosale. Self-financed."
  },
  {
    "SlNo": "355",
    "CollegeName": "Mahatma Gandhi Institute of Medical Sciences Sevagram Wardha",
    "State": "Maharashtra",
    "District": "Wardha",
    "University": "Maharashtra University of Health Sciences Nashik",
    "Management": "Trust",
    "ParentOrganization": "Kasturba Health Society",
    "KeyPeople": [
      {"Name": "Late Dr. Sushila Nayar", "Role": "Founder", "Details": "Freedom fighter, personal physician to Mahatma Gandhi, and former Union Health Minister"},
      {"Name": "Dr. B. S. Garg", "Role": "Secretary", "Details": "Kasturba Health Society"}
    ],
    "PoliticalAffiliation": "None / Historic Gandhian Philanthropic Trust (Supported by Union MoHFW & Maharashtra Govt grants).",
    "FundingSource": "Union Ministry of Health & Family Welfare grant-in-aid (50%), Govt of Maharashtra grant (25%), Kasturba Health Society (25%).",
    "SummaryReport": "India's first rural medical college, established in 1969 at Mahatma Gandhi's Sevagram Ashram by Dr. Sushila Nayar. Unique non-profit trust college receiving 75% combined central & state government funding."
  },
  {
    "SlNo": "356",
    "CollegeName": "Bharati Vidyapeeth Deemed University Medical College & Hospital Sangli",
    "State": "Maharashtra",
    "District": "Sangli",
    "University": "Bharati Vidyapeeth University Deemed Pune",
    "Management": "Trust",
    "ParentOrganization": "Bharati Vidyapeeth Trust",
    "KeyPeople": [
      {"Name": "Late Dr. Patangrao Kadam", "Role": "Founder", "Details": "Former Cabinet Minister for Forest & Revenue (Maharashtra, Congress)"},
      {"Name": "Vishwajeet Kadam", "Role": "Pro-Vice Chancellor", "Details": "Member of Legislative Assembly (Congress, Palus-Kadegaon) and former Minister of State"}
    ],
    "PoliticalAffiliation": "Congress Leader Family. Founded by late Congress Cabinet Minister Dr. Patangrao Kadam; led by Congress MLA Vishwajeet Kadam.",
    "FundingSource": "Bharati Vidyapeeth Deemed University tuition fees, hospital clinical income.",
    "SummaryReport": "Established in 2005 in Sangli as a constituent college of Bharati Vidyapeeth Deemed University. Self-financed."
  },
  {
    "SlNo": "358",
    "CollegeName": "Dr. D Y Patil Medical College Kolhapur",
    "State": "Maharashtra",
    "District": "Kolhapur",
    "University": "D.Y. Patil Education Society Deemed Kolhapur",
    "Management": "Trust",
    "ParentOrganization": "D. Y. Patil Education Society Deemed University",
    "KeyPeople": [
      {"Name": "Satej D. Patil", "Role": "President & Trustee", "Details": "Member of Legislative Council (Congress) and former Minister of State for Home (Maharashtra)"},
      {"Name": "Dr. Sanjay D. Patil", "Role": "Chancellor", "Details": "D. Y. Patil Group Kolhapur"}
    ],
    "PoliticalAffiliation": "Congress Leader. President Satej (Bunty) Patil is a senior Congress MLC and former Minister.",
    "FundingSource": "Deemed university tuition fees, D. Y. Patil Hospital clinical earnings.",
    "SummaryReport": "Established in 1989 in Kadamwadi, Kolhapur. Constituent of D. Y. Patil Education Society Deemed University led by Congress leader Satej Patil. Self-financed."
  },
  {
    "SlNo": "359",
    "CollegeName": "Maharashtra Institute of Medical Sciences & Research Latur",
    "State": "Maharashtra",
    "District": "Latur",
    "University": "Maharashtra University of Health Sciences Nashik",
    "Management": "Trust",
    "ParentOrganization": "MAEER's MIT Group of Institutions Pune",
    "KeyPeople": [{"Name": "Prof. Dr. Vishwanath D. Karad", "Role": "Founder & Executive President", "Details": "Padma Shri awardee and founder of MIT Group Pune"}],
    "PoliticalAffiliation": "None direct / Premier educational conglomerate in Maharashtra.",
    "FundingSource": "MAEER trust reserves, tuition fees, Yashwantrao Chavan Hospital income.",
    "SummaryReport": "Established in 1990 in Latur by MAEER's MIT Group Pune founded by Dr. Vishwanath D. Karad. Self-financed."
  },
  {
    "SlNo": "364",
    "CollegeName": "Terna Medical College Navi Mumbai",
    "State": "Maharashtra",
    "District": "Thane",
    "University": "Maharashtra University of Health Sciences Nashik",
    "Management": "Trust",
    "ParentOrganization": "Terna Public Charitable Trust",
    "KeyPeople": [
      {"Name": "Dr. Padmasinh Bajirao Patil", "Role": "Founder Chairman", "Details": "Former Home Minister of Maharashtra and former Member of Parliament (NCP)"},
      {"Name": "Rana Jagjit-singh Patil", "Role": "President", "Details": "Member of Legislative Assembly (BJP, Tuljapur) and former Minister"}
    ],
    "PoliticalAffiliation": "NCP / BJP Political Leader Family. Founded by former Home Minister Padmasinh Patil; led by BJP MLA Rana Jagjit-singh Patil.",
    "FundingSource": "Terna Trust reserves, tuition fees, hospital operational income.",
    "SummaryReport": "Established in 1991 at Nerul, Navi Mumbai by former Home Minister Padmasinh Patil. Governed by Terna Trust. Self-financed."
  },
  {
    "SlNo": "365",
    "CollegeName": "Mahatma Gandhi Missions Medical College Aurangabad",
    "State": "Maharashtra",
    "District": "Chhatrapati Sambhajinagar",
    "University": "MGM Institute of Health Sciences Deemed Navi Mumbai",
    "Management": "Trust",
    "ParentOrganization": "Mahatma Gandhi Mission Trust (MGM Trust)",
    "KeyPeople": [{"Name": "Kamalkishor Kadam", "Role": "Chairman & Founder", "Details": "Former Education Minister of Maharashtra"}],
    "PoliticalAffiliation": "NCP / Congress Leader. Founded by former Minister Kamalkishor Kadam.",
    "FundingSource": "MGM Deemed University fees, super-specialty hospital clinical income.",
    "SummaryReport": "Established in 1990 at Chhatrapati Sambhajinagar (Aurangabad) under MGM Trust. Constituent of MGM Deemed University. Self-financed."
  },
  {
    "SlNo": "368",
    "CollegeName": "Rural Medical College Loni",
    "State": "Maharashtra",
    "District": "Ahilyanagar",
    "University": "Pravara Institute of Medical Sciences Deemed Ahmednagar",
    "Management": "Trust",
    "ParentOrganization": "Pravara Medical Trust / Pravara Institute of Medical Sciences Deemed University",
    "KeyPeople": [
      {"Name": "Radhakrishna Vikhe Patil", "Role": "Chairman", "Details": "Cabinet Minister for Revenue, Animal Husbandry & Dairy (Maharashtra, BJP) and MLA (Shirdi)"},
      {"Name": "Dr. Sujay Vikhe Patil", "Role": "Trustee", "Details": "Former Member of Parliament (BJP, Ahmednagar)"},
      {"Name": "Late Dr. Vithalrao Vikhe Patil", "Role": "Founder Visionary", "Details": "Padma Shri awardee and pioneer of Indian cooperative movement"}
    ],
    "PoliticalAffiliation": "BJP Cabinet Minister. Governed by Pravara Trust led by senior Maharashtra Cabinet Minister Radhakrishna Vikhe Patil.",
    "FundingSource": "Pravara Medical Trust reserves, deemed university tuition fees, Pravara Hospital clinical revenues.",
    "SummaryReport": "Established in 1984 in Loni, Ahmednagar by Balasaheb Vikhe Patil. Flagship constituent of Pravara Deemed University led by Cabinet Minister Radhakrishna Vikhe Patil. Self-financed."
  },
  {
    "SlNo": "371",
    "CollegeName": "Maharashtra Institute of Medical Education & Research Talegaon Pune",
    "State": "Maharashtra",
    "District": "Pune",
    "University": "Maharashtra University of Health Sciences Nashik",
    "Management": "Trust",
    "ParentOrganization": "MAEER's MIT Group of Institutions Pune",
    "KeyPeople": [{"Name": "Prof. Dr. Vishwanath D. Karad", "Role": "Founder & Executive President", "Details": "MIT Group Pune"}],
    "PoliticalAffiliation": "None direct / MIT Pune Group.",
    "FundingSource": "MAEER Trust funds, tuition fees, Bhausaheb Sardesai Rural Hospital revenues.",
    "SummaryReport": "Established in 1995 at Talegaon Dabhade, Pune by MAEER's MIT Group. Self-financed."
  },
  {
    "SlNo": "372",
    "CollegeName": "Smt. Kashibai Navale Medical College and General Hospital Pune",
    "State": "Maharashtra",
    "District": "Pune",
    "University": "Maharashtra University of Health Sciences Nashik",
    "Management": "Trust",
    "ParentOrganization": "Sinhgad Technical Education Society (STES)",
    "KeyPeople": [
      {"Name": "Prof. M. N. Navale", "Role": "Founder President", "Details": "Sinhgad Group of Institutes"},
      {"Name": "Sunanda M. Navale", "Role": "Secretary", "Details": "STES Pune"}
    ],
    "PoliticalAffiliation": "None direct / Educational conglomerate.",
    "FundingSource": "STES institutional revenues, tuition fees, general hospital earnings.",
    "SummaryReport": "Established in 2007 at Narhe, Pune by Prof. M. N. Navale under Sinhgad Technical Education Society. Self-financed."
  },
  {
    "SlNo": "373",
    "CollegeName": "KJ Somaiyya Medical College & Research Centre Mumbai",
    "State": "Maharashtra",
    "District": "Mumbai Suburban",
    "University": "Maharashtra University of Health Sciences Nashik",
    "Management": "Trust",
    "ParentOrganization": "Somaiya Vidyavihar Trust",
    "KeyPeople": [
      {"Name": "Late Padmabhushan Karamshi Jethabhai Somaiya", "Role": "Founder", "Details": "Industrialist and philanthropist"},
      {"Name": "Samir Somaiya", "Role": "President", "Details": "Somaiya Vidyavihar Trust & Godavari Biorefineries"}
    ],
    "PoliticalAffiliation": "None direct / Historic philanthropic and industrial educational trust.",
    "FundingSource": "Somaiya Vidyavihar trust endowments, student tuition fees, hospital clinical income.",
    "SummaryReport": "Established in 1991 at Sion, Mumbai by Karamshi Jethabhai Somaiya under Somaiya Vidyavihar Trust. Self-funded philanthropic trust."
  },
  {
    "SlNo": "374",
    "CollegeName": "N. K. P. Salve Instt. of Medical Sciences and Research Centre and Lata Mangeshkar Hospital Nagpur",
    "State": "Maharashtra",
    "District": "Nagpur",
    "University": "Maharashtra University of Health Sciences Nashik",
    "Management": "Trust",
    "ParentOrganization": "VSPM Academy of Higher Education (VSPMAHE)",
    "KeyPeople": [
      {"Name": "Ranjit Deshmukh", "Role": "Chairman", "Details": "Former Cabinet Minister (Maharashtra, Congress) and former MPCC President"},
      {"Name": "Late N. K. P. Salve", "Role": "Patron / Namesake", "Details": "Former Union Cabinet Minister and senior Congress leader"}
    ],
    "PoliticalAffiliation": "Congress Leader. Founded by former Maharashtra Congress President and Cabinet Minister Ranjit Deshmukh.",
    "FundingSource": "VSPM Academy reserves, tuition fees, Lata Mangeshkar Hospital revenues.",
    "SummaryReport": "Established in 1990 at Digdoh Hills, Nagpur by former Congress Minister Ranjit Deshmukh. Named after Union Minister N. K. P. Salve. Self-financed."
  },
  {
    "SlNo": "375",
    "CollegeName": "Dr. Vithalrao Vikhe Patil Foundations Medical College & Hospital Ahmednagar",
    "State": "Maharashtra",
    "District": "Ahilyanagar",
    "University": "Maharashtra University of Health Sciences Nashik",
    "Management": "Trust",
    "ParentOrganization": "Dr. Vithalrao Vikhe Patil Foundation (DVVPF)",
    "KeyPeople": [{"Name": "Radhakrishna Vikhe Patil", "Role": "Chairman", "Details": "Cabinet Minister for Revenue (Maharashtra, BJP)"}],
    "PoliticalAffiliation": "BJP Cabinet Minister. Led by Maharashtra Revenue Minister Radhakrishna Vikhe Patil.",
    "FundingSource": "DVVP Foundation funds, student tuition fees, hospital clinical income.",
    "SummaryReport": "Established in 2004 at Vilad Ghat, Ahmednagar by Vikhe Patil family foundation, headed by Cabinet Minister Radhakrishna Vikhe Patil. Self-financed."
  },
  {
    "SlNo": "376",
    "CollegeName": "Padmashree Dr. D.Y.Patil Medical College Navi Mumbai",
    "State": "Maharashtra",
    "District": "Thane",
    "University": "Padmashree Dr. D Y Patil University Deemed Navi Mumbai",
    "Management": "Trust",
    "ParentOrganization": "Dr. D. Y. Patil University Deemed Navi Mumbai",
    "KeyPeople": [{"Name": "Dr. Vijay D. Patil", "Role": "Chancellor & Founder", "Details": "President of DY Patil Group Navi Mumbai"}],
    "PoliticalAffiliation": "Congress Leader Family. Founded by family of former Governor Dr. D. Y. Patil.",
    "FundingSource": "Deemed university tuition fees, super-specialty hospital revenues.",
    "SummaryReport": "Established in 1989 at Nerul, Navi Mumbai. Flagship constituent college of Dr. D. Y. Patil University Navi Mumbai. Self-financed."
  },
  {
    "SlNo": "380",
    "CollegeName": "Dr. Panjabrao Alias Bhausaheb Deshmukh Memorial Medical College Amravati",
    "State": "Maharashtra",
    "District": "Amravati",
    "University": "Maharashtra University of Health Sciences Nashik",
    "Management": "Trust",
    "ParentOrganization": "Shri Shivaji Education Society Amravati",
    "KeyPeople": [
      {"Name": "Late Dr. Panjabrao Deshmukh", "Role": "Founder", "Details": "First Union Minister for Agriculture of India and Constitution Assembly member"},
      {"Name": "Harshvardhan Deshmukh", "Role": "President", "Details": "Shri Shivaji Education Society"}
    ],
    "PoliticalAffiliation": "Historical National Leader. Founded by India's first Agriculture Minister Dr. Panjabrao Deshmukh.",
    "FundingSource": "Shri Shivaji Society institutional reserves, tuition fees, hospital operational income.",
    "SummaryReport": "Established in 1984 in Amravati by historic Shri Shivaji Education Society (est. 1932). Self-financed educational trust."
  },
  {
    "SlNo": "382",
    "CollegeName": "Dr. Ulhas Patil Medical College & Hospital Jalgaon",
    "State": "Maharashtra",
    "District": "Jalgaon",
    "University": "Maharashtra University of Health Sciences Nashik",
    "Management": "Trust",
    "ParentOrganization": "Godavari Foundation",
    "KeyPeople": [
      {"Name": "Dr. Ulhas Patil", "Role": "Founder Chairman", "Details": "Former Member of Parliament (Lok Sabha, Jalgaon, Congress/NCP)"},
      {"Name": "Dr. Varsha Patil", "Role": "Secretary", "Details": "Godavari Foundation"}
    ],
    "PoliticalAffiliation": "Former MP. Founder Dr. Ulhas Patil is a former Member of Parliament.",
    "FundingSource": "Godavari Foundation funds, tuition fees, hospital clinical income.",
    "SummaryReport": "Established in 2008 in Jalgaon by former MP Dr. Ulhas Patil under Godavari Foundation. Self-financed."
  },
  {
    "SlNo": "383",
    "CollegeName": "Jawaharlal Nehru Medical College Sawangi Meghe Wardha",
    "State": "Maharashtra",
    "District": "Wardha",
    "University": "Datta Meghe Instt. of Medical Sciences Deemed Nagpur",
    "Management": "Trust",
    "ParentOrganization": "Datta Meghe Institute of Higher Education & Research (DMIHER Deemed University)",
    "KeyPeople": [
      {"Name": "Datta Meghe", "Role": "Founder Chancellor", "Details": "Former four-time Member of Parliament (Lok Sabha & Rajya Sabha, Congress/NCP/BJP)"},
      {"Name": "Sameer Meghe", "Role": "Trustee", "Details": "Member of Legislative Assembly (BJP, Hingna)"}
    ],
    "PoliticalAffiliation": "BJP Leader Family. Founded by former MP Datta Meghe; led by BJP MLA Sameer Meghe.",
    "FundingSource": "DMIHER Deemed University fees, Acharya Vinoba Bhave Rural Hospital earnings.",
    "SummaryReport": "Established in 1990 at Sawangi (Meghe), Wardha. Flagship constituent of DMIHER Deemed University led by former MP Datta Meghe & BJP MLA Sameer Meghe. Self-financed."
  },
  {
    "SlNo": "384",
    "CollegeName": "Dr. Vasantrao Pawar Medical College Hospital & Research Centre Nasik",
    "State": "Maharashtra",
    "District": "Nashik",
    "University": "Maharashtra University of Health Sciences Nashik",
    "Management": "Trust",
    "ParentOrganization": "Maratha Vidya Prasarak (MVP) Samaj Nashik",
    "KeyPeople": [
      {"Name": "Late Dr. Vasantrao Pawar", "Role": "Former Sarchitnis / Leader", "Details": "Former Member of Parliament (Rajya Sabha, NCP)"},
      {"Name": "Adv. Nitin Thakare", "Role": "Sarchitnis (General Secretary)", "Details": "MVP Samaj Nashik"}
    ],
    "PoliticalAffiliation": "Historic Maratha Educational Society (est. 1914); governed by elected Maratha community leaders.",
    "FundingSource": "MVP Samaj trust reserves, student tuition fees, hospital clinical income.",
    "SummaryReport": "Established in 1990 in Nashik by MVP Samaj (110-year-old historic educational society). Named after former MP Dr. Vasantrao Pawar. Self-financed."
  },
  {
    "SlNo": "385",
    "CollegeName": "Bharatratna Atal Bihari Vajpayee Medical College Pune",
    "State": "Maharashtra",
    "District": "Pune",
    "University": "Maharashtra University of Health Sciences Nashik",
    "Management": "Trust",
    "ParentOrganization": "Pune Municipal Corporation Medical Education Trust (PMC Trust)",
    "KeyPeople": [{"Name": "Commissioner, PMC", "Role": "Ex-Officio Chairman", "Details": "Pune Municipal Corporation"}],
    "PoliticalAffiliation": "Government / Municipal Body Trust (Established under PMC BJP civic administration).",
    "FundingSource": "Pune Municipal Corporation civic funds & subventions, student tuition fees, Kamala Nehru Hospital infrastructure.",
    "SummaryReport": "Established in 2021 by Pune Municipal Corporation (PMC) under its civic medical trust, named after former PM Atal Bihari Vajpayee. Public-Trust model."
  },
  {
    "SlNo": "387",
    "CollegeName": "Dr. N Y Tasgaonkar Institute of Medical Science Karjat",
    "State": "Maharashtra",
    "District": "Raigad",
    "University": "Maharashtra University of Health Sciences Nashik",
    "Management": "Trust",
    "ParentOrganization": "Saraswati Education Society",
    "KeyPeople": [{"Name": "Dr. Nandkumar Y. Tasgaonkar", "Role": "Chairman", "Details": "Saraswati Education Society"}],
    "PoliticalAffiliation": "None direct / Educational trust.",
    "FundingSource": "Tuition fees, hospital earnings.",
    "SummaryReport": "Established in 2021 at Diksal, Karjat by Dr. Nandkumar Y. Tasgaonkar under Saraswati Education Society. Self-financed."
  },
  {
    "SlNo": "391",
    "CollegeName": "Datta Meghe Medical College Nagpur",
    "State": "Maharashtra",
    "District": "Nagpur",
    "University": "Datta Meghe Instt. of Medical Sciences Deemed Nagpur",
    "Management": "Private",
    "ParentOrganization": "Datta Meghe Institute of Higher Education & Research (DMIHER)",
    "KeyPeople": [
      {"Name": "Datta Meghe", "Role": "Founder", "Details": "Former Member of Parliament"},
      {"Name": "Sameer Meghe", "Role": "Trustee", "Details": "MLA (BJP, Hingna)"}
    ],
    "PoliticalAffiliation": "BJP Leader Family. Constituent of DMIHER Deemed University.",
    "FundingSource": "DMIHER deemed university fees, Shalinitai Meghe Hospital revenues.",
    "SummaryReport": "Established in 2020 at Wanadongri, Nagpur under DMIHER Deemed University. Self-financed."
  },
  {
    "SlNo": "392",
    "CollegeName": "Sindhudurg Shikshan Prasarak Mandal Medical College & Lifetime Hospital Padave Sindhudurg",
    "State": "Maharashtra",
    "District": "Sindhudurg",
    "University": "Maharashtra University of Health Sciences Nashik",
    "Management": "Trust",
    "ParentOrganization": "Sindhudurg Shikshan Prasarak Mandal (SSPM Trust)",
    "KeyPeople": [
      {"Name": "Narayan Rane", "Role": "Founder & Chairman", "Details": "Former Chief Minister of Maharashtra, Union Cabinet Minister for MSME, and sitting MP (BJP, Ratnagiri-Sindhudurg)"},
      {"Name": "Nitesh Narayan Rane", "Role": "Trustee", "Details": "Member of Legislative Assembly (BJP, Kankavli)"}
    ],
    "PoliticalAffiliation": "BJP Leader Family. Founded by former CM and Union Cabinet Minister Narayan Rane.",
    "FundingSource": "SSPM Trust funds, tuition fees, Lifetime Hospital clinical earnings.",
    "SummaryReport": "Established in 2020 at Padave, Sindhudurg by former Chief Minister & Union Minister Narayan Rane. Self-financed."
  },
  {
    "SlNo": "393",
    "CollegeName": "Symbiosis Medical College for Women Pune",
    "State": "Maharashtra",
    "District": "Pune",
    "University": "Symbiosis International Deemed University Pune",
    "Management": "Society",
    "ParentOrganization": "Symbiosis Society / Symbiosis International Deemed University",
    "KeyPeople": [
      {"Name": "Prof. Dr. S. B. Mujumdar", "Role": "Founder & Chancellor", "Details": "Padma Bhushan awardee and founder of Symbiosis"},
      {"Name": "Dr. Vidya Yeravdekar", "Role": "Pro-Chancellor", "Details": "Symbiosis International"}
    ],
    "PoliticalAffiliation": "None direct / Internationally renowned academic trust.",
    "FundingSource": "Symbiosis Deemed University fees, Symbiosis University Hospital clinical earnings.",
    "SummaryReport": "Exclusive medical college for women established in 2020 at Lavale, Pune by Dr. S. B. Mujumdar under Symbiosis International University. Self-financed."
  },
  {
    "SlNo": "396",
    "CollegeName": "Vedantaa Institute of Medical Sciences Palghar",
    "State": "Maharashtra",
    "District": "Palghar",
    "University": "Maharashtra University of Health Sciences Nashik",
    "Management": "Private",
    "ParentOrganization": "Vedantaa Institute of Medical Sciences Pvt Ltd",
    "KeyPeople": [{"Name": "Ganesh Shetty", "Role": "Chairman & Managing Director", "Details": "Vedantaa Institute"}],
    "PoliticalAffiliation": "None direct / Corporate medical institution.",
    "FundingSource": "Private promoter equity, tuition fees, hospital clinical earnings.",
    "SummaryReport": "Established in 2017 at Saswand, Dhundalwadi, Palghar district as a private corporate medical college. Self-financed."
  },
  {
    "SlNo": "398",
    "CollegeName": "Prakash Institute of Medical Sciences & Research Sangli",
    "State": "Maharashtra",
    "District": "Sangli",
    "University": "Maharashtra University of Health Sciences Nashik",
    "Management": "Trust",
    "ParentOrganization": "Nishant Educational Trust",
    "KeyPeople": [{"Name": "Prakashoset Patil", "Role": "Founder Chairman", "Details": "Prominent business and community leader"}],
    "PoliticalAffiliation": "Local political leadership standing in Sangli district.",
    "FundingSource": "Tuition fees, hospital earnings.",
    "SummaryReport": "Established in 2016 at Urun-Islampur, Sangli by Nishant Educational Trust. Self-financed."
  },
  {
    "SlNo": "401",
    "CollegeName": "B.K.L. Walawalkar Rural Medical College Ratnagiri",
    "State": "Maharashtra",
    "District": "Ratnagiri",
    "University": "Maharashtra University of Health Sciences Nashik",
    "Management": "Trust",
    "ParentOrganization": "Shri Vithalrao Joshi Charities Trust (SVJCT)",
    "KeyPeople": [
      {"Name": "Dr. Suvarnalata Patil", "Role": "Trustee & Medical Director", "Details": "SVJCT Ratnagiri"},
      {"Name": "Dadasaheb Joshi", "Role": "Founder Visionary", "Details": "SVJCT"}
    ],
    "PoliticalAffiliation": "None direct / Rural Philanthropic Trust.",
    "FundingSource": "SVJCT trust endowments, philanthropic donations, student tuition fees, hospital revenue.",
    "SummaryReport": "Established in 2015 at Kasarwadi, Dervan, Chiplun, Ratnagiri by Shri Vithalrao Joshi Charities Trust. Self-funded rural charitable trust."
  },
  {
    "SlNo": "402",
    "CollegeName": "SMBT Institute of Medical Sciences & Research Centre Nandihills Nashik",
    "State": "Maharashtra",
    "District": "Nashik",
    "University": "Maharashtra University of Health Sciences Nashik",
    "Management": "Trust",
    "ParentOrganization": "SMBT Sevabhavi Trust",
    "KeyPeople": [{"Name": "Dr. Harishchandra Navale", "Role": "Chairman", "Details": "SMBT Trust"}],
    "PoliticalAffiliation": "Local political connections in Nashik/Ahmednagar region.",
    "FundingSource": "SMBT Trust reserves, tuition fees, hospital earnings.",
    "SummaryReport": "Established in 2014 at Dhamangaon, Igatpuri, Nashik by SMBT Sevabhavi Trust. Self-financed."
  },
  {
    "SlNo": "403",
    "CollegeName": "Indian Institute of Medical Science & Research Jalna",
    "State": "Maharashtra",
    "District": "Jalna",
    "University": "Maharashtra University of Health Sciences Nashik",
    "Management": "Trust",
    "ParentOrganization": "Jamia Islamia Ishaatul Uloom Trust",
    "KeyPeople": [{"Name": "Maulana Ghulam Mohammad Vastanvi", "Role": "Founder & President", "Details": "Prominent Islamic scholar and founder of Jamia Akkalkuwa"}],
    "PoliticalAffiliation": "None direct / Leading Muslim Minority Educational Trust in Maharashtra.",
    "FundingSource": "Jamia trust funds, student tuition fees, Noor Hospital clinical earnings.",
    "SummaryReport": "Established in 2013 at Warudi, Badnapur, Jalna as a Muslim minority medical college by Jamia Islamia Ishaatul Uloom Trust. Self-financed."
  },
  {
    "SlNo": "404",
    "CollegeName": "Ashwini Rural Medical College Hospital & Research Centre Solapur",
    "State": "Maharashtra",
    "District": "Solapur",
    "University": "Maharashtra University of Health Sciences Nashik",
    "Management": "Trust",
    "ParentOrganization": "M. M. Patel Public Charitable Trust",
    "KeyPeople": [{"Name": "Dr. B. M. Patel", "Role": "Founder Chairman", "Details": "Physician and educationist"}],
    "PoliticalAffiliation": "None direct / Educational trust.",
    "FundingSource": "Tuition fees, hospital clinical income.",
    "SummaryReport": "Established in 2012 at Kumbhari, Solapur by M. M. Patel Public Charitable Trust. Self-financed."
  },
  {
    "SlNo": "405",
    "CollegeName": "Mahatma Gandhi Missions Medical College Navi Mumbai II",
    "State": "Maharashtra",
    "District": "Navi Mumbai",
    "University": "MGM Institute of Health Sciences Deemed Navi Mumbai",
    "Management": "Trust",
    "ParentOrganization": "Mahatma Gandhi Mission Trust (MGM Trust)",
    "KeyPeople": [{"Name": "Kamalkishor Kadam", "Role": "Chairman", "Details": "Former Maharashtra Education Minister"}],
    "PoliticalAffiliation": "NCP / Congress Leader. MGM Trust.",
    "FundingSource": "Deemed university tuition fees, hospital revenues.",
    "SummaryReport": "Second medical college unit established under MGM Institute of Health Sciences Deemed University in Navi Mumbai. Self-financed."
  },
  {
    "SlNo": "407",
    "CollegeName": "Dr. Rajendra Gode Medical College Amravati",
    "State": "Maharashtra",
    "District": "Amravati",
    "University": "Maharashtra University of Health Sciences Nashik",
    "Management": "Trust",
    "ParentOrganization": "Indira Bahuuddeshiya Shikshan Sanstha (IBSS)",
    "KeyPeople": [
      {"Name": "Yogendra Rajendra Gode", "Role": "President", "Details": "IBSS Amravati"},
      {"Name": "Late Dr. Rajendra Gode", "Role": "Founder", "Details": "Former Minister of State (Maharashtra)"}
    ],
    "PoliticalAffiliation": "Political Family. Founded by family of late Maharashtra Minister Dr. Rajendra Gode.",
    "FundingSource": "IBSS trust funds, tuition fees, hospital clinical income.",
    "SummaryReport": "Established in 2023 at Ghatkheda, Amravati by Indira Bahuuddeshiya Shikshan Sanstha. Self-financed."
  },
  {
    "SlNo": "408",
    "CollegeName": "Bharati Vidyapeeth University Medical College Pune",
    "State": "Maharashtra",
    "District": "Pune",
    "University": "Bharati Vidyapeeth University Deemed Pune",
    "Management": "Trust",
    "ParentOrganization": "Bharati Vidyapeeth Trust",
    "KeyPeople": [
      {"Name": "Late Dr. Patangrao Kadam", "Role": "Founder", "Details": "Former Cabinet Minister (Maharashtra, Congress)"},
      {"Name": "Dr. Shivajirao Kadam", "Role": "Chancellor", "Details": "Bharati Vidyapeeth Deemed University"}
    ],
    "PoliticalAffiliation": "Congress Leader Family. Founded by late Congress Cabinet Minister Dr. Patangrao Kadam.",
    "FundingSource": "Deemed university tuition fees, Bharati Hospital super-specialty revenues.",
    "SummaryReport": "Established in 1989 in Dhankawadi, Pune. Flagship constituent college of Bharati Vidyapeeth Deemed University. Self-financed."
  },

  # --- KERALA ---
  {
    "SlNo": "264",
    "CollegeName": "VN Public Health and Educational Trust Palakkad",
    "State": "Kerala",
    "District": "Palakkad",
    "University": "Kerala University of Health Sciences",
    "Management": "Trust",
    "ParentOrganization": "V. N. Public Health and Educational Trust",
    "KeyPeople": [{"Name": "V. N. Vasavan", "Role": "Patron / Associate", "Details": "Minister for Cooperation and Registration (Kerala, CPI-M)"}],
    "PoliticalAffiliation": "CPI-M Connections. Linked to prominent CPI(M) public trust leadership in Kerala.",
    "FundingSource": "Trust reserves, student tuition fees, hospital earnings.",
    "SummaryReport": "Medical college established in Palakkad under V. N. Public Health and Educational Trust. Self-financed."
  },
  {
    "SlNo": "265",
    "CollegeName": "Jubilee Mission Medical College & Research Institute Thrissur",
    "State": "Kerala",
    "District": "Thrissur",
    "University": "Kerala University of Health Sciences Thrissur",
    "Management": "Trust",
    "ParentOrganization": "Jubilee Mission Hospital Trust / Catholic Archdiocese of Trichur",
    "KeyPeople": [
      {"Name": "Mar Andrews Thazhath", "Role": "Patron & Archbishop", "Details": "Archbishop of Trichur and President of CBCI"},
      {"Name": "Rev. Fr. Renny Muringatheri", "Role": "Director", "Details": "Jubilee Mission"}
    ],
    "PoliticalAffiliation": "None / Catholic Church Trust.",
    "FundingSource": "Archdiocese trust endowments, tuition fees, 1600-bed super-specialty hospital revenues.",
    "SummaryReport": "Established in 2003 (hospital est. 1951) by the Catholic Archdiocese of Trichur. Non-profit Christian minority medical college. Self-funded."
  },
  {
    "SlNo": "266",
    "CollegeName": "Amala Institute of Medical Sciences Thrissur",
    "State": "Kerala",
    "District": "Thrissur",
    "University": "Kerala University of Health Sciences Thrissur",
    "Management": "Trust",
    "ParentOrganization": "CMI St. Joseph's Province (Carmelites of Mary Immaculate)",
    "KeyPeople": [{"Name": "Rev. Fr. Julius Arakkal CMI", "Role": "Director", "Details": "Amala Institute of Medical Sciences"}],
    "PoliticalAffiliation": "None / Catholic Religious Order Trust.",
    "FundingSource": "CMI congregation funds, tuition fees, cancer hospital & super-specialty revenues.",
    "SummaryReport": "Established in 2002 at Amalanagar, Thrissur by Carmelites of Mary Immaculate (CMI) Catholic order. Non-profit Christian minority college. Self-funded."
  },
  {
    "SlNo": "270",
    "CollegeName": "M E S Medical College Perintalmanna Malappuram",
    "State": "Kerala",
    "District": "Malappuram",
    "University": "Kerala University of Health Sciences Thrissur",
    "Management": "Trust",
    "ParentOrganization": "Muslim Educational Society (MES)",
    "KeyPeople": [{"Name": "Dr. P. A. Fazal Ghafoor", "Role": "President", "Details": "Prominent physician and President of Muslim Educational Society"}],
    "PoliticalAffiliation": "Independent Muslim Minority Society with active political voice in Kerala.",
    "FundingSource": "MES institutional reserves, tuition fees, super-specialty hospital revenues.",
    "SummaryReport": "Established in 2002 at Perinthalmanna, Malappuram by Muslim Educational Society led by Dr. P. A. Fazal Ghafoor. Self-financed Muslim minority college."
  },
  {
    "SlNo": "272",
    "CollegeName": "Sree Gokulam Medical College Trust & Research Foundation Trivandrum",
    "State": "Kerala",
    "District": "Thiruvananthapuram",
    "University": "Kerala University of Health Sciences Thrissur",
    "Management": "Trust",
    "ParentOrganization": "Foundation for Higher Education and Research / Sree Gokulam Group",
    "KeyPeople": [{"Name": "Gokulam Gopalan", "Role": "Chairman & Founder", "Details": "Business tycoon (Gokulam Chits & Finance), film producer, and president of Sree Narayana Dharma Paripalana (SNDP) Samrakshana Samithi"}],
    "PoliticalAffiliation": "Prominent business & community leader (SNDP Yogam background).",
    "FundingSource": "Gokulam Group business revenues, tuition fees, 1000-bed hospital clinical income.",
    "SummaryReport": "Established in 2004 at Venjaramoodu, Trivandrum by industrialist Gokulam Gopalan. Self-financed."
  },
  {
    "SlNo": "273",
    "CollegeName": "Travancore Medical College Kollam",
    "State": "Kerala",
    "District": "Kollam",
    "University": "Kerala University of Health Sciences Thrissur",
    "Management": "Trust",
    "ParentOrganization": "Quilon Medical Trust",
    "KeyPeople": [{"Name": "A. Abdul Salam", "Role": "Chairman", "Details": "Medicity Kollam"}],
    "PoliticalAffiliation": "None direct / Educational trust.",
    "FundingSource": "Tuition fees, Medicity hospital clinical income.",
    "SummaryReport": "Established in 2008 at Umayanalloor, Kollam by Quilon Medical Trust. Self-financed Muslim minority institution."
  },
  {
    "SlNo": "274",
    "CollegeName": "Sree Narayana Instt. of Medical Sciences Chalakka Ernakulam",
    "State": "Kerala",
    "District": "Ernakulam",
    "University": "Mahatma Gandhi University Kerala",
    "Management": "Trust",
    "ParentOrganization": "Sree Narayana Health Care Society",
    "KeyPeople": [{"Name": "K. R. Rajan", "Role": "Chairman", "Details": "Sree Narayana Health Care Society"}],
    "PoliticalAffiliation": "Ezhava Community Society inspired by social reformer Sree Narayana Guru.",
    "FundingSource": "Society trust reserves, tuition fees, hospital operational income.",
    "SummaryReport": "Established in 2009 at Chalakka, Ernakulam by Sree Narayana Health Care Society. Self-financed."
  },
  {
    "SlNo": "276",
    "CollegeName": "Azeezia Instt of Medical Science Meeyannoor Kollam",
    "State": "Kerala",
    "District": "Kollam",
    "University": "Kerala University of Health Sciences Thrissur",
    "Management": "Trust",
    "ParentOrganization": "Podikunju Musaliar Memorial Charitable & Educational Trust",
    "KeyPeople": [{"Name": "M. Abdul Azeez", "Role": "Chairman", "Details": "Azeezia Group of Institutions"}],
    "PoliticalAffiliation": "None direct / Muslim minority trust.",
    "FundingSource": "Group reserves, tuition fees, hospital clinical income.",
    "SummaryReport": "Established in 2008 at Meeyannoor, Kollam by Podikunju Musaliar Memorial Trust. Self-financed."
  },
  {
    "SlNo": "278",
    "CollegeName": "Kannur Medical College Kannur",
    "State": "Kerala",
    "District": "Kannur",
    "University": "Kerala University of Health Sciences Thrissur",
    "Management": "Trust",
    "ParentOrganization": "Prestige Educational Trust",
    "KeyPeople": [{"Name": "Dr. P. K. Mohamed", "Role": "Chairman", "Details": "Prestige Educational Trust"}],
    "PoliticalAffiliation": "None direct / Educational trust.",
    "FundingSource": "Tuition fees, hospital earnings.",
    "SummaryReport": "Established in 2006 at Anjarakandy, Kannur by Prestige Educational Trust. Self-financed."
  },
  {
    "SlNo": "279",
    "CollegeName": "Karuna Medical College Palakkad",
    "State": "Kerala",
    "District": "Palakkad",
    "University": "Calicut University",
    "Management": "Trust",
    "ParentOrganization": "Safe Development Alms Trust",
    "KeyPeople": [{"Name": "K. A. Rauf", "Role": "Chairman", "Details": "Industrialist"}],
    "PoliticalAffiliation": "Local business and political connections in Malabar region.",
    "FundingSource": "Trust funds, tuition fees, hospital revenue.",
    "SummaryReport": "Established in 2006 at Vilayodi, Chittur, Palakkad by Safe Development Alms Trust. Self-financed."
  },
  {
    "SlNo": "280",
    "CollegeName": "Sree Uthradom Thiurnal Academy of Medical Sciences Trivandrum",
    "State": "Kerala",
    "District": "Thiruvananthapuram",
    "University": "Kerala University of Health Sciences Thrissur",
    "Management": "Trust",
    "ParentOrganization": "Moogambigai Charitable Trust / SUT Hospital Trust",
    "KeyPeople": [{"Name": "Dr. A. C. Shanmugam", "Role": "Chairman", "Details": "Former MP and New Justice Party President"}],
    "PoliticalAffiliation": "Political Leader. Acquired and managed by Rajarajeswari / Moogambigai Group (Dr. A. C. Shanmugam).",
    "FundingSource": "Moogambigai Trust reserves, tuition fees, SUT Hospital clinical income.",
    "SummaryReport": "Established in 2006 at Vattampara, Trivandrum; managed by Moogambigai Trust (Dr. A. C. Shanmugam). Self-financed."
  },
  {
    "SlNo": "282",
    "CollegeName": "Amrita School of Medicine Elamkara Kochi",
    "State": "Kerala",
    "District": "Ernakulam",
    "University": "Amrita Vishwa Vidyapeetham Deemed Coimbatore",
    "Management": "Trust",
    "ParentOrganization": "Mata Amritanandamayi Math (MAM Trust) / Amrita Vishwa Vidyapeetham",
    "KeyPeople": [{"Name": "Mata Amritanandamayi (Amma)", "Role": "Chancellor & Founder", "Details": "World-renowned spiritual leader and humanitarian"}],
    "PoliticalAffiliation": "Global Spiritual Trust with national and international stature.",
    "FundingSource": "Mata Amritanandamayi Math endowments, global humanitarian donations, student fees, 1300-bed super-specialty hospital revenues.",
    "SummaryReport": "Established in 1998 in Kochi as constituent college of Amrita Vishwa Vidyapeetham. World-class non-profit spiritual trust medical institute. Self-funded."
  },
  {
    "SlNo": "284",
    "CollegeName": "Believers Church Medical College Hospital Thiruvalla",
    "State": "Kerala",
    "District": "Pathanamthitta",
    "University": "Kerala University of Health Sciences Thrissur",
    "Management": "Trust",
    "ParentOrganization": "Believers Eastern Church",
    "KeyPeople": [{"Name": "Moran Mor Athanasius Yohan", "Role": "Founder Metropolitan", "Details": "Late Metropolitan of Believers Eastern Church (Dr. K. P. Yohannan)"}],
    "PoliticalAffiliation": "None / Christian Missionary Church Trust.",
    "FundingSource": "Church trust reserves, tuition fees, super-specialty hospital earnings.",
    "SummaryReport": "Established in 2014 in Thiruvalla by Believers Eastern Church. Self-funded Christian minority trust."
  },
  {
    "SlNo": "286",
    "CollegeName": "Al-Azhar Medical College and Super Speciality Hospital Thodupuzha",
    "State": "Kerala",
    "District": "Idukki",
    "University": "Kerala University of Health Sciences Thrissur",
    "Management": "Trust",
    "ParentOrganization": "Human Resources Development Trust (HRD Trust)",
    "KeyPeople": [{"Name": "K. M. Moosa", "Role": "Chairman", "Details": "Al-Azhar Group of Institutions"}],
    "PoliticalAffiliation": "None direct / Muslim minority educational trust.",
    "FundingSource": "HRD Trust funds, tuition fees, hospital clinical income.",
    "SummaryReport": "Established in 2014 at Perumpillichira, Thodupuzha, Idukki by HRD Trust. Self-financed."
  },
  {
    "SlNo": "287",
    "CollegeName": "P K Das Institute of Medical Sciences Palakkad",
    "State": "Kerala",
    "District": "Palakkad",
    "University": "Kerala University of Health Sciences Thrissur",
    "Management": "Trust",
    "ParentOrganization": "Nehru College Educational and Charitable Trust",
    "KeyPeople": [
      {"Name": "Late P. K. Das", "Role": "Founder", "Details": "Founder of Nehru Group of Institutions"},
      {"Name": "Adv. Dr. P. Krishnadas", "Role": "Chairman & Managing Trustee", "Details": "Nehru Group"}
    ],
    "PoliticalAffiliation": "None direct / Major educational trust across Kerala & Tamil Nadu.",
    "FundingSource": "Nehru Group funds, tuition fees, hospital operational income.",
    "SummaryReport": "Established in 2014 at Vaniamkulam, Ottapalam, Palakkad by Nehru College Educational and Charitable Trust. Self-financed."
  },
  {
    "SlNo": "288",
    "CollegeName": "Mount Zion Medical College Chayalode Ezhamkulam Adoor Pathanamthitta",
    "State": "Kerala",
    "District": "Pathanamthitta",
    "University": "Kerala University of Health Sciences Thrissur",
    "Management": "Society",
    "ParentOrganization": "Charitable Educational Financial Society",
    "KeyPeople": [{"Name": "A. J. Abraham", "Role": "Chairman", "Details": "Mount Zion Group"}],
    "PoliticalAffiliation": "None direct / Educational society.",
    "FundingSource": "Tuition fees, hospital earnings.",
    "SummaryReport": "Established in 2014 at Adoor, Pathanamthitta by Charitable Educational Financial Society. Self-financed."
  },
  {
    "SlNo": "289",
    "CollegeName": "DM Wayanad Institute of Medical Sciences Wayanad",
    "State": "Kerala",
    "District": "Wayanad",
    "University": "Kerala University of Health Sciences Thrissur",
    "Management": "Trust",
    "ParentOrganization": "DM Education and Research Foundation (DMERF) / Aster DM Healthcare",
    "KeyPeople": [{"Name": "Dr. Azad Moopen", "Role": "Founder Chairman", "Details": "Padma Shri awardee, physician, and Founder-Chairman of Aster DM Healthcare"}],
    "PoliticalAffiliation": "None direct / Leading international healthcare group.",
    "FundingSource": "Aster DM Healthcare Foundation capital, student tuition fees, hospital clinical income.",
    "SummaryReport": "Established in 2013 at Naseera Nagar, Meppadi, Wayanad by Dr. Azad Moopen. High-quality rural medical institute self-financed through Aster DM Healthcare foundation."
  },
  {
    "SlNo": "291",
    "CollegeName": "Malabar Medical College Kozhikode Calicut",
    "State": "Kerala",
    "District": "Kozhikode",
    "University": "Kerala University of Health Sciences Thrissur",
    "Management": "Trust",
    "ParentOrganization": "Sree Anjaneya Medical Trust",
    "KeyPeople": [{"Name": "V. Anil Kumar", "Role": "Chairman", "Details": "MMC Kozhikode"}],
    "PoliticalAffiliation": "None direct / Educational trust.",
    "FundingSource": "Tuition fees, hospital earnings, promoter capital.",
    "SummaryReport": "Established in 2010 at Modakkallur, Kozhikode by Sree Anjaneya Medical Trust. Self-financed."
  },
  {
    "SlNo": "292",
    "CollegeName": "KMCT Medical College Kozhikode Calicut",
    "State": "Kerala",
    "District": "Kozhikode",
    "University": "Kerala University of Health Sciences Thrissur",
    "Management": "Trust",
    "ParentOrganization": "Kunhitharuvai Memorial Charitable Trust (KMCT)",
    "KeyPeople": [{"Name": "Dr. K. Moidu", "Role": "Founder Chairman", "Details": "KMCT Group"}],
    "PoliticalAffiliation": "None direct / Muslim minority educational trust.",
    "FundingSource": "KMCT Group funds, tuition fees, hospital clinical income.",
    "SummaryReport": "Established in 2008 at Manassery, Mukkam, Kozhikode by Dr. K. Moidu under KMCT. Self-financed Muslim minority college."
  },
  {
    "SlNo": "293",
    "CollegeName": "Dr. Somervel Memorial CSI Hospital & Medical College Karakonam Thiruvananthapuram",
    "State": "Kerala",
    "District": "Thiruvananthapuram",
    "University": "Kerala University of Health Sciences Thrissur",
    "Management": "Trust",
    "ParentOrganization": "Church of South India (CSI) South Kerala Diocese",
    "KeyPeople": [
      {"Name": "Rt. Rev. A. Dharmaraj Rasalam", "Role": "Bishop / Chairman", "Details": "CSI South Kerala Diocese"},
      {"Name": "Dr. Bennet Abraham", "Role": "Director", "Details": "Former Lok Sabha candidate"}
    ],
    "PoliticalAffiliation": "CSI Church Trust / Political connections (Director Dr. Bennet Abraham contested Lok Sabha election for CPI).",
    "FundingSource": "CSI Diocese trust funds, tuition fees, hospital clinical revenues.",
    "SummaryReport": "Established in 2002 at Karakonam, Trivandrum by CSI South Kerala Diocese. Christian minority trust medical college. Self-funded."
  },
  {
    "SlNo": "294",
    "CollegeName": "Malankara Orthodox Syrian Church Medical College Kolenchery",
    "State": "Kerala",
    "District": "Ernakulam",
    "University": "Kerala University of Health Sciences Thrissur",
    "Management": "Trust",
    "ParentOrganization": "Malankara Orthodox Syrian Church Medical Mission Society",
    "KeyPeople": [{"Name": "Baselios Marthoma Mathews III", "Role": "President & Catholicos", "Details": "Supreme Head of Malankara Orthodox Syrian Church"}],
    "PoliticalAffiliation": "None / Historic Orthodox Church Trust.",
    "FundingSource": "Orthodox Church trust endowments, tuition fees, 1100-bed super-specialty hospital earnings.",
    "SummaryReport": "Established in 2002 at Kolenchery, Ernakulam by Malankara Orthodox Syrian Church. Non-profit Christian minority medical college. Self-funded."
  },
  {
    "SlNo": "297",
    "CollegeName": "Pushpagiri Institute Of Medical Sciences and Research Centre Tiruvalla",
    "State": "Kerala",
    "District": "Pathanamthitta",
    "University": "Kerala University of Health Sciences Thrissur",
    "Management": "Trust",
    "ParentOrganization": "Pushpagiri Medical Society / Syro-Malankara Catholic Archeparchy of Tiruvalla",
    "KeyPeople": [
      {"Name": "Thomas Mar Koorilos", "Role": "Patron & Archbishop", "Details": "Archbishop of Syro-Malankara Catholic Archeparchy of Tiruvalla"},
      {"Name": "Rev. Fr. Aby Vadakkumthala", "Role": "Director", "Details": "Pushpagiri Group"}
    ],
    "PoliticalAffiliation": "None / Catholic Church Trust.",
    "FundingSource": "Archeparchy trust endowments, tuition fees, 1200-bed super-specialty hospital clinical income.",
    "SummaryReport": "Established in 2002 (hospital est. 1959) at Tiruvalla by Syro-Malankara Catholic Church. Premier non-profit Christian minority medical college. Self-funded."
  }
]

mh_kl_sources = [
  {"SlNo": "331", "CollegeName": "Mahatma Gandhi Missions Medical College Navi Mumbai", "Sources": ["https://mgmsopnm.edu.in/", "https://en.wikipedia.org/wiki/Kamalkishor_Kadam"]},
  {"SlNo": "332", "CollegeName": "Shri Ramchandra Institute of Medical Sciences Aurangabad", "Sources": ["https://srims.co.in/"]},
  {"SlNo": "342", "CollegeName": "Mahatma Gandhi Mission Medical College Vashi", "Sources": ["https://mgmmcvashi.edu.in/"]},
  {"SlNo": "344", "CollegeName": "Parbhani Medical College", "Sources": ["https://parbhanimedicalcollege.com/"]},
  {"SlNo": "348", "CollegeName": "ACPM Medical College Dhule", "Sources": ["https://acpmjmf.com/", "https://myneta.info/"]},
  {"SlNo": "350", "CollegeName": "Dr. D Y Patil Medical College Hospital and Research Centre Pimpri Pune", "Sources": ["https://medical.dpu.edu.in/", "https://en.wikipedia.org/wiki/D._Y._Patil"]},
  {"SlNo": "352", "CollegeName": "Krishna Institute of Medical Sciences Karad", "Sources": ["https://kimskarad.in/"]},
  {"SlNo": "355", "CollegeName": "Mahatma Gandhi Institute of Medical Sciences Sevagram Wardha", "Sources": ["https://mgims.ac.in/", "https://en.wikipedia.org/wiki/Sushila_Nayar"]},
  {"SlNo": "356", "CollegeName": "Bharati Vidyapeeth Deemed University Medical College & Hospital Sangli", "Sources": ["https://mcsangli.bharatividyapeeth.edu/", "https://en.wikipedia.org/wiki/Patangrao_Kadam"]},
  {"SlNo": "358", "CollegeName": "Dr. D Y Patil Medical College Kolhapur", "Sources": ["https://dypatilmedicalkop.org/", "https://en.wikipedia.org/wiki/Satej_Patil"]},
  {"SlNo": "359", "CollegeName": "Maharashtra Institute of Medical Sciences & Research Latur", "Sources": ["https://mimsr.edu.in/"]},
  {"SlNo": "364", "CollegeName": "Terna Medical College Navi Mumbai", "Sources": ["https://ternamedical.org/", "https://en.wikipedia.org/wiki/Padmasinh_Bajirao_Patil"]},
  {"SlNo": "365", "CollegeName": "Mahatma Gandhi Missions Medical College Aurangabad", "Sources": ["https://mgmmcha.org/"]},
  {"SlNo": "368", "CollegeName": "Rural Medical College Loni", "Sources": ["https://pmtpims.org/", "https://en.wikipedia.org/wiki/Radhakrishna_Vikhe_Patil"]},
  {"SlNo": "371", "CollegeName": "Maharashtra Institute of Medical Education & Research Talegaon Pune", "Sources": ["https://mimerpune.edu.in/"]},
  {"SlNo": "372", "CollegeName": "Smt. Kashibai Navale Medical College and General Hospital Pune", "Sources": ["https://sknmcgh.org/"]},
  {"SlNo": "373", "CollegeName": "KJ Somaiyya Medical College & Research Centre Mumbai", "Sources": ["https://kjsmc.somaiya.edu/en/"]},
  {"SlNo": "374", "CollegeName": "N. K. P. Salve Instt. of Medical Sciences and Research Centre and Lata Mangeshkar Hospital Nagpur", "Sources": ["https://nkpsims.edu.in/", "https://en.wikipedia.org/wiki/N._K._P._Salve"]},
  {"SlNo": "375", "CollegeName": "Dr. Vithalrao Vikhe Patil Foundations Medical College & Hospital Ahmednagar", "Sources": ["https://vpmrvh.edu.in/"]},
  {"SlNo": "376", "CollegeName": "Padmashree Dr. D.Y.Patil Medical College Navi Mumbai", "Sources": ["https://dypatil.edu/"]},
  {"SlNo": "380", "CollegeName": "Dr. Panjabrao Alias Bhausaheb Deshmukh Memorial Medical College Amravati", "Sources": ["https://pdmmc.edu.in/", "https://en.wikipedia.org/wiki/Panjabrao_Deshmukh"]},
  {"SlNo": "382", "CollegeName": "Dr. Ulhas Patil Medical College & Hospital Jalgaon", "Sources": ["https://dupmc.ac.in/"]},
  {"SlNo": "383", "CollegeName": "Jawaharlal Nehru Medical College Sawangi Meghe Wardha", "Sources": ["https://dmiher.edu.in/", "https://en.wikipedia.org/wiki/Datta_Meghe"]},
  {"SlNo": "384", "CollegeName": "Dr. Vasantrao Pawar Medical College Hospital & Research Centre Nasik", "Sources": ["https://drvasantraopawarmedicalcollege.in/", "https://mvp.edu.in/"]},
  {"SlNo": "385", "CollegeName": "Bharatratna Atal Bihari Vajpayee Medical College Pune", "Sources": ["https://pmc.gov.in/"]},
  {"SlNo": "387", "CollegeName": "Dr. N Y Tasgaonkar Institute of Medical Science Karjat", "Sources": ["https://nytims.edu.in/"]},
  {"SlNo": "391", "CollegeName": "Datta Meghe Medical College Nagpur", "Sources": ["https://dmmcnagpur.com/"]},
  {"SlNo": "392", "CollegeName": "Sindhudurg Shikshan Prasarak Mandal Medical College & Lifetime Hospital Padave Sindhudurg", "Sources": ["https://sspmmedcol.ac.in/", "https://en.wikipedia.org/wiki/Narayan_Rane"]},
  {"SlNo": "393", "CollegeName": "Symbiosis Medical College for Women Pune", "Sources": ["https://smcw.edu.in/"]},
  {"SlNo": "396", "CollegeName": "Vedantaa Institute of Medical Sciences Palghar", "Sources": ["https://vedantaa.institute/"]},
  {"SlNo": "398", "CollegeName": "Prakash Institute of Medical Sciences & Research Sangli", "Sources": ["https://pims.ac.in/"]},
  {"SlNo": "401", "CollegeName": "B.K.L. Walawalkar Rural Medical College Ratnagiri", "Sources": ["https://bklwrmc.com/"]},
  {"SlNo": "402", "CollegeName": "SMBT Institute of Medical Sciences & Research Centre Nandihills Nashik", "Sources": ["https://smbt.edu.in/"]},
  {"SlNo": "403", "CollegeName": "Indian Institute of Medical Science & Research Jalna", "Sources": ["https://iimsr.co.in/"]},
  {"SlNo": "404", "CollegeName": "Ashwini Rural Medical College Hospital & Research Centre Solapur", "Sources": ["https://armch.org.in/"]},
  {"SlNo": "405", "CollegeName": "Mahatma Gandhi Missions Medical College Navi Mumbai II", "Sources": ["https://mgmims.ac.in/"]},
  {"SlNo": "407", "CollegeName": "Dr. Rajendra Gode Medical College Amravati", "Sources": ["https://drgodehospital.org/"]},
  {"SlNo": "408", "CollegeName": "Bharati Vidyapeeth University Medical College Pune", "Sources": ["https://mcpune.bharatividyapeeth.edu/"]},

  {"SlNo": "264", "CollegeName": "VN Public Health and Educational Trust Palakkad", "Sources": ["https://vntrust.in/"]},
  {"SlNo": "265", "CollegeName": "Jubilee Mission Medical College & Research Institute Thrissur", "Sources": ["https://jubileemission.org/"]},
  {"SlNo": "266", "CollegeName": "Amala Institute of Medical Sciences Thrissur", "Sources": ["https://amalaims.org/"]},
  {"SlNo": "270", "CollegeName": "M E S Medical College Perintalmanna Malappuram", "Sources": ["https://mesmc.in/"]},
  {"SlNo": "272", "CollegeName": "Sree Gokulam Medical College Trust & Research Foundation Trivandrum", "Sources": ["https://sgmc.in/"]},
  {"SlNo": "273", "CollegeName": "Travancore Medical College Kollam", "Sources": ["https://tmc.ac.in/"]},
  {"SlNo": "274", "CollegeName": "Sree Narayana Instt. of Medical Sciences Chalakka Ernakulam", "Sources": ["https://snims.org/"]},
  {"SlNo": "276", "CollegeName": "Azeezia Instt of Medical Science Meeyannoor Kollam", "Sources": ["https://azeezia.com/"]},
  {"SlNo": "278", "CollegeName": "Kannur Medical College Kannur", "Sources": ["https://kannurmedicalcollege.ac.in/"]},
  {"SlNo": "279", "CollegeName": "Karuna Medical College Palakkad", "Sources": ["https://karumedcol.org/"]},
  {"SlNo": "280", "CollegeName": "Sree Uthradom Thiurnal Academy of Medical Sciences Trivandrum", "Sources": ["https://sutams.edu.in/"]},
  {"SlNo": "282", "CollegeName": "Amrita School of Medicine Elamkara Kochi", "Sources": ["https://amrita.edu/school/medicine/kochi/"]},
  {"SlNo": "284", "CollegeName": "Believers Church Medical College Hospital Thiruvalla", "Sources": ["https://bcmch.org/"]},
  {"SlNo": "286", "CollegeName": "Al-Azhar Medical College and Super Speciality Hospital Thodupuzha", "Sources": ["https://alazhar.in/medicalcollege/"]},
  {"SlNo": "287", "CollegeName": "P K Das Institute of Medical Sciences Palakkad", "Sources": ["https://pkdims.org/"]},
  {"SlNo": "288", "CollegeName": "Mount Zion Medical College Chayalode Ezhamkulam Adoor Pathanamthitta", "Sources": ["https://mountzionmedicalcollege.com/"]},
  {"SlNo": "289", "CollegeName": "DM Wayanad Institute of Medical Sciences Wayanad", "Sources": ["https://dmwims.com/"]},
  {"SlNo": "291", "CollegeName": "Malabar Medical College Kozhikode Calicut", "Sources": ["https://mmc.ac.in/"]},
  {"SlNo": "292", "CollegeName": "KMCT Medical College Kozhikode Calicut", "Sources": ["https://kmctmedicalcollege.org/"]},
  {"SlNo": "293", "CollegeName": "Dr. Somervel Memorial CSI Hospital & Medical College Karakonam Thiruvananthapuram", "Sources": ["https://smcsimc.ac.in/"]},
  {"SlNo": "294", "CollegeName": "Malankara Orthodox Syrian Church Medical College Kolenchery", "Sources": ["https://moscmc.org/"]},
  {"SlNo": "297", "CollegeName": "Pushpagiri Institute Of Medical Sciences and Research Centre Tiruvalla", "Sources": ["https://pushpagiri.in/"]}
]

own.extend(mh_kl_records)
src.extend(mh_kl_sources)

save_db(own, src)
