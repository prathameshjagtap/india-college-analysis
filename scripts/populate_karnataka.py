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

ka_records = [
  {
    "SlNo": "191",
    "CollegeName": "BGS Medical College and Hospital Bengaluru",
    "State": "Karnataka",
    "District": "Bengaluru",
    "University": "Adichunchanagiri University Karnataka",
    "Management": "Private",
    "ParentOrganization": "Sri Adichunchanagiri Shikshana Trust / Adichunchanagiri University",
    "KeyPeople": [{"Name": "Sri Sri Sri Dr. Nirmalanandanatha Swamiji", "Role": "Chancellor & Mathadipathi", "Details": "Head of Sri Adichunchanagiri Mahasamsthana Math"}],
    "PoliticalAffiliation": "None direct / Prominent Vokkaliga spiritual math with significant bipartisan political reverence across Karnataka.",
    "FundingSource": "Math trust reserves, university student tuition fees, super-specialty hospital service revenues.",
    "SummaryReport": "Constituent medical college of Adichunchanagiri University, managed by Sri Adichunchanagiri Shikshana Trust under the spiritual leadership of Sri Sri Sri Dr. Nirmalanandanatha Swamiji. Self-financed."
  },
  {
    "SlNo": "192",
    "CollegeName": "PES University Institute of Medical Sciences and Research Bangalore",
    "State": "Karnataka",
    "District": "Bengaluru",
    "University": "PES University",
    "Management": "Private",
    "ParentOrganization": "People's Education Society (PES University Trust)",
    "KeyPeople": [
      {"Name": "Dr. M. R. Doreswamy", "Role": "Founder & Chancellor", "Details": "Former Member of Legislative Council (MLC, BJP) and former Education Advisor to Govt of Karnataka"},
      {"Name": "Prof. D. Jawahar", "Role": "Pro-Chancellor", "Details": "PES University"}
    ],
    "PoliticalAffiliation": "BJP Affiliation. Founder Dr. M. R. Doreswamy is a former BJP MLC and state government education advisor.",
    "FundingSource": "PES University fee revenue, hospital revenues, promoter trust capital.",
    "SummaryReport": "Constituent medical college of PES Private University, established by former BJP MLC Dr. M.R. Doreswamy. Self-financed."
  },
  {
    "SlNo": "193",
    "CollegeName": "SR Patil Medical College and Hospital Bagalkot",
    "State": "Karnataka",
    "District": "Bagalkot",
    "University": "Rajiv Gandhi University of Health Sciences Bengaluru",
    "Management": "Trust",
    "ParentOrganization": "S.R. Patil Education and Charitable Trust",
    "KeyPeople": [{"Name": "S. R. Patil", "Role": "Founder Chairman", "Details": "Former Cabinet Minister for Infrastructure & IT (Karnataka, Congress) and former Leader of Opposition in Legislative Council"}],
    "PoliticalAffiliation": "Congress Leader. Founded by senior Congress politician S. R. Patil.",
    "FundingSource": "Promoter trust funds, student tuition fees, hospital clinical earnings.",
    "SummaryReport": "Medical college at Badagandi, Bagalkot district, founded by former Congress Minister & MLC S. R. Patil under his charitable trust. Self-financed."
  },
  {
    "SlNo": "195",
    "CollegeName": "Sri Chamundeshwari Medical College Hospital & Research Institute",
    "State": "Karnataka",
    "District": "Ramanagara",
    "University": "Rajiv Gandhi University of Health Sciences",
    "Management": "Trust",
    "ParentOrganization": "Moogambigai Charitable and Educational Trust / Rajarajeswari Group",
    "KeyPeople": [{"Name": "Dr. A. C. Shanmugam", "Role": "Chairman & Founder", "Details": "Founder of New Justice Party, former MP (AIADMK) and MLA"}],
    "PoliticalAffiliation": "Political Leader. Founder Dr. A. C. Shanmugam is a former MP, MLA, and founder-president of New Justice Party.",
    "FundingSource": "Moogambigai Trust reserves, tuition fees, hospital patient revenues.",
    "SummaryReport": "Established at Channapatna under Moogambigai Trust headed by political leader Dr. A. C. Shanmugam. Self-financed."
  },
  {
    "SlNo": "196",
    "CollegeName": "Khaja Bandanawaz University Faculty of Medical Sciences Gulbarga",
    "State": "Karnataka",
    "District": "Kalaburagi",
    "University": "Khaja Bandanawaz University",
    "Management": "Trust",
    "ParentOrganization": "Khaja Education Society",
    "KeyPeople": [{"Name": "Dr. Syed Shah Khusro Hussaini", "Role": "Chancellor & President", "Details": "President of Khaja Education Society and Sajjada Nasheen of Hazrat Khaja Bande Nawaz Dargah"}],
    "PoliticalAffiliation": "None direct / Eminent Muslim spiritual and educational trust in Kalyana Karnataka.",
    "FundingSource": "Sufi shrine trust endowments, university tuition fees, hospital earnings.",
    "SummaryReport": "Constituent medical college of Khaja Bandanawaz University, established by Khaja Education Society led by Dr. Syed Shah Khusro Hussaini. Self-financed."
  },
  {
    "SlNo": "197",
    "CollegeName": "St. Johns Medical College Bangalore",
    "State": "Karnataka",
    "District": "Bengaluru",
    "University": "Rajiv Gandhi University of Health Sciences Karnataka",
    "Management": "Trust",
    "ParentOrganization": "Catholic Bishops' Conference of India (CBCI Society for Medical Education)",
    "KeyPeople": [
      {"Name": "Most Rev. Andrews Thazhath", "Role": "President, CBCI", "Details": "Archbishop of Trichur"},
      {"Name": "Rev. Dr. Paul Parathazham", "Role": "Director", "Details": "St. John's National Academy of Health Sciences"}
    ],
    "PoliticalAffiliation": "None identified / Premier Christian Minority Institution managed by apex Catholic body.",
    "FundingSource": "CBCI institutional endowment, student tuition fees, clinical super-specialty hospital revenues, research grants.",
    "SummaryReport": "Established in 1963 by CBCI as a premier non-profit Christian minority medical college in Bangalore. Self-funded through institutional reserves and hospital earnings."
  },
  {
    "SlNo": "198",
    "CollegeName": "A J Institute of Medical Sciences & Research Centre Mangalore",
    "State": "Karnataka",
    "District": "Dakshina Kannada",
    "University": "Rajiv Gandhi University of Health Sciences Karnataka",
    "Management": "Trust",
    "ParentOrganization": "Laxmi Memorial Education Trust",
    "KeyPeople": [{"Name": "Dr. A. J. Shetty", "Role": "President & Founder", "Details": "Industrialist, hotelier and philanthropist (AJ Group)"}],
    "PoliticalAffiliation": "None direct / Prominent coastal Karnataka industrial group.",
    "FundingSource": "AJ Group enterprise capital, tuition fees, super-specialty hospital earnings.",
    "SummaryReport": "Founded in 2002 by Dr. A. J. Shetty under Laxmi Memorial Education Trust. Self-financed through business group capital and college fees."
  },
  {
    "SlNo": "199",
    "CollegeName": "Raja Rajeswari Medical College & Hospital Bangalore",
    "State": "Karnataka",
    "District": "Bengaluru",
    "University": "Rajiv Gandhi University of Health Sciences Karnataka",
    "Management": "Trust",
    "ParentOrganization": "Moogambigai Charitable and Educational Trust",
    "KeyPeople": [{"Name": "Dr. A. C. Shanmugam", "Role": "Chairman", "Details": "Former MP and founder of New Justice Party"}],
    "PoliticalAffiliation": "Political Leader. Managed by trust led by Dr. A. C. Shanmugam (former MP & MLA).",
    "FundingSource": "Moogambigai Trust reserves, tuition fees, hospital operational income.",
    "SummaryReport": "Established in 2005 on Mysore Road, Bangalore by Dr. A. C. Shanmugam. Self-financed trust institution."
  },
  {
    "SlNo": "200",
    "CollegeName": "Yenepoya Medical College Mangalore",
    "State": "Karnataka",
    "District": "Dakshina Kannada",
    "University": "Yenepoya University Deemed",
    "Management": "Trust",
    "ParentOrganization": "Islamic Academy of Education / Yenepoya Deemed University",
    "KeyPeople": [{"Name": "Yenepoya Abdulla Kunhi", "Role": "Chancellor & Founder", "Details": "Industrialist and founder of Yenepoya Group"}],
    "PoliticalAffiliation": "None direct / Prominent Muslim minority educational trust and enterprise group.",
    "FundingSource": "Yenepoya Group enterprise capital, deemed university fees, hospital services.",
    "SummaryReport": "Established in 1999 as a constituent college of Yenepoya Deemed University, founded by Yenepoya Abdulla Kunhi under Islamic Academy of Education. Self-financed."
  },
  {
    "SlNo": "201",
    "CollegeName": "Al-Ameen Medical College Bijapur",
    "State": "Karnataka",
    "District": "Vijayapura",
    "University": "Rajiv Gandhi University of Health Sciences Karnataka",
    "Management": "Trust",
    "ParentOrganization": "Al-Ameen Educational Society",
    "KeyPeople": [
      {"Name": "Dr. Mumtaz Ahmed Khan", "Role": "Founder", "Details": "Eminent educationist and founder of Al-Ameen movement"},
      {"Name": "Umar Ismail Khan", "Role": "Chairman", "Details": "Al-Ameen Educational Society"}
    ],
    "PoliticalAffiliation": "None direct / Leading Muslim minority educational society in Karnataka.",
    "FundingSource": "Al-Ameen Society reserves, tuition fees, hospital revenue.",
    "SummaryReport": "Established in 1984 in Vijayapura (Bijapur) by Dr. Mumtaz Ahmed Khan under Al-Ameen Educational Society. Self-financed minority trust."
  },
  {
    "SlNo": "203",
    "CollegeName": "Vydehi Institute Of Medical Sciences & Research Centre Bangalore",
    "State": "Karnataka",
    "District": "Bengaluru",
    "University": "Rajiv Gandhi University of Health Sciences Karnataka",
    "Management": "Trust",
    "ParentOrganization": "Srinivasa Trust",
    "KeyPeople": [
      {"Name": "D. K. Audikesavulu", "Role": "Founder", "Details": "Late Member of Parliament (TDP/Congress) and former Chairman of Tirumala Tirupati Devasthanams (TTD)"},
      {"Name": "D. A. Kalpaja", "Role": "Chairperson / Director", "Details": "Vydehi Group"}
    ],
    "PoliticalAffiliation": "Political Family. Founded by family of late MP and TTD Chairman D. K. Audikesavulu.",
    "FundingSource": "Srinivasa Trust capital, tuition fees, 1600-bed super-specialty hospital revenue.",
    "SummaryReport": "Established in 2000 in Whitefield, Bangalore by late MP D. K. Audikesavulu under Srinivasa Trust. Self-financed super-specialty medical institute."
  },
  {
    "SlNo": "204",
    "CollegeName": "S S Institute of Medical Sciences & Research Centre Davangere",
    "State": "Karnataka",
    "District": "Davangere",
    "University": "Rajiv Gandhi University of Health Sciences Karnataka",
    "Management": "Trust",
    "ParentOrganization": "Bapuji Educational Association (BEA)",
    "KeyPeople": [
      {"Name": "Shamanur Shivashankarappa", "Role": "President", "Details": "Cabinet Minister for Cabinet Affairs/Infrastructure (Karnataka, Congress), sitting MLA (Davangere South), and All India Veerashaiva Mahasabha President"},
      {"Name": "S. S. Mallikarjun", "Role": "Joint Secretary", "Details": "Cabinet Minister for Mines & Geology (Karnataka, Congress) and MLA"}
    ],
    "PoliticalAffiliation": "Congress Leaders. Managed by Shamanur Shivashankarappa (sitting Congress Minister/MLA) and S. S. Mallikarjun (Cabinet Minister).",
    "FundingSource": "Bapuji Educational Association funds, tuition fees, hospital revenue.",
    "SummaryReport": "Established in 2002 by BEA led by veteran Congress Minister Shamanur Shivashankarappa. Self-financed Lingayat educational trust."
  },
  {
    "SlNo": "206",
    "CollegeName": "M S Ramaiah Medical College Bangalore",
    "State": "Karnataka",
    "District": "Bengaluru",
    "University": "Rajiv Gandhi University of Health Sciences Karnataka",
    "Management": "Trust",
    "ParentOrganization": "Gokula Education Foundation (GEF)",
    "KeyPeople": [
      {"Name": "Late Dr. M. S. Ramaiah", "Role": "Founder", "Details": "Industrialist, philanthropist and founder of Ramaiah Group"},
      {"Name": "M. R. Seetharam", "Role": "Vice Chairman", "Details": "Former Minister for Planning & Statistics (Karnataka, Congress) and former MLC"}
    ],
    "PoliticalAffiliation": "Congress Leader Family. Vice Chairman M. R. Seetharam is a former Congress Cabinet Minister and MLC.",
    "FundingSource": "Ramaiah Group institutional funds, student tuition fees, 1000+ bed hospital revenues.",
    "SummaryReport": "Established in 1979 by industrialist M. S. Ramaiah. Governed by Gokula Education Foundation headed by former Congress Minister M. R. Seetharam. Self-financed."
  },
  {
    "SlNo": "208",
    "CollegeName": "Sri Siddhartha Medical College Tumkur",
    "State": "Karnataka",
    "District": "Tumakuru",
    "University": "Sri Siddhartha Academy of Higher Education Tumkur",
    "Management": "Trust",
    "ParentOrganization": "Sri Siddhartha Education Society (SSES) / SSAHE Deemed University",
    "KeyPeople": [
      {"Name": "Dr. G. Parameshwara", "Role": "Chancellor", "Details": "Home Minister of Karnataka (Congress), former Deputy Chief Minister, and KPCC President"},
      {"Name": "Late H. M. Gangadharaiah", "Role": "Founder", "Details": "Veteran MLC and freedom fighter"}
    ],
    "PoliticalAffiliation": "Strong Congress Leadership. Chancellor Dr. G. Parameshwara is the sitting Home Minister of Karnataka and former Deputy CM.",
    "FundingSource": "SSES trust reserves, deemed university tuition fees, teaching hospital income.",
    "SummaryReport": "Established in 1988 in Tumkur by SSES, founded by H.M. Gangadharaiah and headed by Home Minister Dr. G. Parameshwara. Self-financed."
  },
  {
    "SlNo": "209",
    "CollegeName": "S. Nijalingappa Medical College & HSK Hospital & Research Centre Bagalkot",
    "State": "Karnataka",
    "District": "Bagalkot",
    "University": "Rajiv Gandhi University of Health Sciences Karnataka",
    "Management": "Trust",
    "ParentOrganization": "Basaveshwar Veerashaiva Vidyavardhaka Sangha (BVV Sangha)",
    "KeyPeople": [{"Name": "Dr. Veeranna C. Charantimath", "Role": "Chairman", "Details": "Former Member of Legislative Assembly (BJP, Bagalkot)"}],
    "PoliticalAffiliation": "BJP Leader. Chairman Dr. Veeranna Charantimath is a former BJP MLA.",
    "FundingSource": "BVV Sangha community educational trust funds, tuition fees, HSK Hospital revenues.",
    "SummaryReport": "Established in 2002 by BVV Sangha (historic Lingayat educational society est. 1906), led by former BJP MLA Dr. Veeranna Charantimath. Self-financed."
  },
  {
    "SlNo": "210",
    "CollegeName": "MVJ Medical College and Research Hospital Bangalore",
    "State": "Karnataka",
    "District": "Bengaluru Rural",
    "University": "Rajiv Gandhi University of Health Sciences Karnataka",
    "Management": "Trust",
    "ParentOrganization": "Venkatesha Education Trust",
    "KeyPeople": [
      {"Name": "Late Dr. M. V. Jayaraman", "Role": "Founder", "Details": "Eminent educationist"},
      {"Name": "M. J. Balachandar", "Role": "Chairman", "Details": "MVJ Group"}
    ],
    "PoliticalAffiliation": "None direct / Private educational trust.",
    "FundingSource": "MVJ Group funds, tuition fees, hospital clinical income.",
    "SummaryReport": "Established in 2001 at Hoskote, Bangalore Rural by Venkatesha Education Trust. Self-financed."
  },
  {
    "SlNo": "211",
    "CollegeName": "K S Hegde Medical Academy Mangalore",
    "State": "Karnataka",
    "District": "Dakshina Kannada",
    "University": "Nitte University Deemed Mangalore",
    "Management": "Trust",
    "ParentOrganization": "Nitte Education Trust / Nitte Deemed University",
    "KeyPeople": [
      {"Name": "N. Vinaya Hegde", "Role": "Chancellor", "Details": "Industrialist and President of Nitte Education Trust"},
      {"Name": "Late Justice K. S. Hegde", "Role": "Founder", "Details": "Former Speaker of Lok Sabha and Judge of Supreme Court of India"}
    ],
    "PoliticalAffiliation": "Historical Legal/Political Stature. Founded in memory of former Lok Sabha Speaker Justice K. S. Hegde.",
    "FundingSource": "Nitte Trust reserves, deemed university fees, super-specialty hospital earnings.",
    "SummaryReport": "Constituent medical college of Nitte Deemed University, established in 1999 by N. Vinaya Hegde under Nitte Education Trust. Self-financed."
  },
  {
    "SlNo": "215",
    "CollegeName": "Dr BR Ambedkar Medical College Bangalore",
    "State": "Karnataka",
    "District": "Bengaluru",
    "University": "Rajiv Gandhi University of Health Sciences Karnataka",
    "Management": "Trust",
    "ParentOrganization": "Ananda Social and Educational Trust",
    "KeyPeople": [{"Name": "Late B. R. Jalappa", "Role": "Founder & Former Chairman", "Details": "Former Union Cabinet Minister for Textiles (Congress/JD) and MP"}],
    "PoliticalAffiliation": "Congress Leader Family. Founded by late Union Minister B. R. Jalappa.",
    "FundingSource": "Ananda Trust funds, student tuition fees, hospital operational income.",
    "SummaryReport": "Established in 1981 at Kadugondanahalli, Bangalore by Ananda Social & Educational Trust led by late Union Minister B. R. Jalappa. Self-financed."
  },
  {
    "SlNo": "216",
    "CollegeName": "Mahadevappa Rampure Medical College Kalaburagi Gulbarga",
    "State": "Karnataka",
    "District": "Kalaburagi",
    "University": "Rajiv Gandhi University of Health Sciences Karnataka",
    "Management": "Trust",
    "ParentOrganization": "Hyderabad Karnataka Education (HKE) Society",
    "KeyPeople": [
      {"Name": "Dr. Bhimashankar C. Bilgundi", "Role": "President", "Details": "HKE Society"},
      {"Name": "Shashil G. Namoshi", "Role": "Executive Committee Member", "Details": "Member of Legislative Council (MLC, BJP)"}
    ],
    "PoliticalAffiliation": "BJP & Regional Political Leaders. HKE Society board includes active political figures like BJP MLC Shashil G. Namoshi.",
    "FundingSource": "HKE Society trust reserves, tuition fees, Basaveshwar Hospital earnings.",
    "SummaryReport": "Established in 1963 as one of Karnataka's pioneer private medical colleges by HKE Society in Kalaburagi. Self-financed educational trust."
  },
  {
    "SlNo": "220",
    "CollegeName": "JSS Medical College Mysore",
    "State": "Karnataka",
    "District": "Mysuru",
    "University": "JSS Academy of Higher Education & Research Mysuru",
    "Management": "Trust",
    "ParentOrganization": "JSS Mahavidyapeetha / Suttur Math",
    "KeyPeople": [{"Name": "Jagadguru Sri Shivarathri Deshikendra Mahaswamiji", "Role": "Chancellor & President", "Details": "Head of Suttur Math / JSS Mahavidyapeetha"}],
    "PoliticalAffiliation": "Spiritual/Social Eminence. Suttur Math wields immense non-partisan spiritual and political influence in Karnataka.",
    "FundingSource": "JSS Mahavidyapeetha institutional endowments, university fees, 1800-bed super-specialty hospital revenues.",
    "SummaryReport": "Established in 1984 in Mysuru under JSS Mahavidyapeetha (Suttur Math). Constituent college of JSS AHER Deemed University. Self-funded through institutional trust."
  },
  {
    "SlNo": "221",
    "CollegeName": "Kempegowda Institute of Medical Sciences Bangalore",
    "State": "Karnataka",
    "District": "Bengaluru",
    "University": "Rajiv Gandhi University of Health Sciences Karnataka",
    "Management": "Trust",
    "ParentOrganization": "Rajya Vokkaligara Sangha",
    "KeyPeople": [{"Name": "D. Hanumanthaiah", "Role": "President", "Details": "Rajya Vokkaligara Sangha"}],
    "PoliticalAffiliation": "Vokkaliga Community Apex Body. Governed by elected directors comprising prominent Vokkaliga community politicians (Congress, JD-S, BJP).",
    "FundingSource": "Vokkaligara Sangha community trust funds, tuition fees, hospital clinical income.",
    "SummaryReport": "Established in 1980 by Rajya Vokkaligara Sangha in Bangalore. Governed by elected board of Vokkaliga community leaders. Self-financed."
  },
  {
    "SlNo": "222",
    "CollegeName": "JJM Medical College Davangere",
    "State": "Karnataka",
    "District": "Davangere",
    "University": "Rajiv Gandhi University of Health Sciences Karnataka",
    "Management": "Trust",
    "ParentOrganization": "Bapuji Educational Association (BEA)",
    "KeyPeople": [{"Name": "Shamanur Shivashankarappa", "Role": "President", "Details": "Cabinet Minister (Karnataka, Congress) and MLA"}],
    "PoliticalAffiliation": "Congress Leader. Managed by BEA headed by senior Congress Cabinet Minister Shamanur Shivashankarappa.",
    "FundingSource": "BEA trust funds, tuition fees, Bapuji Hospital & Chigateri Hospital operations.",
    "SummaryReport": "Established in 1965 in Davangere by Bapuji Educational Association led by Shamanur Shivashankarappa. Premier self-financed Lingayat trust college."
  },
  {
    "SlNo": "223",
    "CollegeName": "Kasturba Medical College Manipal",
    "State": "Karnataka",
    "District": "Udupi",
    "University": "Manipal Academy of Higher Education Deemed Manipal",
    "Management": "Trust",
    "ParentOrganization": "Manipal Academy of Higher Education (MAHE Deemed University) / Pai Family Trust",
    "KeyPeople": [
      {"Name": "Dr. Ramdas M. Pai", "Role": "Chancellor", "Details": "Padma Bhushan awardee and Chairman of Manipal Education & Medical Group"},
      {"Name": "Dr. Ranjan Pai", "Role": "President", "Details": "MEMG (Manipal Group)"},
      {"Name": "Late Dr. T. M. A. Pai", "Role": "Founder", "Details": "Pioneer of self-financing education in India"}
    ],
    "PoliticalAffiliation": "None direct / Premier corporate healthcare and education conglomerate.",
    "FundingSource": "MAHE tuition fees, MEMG group investments, Kasturba Hospital clinical operations, international student quotas.",
    "SummaryReport": "Established in 1953 by Dr. T. M. A. Pai as India's first self-financing private medical college. Constituent college of MAHE Deemed University. Self-funded."
  },
  {
    "SlNo": "224",
    "CollegeName": "Kasturba Medical College Mangalore",
    "State": "Karnataka",
    "District": "Dakshina Kannada",
    "University": "Manipal Academy of Higher Education Deemed Manipal",
    "Management": "Trust",
    "ParentOrganization": "Manipal Academy of Higher Education (MAHE)",
    "KeyPeople": [
      {"Name": "Dr. Ramdas M. Pai", "Role": "Chancellor", "Details": "MAHE"},
      {"Name": "Dr. Ranjan Pai", "Role": "Chairman", "Details": "MEMG"}
    ],
    "PoliticalAffiliation": "None direct / Manipal Group.",
    "FundingSource": "MAHE tuition fees, hospital clinical earnings.",
    "SummaryReport": "Established in 1955 as KMC Mangalore under MAHE Deemed University. Sister campus of KMC Manipal. Self-financed."
  },
  {
    "SlNo": "225",
    "CollegeName": "Sri Devaraj URS Medical College Kolar",
    "State": "Karnataka",
    "District": "Kolar",
    "University": "Sri Devaraj Urs Academy of Higher Education and Research Deemed Kolar",
    "Management": "Trust",
    "ParentOrganization": "Sri Devaraj Urs Educational Trust",
    "KeyPeople": [{"Name": "Late R. L. Jalappa", "Role": "Founder & Former Chairman", "Details": "Former Union Cabinet Minister (Congress/JD)"}],
    "PoliticalAffiliation": "Congress Leader Family. Founded by former Union Minister R. L. Jalappa.",
    "FundingSource": "Deemed university tuition fees, RL Jalappa Hospital earnings.",
    "SummaryReport": "Established in 1986 at Tamaka, Kolar by Sri Devaraj Urs Educational Trust founded by Union Minister R. L. Jalappa. Deemed university status. Self-financed."
  },
  {
    "SlNo": "226",
    "CollegeName": "K V G Medical College Sullia",
    "State": "Karnataka",
    "District": "Dakshina Kannada",
    "University": "Rajiv Gandhi University of Health Sciences Karnataka",
    "Management": "Trust",
    "ParentOrganization": "Academy of Liberal Education Sullia",
    "KeyPeople": [
      {"Name": "Late Dr. K. V. Gowda", "Role": "Founder", "Details": "Educationist and founder of KVG Institutions"},
      {"Name": "Dr. Renuka Prasad K. V.", "Role": "President", "Details": "Academy of Liberal Education"}
    ],
    "PoliticalAffiliation": "None direct / Private educational trust.",
    "FundingSource": "Tuition fees, hospital clinical revenues.",
    "SummaryReport": "Established in 2002 at Sullia by Academy of Liberal Education. Self-financed."
  },
  {
    "SlNo": "227",
    "CollegeName": "Jawaharlal Nehru Medical College Belgaum",
    "State": "Karnataka",
    "District": "Belagavi",
    "University": "KLE Academy of Higher Education & Research Deemed Belgaum",
    "Management": "Trust",
    "ParentOrganization": "KLE Society (Karnatak Lingayat Education Society)",
    "KeyPeople": [{"Name": "Dr. Prabhakar Kore", "Role": "Chairman", "Details": "Former Member of Parliament (Rajya Sabha, BJP) and veteran Lingayat educationist"}],
    "PoliticalAffiliation": "BJP Leader. Chairman Dr. Prabhakar Kore is a former three-term BJP Rajya Sabha MP.",
    "FundingSource": "KLE Society institutional reserves, deemed university tuition fees, KLES Prabhakar Kore Hospital revenues.",
    "SummaryReport": "Established in 1963 in Belagavi by KLE Society (est. 1916). Led by former BJP MP Dr. Prabhakar Kore. Constituent college of KAHER Deemed University. Self-financed."
  },
  {
    "SlNo": "228",
    "CollegeName": "Adichunchanagiri Institute of Medical Sciences Bellur",
    "State": "Karnataka",
    "District": "Mandya",
    "University": "Rajiv Gandhi University of Health Sciences Karnataka",
    "Management": "Trust",
    "ParentOrganization": "Sri Adichunchanagiri Shikshana Trust",
    "KeyPeople": [{"Name": "Sri Sri Sri Dr. Nirmalanandanatha Swamiji", "Role": "President", "Details": "Head of Sri Adichunchanagiri Math"}],
    "PoliticalAffiliation": "Vokkaliga Spiritual Math with bipartisan political stature.",
    "FundingSource": "Trust reserves, tuition fees, hospital operational income.",
    "SummaryReport": "Established in 1986 at BG Nagara, Bellur by Sri Adichunchanagiri Shikshana Trust under late Sri Balagangadharanatha Swamiji. Self-financed."
  },
  {
    "SlNo": "229",
    "CollegeName": "Father Mullers Medical College Mangalore",
    "State": "Karnataka",
    "District": "Dakshina Kannada",
    "University": "Rajiv Gandhi University of Health Sciences Karnataka",
    "Management": "Trust",
    "ParentOrganization": "Father Muller Charitable Institutions (Diocese of Mangalore)",
    "KeyPeople": [
      {"Name": "Most Rev. Dr. Peter Paul Saldanha", "Role": "President", "Details": "Bishop of Mangalore Diocese"},
      {"Name": "Rev. Fr. Richard Aloysius Coelho", "Role": "Director", "Details": "FMCI Mangalore"}
    ],
    "PoliticalAffiliation": "None identified / Historic Catholic Charitable Trust.",
    "FundingSource": "Diocese trust endowments, tuition fees, 1250-bed super-specialty hospital revenues.",
    "SummaryReport": "Established as a medical college in 1999 (charitable institution founded 1880) by the Catholic Diocese of Mangalore. Self-funded Christian minority trust."
  },
  {
    "SlNo": "232",
    "CollegeName": "G R Medical College Hospital & Research Centre Mangaluru",
    "State": "Karnataka",
    "District": "Dakshina Kannada",
    "University": "Rajiv Gandhi University of Health Sciences Karnataka",
    "Management": "Trust",
    "ParentOrganization": "G.R. Educational Trust",
    "KeyPeople": [{"Name": "Dr. G. R. Shetty", "Role": "Chairman", "Details": "G.R. Educational Trust"}],
    "PoliticalAffiliation": "None identified / Private educational trust.",
    "FundingSource": "Tuition fees, hospital earnings.",
    "SummaryReport": "Medical college in Mangaluru operated by G.R. Educational Trust. Self-financed."
  },
  {
    "SlNo": "233",
    "CollegeName": "Jagadguru Gangadhar Mahaswamigalu Moorusavirmath Medical College Hubli",
    "State": "Karnataka",
    "District": "Dharwad",
    "University": "KLE Academy of Higher Education & Research Deemed Belgaum",
    "Management": "Trust",
    "ParentOrganization": "KLE Society / Moorusavirmath Trust",
    "KeyPeople": [{"Name": "Dr. Prabhakar Kore", "Role": "Chairman", "Details": "Former MP (BJP) and Chairman of KLE Society"}],
    "PoliticalAffiliation": "BJP Leader. Managed by KLE Society (Dr. Prabhakar Kore, former BJP MP).",
    "FundingSource": "KLE Society trust funds, tuition fees, hospital revenue.",
    "SummaryReport": "Established at Hubballi under KLE Society in collaboration with historic Moorusavirmath Trust. Constituent of KAHER Deemed University. Self-financed."
  },
  {
    "SlNo": "234",
    "CollegeName": "Sri Madhusudan Sai Institute of Medical Sciences & Research Chikballapur",
    "State": "Karnataka",
    "District": "Chikkaballapur",
    "University": "Sri Sathya Sai University for Human Excellence Navanihal",
    "Management": "Trust",
    "ParentOrganization": "Sri Sathya Sai Loka Seva Gurukulam / Prashanthi Balamandira Trust",
    "KeyPeople": [{"Name": "Sri Madhusudan Sai", "Role": "Founder & Spiritual Leader", "Details": "Sri Sathya Sai Loka Seva movement"}],
    "PoliticalAffiliation": "None / Philanthropic Spiritual Trust (Inaugurated by Prime Minister Narendra Modi in 2023).",
    "FundingSource": "100% Philanthropic donations & global charity trusts. Medical education and hospital treatment are provided COMPLETELY FREE OF COST.",
    "SummaryReport": "India's first completely FREE private medical college, inaugurated in 2023 at Sathya Sai Grama, Muddenahalli by PM Narendra Modi. Funded 100% through philanthropic global donations."
  },
  {
    "SlNo": "235",
    "CollegeName": "Dr. Chandramma Dayananda Sagar Instt. of Medical Education & Research Harohalli Hubli",
    "State": "Karnataka",
    "District": "Ramanagara",
    "University": "Dayananda Sagar University Bangalore",
    "Management": "Trust",
    "ParentOrganization": "Mahatma Gandhi Vidya Peetha Trust (MGVP)",
    "KeyPeople": [
      {"Name": "Dr. D. Hemachandra Sagar", "Role": "Chairman", "Details": "Former Member of Legislative Assembly (BJP, Chikpet) and Chancellor of DSU"},
      {"Name": "Dr. D. Premachandra Sagar", "Role": "Vice Chairman", "Details": "Dayananda Sagar Institutions"}
    ],
    "PoliticalAffiliation": "BJP Leader Family. Chairman Dr. D. Hemachandra Sagar is a former BJP MLA.",
    "FundingSource": "Dayananda Sagar University fees, MGVP trust reserves, hospital revenue.",
    "SummaryReport": "Constituent medical college of Dayananda Sagar University at Harohalli, founded by former BJP MLA Dr. D. Hemachandra Sagar under MGVP Trust. Self-financed."
  },
  {
    "SlNo": "237",
    "CollegeName": "Sri siddhartha Institute of Medical Sciences & Research Centre Bengaluru",
    "State": "Karnataka",
    "District": "Bengaluru Rural",
    "University": "Sri Siddhartha Academy of Higher Education Tumkur",
    "Management": "Trust",
    "ParentOrganization": "Sri Siddhartha Education Society (SSES)",
    "KeyPeople": [{"Name": "Dr. G. Parameshwara", "Role": "Chancellor", "Details": "Home Minister of Karnataka (Congress)"}],
    "PoliticalAffiliation": "Congress Leadership. Governed by SSES headed by Home Minister Dr. G. Parameshwara.",
    "FundingSource": "SSES trust reserves, tuition fees, hospital clinical income.",
    "SummaryReport": "Established at T. Begur, Nelamangala (Bengaluru Rural) under SSES by Home Minister Dr. G. Parameshwara. Constituent of SSAHE Deemed University. Self-financed."
  },
  {
    "SlNo": "238",
    "CollegeName": "East Point College of Medical Sciences & Research Centre Bengaluru",
    "State": "Karnataka",
    "District": "Bengaluru",
    "University": "Rajiv Gandhi University of Health Sciences Karnataka",
    "Management": "Trust",
    "ParentOrganization": "M.G. Charitable Trust",
    "KeyPeople": [
      {"Name": "Late S. M. Venkatpathi", "Role": "Founder", "Details": "Educationist and founder of East Point Group"},
      {"Name": "B. N. Purushothaman", "Role": "Chairman", "Details": "East Point Group"}
    ],
    "PoliticalAffiliation": "None direct / Private educational trust.",
    "FundingSource": "East Point Group funds, student tuition fees, hospital revenues.",
    "SummaryReport": "Established in 2017 at Bidarahalli, Bangalore by M.G. Charitable Trust. Self-financed."
  },
  {
    "SlNo": "239",
    "CollegeName": "Sambhram Institute of Medical Sciences & Research Kolar",
    "State": "Karnataka",
    "District": "Kolar",
    "University": "Rajiv Gandhi University of Health Sciences Karnataka",
    "Management": "Trust",
    "ParentOrganization": "Sambhram Educational Trust",
    "KeyPeople": [{"Name": "V. Nagaraj", "Role": "Chairman", "Details": "Sambhram Group of Institutions"}],
    "PoliticalAffiliation": "None direct / Educational trust.",
    "FundingSource": "Tuition fees, hospital operational income.",
    "SummaryReport": "Established at Kolar Gold Fields (KGF) by Sambhram Educational Trust. Self-financed."
  },
  {
    "SlNo": "240",
    "CollegeName": "Akash Institute of Medical Sciences & Research Centre Devanhalli Bangalore",
    "State": "Karnataka",
    "District": "Bengaluru Rural",
    "University": "Rajiv Gandhi University of Health Sciences Karnataka",
    "Management": "Trust",
    "ParentOrganization": "Akash Education Trust",
    "KeyPeople": [{"Name": "K. Amaranath", "Role": "Chairman", "Details": "Akash Group of Institutions"}],
    "PoliticalAffiliation": "Local political connections in Devanahalli / Bangalore Rural region.",
    "FundingSource": "Tuition fees, hospital earnings, promoter capital.",
    "SummaryReport": "Established in 2016 near Devanahalli, Bangalore by Akash Education Trust. Self-financed."
  },
  {
    "SlNo": "241",
    "CollegeName": "Kanachur Institute of Medical Sciences Mangalore",
    "State": "Karnataka",
    "District": "Dakshina Kannada",
    "University": "Rajiv Gandhi University of Health Sciences Karnataka",
    "Management": "Trust",
    "ParentOrganization": "Kanachur Islamic Education Trust",
    "KeyPeople": [{"Name": "Kanachur Monu", "Role": "Chairman & Founder", "Details": "Prominent business leader and Muslim community leader in Mangalore"}],
    "PoliticalAffiliation": "Muslim minority trust; prominent business and community leadership in Mangaluru.",
    "FundingSource": "Kanachur Group revenues, tuition fees, hospital clinical income.",
    "SummaryReport": "Established in 2016 at Natekal, Mangalore by Kanachur Monu under Kanachur Islamic Education Trust. Self-financed Muslim minority college."
  },
  {
    "SlNo": "248",
    "CollegeName": "The Oxford Medical College Hospital & Research Centre Bangalore",
    "State": "Karnataka",
    "District": "Bengaluru",
    "University": "Rajiv Gandhi University of Health Sciences Karnataka",
    "Management": "Society",
    "ParentOrganization": "Children's Education Society",
    "KeyPeople": [{"Name": "Late S. Narasa Raju", "Role": "Founder Chairman", "Details": "Founder of Oxford Educational Institutions"}],
    "PoliticalAffiliation": "None direct / Educational conglomerate.",
    "FundingSource": "Oxford Educational Group institutional fees, hospital revenue.",
    "SummaryReport": "Established in 2014 at Attibele, Bangalore by Children's Education Society. Self-financed."
  },
  {
    "SlNo": "250",
    "CollegeName": "Shridevi Institute of Medical Sciences & Research Hospital Tumkur",
    "State": "Karnataka",
    "District": "Tumakuru",
    "University": "Rajiv Gandhi University of Health Sciences Karnataka",
    "Management": "Trust",
    "ParentOrganization": "Sri Shridevi Charitable Trust",
    "KeyPeople": [{"Name": "Dr. M. R. Hulinaykar", "Role": "Chairman & Managing Trustee", "Details": "Former Member of Legislative Council (MLC, JD-S/BJP)"}],
    "PoliticalAffiliation": "Political Leader. Founder Dr. M. R. Hulinaykar is a former MLC.",
    "FundingSource": "Shridevi Group funds, tuition fees, hospital clinical earnings.",
    "SummaryReport": "Established in 2013 in Tumkur by former MLC Dr. M. R. Hulinaykar under Sri Shridevi Charitable Trust. Self-financed."
  },
  {
    "SlNo": "251",
    "CollegeName": "BGS Global Institute of Medical Sciences Bangalore",
    "State": "Karnataka",
    "District": "Bengaluru",
    "University": "Rajiv Gandhi University of Health Sciences Karnataka",
    "Management": "Trust",
    "ParentOrganization": "Sri Adichunchanagiri Shikshana Trust",
    "KeyPeople": [{"Name": "Sri Sri Sri Dr. Nirmalanandanatha Swamiji", "Role": "President", "Details": "Head of Sri Adichunchanagiri Math"}],
    "PoliticalAffiliation": "Vokkaliga Spiritual Math with bipartisan stature.",
    "FundingSource": "Math trust reserves, tuition fees, BGS Global Hospital clinical earnings.",
    "SummaryReport": "Established in 2013 at Kengeri, Bangalore by Sri Adichunchanagiri Shikshana Trust. Self-financed trust medical college."
  },
  {
    "SlNo": "252",
    "CollegeName": "Subbaiah Institute of Medical Sciences Shimoga",
    "State": "Karnataka",
    "District": "Shivamogga",
    "University": "Rajiv Gandhi University of Health Sciences Karnataka",
    "Management": "Trust",
    "ParentOrganization": "Tantara Educational Trust",
    "KeyPeople": [{"Name": "K. T. Subbaiah", "Role": "Chairman", "Details": "Subbaiah Group of Institutions"}],
    "PoliticalAffiliation": "Local political connections in Shivamogga district.",
    "FundingSource": "Tuition fees, hospital operational income, promoter equity.",
    "SummaryReport": "Established in 2012 in Shivamogga by Tantara Educational Trust. Self-financed."
  },
  {
    "SlNo": "254",
    "CollegeName": "Srinivas Institute of Medical Research Centre Srinivasnagar Mangalore",
    "State": "Karnataka",
    "District": "Dakshina Kannada",
    "University": "Rajiv Gandhi University of Health Sciences Karnataka",
    "Management": "Trust",
    "ParentOrganization": "A. Shama Rao Foundation / Srinivas Group",
    "KeyPeople": [{"Name": "CA A. Raghavendra Rao", "Role": "President", "Details": "Chartered Accountant and founder of Srinivas Group of Institutions"}],
    "PoliticalAffiliation": "None direct / Educational foundation.",
    "FundingSource": "Srinivas Group funds, tuition fees, hospital clinical income.",
    "SummaryReport": "Established in 2011 at Mukka, Mangalore by A. Shama Rao Foundation. Self-financed."
  },
  {
    "SlNo": "255",
    "CollegeName": "Sapthagiri Institute of Medical Sciences & Research Centre Bangalore",
    "State": "Karnataka",
    "District": "Bengaluru",
    "University": "Rajiv Gandhi University of Health Sciences Karnataka",
    "Management": "Trust",
    "ParentOrganization": "Sri Srinivasa Educational & Charitable Trust",
    "KeyPeople": [
      {"Name": "Late G. Dayanand", "Role": "Founder Chairman", "Details": "Industrialist"},
      {"Name": "G. D. Manoj", "Role": "Executive Director", "Details": "Sapthagiri Group"}
    ],
    "PoliticalAffiliation": "None direct / Private business and educational trust.",
    "FundingSource": "Sapthagiri Group enterprise funds, tuition fees, hospital revenues.",
    "SummaryReport": "Established in 2011 on Hesaraghatta Main Road, Bangalore by Sri Srinivasa Educational & Charitable Trust. Self-financed."
  },
  {
    "SlNo": "256",
    "CollegeName": "SDM College of Medical Sciences & Hospital Sattur Dharwad",
    "State": "Karnataka",
    "District": "Dharwad",
    "University": "Rajiv Gandhi University of Health Sciences Karnataka",
    "Management": "Trust",
    "ParentOrganization": "SDM Educational Society / SDM University Dharwad",
    "KeyPeople": [{"Name": "Dr. D. Veerendra Heggade", "Role": "President & Chancellor", "Details": "Member of Parliament (Rajya Sabha, Nominated), Padma Vibhushan awardee, and Dharmadhikari of Shri Kshethra Dharmasthala"}],
    "PoliticalAffiliation": "Nominated MP (Rajya Sabha). Headed by Dr. D. Veerendra Heggade, revered spiritual leader and nominated Rajya Sabha Member of Parliament.",
    "FundingSource": "SDM Trust reserves, university tuition fees, SDM Hospital earnings.",
    "SummaryReport": "Established in 2003 in Dharwad by SDM Educational Society led by Rajya Sabha MP Dr. D. Veerendra Heggade. Constituent of SDM University. Self-funded philanthropic trust."
  },
  {
    "SlNo": "257",
    "CollegeName": "Navodaya Medical College Raichur",
    "State": "Karnataka",
    "District": "Raichur",
    "University": "Rajiv Gandhi University of Health Sciences Karnataka",
    "Management": "Trust",
    "ParentOrganization": "Navodaya Education Trust (NET)",
    "KeyPeople": [{"Name": "S. R. Reddy", "Role": "Founder Chairman", "Details": "Educationist and industrialist in Raichur"}],
    "PoliticalAffiliation": "Local political influence in Kalyana Karnataka (Raichur) region.",
    "FundingSource": "Navodaya Trust funds, tuition fees, hospital clinical income.",
    "SummaryReport": "Established in 2001 in Raichur by S. R. Reddy under Navodaya Education Trust. Self-financed."
  },
  {
    "SlNo": "258",
    "CollegeName": "Basaveswara Medical College and Hospital Chitradurga",
    "State": "Karnataka",
    "District": "Chitradurga",
    "University": "Rajiv Gandhi University of Health Sciences Karnataka",
    "Management": "Trust",
    "ParentOrganization": "Sri Jagadguru Murugharajendra (SJM) Vidyapeetha / Murugha Math",
    "KeyPeople": [{"Name": "Sri Shivamurthy Murugha Sharanaru", "Role": "Former President", "Details": "Head of SJM Vidyapeetha"}],
    "PoliticalAffiliation": "Lingayat Math Trust; significant local political and social standing in Chitradurga.",
    "FundingSource": "SJM Math trust reserves, student tuition fees, hospital treatment fees.",
    "SummaryReport": "Established in 2001 in Chitradurga by SJM Vidyapeetha (Sri Murugha Math). Self-financed Lingayat community educational trust."
  },
  {
    "SlNo": "259",
    "CollegeName": "Siddaganga Medical College and Research Institute Tumakuru",
    "State": "Karnataka",
    "District": "Tumakuru",
    "University": "Rajiv Gandhi University of Health Sciences Bengaluru",
    "Management": "Trust",
    "ParentOrganization": "Sri Siddaganga Education Society (SSES) / Siddaganga Math",
    "KeyPeople": [
      {"Name": "Sri Siddalinga Swamiji", "Role": "President", "Details": "Head of Sri Siddaganga Math"},
      {"Name": "Late Dr. Sri Sri Sri Shivakumara Swamiji", "Role": "Founder Visionary", "Details": "Karnataka Ratna awardee and centenarian spiritual icon"}
    ],
    "PoliticalAffiliation": "Revered Spiritual Math Trust; holds monumental non-partisan political respect across India.",
    "FundingSource": "Siddaganga Math trust reserves, tuition fees, hospital earnings.",
    "SummaryReport": "Established in 2022 in Tumakuru under Sri Siddaganga Education Society, founded by centenarian seer Dr. Shivakumara Swamiji. Self-financed philanthropic math trust."
  },
  {
    "SlNo": "263",
    "CollegeName": "Shri B M Patil Medical College Hospital & Research Centre Vijayapura",
    "State": "Karnataka",
    "District": "Vijayapura",
    "University": "Rajiv Gandhi University of Health Sciences Karnataka",
    "Management": "Trust",
    "ParentOrganization": "BLDE Association (Bijapur Lingayat District Educational Association) / BLDE Deemed University",
    "KeyPeople": [
      {"Name": "M. B. Patil", "Role": "President", "Details": "Cabinet Minister for Infrastructure Development, Large & Medium Industries (Karnataka, Congress) and sitting MLA (Babaleshwar)"},
      {"Name": "Late B. M. Patil", "Role": "Founder Visionary", "Details": "Former Minister and veteran leader"}
    ],
    "PoliticalAffiliation": "Congress Cabinet Minister. Governed by BLDE Association headed by senior Karnataka Cabinet Minister M. B. Patil.",
    "FundingSource": "BLDE Association trust reserves, deemed university fees, Shri B.M. Patil Hospital clinical earnings.",
    "SummaryReport": "Established in 1986 in Vijayapura by BLDE Association (est. 1910). Constituent college of BLDE Deemed University, headed by Cabinet Minister M. B. Patil. Self-financed."
  }
]

ka_sources = [
  {"SlNo": "191", "CollegeName": "BGS Medical College and Hospital Bengaluru", "Sources": ["https://bgsgims.edu.in/", "https://acu.edu.in/"]},
  {"SlNo": "192", "CollegeName": "PES University Institute of Medical Sciences and Research Bangalore", "Sources": ["https://pes.edu/", "https://en.wikipedia.org/wiki/M._R._Doreswamy"]},
  {"SlNo": "193", "CollegeName": "SR Patil Medical College and Hospital Bagalkot", "Sources": ["https://srpatilmedicalcollege.org/", "https://en.wikipedia.org/wiki/S._R._Patil"]},
  {"SlNo": "195", "CollegeName": "Sri Chamundeshwari Medical College Hospital & Research Institute", "Sources": ["https://scmchri.ac.in/", "https://en.wikipedia.org/wiki/A._C._Shanmugam"]},
  {"SlNo": "196", "CollegeName": "Khaja Bandanawaz University Faculty of Medical Sciences Gulbarga", "Sources": ["https://kbn.university/", "https://kbnmedical.com/"]},
  {"SlNo": "197", "CollegeName": "St. Johns Medical College Bangalore", "Sources": ["https://stjohns.in/", "https://en.wikipedia.org/wiki/St._John%27s_Medical_College"]},
  {"SlNo": "198", "CollegeName": "A J Institute of Medical Sciences & Research Centre Mangalore", "Sources": ["https://ajims.edu.in/"]},
  {"SlNo": "199", "CollegeName": "Raja Rajeswari Medical College & Hospital Bangalore", "Sources": ["https://rrmch.org/", "https://en.wikipedia.org/wiki/A._C._Shanmugam"]},
  {"SlNo": "200", "CollegeName": "Yenepoya Medical College Mangalore", "Sources": ["https://yenepoya.edu.in/"]},
  {"SlNo": "201", "CollegeName": "Al-Ameen Medical College Bijapur", "Sources": ["https://alameenmedical.org/"]},
  {"SlNo": "203", "CollegeName": "Vydehi Institute Of Medical Sciences & Research Centre Bangalore", "Sources": ["https://vims.ac.in/", "https://en.wikipedia.org/wiki/D._K._Audikesavulu"]},
  {"SlNo": "204", "CollegeName": "S S Institute of Medical Sciences & Research Centre Davangere", "Sources": ["https://ssimsrc.act.in/", "https://en.wikipedia.org/wiki/Shamanur_Shivashankarappa"]},
  {"SlNo": "206", "CollegeName": "M S Ramaiah Medical College Bangalore", "Sources": ["https://msrmc.ac.in/", "https://en.wikipedia.org/wiki/M._S._Ramaiah"]},
  {"SlNo": "208", "CollegeName": "Sri Siddhartha Medical College Tumkur", "Sources": ["https://ssmctumkur.org/", "https://en.wikipedia.org/wiki/G._Parameshwara"]},
  {"SlNo": "209", "CollegeName": "S. Nijalingappa Medical College & HSK Hospital & Research Centre Bagalkot", "Sources": ["https://snmcbgk.in/", "https://bvvssangha.org/"]},
  {"SlNo": "210", "CollegeName": "MVJ Medical College and Research Hospital Bangalore", "Sources": ["https://mvjmc.edu.in/"]},
  {"SlNo": "211", "CollegeName": "K S Hegde Medical Academy Mangalore", "Sources": ["https://kshema.nitte.edu.in/", "https://en.wikipedia.org/wiki/K._S._Hegde"]},
  {"SlNo": "215", "CollegeName": "Dr BR Ambedkar Medical College Bangalore", "Sources": ["https://bramc.edu.in/", "https://en.wikipedia.org/wiki/B._R._Jalappa"]},
  {"SlNo": "216", "CollegeName": "Mahadevappa Rampure Medical College Kalaburagi Gulbarga", "Sources": ["https://mrmcklb.edu.in/", "https://hkes.edu.in/"]},
  {"SlNo": "220", "CollegeName": "JSS Medical College Mysore", "Sources": ["https://jssuni.edu.in/JSSWEB/JSSMC/JSSMC.aspx"]},
  {"SlNo": "221", "CollegeName": "Kempegowda Institute of Medical Sciences Bangalore", "Sources": ["https://kimsbangalore.edu.in/"]},
  {"SlNo": "222", "CollegeName": "JJM Medical College Davangere", "Sources": ["https://jjmc.edu.in/", "https://en.wikipedia.org/wiki/Shamanur_Shivashankarappa"]},
  {"SlNo": "223", "CollegeName": "Kasturba Medical College Manipal", "Sources": ["https://manipal.edu/kmc-manipal.html", "https://en.wikipedia.org/wiki/Kasturba_Medical_College,_Manipal"]},
  {"SlNo": "224", "CollegeName": "Kasturba Medical College Mangalore", "Sources": ["https://manipal.edu/kmc-mangalore.html"]},
  {"SlNo": "225", "CollegeName": "Sri Devaraj URS Medical College Kolar", "Sources": ["https://sduu.ac.in/", "https://sdumc.ac.in/"]},
  {"SlNo": "226", "CollegeName": "K V G Medical College Sullia", "Sources": ["https://kvgmc.org/"]},
  {"SlNo": "227", "CollegeName": "Jawaharlal Nehru Medical College Belgaum", "Sources": ["https://jnmc.edu/", "https://en.wikipedia.org/wiki/Prabhakar_Kore"]},
  {"SlNo": "228", "CollegeName": "Adichunchanagiri Institute of Medical Sciences Bellur", "Sources": ["https://bims.edu.in/"]},
  {"SlNo": "229", "CollegeName": "Father Mullers Medical College Mangalore", "Sources": ["https://fathermuller.edu.in/medicalcollege/"]},
  {"SlNo": "232", "CollegeName": "G R Medical College Hospital & Research Centre Mangaluru", "Sources": ["https://grmc.edu.in/"]},
  {"SlNo": "233", "CollegeName": "Jagadguru Gangadhar Mahaswamigalu Moorusavirmath Medical College Hubli", "Sources": ["https://jmmc.kledeemeduniversity.edu.in/"]},
  {"SlNo": "234", "CollegeName": "Sri Madhusudan Sai Institute of Medical Sciences & Research Chikballapur", "Sources": ["https://smsimsr.org/", "https://pib.gov.in/PressReleaseIframePage.aspx?PRID=1910609"]},
  {"SlNo": "235", "CollegeName": "Dr. Chandramma Dayananda Sagar Instt. of Medical Education & Research Harohalli Hubli", "Sources": ["https://cdsimer.edu.in/"]},
  {"SlNo": "237", "CollegeName": "Sri siddhartha Institute of Medical Sciences & Research Centre Bengaluru", "Sources": ["https://ssimsrc.in/"]},
  {"SlNo": "238", "CollegeName": "East Point College of Medical Sciences & Research Centre Bengaluru", "Sources": ["https://eastpoint.ac.in/medical-college/"]},
  {"SlNo": "239", "CollegeName": "Sambhram Institute of Medical Sciences & Research Kolar", "Sources": ["https://sambhramimsr.com/"]},
  {"SlNo": "240", "CollegeName": "Akash Institute of Medical Sciences & Research Centre Devanhalli Bangalore", "Sources": ["https://akashinstitute.in/"]},
  {"SlNo": "241", "CollegeName": "Kanachur Institute of Medical Sciences Mangalore", "Sources": ["https://kanachurims.com/"]},
  {"SlNo": "248", "CollegeName": "The Oxford Medical College Hospital & Research Centre Bangalore", "Sources": ["http://theoxfordmedical.org/"]},
  {"SlNo": "250", "CollegeName": "Shridevi Institute of Medical Sciences & Research Hospital Tumkur", "Sources": ["https://shridevimedical.org/"]},
  {"SlNo": "251", "CollegeName": "BGS Global Institute of Medical Sciences Bangalore", "Sources": ["https://bgsgims.edu.in/"]},
  {"SlNo": "252", "CollegeName": "Subbaiah Institute of Medical Sciences Shimoga", "Sources": ["https://smcshimoga.org/"]},
  {"SlNo": "254", "CollegeName": "Srinivas Institute of Medical Research Centre Srinivasnagar Mangalore", "Sources": ["https://srinivasgroup.com/simsrc/"]},
  {"SlNo": "255", "CollegeName": "Sapthagiri Institute of Medical Sciences & Research Centre Bangalore", "Sources": ["https://sapthagiri.edu.in/"]},
  {"SlNo": "256", "CollegeName": "SDM College of Medical Sciences & Hospital Sattur Dharwad", "Sources": ["https://sdmmedicalcollege.org/", "https://en.wikipedia.org/wiki/D._Veerendra_Heggade"]},
  {"SlNo": "257", "CollegeName": "Navodaya Medical College Raichur", "Sources": ["https://navodaya.edu.in/nmc/"]},
  {"SlNo": "258", "CollegeName": "Basaveswara Medical College and Hospital Chitradurga", "Sources": ["https://bmch.co.in/"]},
  {"SlNo": "259", "CollegeName": "Siddaganga Medical College and Research Institute Tumakuru", "Sources": ["https://smcri.edu.in/"]},
  {"SlNo": "263", "CollegeName": "Shri B M Patil Medical College Hospital & Research Centre Vijayapura", "Sources": ["https://bldedu.ac.in/", "https://en.wikipedia.org/wiki/M._B._Patil"]}
]

own.extend(ka_records)
src.extend(ka_sources)

save_db(own, src)
