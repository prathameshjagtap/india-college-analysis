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

tn_py_records = [
  # --- TAMIL NADU ---
  {
    "SlNo": "503",
    "CollegeName": "J R Medical College and Hospital Villupuram",
    "State": "Tamil Nadu",
    "District": "Villupuram",
    "University": "Bharath Institute of Higher Education & Research Deemed",
    "Management": "Society",
    "ParentOrganization": "Bharath Institute of Higher Education & Research (BIHER) / Sri Chockalingam Trust",
    "KeyPeople": [{"Name": "Dr. S. Jagathrakshakan", "Role": "Founder & Managing Trustee", "Details": "Member of Parliament (DMK, Arakkonam) and former Union Minister of State"}],
    "PoliticalAffiliation": "DMK Leader. Founder Dr. S. Jagathrakshakan is a senior DMK MP and former Union Minister.",
    "FundingSource": "BIHER Deemed University tuition fees, hospital clinical income, promoter group capital.",
    "SummaryReport": "Constituent medical college of BIHER Deemed University, established by DMK MP Dr. S. Jagathrakshakan. Self-financed."
  },
  {
    "SlNo": "504",
    "CollegeName": "Kanyakumari Medical Mission Research Centre Kanyakumari",
    "State": "Tamil Nadu",
    "District": "Kanyakumari",
    "University": "St. Joseph's University",
    "Management": "Trust",
    "ParentOrganization": "Kanyakumari Medical Mission / CSI Kanyakumari Diocese",
    "KeyPeople": [{"Name": "Rt. Rev. A.R. Chelliah", "Role": "Bishop / Chairman", "Details": "CSI Kanyakumari Diocese"}],
    "PoliticalAffiliation": "None identified / Christian Minority Trust.",
    "FundingSource": "Church diocese trust funds, student tuition fees, charitable hospital receipts.",
    "SummaryReport": "Christian minority medical college managed by Church of South India (CSI) Kanyakumari Diocese. Self-funded."
  },
  {
    "SlNo": "505",
    "CollegeName": "Nandha Medical College & Hospital Erode",
    "State": "Tamil Nadu",
    "District": "Erode",
    "University": "The Tamilnadu Dr. MGR Medical University Chennai",
    "Management": "Trust",
    "ParentOrganization": "Sri Nandha Educational Trust",
    "KeyPeople": [{"Name": "V. Shanmugan", "Role": "Chairman", "Details": "Nandha Educational Institutions"}],
    "PoliticalAffiliation": "None direct / Educational trust in Western Tamil Nadu.",
    "FundingSource": "Tuition fees, hospital earnings.",
    "SummaryReport": "Established at Pitchandampalayam, Erode by Sri Nandha Educational Trust. Self-financed."
  },
  {
    "SlNo": "506",
    "CollegeName": "Dhanalakshmi Srinivasan Institute of Medical Sciences and Hospital Perambalur",
    "State": "Tamil Nadu",
    "District": "Perambalur",
    "University": "Dhanalakshmi Srinivasan Institute of Science and Research Deemed",
    "Management": "Trust",
    "ParentOrganization": "Dhanalakshmi Srinivasan Educational Trust",
    "KeyPeople": [{"Name": "A. Srinivasan", "Role": "Founder Chairman", "Details": "Dhanalakshmi Srinivasan Group"}],
    "PoliticalAffiliation": "Prominent educational & industrial group in Central Tamil Nadu.",
    "FundingSource": "DS Group revenues, tuition fees, hospital clinical income.",
    "SummaryReport": "Established in Perambalur by A. Srinivasan under Dhanalakshmi Srinivasan Educational Trust. Self-financed."
  },
  {
    "SlNo": "508",
    "CollegeName": "Sree Balaji Medical College and Hospital Chennai",
    "State": "Tamil Nadu",
    "District": "Chennai",
    "University": "Bharath Institute of Higher Education & Research Deemed Chennai",
    "Management": "Trust",
    "ParentOrganization": "Sri Chockalingam Trust / BIHER Deemed University",
    "KeyPeople": [
      {"Name": "Dr. S. Jagathrakshakan", "Role": "Founder", "Details": "Member of Parliament (DMK) and former Union Minister"},
      {"Name": "J. Sundeep Anand", "Role": "President", "Details": "BIHER Group"}
    ],
    "PoliticalAffiliation": "DMK Leader Family. Founded by DMK MP Dr. S. Jagathrakshakan.",
    "FundingSource": "BIHER tuition fees, hospital clinical earnings, group revenues.",
    "SummaryReport": "Established in 2003 at Chromepet, Chennai by DMK MP Dr. S. Jagathrakshakan under Sri Chockalingam Trust. Constituent of BIHER Deemed University. Self-financed."
  },
  {
    "SlNo": "509",
    "CollegeName": "PSP Medical College Hospital and Research Institute Chennai",
    "State": "Tamil Nadu",
    "District": "Kanchipuram",
    "University": "The Tamilnadu Dr. MGR Medical University Chennai",
    "Management": "Trust",
    "ParentOrganization": "PSP Educational Trust",
    "KeyPeople": [{"Name": "P. S. P. K. Shanmugam", "Role": "Chairman", "Details": "PSP Educational Group"}],
    "PoliticalAffiliation": "None identified / Educational trust.",
    "FundingSource": "Tuition fees, hospital earnings.",
    "SummaryReport": "Medical college near Chennai operated by PSP Educational Trust. Self-financed."
  },
  {
    "SlNo": "510",
    "CollegeName": "Rajah Muthiah Medical College Annamalainagar",
    "State": "Tamil Nadu",
    "District": "Cuddalore",
    "University": "Annamalai University",
    "Management": "Trust",
    "ParentOrganization": "Annamalai University (Historically Raja Sir Annamalai Chettiar Trust, transitioned to State University governance)",
    "KeyPeople": [{"Name": "Dr. M. A. M. Ramaswamy", "Role": "Historical Founder", "Details": "Late Pro-Chancellor of Annamalai University and industrialist"}],
    "PoliticalAffiliation": "Transitioned to State Administration. Originally established by Chettinad royal trust, taken over by Tamil Nadu Government.",
    "FundingSource": "State government subventions, student fees, teaching hospital services.",
    "SummaryReport": "Established in 1980 by Chettinad royal family under Annamalai University; transitioned to state government management under Tamil Nadu Health Department."
  },
  {
    "SlNo": "512",
    "CollegeName": "Karpaga Vinayaga Institute of Medical Sciences Maduranthagam",
    "State": "Tamil Nadu",
    "District": "Chengalpattu",
    "University": "The Tamilnadu Dr. MGR Medical University Chennai",
    "Management": "Trust",
    "ParentOrganization": "Karpaga Vinayaga Educational Trust",
    "KeyPeople": [{"Name": "S. Regupathy", "Role": "Founder & Managing Trustee", "Details": "Minister for Law, Courts and Prisons (Tamil Nadu, DMK) and MLA (Viralimalai)"}],
    "PoliticalAffiliation": "DMK Cabinet Minister. Founded by S. Regupathy, senior DMK Cabinet Minister.",
    "FundingSource": "Tuition fees, hospital operational revenues, trust capital.",
    "SummaryReport": "Established in 2009 at Maduranthakam by DMK Law Minister S. Regupathy under Karpaga Vinayaga Educational Trust. Self-financed."
  },
  {
    "SlNo": "513",
    "CollegeName": "Shri Sathya Sai Medical College and Research Institute Kancheepuram",
    "State": "Tamil Nadu",
    "District": "Chengalpattu",
    "University": "Sri Balaji Vidyapeeth Deemed University Pondicherry",
    "Management": "Trust",
    "ParentOrganization": "Sri Balaji Vidyapeeth Deemed University / Sri Selva Vinayakar Trust",
    "KeyPeople": [{"Name": "M. K. Rajagopalan", "Role": "Chancellor", "Details": "Educational entrepreneur and Chancellor of Sri Balaji Vidyapeeth"}],
    "PoliticalAffiliation": "None direct / Educational conglomerate.",
    "FundingSource": "Deemed university tuition fees, super-specialty hospital revenues.",
    "SummaryReport": "Established in 2008 at Ammapettai, Chengalpattu as a constituent college of Sri Balaji Vidyapeeth Deemed University. Self-financed."
  },
  {
    "SlNo": "514",
    "CollegeName": "PSG Institute of Medical Sciences Coimbatore",
    "State": "Tamil Nadu",
    "District": "Coimbatore",
    "University": "The Tamilnadu Dr. MGR Medical University Chennai",
    "Management": "Trust",
    "ParentOrganization": "PSG & Sons' Charities",
    "KeyPeople": [
      {"Name": "L. Gopalakrishnan", "Role": "Managing Trustee", "Details": "PSG & Sons' Charities"},
      {"Name": "PSG Family", "Role": "Founders", "Details": "Historic industrial and philanthropic family of Coimbatore"}
    ],
    "PoliticalAffiliation": "None direct / Historic philanthropic and industrial trust of Western Tamil Nadu.",
    "FundingSource": "PSG Charities trust endowments, student tuition fees, 1400-bed super-specialty hospital income.",
    "SummaryReport": "Established in 1985 in Peelamedu, Coimbatore by PSG & Sons' Charities (est. 1926). Highly respected non-profit educational trust medical college. Self-funded."
  },
  {
    "SlNo": "516",
    "CollegeName": "Christian Medical College Vellore",
    "State": "Tamil Nadu",
    "District": "Vellore",
    "University": "The Tamilnadu Dr. MGR Medical University Chennai",
    "Management": "Trust",
    "ParentOrganization": "Christian Medical College Vellore Association (CMC Vellore Society)",
    "KeyPeople": [
      {"Name": "Dr. Ida S. Scudder", "Role": "Founder", "Details": "Pioneer medical missionary"},
      {"Name": "Dr. Vikram Mathews", "Role": "Director", "Details": "CMC Vellore"}
    ],
    "PoliticalAffiliation": "None / Globally renowned Christian Charitable Institution.",
    "FundingSource": "Philanthropic medical association funds, subsidized student fees, clinical hospital revenues, international research grants.",
    "SummaryReport": "Founded in 1900 by Dr. Ida Scudder. Globally acclaimed non-profit Christian minority medical institution governed by an inter-denominational council of 50+ churches. Self-funded."
  },
  {
    "SlNo": "523",
    "CollegeName": "Chettinad Hospital & Research Institute Kanchipuram",
    "State": "Tamil Nadu",
    "District": "Chengalpattu",
    "University": "Chettinad Academy of Research and Education Deemed",
    "Management": "Trust",
    "ParentOrganization": "Raja Sir M. A. Muthiah Chettiar Charitable Trust / Chettinad Group",
    "KeyPeople": [{"Name": "M. A. M. R. Muthiah", "Role": "Managing Trustee", "Details": "Industrialist and head of Chettinad Group"}],
    "PoliticalAffiliation": "None direct / Historic Chettinad industrial house.",
    "FundingSource": "Chettinad Group corporate revenues, deemed university tuition fees, super-specialty hospital earnings.",
    "SummaryReport": "Established in 2006 at Kelambakkam by Chettinad Group under Raja Sir M. A. Muthiah Chettiar Trust. Constituent of CARE Deemed University. Self-financed."
  },
  {
    "SlNo": "524",
    "CollegeName": "Sree Mookambika Institute of Medical Sciences Kanyakumari",
    "State": "Tamil Nadu",
    "District": "Kanyakumari",
    "University": "The Tamilnadu Dr. MGR Medical University Chennai",
    "Management": "Trust",
    "ParentOrganization": "Velayudhan Memorial Trust",
    "KeyPeople": [{"Name": "Dr. C. V. Velayudhan", "Role": "Chairman", "Details": "Physician and founder of SMIMS"}],
    "PoliticalAffiliation": "None direct / Educational trust.",
    "FundingSource": "Tuition fees, hospital earnings.",
    "SummaryReport": "Established in 2006 at Kulasekharam, Kanyakumari district by Velayudhan Memorial Trust. Self-financed."
  },
  {
    "SlNo": "526",
    "CollegeName": "Sri Ramachandra Medical College & Research Institute Chennai",
    "State": "Tamil Nadu",
    "District": "Chennai",
    "University": "Sri Ramachandra Institute of Higher Education & Research Deemed Chennai",
    "Management": "Trust",
    "ParentOrganization": "Sri Ramachandra Educational and Health Trust",
    "KeyPeople": [
      {"Name": "Late N. P. V. Ramasamy Udayar", "Role": "Founder", "Details": "Prominent industrialist and educationist"},
      {"Name": "V. R. Venkataachalam", "Role": "Chancellor", "Details": "Sri Ramachandra Deemed University"}
    ],
    "PoliticalAffiliation": "Historical political connections across Tamil Nadu parties.",
    "FundingSource": "Deemed university tuition fees, 1500-bed super-specialty hospital revenue, research grants.",
    "SummaryReport": "Established in 1985 at Porur, Chennai by N. P. V. Ramasamy Udayar. Premier deemed university medical college. Self-financed."
  },
  {
    "SlNo": "528",
    "CollegeName": "Vinayaka Missions Kirupananda Variyar Medical College Salem",
    "State": "Tamil Nadu",
    "District": "Salem",
    "University": "Vinayaka Missions University Deemed Salem",
    "Management": "Trust",
    "ParentOrganization": "Thirumuruga Kirupananda Variyar Thavathiru Sundara Swamigal Medical Educational Trust",
    "KeyPeople": [
      {"Name": "Late Dr. A. Shanmugasundaram", "Role": "Founder Chancellor", "Details": "Founder of Vinayaka Missions Research Foundation"},
      {"Name": "Dato' Sri Dr. S. Sharavanan", "Role": "Pro-Chancellor", "Details": "VMRF Group"}
    ],
    "PoliticalAffiliation": "None direct / Major educational trust in Western Tamil Nadu.",
    "FundingSource": "VMRF deemed university fees, hospital revenues.",
    "SummaryReport": "Established in 1995 in Salem by Dr. A. Shanmugasundaram. Constituent college of Vinayaka Missions Research Foundation Deemed University. Self-financed."
  },
  {
    "SlNo": "530",
    "CollegeName": "Meenakshi Medical College and Research Institute Enathur",
    "State": "Tamil Nadu",
    "District": "Kanchipuram",
    "University": "Meenakshi University Deemed Chennai",
    "Management": "Trust",
    "ParentOrganization": "Meenakshi Ammal Trust",
    "KeyPeople": [{"Name": "A. N. Radhakrishnan", "Role": "Chancellor", "Details": "Meenakshi Academy of Higher Education and Research"}],
    "PoliticalAffiliation": "None direct / Private educational trust.",
    "FundingSource": "MAHER deemed university fees, hospital clinical earnings.",
    "SummaryReport": "Established in 2003 at Enathur, Kanchipuram by Meenakshi Ammal Trust. Constituent of MAHER Deemed University. Self-financed."
  },
  {
    "SlNo": "531",
    "CollegeName": "Tagore Medical College and Hospital Chennai",
    "State": "Tamil Nadu",
    "District": "Chennai",
    "University": "The Tamilnadu Dr. MGR Medical University Chennai",
    "Management": "Trust",
    "ParentOrganization": "Southern Educational and Educational Trust",
    "KeyPeople": [{"Name": "Prof. M. Mala", "Role": "Chairperson", "Details": "Tagore Educational Group"}],
    "PoliticalAffiliation": "None direct / Private educational trust.",
    "FundingSource": "Tuition fees, hospital operational income.",
    "SummaryReport": "Established in 2010 at Rathinamangalam, Chennai by Southern Educational Trust. Self-financed."
  },
  {
    "SlNo": "537",
    "CollegeName": "Saveetha Medical College and Hospital Kanchipuram",
    "State": "Tamil Nadu",
    "District": "Tiruvallur",
    "University": "Saveetha University Deemed Chennai",
    "Management": "Trust",
    "ParentOrganization": "Saveetha Institute of Medical and Technical Sciences (SIMATS Deemed)",
    "KeyPeople": [{"Name": "Dr. N. M. Veeraiyan", "Role": "Founder & Chancellor", "Details": "Dentist and founder of Saveetha Group"}],
    "PoliticalAffiliation": "None direct / Educational conglomerate.",
    "FundingSource": "SIMATS deemed university tuition fees, super-specialty hospital clinical income.",
    "SummaryReport": "Established in 2008 at Thandalam, Chennai by Dr. N. M. Veeraiyan. Constituent of SIMATS Deemed University. Self-financed."
  },
  {
    "SlNo": "540",
    "CollegeName": "Swamy Vivekanandha Medical College Hospital And Research Institute Namakkal",
    "State": "Tamil Nadu",
    "District": "Namakkal",
    "University": "The Tamilnadu Dr. MGR Medical University Chennai",
    "Management": "Trust",
    "ParentOrganization": "Rabindhranath Tagore Educational Charitable Trust",
    "KeyPeople": [{"Name": "Prof. Dr. M. Karunanithi", "Role": "Chairman & Secretary", "Details": "Vivekanandha Educational Institutions"}],
    "PoliticalAffiliation": "None direct / Leading women's and professional education group in Kongu region.",
    "FundingSource": "Vivekanandha Group funds, tuition fees, hospital earnings.",
    "SummaryReport": "Established in 2021 at Elayampalayam, Namakkal by Rabindhranath Tagore Educational Trust. Self-financed."
  },
  {
    "SlNo": "542",
    "CollegeName": "Arunai Medical College And Hospital Tiruvannamalai",
    "State": "Tamil Nadu",
    "District": "Tiruvannamalai",
    "University": "The Tamilnadu Dr. MGR Medical University Chennai",
    "Management": "Trust",
    "ParentOrganization": "Arunai Educational Trust",
    "KeyPeople": [{"Name": "E. V. Velu", "Role": "Founder & Chairman", "Details": "Cabinet Minister for Public Works, Buildings & Highways (Tamil Nadu, DMK) and MLA (Tiruvannamalai)"}],
    "PoliticalAffiliation": "DMK Cabinet Minister. Founded by senior DMK Minister E. V. Velu.",
    "FundingSource": "Promoter trust funds, tuition fees, hospital operational income.",
    "SummaryReport": "Established in 2021 in Tiruvannamalai by DMK Public Works Minister E. V. Velu under Arunai Educational Trust. Self-financed."
  },
  {
    "SlNo": "547",
    "CollegeName": "Srinivasan Medical College and Hospital Tiruchirappalli",
    "State": "Tamil Nadu",
    "District": "Tiruchirappalli",
    "University": "Dhanalakshmi Srinivasan University",
    "Management": "Trust",
    "ParentOrganization": "Dhanalakshmi Srinivasan Educational Trust",
    "KeyPeople": [{"Name": "A. Srinivasan", "Role": "Chancellor", "Details": "Dhanalakshmi Srinivasan University"}],
    "PoliticalAffiliation": "Prominent educational group in Central TN.",
    "FundingSource": "University tuition fees, hospital revenues.",
    "SummaryReport": "Established at Samayapuram, Trichy under Dhanalakshmi Srinivasan University. Self-financed."
  },
  {
    "SlNo": "548",
    "CollegeName": "Faculty of Medicine Sri Lalithambigai Medical College and Hospital Chennai",
    "State": "Tamil Nadu",
    "District": "Chennai",
    "University": "Dr. MGR Educational and Research Institute Deemed Chennai",
    "Management": "Trust",
    "ParentOrganization": "Thai Moogambigai Educational and Charitable Trust",
    "KeyPeople": [{"Name": "Dr. A. C. Shanmugam", "Role": "Founder & Chancellor", "Details": "Former MP and New Justice Party President"}],
    "PoliticalAffiliation": "Political Leader. Managed by Dr. A. C. Shanmugam (former MP).",
    "FundingSource": "Deemed university tuition fees, hospital earnings.",
    "SummaryReport": "Established at Anekal, Chennai under Dr. M.G.R. Educational and Research Institute Deemed University. Self-financed."
  },
  {
    "SlNo": "549",
    "CollegeName": "VELS Medical College & Hospital Tiruvallur",
    "State": "Tamil Nadu",
    "District": "Tiruvallur",
    "University": "Vels Institute Of Science Technology & Advanced Studies Deemed",
    "Management": "Trust",
    "ParentOrganization": "Vels Educational Trust / VISTAS Deemed University",
    "KeyPeople": [{"Name": "Dr. Ishari K. Ganesh", "Role": "Founder & Chancellor", "Details": "Film producer, actor, and politician (Vice President of AIADMK-allied front / MGR Kazhagam background)"}],
    "PoliticalAffiliation": "Political/Media Stature. Chancellor Dr. Ishari K. Ganesh has active political and film industry prominent standing.",
    "FundingSource": "Vels Group revenues, deemed university fees, hospital earnings.",
    "SummaryReport": "Established in 2021 at Periyapalayam, Tiruvallur by Dr. Ishari K. Ganesh under Vels Educational Trust. Self-financed."
  },
  {
    "SlNo": "554",
    "CollegeName": "ST Peters Medical College Hospital & Research Institute Hosur",
    "State": "Tamil Nadu",
    "District": "Krishnagiri",
    "University": "The Tamilnadu Dr. MGR Medical University Chennai",
    "Management": "Trust",
    "ParentOrganization": "St. Peter's Institute of Higher Education and Research Trust",
    "KeyPeople": [
      {"Name": "Dr. T. Banumathi", "Role": "Chairperson", "Details": "St. Peter's Educational Trust"},
      {"Name": "M. Thambidurai", "Role": "Patron / Associate", "Details": "Member of Parliament (Rajya Sabha, AIADMK) and former Deputy Speaker of Lok Sabha"}
    ],
    "PoliticalAffiliation": "AIADMK Leader Family. Associated with family of senior AIADMK MP and former Deputy Speaker M. Thambidurai.",
    "FundingSource": "St. Peter's Group funds, tuition fees, hospital clinical income.",
    "SummaryReport": "Established in 2021 in Hosur by St. Peter's Trust, connected to senior AIADMK leader M. Thambidurai. Self-financed."
  },
  {
    "SlNo": "555",
    "CollegeName": "Indira Medical College & Hospitals Thiruvallur",
    "State": "Tamil Nadu",
    "District": "Tiruvallur",
    "University": "The Tamilnadu Dr. MGR Medical University Chennai",
    "Management": "Private",
    "ParentOrganization": "Indira Educational and Charitable Trust",
    "KeyPeople": [{"Name": "VG Raajendran", "Role": "Chairman", "Details": "Member of Legislative Assembly (DMK, Tiruvallur)"}],
    "PoliticalAffiliation": "DMK MLA. Founded by VG Raajendran, sitting DMK MLA for Tiruvallur constituency.",
    "FundingSource": "Indira Group funds, student tuition fees, hospital revenues.",
    "SummaryReport": "Established in 2020 at Pandur, Tiruvallur by sitting DMK MLA VG Raajendran. Self-financed."
  },
  {
    "SlNo": "556",
    "CollegeName": "Bhaarat Medical College & Hospital Chennai",
    "State": "Tamil Nadu",
    "District": "Chennai",
    "University": "Bharath Institute of Higher Education & Research Deemed Chennai",
    "Management": "Trust",
    "ParentOrganization": "Sri Chockalingam Trust / BIHER Deemed University",
    "KeyPeople": [{"Name": "Dr. S. Jagathrakshakan", "Role": "Founder", "Details": "Member of Parliament (DMK)"}],
    "PoliticalAffiliation": "DMK Leader. Constituent of BIHER Deemed University founded by DMK MP Dr. S. Jagathrakshakan.",
    "FundingSource": "BIHER tuition fees, hospital operational revenues.",
    "SummaryReport": "Established in 2020 at Selaiyur, Chennai as part of BIHER Deemed University network. Self-financed."
  },
  {
    "SlNo": "557",
    "CollegeName": "Panimalar Medical College Hospital & Research Institute Chennai",
    "State": "Tamil Nadu",
    "District": "Tiruvallur",
    "University": "The Tamilnadu Dr. MGR Medical University Chennai",
    "Management": "Trust",
    "ParentOrganization": "Jaisakthi Educational Trust",
    "KeyPeople": [{"Name": "Dr. P. Chinnadurai", "Role": "Chairman & Managing Trustee", "Details": "Panimalar Educational Institutions"}],
    "PoliticalAffiliation": "None direct / Major Christian/Christian-allied educational group.",
    "FundingSource": "Panimalar Group reserves, tuition fees, hospital clinical income.",
    "SummaryReport": "Established in 2020 at Varadharajapuram, Chennai by Dr. P. Chinnadurai under Jaisakthi Educational Trust. Self-financed."
  },
  {
    "SlNo": "558",
    "CollegeName": "KMCH Institute of Health Sciences and Research Coimbatore",
    "State": "Tamil Nadu",
    "District": "Coimbatore",
    "University": "The Tamilnadu Dr. MGR Medical University Chennai",
    "Management": "Private",
    "ParentOrganization": "Kovai Medical Center and Hospital Limited (KMCH Corporate Hospital)",
    "KeyPeople": [{"Name": "Dr. Nalla G. Palaniswami", "Role": "Chairman & Managing Director", "Details": "Physician, industrialist and founder of KMCH"}],
    "PoliticalAffiliation": "None direct / Corporate hospital company listed on BSE.",
    "FundingSource": "KMCH Ltd corporate revenues, student tuition fees, clinical hospital income.",
    "SummaryReport": "Established in 2019 in Coimbatore by Kovai Medical Center and Hospital Ltd (KMCH). Self-financed corporate healthcare institution."
  },
  {
    "SlNo": "564",
    "CollegeName": "Velammal Medical College Hospital and Research Institute Madurai",
    "State": "Tamil Nadu",
    "District": "Madurai",
    "University": "The Tamilnadu Dr. MGR Medical University Chennai",
    "Management": "Trust",
    "ParentOrganization": "Velammal Educational Trust",
    "KeyPeople": [{"Name": "M. V. Muthuramalingam", "Role": "Chairman", "Details": "Velammal Educational Group"}],
    "PoliticalAffiliation": "None direct / Prominent educational group across Tamil Nadu.",
    "FundingSource": "Velammal Group funds, tuition fees, hospital earnings.",
    "SummaryReport": "Established in 2013 at Anuppanadi, Madurai by M. V. Muthuramalingam under Velammal Educational Trust. Self-financed."
  },
  {
    "SlNo": "567",
    "CollegeName": "Karpagam Faculty of Medical Sciences & Research Coimbatore",
    "State": "Tamil Nadu",
    "District": "Coimbatore",
    "University": "The Tamilnadu Dr. MGR Medical University Chennai",
    "Management": "Trust",
    "ParentOrganization": "Karpagam Educational Trust",
    "KeyPeople": [{"Name": "Dr. S. Sudalaimuthu", "Role": "Chairman", "Details": "Karpagam Institutions"}],
    "PoliticalAffiliation": "None direct / Private educational trust.",
    "FundingSource": "Karpagam Group funds, tuition fees, hospital clinical income.",
    "SummaryReport": "Established in 2012 at Othakkalmandapam, Coimbatore by Karpagam Educational Trust. Self-financed."
  },
  {
    "SlNo": "568",
    "CollegeName": "Madha Medical College and Hospital Thandalam Chennai",
    "State": "Tamil Nadu",
    "District": "Kanchipuram",
    "University": "The Tamilnadu Dr. MGR Medical University Chennai",
    "Management": "Trust",
    "ParentOrganization": "Soosaiya Peter Educational Trust",
    "KeyPeople": [{"Name": "S. Peter", "Role": "Founder & Chairman", "Details": "Madha Group of Academic Institutions"}],
    "PoliticalAffiliation": "None identified / Christian Minority Trust.",
    "FundingSource": "Madha Group trust funds, student fees, hospital revenue.",
    "SummaryReport": "Established in 2011 at Kundrathur, Chennai as a Christian minority medical college operated by Soosaiya Peter Educational Trust. Self-financed."
  },
  {
    "SlNo": "569",
    "CollegeName": "Annapoorna Medical College & Hospital Salem",
    "State": "Tamil Nadu",
    "District": "Salem",
    "University": "The Tamilnadu Dr. MGR Medical University Chennai",
    "Management": "Trust",
    "ParentOrganization": "V. M. Ramalingam Educational Trust",
    "KeyPeople": [{"Name": "N. V. Natarajan", "Role": "Chairman", "Details": "Annapoorna Educational Group"}],
    "PoliticalAffiliation": "None direct / Educational trust.",
    "FundingSource": "Tuition fees, hospital clinical income.",
    "SummaryReport": "Established in 2011 in Salem by V. M. Ramalingam Educational Trust. Self-financed."
  },
  {
    "SlNo": "570",
    "CollegeName": "Dhanalakshmi Srinivasan Medical College and Hospital Perambalur",
    "State": "Tamil Nadu",
    "District": "Perambalur",
    "University": "The Tamilnadu Dr. MGR Medical University Chennai",
    "Management": "Trust",
    "ParentOrganization": "Dhanalakshmi Srinivasan Charitable Trust",
    "KeyPeople": [{"Name": "A. Srinivasan", "Role": "Chairman", "Details": "Dhanalakshmi Srinivasan Group"}],
    "PoliticalAffiliation": "Prominent business & educational group.",
    "FundingSource": "DS Group capital, tuition fees, hospital earnings.",
    "SummaryReport": "Established in 2011 in Siruvachur, Perambalur by A. Srinivasan. Self-financed trust medical college."
  },
  {
    "SlNo": "573",
    "CollegeName": "Sri Muthukumaran Medical College Chennai",
    "State": "Tamil Nadu",
    "District": "Kanchipuram",
    "University": "The Tamilnadu Dr. MGR Medical University Chennai",
    "Management": "Trust",
    "ParentOrganization": "Sri Muthukumaran Educational Trust",
    "KeyPeople": [{"Name": "Radha Jeyalakshmi", "Role": "Managing Trustee", "Details": "Sri Muthukumaran Group"}],
    "PoliticalAffiliation": "None direct / Educational trust.",
    "FundingSource": "Tuition fees, hospital earnings.",
    "SummaryReport": "Established in 2010 at Chikkarayapuram, Mangadu near Chennai. Self-financed."
  },
  {
    "SlNo": "574",
    "CollegeName": "Trichy SRM Medical College Hospital & Research Centre Trichy",
    "State": "Tamil Nadu",
    "District": "Tiruchirappalli",
    "University": "The Tamilnadu Dr. MGR Medical University Chennai",
    "Management": "Trust",
    "ParentOrganization": "SRM Group / Valliammai Society",
    "KeyPeople": [{"Name": "Dr. T. R. Paarivendhar (P. Pachamuthu)", "Role": "Founder & Chairman", "Details": "Former Member of Parliament (Perambalur) and founder of Indhiya Jananayaga Katchi (IJK)"}],
    "PoliticalAffiliation": "Political Party Founder. Founder Dr. T. R. Paarivendhar is a former MP and founder of IJK political party.",
    "FundingSource": "SRM Group institutional revenues, student fees, hospital clinical income.",
    "SummaryReport": "Established in 2008 at Irungalur, Trichy by SRM Group founder Dr. T. R. Paarivendhar. Self-financed."
  },
  {
    "SlNo": "575",
    "CollegeName": "ACS Medical College and Hospital Chennai",
    "State": "Tamil Nadu",
    "District": "Chennai",
    "University": "Dr. MGR Educational and Research Institute Deemed Chennai",
    "Management": "Trust",
    "ParentOrganization": "Thai Moogambigai Educational and Charitable Trust",
    "KeyPeople": [{"Name": "Dr. A. C. Shanmugam", "Role": "Founder & Chancellor", "Details": "Former MP and New Justice Party President"}],
    "PoliticalAffiliation": "Political Leader. Governed by trust led by former MP Dr. A. C. Shanmugam.",
    "FundingSource": "Deemed university tuition fees, hospital operational income.",
    "SummaryReport": "Established in 2008 at Velappanchavadi, Chennai under Dr. M.G.R. Educational and Research Institute Deemed University. Self-financed."
  },
  {
    "SlNo": "576",
    "CollegeName": "Sri Venkateswaraa Medical College Hospital and Research Institute Chennai",
    "State": "Tamil Nadu",
    "District": "Chennai",
    "University": "Sri Venkateswaraa University Chennai",
    "Management": "Trust",
    "ParentOrganization": "Ramachandra Educational Trust",
    "KeyPeople": [{"Name": "B. Ramachandran", "Role": "Chairman", "Details": "Sri Venkateswaraa Group"}],
    "PoliticalAffiliation": "None direct / Private educational trust.",
    "FundingSource": "Group reserves, tuition fees, hospital revenue.",
    "SummaryReport": "Medical college at Red Hills, Chennai operated by Ramachandra Educational Trust. Self-financed."
  },
  {
    "SlNo": "577",
    "CollegeName": "Melmaruvathur Adiparasakthi Instt. Medical Sciences and Research Melmaruvathur",
    "State": "Tamil Nadu",
    "District": "Chengalpattu",
    "University": "The Tamilnadu Dr. MGR Medical University Chennai",
    "Management": "Trust",
    "ParentOrganization": "Adhiparasakthi Charitable Medical Educational and Cultural Trust",
    "KeyPeople": [
      {"Name": "Bangaru Adigalar", "Role": "Spiritual Founder", "Details": "Padma Shri spiritual leader of Melmaruvathur Siddhar Peetham"},
      {"Name": "Dr. G. B. Anbalagan", "Role": "Managing Trustee", "Details": "Adhiparasakthi Trust"}
    ],
    "PoliticalAffiliation": "Spiritual Trust with wide cross-party political patronage in Tamil Nadu.",
    "FundingSource": "Siddhar Peetham trust donations, student tuition fees, hospital service charges.",
    "SummaryReport": "Established in 2008 at Melmaruvathur by Adhiparasakthi Trust under spiritual leader Bangaru Adigalar. Self-funded philanthropic trust."
  },
  {
    "SlNo": "578",
    "CollegeName": "SRM Medical College Hospital & Research Centre Kancheepuram",
    "State": "Tamil Nadu",
    "District": "Chengalpattu",
    "University": "SRM Institute of Science & Technology",
    "Management": "Trust",
    "ParentOrganization": "SRM Institute of Science and Technology (SRM IST Deemed University)",
    "KeyPeople": [
      {"Name": "Dr. T. R. Paarivendhar", "Role": "Founder Chancellor", "Details": "Former MP (Perambalur) and founder of IJK political party"},
      {"Name": "Dr. P. Sathyanarayanan", "Role": "President", "Details": "SRM IST"}
    ],
    "PoliticalAffiliation": "Political Leader. Founder Dr. T. R. Paarivendhar is a former MP and political party leader.",
    "FundingSource": "SRM IST deemed university tuition fees, 1200+ bed super-specialty hospital earnings.",
    "SummaryReport": "Established in 2005 at Kattankulathur, Chengalpattu as flagship medical college of SRM Deemed University. Self-financed."
  },

  # --- PONDICHERRY ---
  {
    "SlNo": "436",
    "CollegeName": "Sri Manakula Vinayagar Medical College & Hospital Pondicherry",
    "State": "Pondicherry",
    "District": "Puducherry",
    "University": "Pondicherry University",
    "Management": "Trust",
    "ParentOrganization": "Sri Manakula Vinayagar Educational Trust",
    "KeyPeople": [{"Name": "M. Dhanasekaran", "Role": "Chairman & Managing Director", "Details": "SMV Trust"}],
    "PoliticalAffiliation": "Prominent business & regional leadership standing in Puducherry.",
    "FundingSource": "SMV Trust funds, student tuition fees, hospital operational income.",
    "SummaryReport": "Established in 2006 at Kalitheerthalkuppam, Puducherry by Sri Manakula Vinayagar Educational Trust. Self-financed."
  },
  {
    "SlNo": "437",
    "CollegeName": "Puducherry Institute of Medical Sciences & Research Pondicherry",
    "State": "Pondicherry",
    "District": "Puducherry",
    "University": "Pondicherry University",
    "Management": "Trust",
    "ParentOrganization": "Madras Christian College Association (PIMS Society)",
    "KeyPeople": [{"Name": "Dr. K. Rajpal", "Role": "Chairman", "Details": "PIMS Society"}],
    "PoliticalAffiliation": "None identified / Christian Minority Institution affiliated with MCC.",
    "FundingSource": "Christian missionary society funds, tuition fees, hospital service charges.",
    "SummaryReport": "Established in 2002 at Kalapet, Puducherry by Madras Christian College Association. Self-funded Christian minority trust."
  },
  {
    "SlNo": "438",
    "CollegeName": "Aarupadai Veedu Medical College Pondicherry",
    "State": "Pondicherry",
    "District": "Puducherry",
    "University": "Vinayaka Missions University Deemed Salem",
    "Management": "Trust",
    "ParentOrganization": "Thirumuruga Kirupananda Variyar Trust / Vinayaka Missions Research Foundation",
    "KeyPeople": [{"Name": "Late Dr. A. Shanmugasundaram", "Role": "Founder", "Details": "VMRF Group"}],
    "PoliticalAffiliation": "None direct / Educational group.",
    "FundingSource": "VMRF deemed university fees, hospital earnings.",
    "SummaryReport": "Established in 1999 at Kirumampakkam, Puducherry. Constituent college of Vinayaka Missions Deemed University. Self-financed."
  },
  {
    "SlNo": "439",
    "CollegeName": "Vinayaka Missions Medical College Karaikal Pondicherry",
    "State": "Pondicherry",
    "District": "Karaikal",
    "University": "Vinayaka Missions University Deemed Salem",
    "Management": "Trust",
    "ParentOrganization": "Vinayaka Missions Research Foundation (VMRF)",
    "KeyPeople": [{"Name": "Late Dr. A. Shanmugasundaram", "Role": "Founder", "Details": "VMRF Group"}],
    "PoliticalAffiliation": "None direct / Educational trust.",
    "FundingSource": "Deemed university tuition fees, hospital clinical income.",
    "SummaryReport": "Established in 1996 in Karaikal, Puducherry UT by Vinayaka Missions. Constituent of VMRF Deemed University. Self-financed."
  },
  {
    "SlNo": "441",
    "CollegeName": "Sri Venkateswaraa Medical College Hospital & Research Centre Pondicherry",
    "State": "Pondicherry",
    "District": "Puducherry",
    "University": "Pondicherry University",
    "Management": "Trust",
    "ParentOrganization": "Ramachandra Educational Trust",
    "KeyPeople": [{"Name": "B. Ramachandran", "Role": "Chairman", "Details": "Sri Venkateswaraa Group"}],
    "PoliticalAffiliation": "None direct / Educational trust.",
    "FundingSource": "Tuition fees, hospital earnings.",
    "SummaryReport": "Established in 2007 at Ariyur, Puducherry by Ramachandra Educational Trust. Self-financed."
  },
  {
    "SlNo": "442",
    "CollegeName": "Mahatma Gandhi Medical College & Research Institute Pondicherry",
    "State": "Pondicherry",
    "District": "Puducherry",
    "University": "Sri Balaji Vidyapeeth Deemed University Pondicherry",
    "Management": "Trust",
    "ParentOrganization": "Sri Balaji Vidyapeeth Deemed University / Sri Selva Vinayakar Trust",
    "KeyPeople": [{"Name": "M. K. Rajagopalan", "Role": "Founder & Chancellor", "Details": "Sri Balaji Vidyapeeth"}],
    "PoliticalAffiliation": "None direct / Major educational conglomerate in Puducherry.",
    "FundingSource": "Deemed university tuition fees, 1000+ bed hospital revenues.",
    "SummaryReport": "Established in 2001 at Pillaiyarkuppam, Puducherry. Flagship medical college of Sri Balaji Vidyapeeth Deemed University. Self-financed."
  },
  {
    "SlNo": "443",
    "CollegeName": "Sri Lakshmi Narayana Institute of Medical Sciences Pondicherry",
    "State": "Pondicherry",
    "District": "Puducherry",
    "University": "Bharath Institute of Higher Education & Research Deemed Chennai",
    "Management": "Trust",
    "ParentOrganization": "Sri Chockalingam Trust / BIHER Deemed University",
    "KeyPeople": [{"Name": "Dr. S. Jagathrakshakan", "Role": "Founder", "Details": "Member of Parliament (DMK)"}],
    "PoliticalAffiliation": "DMK Leader. Founded by DMK MP Dr. S. Jagathrakshakan.",
    "FundingSource": "BIHER tuition fees, hospital clinical income.",
    "SummaryReport": "Established in 2006 at Osudu, Agaram, Puducherry by DMK MP Dr. S. Jagathrakshakan. Constituent of BIHER Deemed University. Self-financed."
  }
]

tn_py_sources = [
  {"SlNo": "503", "CollegeName": "J R Medical College and Hospital Villupuram", "Sources": ["https://jrmch.biher.ac.in/", "https://en.wikipedia.org/wiki/S._Jagathrakshakan"]},
  {"SlNo": "504", "CollegeName": "Kanyakumari Medical Mission Research Centre Kanyakumari", "Sources": ["https://kmmrc.org/"]},
  {"SlNo": "505", "CollegeName": "Nandha Medical College & Hospital Erode", "Sources": ["https://nandhamedicalcollege.org/"]},
  {"SlNo": "506", "CollegeName": "Dhanalakshmi Srinivasan Institute of Medical Sciences and Hospital Perambalur", "Sources": ["https://dsims.ac.in/"]},
  {"SlNo": "508", "CollegeName": "Sree Balaji Medical College and Hospital Chennai", "Sources": ["https://sbmch.ac.in/", "https://en.wikipedia.org/wiki/S._Jagathrakshakan"]},
  {"SlNo": "509", "CollegeName": "PSP Medical College Hospital and Research Institute Chennai", "Sources": ["https://pspmedicalcollege.com/"]},
  {"SlNo": "510", "CollegeName": "Rajah Muthiah Medical College Annamalainagar", "Sources": ["https://annamalaiuniversity.ac.in/rmmc/"]},
  {"SlNo": "512", "CollegeName": "Karpaga Vinayaga Institute of Medical Sciences Maduranthagam", "Sources": ["https://kims.edu.in/", "https://en.wikipedia.org/wiki/S._Regupathy"]},
  {"SlNo": "513", "CollegeName": "Shri Sathya Sai Medical College and Research Institute Kancheepuram", "Sources": ["https://sssmcri.ac.in/"]},
  {"SlNo": "514", "CollegeName": "PSG Institute of Medical Sciences Coimbatore", "Sources": ["https://psgimsr.ac.in/"]},
  {"SlNo": "516", "CollegeName": "Christian Medical College Vellore", "Sources": ["https://cmch-vellore.edu/", "https://en.wikipedia.org/wiki/Christian_Medical_College_Vellore"]},
  {"SlNo": "523", "CollegeName": "Chettinad Hospital & Research Institute Kanchipuram", "Sources": ["https://care.edu.in/chri/"]},
  {"SlNo": "524", "CollegeName": "Sree Mookambika Institute of Medical Sciences Kanyakumari", "Sources": ["https://smims.act.in/"]},
  {"SlNo": "526", "CollegeName": "Sri Ramachandra Medical College & Research Institute Chennai", "Sources": ["https://sriramachandra.edu.in/"]},
  {"SlNo": "528", "CollegeName": "Vinayaka Missions Kirupananda Variyar Medical College Salem", "Sources": ["https://vmkvmc.edu.in/"]},
  {"SlNo": "530", "CollegeName": "Meenakshi Medical College and Research Institute Enathur", "Sources": ["https://mmcri.ac.in/"]},
  {"SlNo": "531", "CollegeName": "Tagore Medical College and Hospital Chennai", "Sources": ["https://tagoremch.com/"]},
  {"SlNo": "537", "CollegeName": "Saveetha Medical College and Hospital Kanchipuram", "Sources": ["https://saveethamedicalcollege.com/"]},
  {"SlNo": "540", "CollegeName": "Swamy Vivekanandha Medical College Hospital And Research Institute Namakkal", "Sources": ["https://svmchri.ac.in/"]},
  {"SlNo": "542", "CollegeName": "Arunai Medical College And Hospital Tiruvannamalai", "Sources": ["https://amc.edu.in/", "https://en.wikipedia.org/wiki/E._V._Velu"]},
  {"SlNo": "547", "CollegeName": "Srinivasan Medical College and Hospital Tiruchirappalli", "Sources": ["https://smch.dsuniversity.ac.in/"]},
  {"SlNo": "548", "CollegeName": "Faculty of Medicine Sri Lalithambigai Medical College and Hospital Chennai", "Sources": ["https://slmch.ac.in/", "https://en.wikipedia.org/wiki/A._C._Shanmugam"]},
  {"SlNo": "549", "CollegeName": "VELS Medical College & Hospital Tiruvallur", "Sources": ["https://velsmedicalcollege.com/", "https://en.wikipedia.org/wiki/Ishari_K._Ganesh"]},
  {"SlNo": "554", "CollegeName": "ST Peters Medical College Hospital & Research Institute Hosur", "Sources": ["https://spmchri.ac.in/", "https://en.wikipedia.org/wiki/M._Thambidurai"]},
  {"SlNo": "555", "CollegeName": "Indira Medical College & Hospitals Thiruvallur", "Sources": ["https://indiramedicalcollege.com/", "https://myneta.info/"]},
  {"SlNo": "556", "CollegeName": "Bhaarat Medical College & Hospital Chennai", "Sources": ["https://bmch.biher.ac.in/"]},
  {"SlNo": "557", "CollegeName": "Panimalar Medical College Hospital & Research Institute Chennai", "Sources": ["https://pmchri.ac.in/"]},
  {"SlNo": "558", "CollegeName": "KMCH Institute of Health Sciences and Research Coimbatore", "Sources": ["https://kmchihsr.edu.in/"]},
  {"SlNo": "564", "CollegeName": "Velammal Medical College Hospital and Research Institute Madurai", "Sources": ["https://velammalmedicalcollege.edu.in/"]},
  {"SlNo": "567", "CollegeName": "Karpagam Faculty of Medical Sciences & Research Coimbatore", "Sources": ["https://karpagammedicalcollege.edu.in/"]},
  {"SlNo": "568", "CollegeName": "Madha Medical College and Hospital Thandalam Chennai", "Sources": ["https://madhamedicalcollege.org/"]},
  {"SlNo": "569", "CollegeName": "Annapoorna Medical College & Hospital Salem", "Sources": ["https://amch.in/"]},
  {"SlNo": "570", "CollegeName": "Dhanalakshmi Srinivasan Medical College and Hospital Perambalur", "Sources": ["https://dsins.org/"]},
  {"SlNo": "573", "CollegeName": "Sri Muthukumaran Medical College Chennai", "Sources": ["https://smmchri.res.in/"]},
  {"SlNo": "574", "CollegeName": "Trichy SRM Medical College Hospital & Research Centre Trichy", "Sources": ["https://tsrmc.edu.in/", "https://en.wikipedia.org/wiki/T._R._Paarivendhar"]},
  {"SlNo": "575", "CollegeName": "ACS Medical College and Hospital Chennai", "Sources": ["https://acsmch.ac.in/"]},
  {"SlNo": "576", "CollegeName": "Sri Venkateswaraa Medical College Hospital and Research Institute Chennai", "Sources": ["https://svmchri.ac.in/"]},
  {"SlNo": "577", "CollegeName": "Melmaruvathur Adiparasakthi Instt. Medical Sciences and Research Melmaruvathur", "Sources": ["https://mapims.org/"]},
  {"SlNo": "578", "CollegeName": "SRM Medical College Hospital & Research Centre Kancheepuram", "Sources": ["https://srmist.edu.in/", "https://en.wikipedia.org/wiki/T._R._Paarivendhar"]},

  {"SlNo": "436", "CollegeName": "Sri Manakula Vinayagar Medical College & Hospital Pondicherry", "Sources": ["https://smvmch.ac.in/"]},
  {"SlNo": "437", "CollegeName": "Puducherry Institute of Medical Sciences & Research Pondicherry", "Sources": ["https://pimsmma.edu.in/"]},
  {"SlNo": "438", "CollegeName": "Aarupadai Veedu Medical College Pondicherry", "Sources": ["https://avmc.edu.in/"]},
  {"SlNo": "439", "CollegeName": "Vinayaka Missions Medical College Karaikal Pondicherry", "Sources": ["https://vmmckkl.edu.in/"]},
  {"SlNo": "441", "CollegeName": "Sri Venkateswaraa Medical College Hospital & Research Centre Pondicherry", "Sources": ["https://svmcpdy.ac.in/"]},
  {"SlNo": "442", "CollegeName": "Mahatma Gandhi Medical College & Research Institute Pondicherry", "Sources": ["https://mgmcri.ac.in/"]},
  {"SlNo": "443", "CollegeName": "Sri Lakshmi Narayana Institute of Medical Sciences Pondicherry", "Sources": ["https://slims.ac.in/"]}
]

own.extend(tn_py_records)
src.extend(tn_py_sources)

save_db(own, src)
