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
    print(f"TOTAL COMPLETED: {len(sorted_own)} records")

own, src = load_db()

final_records = [
  # --- BIHAR ---
  {
    "SlNo": "60",
    "CollegeName": "Katihar Medical College Katihar",
    "State": "Bihar",
    "District": "Katihar",
    "University": "Al-Karim University Katihar",
    "Management": "Trust",
    "ParentOrganization": "Al-Karim Educational Trust",
    "KeyPeople": [{"Name": "Ahmad Ashfaque Karim", "Role": "Founder & Chancellor", "Details": "Former Member of Parliament (Rajya Sabha, RJD) and founder of Al-Karim Educational Trust"}],
    "PoliticalAffiliation": "RJD Leader. Founder Ahmad Ashfaque Karim is a former RJD Rajya Sabha MP.",
    "FundingSource": "Al-Karim Trust reserves, university tuition fees, hospital operational income.",
    "SummaryReport": "Established in 1987 in Katihar as a premier Muslim minority medical college by former RJD MP Ahmad Ashfaque Karim. Constituent of Al-Karim Private University. Self-financed."
  },
  {
    "SlNo": "61",
    "CollegeName": "Mata Gujri Memorial Medical College Kishanganj",
    "State": "Bihar",
    "District": "Kishanganj",
    "University": "B.N. Mandal University",
    "Management": "Trust",
    "ParentOrganization": "Mata Gujri Memorial Medical College Trust / Takht Sri Harimandir Ji Patna Sahib",
    "KeyPeople": [{"Name": "Takht Sri Harimandir Ji Prabandhak Committee", "Role": "Managing Body", "Details": "Sikh Religious Shrine Board"}],
    "PoliticalAffiliation": "None direct / Sikh Religious Minority Institution.",
    "FundingSource": "Sikh shrine trust endowments, student tuition fees, Lions Seva Kendra hospital earnings.",
    "SummaryReport": "Established in 1990 in Kishanganj as India's only Sikh religious minority medical college in Bihar. Managed under Sikh shrine board trust. Self-funded."
  },
  {
    "SlNo": "66",
    "CollegeName": "Radha Devi Jageshwari Memorial Medical College and Hospital Turki",
    "State": "Bihar",
    "District": "Muzaffarpur",
    "University": "Aryabhatta Knowledge University Patna",
    "Management": "Society",
    "ParentOrganization": "Sri Jageshwari Memorial Trust",
    "KeyPeople": [{"Name": "Dr. R. D. Sharma", "Role": "Chairman", "Details": "RDJM Medical Group"}],
    "PoliticalAffiliation": "Local political connections in Muzaffarpur region.",
    "FundingSource": "Tuition fees, hospital earnings.",
    "SummaryReport": "Established at Turki, Muzaffarpur by Sri Jageshwari Memorial Trust. Self-financed."
  },
  {
    "SlNo": "67",
    "CollegeName": "Shree Narayan Medical Institute and Hospital Rohtas",
    "State": "Bihar",
    "District": "Saharsa",
    "University": "Bhupendra Narayan Mandal University Madhepura",
    "Management": "Trust",
    "ParentOrganization": "Shree Narayan Educational Trust",
    "KeyPeople": [{"Name": "R. K. Singh", "Role": "Chairman", "Details": "Shree Narayan Group"}],
    "PoliticalAffiliation": "None direct / Educational trust.",
    "FundingSource": "Tuition fees, hospital earnings.",
    "SummaryReport": "Established in Saharsa/Rohtas region by Shree Narayan Educational Trust. Self-financed."
  },
  {
    "SlNo": "70",
    "CollegeName": "Netaji Subhas Medical College & Hospital Amhara Bihta Patna",
    "State": "Bihar",
    "District": "Patna",
    "University": "Aryabhatta Knowledge University Patna",
    "Management": "Society",
    "ParentOrganization": "Sitwanto Devi Mahila Kalyan Sansthan",
    "KeyPeople": [{"Name": "M. M. Singh", "Role": "Chairman", "Details": "Netaji Subhas Group"}],
    "PoliticalAffiliation": "None direct / Educational society.",
    "FundingSource": "Group capital, student tuition fees, hospital clinical income.",
    "SummaryReport": "Established in 2020 at Bihta, Patna by Sitwanto Devi Mahila Kalyan Sansthan. Self-financed."
  },
  {
    "SlNo": "71",
    "CollegeName": "Lord Buddha Koshi Medical College and Hospital Saharsa",
    "State": "Bihar",
    "District": "Saharsa",
    "University": "B.N. Mandal University",
    "Management": "Trust",
    "ParentOrganization": "Lord Buddha Koshi Medical College Trust",
    "KeyPeople": [{"Name": "Dr. Ramesh Chandra Yadav", "Role": "Chairman", "Details": "Koshi Educational Trust"}],
    "PoliticalAffiliation": "Local political links in Kosi region of Bihar.",
    "FundingSource": "Tuition fees, hospital clinical earnings.",
    "SummaryReport": "Established in 2012 in Saharsa by Lord Buddha Koshi Trust. Self-financed."
  },
  {
    "SlNo": "72",
    "CollegeName": "Madhubani Medical College Madhubani",
    "State": "Bihar",
    "District": "Madhubani",
    "University": "Aryabhatta Knowledge University Patna",
    "Management": "Trust",
    "ParentOrganization": "Falah-e-Aam Trust",
    "KeyPeople": [{"Name": "Dr. Faiyaz Ahmad", "Role": "Founder Chairman", "Details": "Member of Parliament (Rajya Sabha, RJD) and former MLA"}],
    "PoliticalAffiliation": "RJD Leader. Founder Dr. Faiyaz Ahmad is a sitting RJD Rajya Sabha MP.",
    "FundingSource": "Falah-e-Aam Trust funds, tuition fees, hospital clinical income.",
    "SummaryReport": "Established in 2019 in Madhubani as a Muslim minority medical college by RJD MP Dr. Faiyaz Ahmad. Self-financed."
  },
  {
    "SlNo": "76",
    "CollegeName": "Narayan Medical College & Hospital Sasaram",
    "State": "Bihar",
    "District": "Rohtas",
    "University": "Gopal Narayan Singh University",
    "Management": "Trust",
    "ParentOrganization": "Deo Mangal Memorial Trust / Gopal Narayan Singh Private University",
    "KeyPeople": [{"Name": "Gopal Narayan Singh", "Role": "Founder & Chancellor", "Details": "Former Member of Parliament (Rajya Sabha, BJP) and senior BJP leader"}],
    "PoliticalAffiliation": "BJP Leader. Founder Gopal Narayan Singh is a senior BJP political leader and former Rajya Sabha MP.",
    "FundingSource": "GNS Private University tuition fees, super-specialty hospital clinical earnings.",
    "SummaryReport": "Established in 2008 at Jamuhar, Sasaram. Flagship constituent of Gopal Narayan Singh Private University founded by BJP leader Gopal Narayan Singh. Self-financed."
  },

  # --- CHATTISGARH ---
  {
    "SlNo": "78",
    "CollegeName": "Abhishek Mishra Memorial Medical College & RC Bhilai",
    "State": "Chattisgarh",
    "District": "Durg",
    "University": "Pt. Deendayal Upadhyay Memorial Health Sciences and Ayush University of Chhattisgarh Raipur",
    "Management": "Private",
    "ParentOrganization": "Shri Gangajali Education Society (SGES)",
    "KeyPeople": [{"Name": "IP Mishra", "Role": "Chairman", "Details": "SGES Group"}],
    "PoliticalAffiliation": "None direct / Educational society.",
    "FundingSource": "Tuition fees, hospital earnings.",
    "SummaryReport": "Established in Bhilai under Shri Gangajali Education Society. Self-financed."
  },
  {
    "SlNo": "79",
    "CollegeName": "Shri Rawatpura Sarkar Institute of Medical Sciences and Research Atal Nagar Raipur",
    "State": "Chattisgarh",
    "District": "Raipur",
    "University": "Pandit Deendayal Upadhyay Memorial Health Science & Ayush University of Chattisgarh",
    "Management": "Private",
    "ParentOrganization": "Shri Rawatpura Sarkar Lok Kalyan Trust",
    "KeyPeople": [{"Name": "Anant Shri Vibhushit Shri Rawatpura Sarkar Maharaj", "Role": "Founder & Spiritual Patron", "Details": "Rawatpura Sarkar Ashram Trust"}],
    "PoliticalAffiliation": "Spiritual Trust with bipartisan political influence across Central India.",
    "FundingSource": "Ashram trust endowments, student tuition fees, hospital clinical income.",
    "SummaryReport": "Established at Naya Raipur (Atal Nagar) by Shri Rawatpura Sarkar Lok Kalyan Trust. Self-funded philanthropic trust."
  },
  {
    "SlNo": "85",
    "CollegeName": "Shri Balaji Institute of Medical Science Mowa",
    "State": "Chattisgarh",
    "District": "Raipur",
    "University": "Pandit Deendayal Upadhyay Memorial Health Science & Ayush University of Chattisgarh",
    "Management": "Society",
    "ParentOrganization": "Shri Balaji Health and Education Society",
    "KeyPeople": [{"Name": "Dr. Devendra Naik", "Role": "Founder & CMD", "Details": "Shri Balaji Hospital Raipur"}],
    "PoliticalAffiliation": "None direct / Healthcare enterprise.",
    "FundingSource": "Shri Balaji Hospital corporate earnings, student tuition fees.",
    "SummaryReport": "Established in 2021 at Mowa, Raipur by Dr. Devendra Naik. Self-financed."
  },
  {
    "SlNo": "86",
    "CollegeName": "Raipur Institute of Medical Sciences (RIMS) Raipur",
    "State": "Chattisgarh",
    "District": "Raipur",
    "University": "Pt. Deendayal Upadhyay Memorial Health Sciences and Ayush University Raipur",
    "Management": "Society",
    "ParentOrganization": "Lord Buddha Educational Society",
    "KeyPeople": [{"Name": "Dr. Gambhir Singh", "Role": "Chairman", "Details": "RIMS Raipur"}],
    "PoliticalAffiliation": "Local political ties in Chhattisgarh.",
    "FundingSource": "Tuition fees, hospital operational income.",
    "SummaryReport": "Established in 2012 at Bhansoj, Raipur by Lord Buddha Educational Society. Self-financed."
  },
  {
    "SlNo": "87",
    "CollegeName": "Shri Shankaracharya Institute of Medical Sciences Bhilai",
    "State": "Chattisgarh",
    "District": "Durg",
    "University": "Pt. Deendayal Upadhyay Memorial Health Sciences and Ayush University Raipur",
    "Management": "Society",
    "ParentOrganization": "Shri Gangajali Education Society (SGES)",
    "KeyPeople": [
      {"Name": "IP Mishra", "Role": "President", "Details": "SGES Group"},
      {"Name": "Vijay Kumar Gupta", "Role": "Chairman", "Details": "SSIMS"}
    ],
    "PoliticalAffiliation": "Prominent business & educational standing in Bhilai/Durg.",
    "FundingSource": "SGES Group funds, tuition fees, hospital clinical income.",
    "SummaryReport": "Established in 2013 at Junwani, Bhilai by Shri Gangajali Education Society. Self-financed."
  },

  # --- DELHI ---
  {
    "SlNo": "96",
    "CollegeName": "Army College of Medical Sciences New Delhi",
    "State": "Delhi",
    "District": "South West Delhi",
    "University": "Guru Gobind Singh Indraprastha University",
    "Management": "Trust",
    "ParentOrganization": "Army Welfare Education Society (AWES) / Indian Army",
    "KeyPeople": [
      {"Name": "Chief of Army Staff (COAS)", "Role": "Patron-in-Chief", "Details": "Indian Army"},
      {"Name": "Army Commander, HQ Western Command", "Role": "Patron", "Details": "Indian Army"}
    ],
    "PoliticalAffiliation": "Statutory Defense Welfare Institution (Non-partisan Indian Armed Forces Establishment).",
    "FundingSource": "Army Welfare Education Society welfare funds, subsidized tuition fees (for wards of Army personnel/veterans), Base Hospital clinical support.",
    "SummaryReport": "Premier medical college established in 2008 at Delhi Cantt by Army Welfare Education Society (AWES) for children of serving & retired Indian Army personnel. Non-profit defense welfare institution."
  },
  {
    "SlNo": "104",
    "CollegeName": "Hamdard Institute of Medical Sciences & Research New Delhi",
    "State": "Delhi",
    "District": "South Delhi",
    "University": "University of Jamia Hamdard",
    "Management": "Society",
    "ParentOrganization": "Hamdard National Foundation (HNF) / Jamia Hamdard Deemed University",
    "KeyPeople": [
      {"Name": "Late Hakeem Abdul Hameed", "Role": "Founder", "Details": "Unani physician, Padma Bhushan awardee, and founder of Hamdard Laboratories"},
      {"Name": "Hammad Ahmed", "Role": "Chancellor", "Details": "Jamia Hamdard"}
    ],
    "PoliticalAffiliation": "None direct / Globally acclaimed Muslim Minority Deemed University and Charitable Foundation.",
    "FundingSource": "Hamdard National Foundation CSR & business profits, university tuition fees, Hakeem Abdul Hameed Centenary Hospital earnings.",
    "SummaryReport": "Established in 2012 at Hamdard Nagar, New Delhi as constituent medical college of Jamia Hamdard Deemed University. Self-funded philanthropic minority trust."
  },

  # --- HARYANA ---
  {
    "SlNo": "147",
    "CollegeName": "Maharishi Markandeshwar College of Medical Sciences & Research Sadopur",
    "State": "Haryana",
    "District": "Ambala",
    "University": "Maharishi Markandeshwar University Deemed Ambala",
    "Management": "Private",
    "ParentOrganization": "Maharishi Markandeshwar University Trust",
    "KeyPeople": [{"Name": "Tarsem Kumar Garg", "Role": "Founder & Chancellor", "Details": "Former BJP leader and Chancellor of MMU"}],
    "PoliticalAffiliation": "BJP Connections. Founder Tarsem Garg is a former BJP political leader.",
    "FundingSource": "MMU Deemed University fees, hospital clinical earnings.",
    "SummaryReport": "Constituent medical college of MMU Deemed University at Sadopur, Ambala. Self-financed."
  },
  {
    "SlNo": "148",
    "CollegeName": "Amrita School of Medicine Faridabad",
    "State": "Haryana",
    "District": "Faridabad",
    "University": "Amrita Vishwa Vidyapeetham",
    "Management": "Trust",
    "ParentOrganization": "Mata Amritanandamayi Math (MAM Trust) / Amrita Vishwa Vidyapeetham",
    "KeyPeople": [{"Name": "Mata Amritanandamayi (Amma)", "Role": "Chancellor & Founder", "Details": "World-renowned spiritual leader"}],
    "PoliticalAffiliation": "Global Spiritual Trust (Inaugurated by Prime Minister Narendra Modi in 2022).",
    "FundingSource": "MAM Trust endowments, global philanthropic contributions, university tuition fees, 2600-bed Amrita Super-specialty Hospital earnings.",
    "SummaryReport": "Inaugurated in 2022 in Faridabad by PM Narendra Modi as Asia's largest private super-specialty hospital and medical research campus. Self-funded spiritual philanthropic trust."
  },
  {
    "SlNo": "149",
    "CollegeName": "Maharaja Agrasen Medical College Agroha",
    "State": "Haryana",
    "District": "Hisar",
    "University": "PT. B.D. Sharma University of Health Sciences Rohtak",
    "Management": "Trust",
    "ParentOrganization": "Maharaja Agrasen Medical Education & Scientific Society",
    "KeyPeople": [
      {"Name": "Savitri Jindal", "Role": "President", "Details": "Chairperson Emeritus of O.P. Jindal Group, Cabinet Minister (Haryana, BJP/Congress)"},
      {"Name": "Naveen Jindal", "Role": "Patron", "Details": "Member of Parliament (BJP, Kurukshetra) and Chairman of Jindal Steel & Power"}
    ],
    "PoliticalAffiliation": "Jindal Family (BJP/Congress). Led by Savitri Jindal (Haryana Cabinet Minister) and MP Naveen Jindal.",
    "FundingSource": "Jindal Industrial Group CSR capital, Haryana State Govt grant-in-aid (50%), student tuition fees, hospital clinical income.",
    "SummaryReport": "Established in 1988 at Agroha, Hisar by O.P. Jindal. Unique public-private trust model supported by Jindal Group and Haryana State Government."
  },
  {
    "SlNo": "150",
    "CollegeName": "Faculty of Medicine and Health Sciences Gurgaon",
    "State": "Haryana",
    "District": "Gurugram",
    "University": "SGT University Gurugram",
    "Management": "Trust",
    "ParentOrganization": "Dashmesh Educational Charitable Trust",
    "KeyPeople": [
      {"Name": "Manmohan Singh Chawla", "Role": "Managing Trustee", "Details": "SGT University"},
      {"Name": "Ram Bahadur Rai", "Role": "Chancellor", "Details": "Padma Shri journalist and Chairman of Indira Gandhi National Centre for the Arts"}
    ],
    "PoliticalAffiliation": "Prominent cultural & educational stature.",
    "FundingSource": "SGT Private University tuition fees, 800-bed hospital operational income.",
    "SummaryReport": "Established in 2010 at Budhera, Gurugram as constituent medical college of SGT University. Self-financed."
  },
  {
    "SlNo": "152",
    "CollegeName": "Maharishi Markandeshwar Institute Of Medical Sciences & Research Mullana Ambala",
    "State": "Haryana",
    "District": "Ambala",
    "University": "Maharishi Markandeshwar University Deemed Ambala",
    "Management": "Trust",
    "ParentOrganization": "Maharishi Markandeshwar Education Trust",
    "KeyPeople": [{"Name": "Tarsem Kumar Garg", "Role": "Founder Chancellor", "Details": "Former BJP leader"}],
    "PoliticalAffiliation": "BJP Connections. Founded by Tarsem Garg.",
    "FundingSource": "MMU Deemed University fees, 1100-bed MM Hospital clinical income.",
    "SummaryReport": "Established in 2003 at Mullana, Ambala. Flagship medical college of MMU Deemed University. Self-financed."
  },
  {
    "SlNo": "153",
    "CollegeName": "Al Falah School of Medical Sciences & Research Centre Faridabad",
    "State": "Haryana",
    "District": "Faridabad",
    "University": "Al-Falah University",
    "Management": "Private",
    "ParentOrganization": "Al-Falah Charitable Trust",
    "KeyPeople": [{"Name": "Jawad Ahmed Siddiqui", "Role": "Founder & Chancellor", "Details": "Al-Falah University"}],
    "PoliticalAffiliation": "None direct / Muslim Minority Private University.",
    "FundingSource": "Al-Falah University tuition fees, hospital clinical income.",
    "SummaryReport": "Established in 2019 at Dhoj, Faridabad as constituent medical college of Al-Falah Muslim Minority University. Self-financed."
  },
  {
    "SlNo": "155",
    "CollegeName": "Adesh Medical College and Hospital Shahabad Kurukshetra",
    "State": "Haryana",
    "District": "Kurukshetra",
    "University": "PT. B.D. Sharma University of Health Sciences Rohtak",
    "Management": "Society",
    "ParentOrganization": "Adesh Welfare Society",
    "KeyPeople": [{"Name": "Dr. H. S. Gill", "Role": "Chairman", "Details": "Adesh Group of Institutions"}],
    "PoliticalAffiliation": "None direct / Educational society.",
    "FundingSource": "Adesh Group funds, tuition fees, hospital earnings.",
    "SummaryReport": "Established in 2017 at Mohri, Shahabad, Kurukshetra by Adesh Welfare Society. Self-financed."
  },
  {
    "SlNo": "156",
    "CollegeName": "N.C. Medical College & Hospital Panipat",
    "State": "Haryana",
    "District": "Panipat",
    "University": "PT. B.D. Sharma University of Health Sciences Rohtak",
    "Management": "Trust",
    "ParentOrganization": "Shanti Devi Charitable Trust",
    "KeyPeople": [{"Name": "S. N. Sharma", "Role": "Chairman", "Details": "NC Group"}],
    "PoliticalAffiliation": "None direct / Educational trust.",
    "FundingSource": "Tuition fees, hospital earnings.",
    "SummaryReport": "Established in 2016 at Israna, Panipat by Shanti Devi Charitable Trust. Self-financed."
  },
  {
    "SlNo": "157",
    "CollegeName": "World College of Medical Sciences & Research Jhajjar",
    "State": "Haryana",
    "District": "Jhajjar",
    "University": "PT. B.D. Sharma University of Health Sciences Rohtak",
    "Management": "Trust",
    "ParentOrganization": "Amma Chandravati Educational & Charitable Trust",
    "KeyPeople": [{"Name": "Dr. Narendra Singh", "Role": "Chairman", "Details": "WCMSR Jhajjar"}],
    "PoliticalAffiliation": "None direct / Educational trust.",
    "FundingSource": "Tuition fees, hospital operational income.",
    "SummaryReport": "Established in 2016 at Gurawar, Jhajjar by Amma Chandravati Educational Trust. Self-financed."
  },

  # --- HIMACHAL PRADESH ---
  {
    "SlNo": "168",
    "CollegeName": "Maharishi Markandeshwar Medical College & Hospital Solan",
    "State": "Himachal Pradesh",
    "District": "Solan",
    "University": "Maharishi Markandeshwar University Kumarhatti Solan",
    "Management": "Trust",
    "ParentOrganization": "Maharishi Markandeshwar University Trust",
    "KeyPeople": [{"Name": "Tarsem Kumar Garg", "Role": "Chancellor", "Details": "Former BJP leader"}],
    "PoliticalAffiliation": "BJP Connections. MMU Trust.",
    "FundingSource": "MMU Solan tuition fees, hospital clinical income.",
    "SummaryReport": "Established in 2013 at Kumarhatti, Solan as Himachal Pradesh's first private medical college under MMU Trust. Self-financed."
  },

  # --- JAMMU & KASHMIR ---
  {
    "SlNo": "181",
    "CollegeName": "Acharya Shri Chander College of Medical Sciences Jammu",
    "State": "Jammu & Kashmir",
    "District": "Jammu",
    "University": "Jammu University",
    "Management": "Trust",
    "ParentOrganization": "Shri Chander Chinar Bada Akhara Udasin Trust",
    "KeyPeople": [{"Name": "Mahant Jamesvar Das", "Role": "President & Trustee", "Details": "Bada Akhara Udasin Trust"}],
    "PoliticalAffiliation": "Spiritual Hindu Religious Trust.",
    "FundingSource": "Bada Akhara Udasin trust endowments, student tuition fees, ASCOMS hospital clinical earnings.",
    "SummaryReport": "Established in 1996 at Sidhra, Jammu by Shri Chander Chinar Bada Akhara Udasin Trust. J&K's pioneer private medical college. Self-funded."
  },

  # --- JHARKHAND ---
  {
    "SlNo": "186",
    "CollegeName": "Laxmi Chandravansi Medical College and Hospital Bishrampur",
    "State": "Jharkhand",
    "District": "Palamu",
    "University": "Ramchandra Chandravansi University Bishrampur Palamu",
    "Management": "Trust",
    "ParentOrganization": "Ramchandra Chandravansi Welfare Trust",
    "KeyPeople": [{"Name": "Ramchandra Chandravansi", "Role": "Founder & Chancellor", "Details": "Former Health Minister of Jharkhand (BJP) and MLA (Bishrampur)"}],
    "PoliticalAffiliation": "BJP Leader. Founder Ramchandra Chandravansi is a former Health Minister of Jharkhand.",
    "FundingSource": "RC University tuition fees, hospital clinical earnings.",
    "SummaryReport": "Established in 2021 in Bishrampur, Palamu by former Jharkhand Health Minister Ramchandra Chandravansi. Self-financed."
  },
  {
    "SlNo": "187",
    "CollegeName": "Manipal Tata Medical College Baridih Jameshedpur",
    "State": "Jharkhand",
    "District": "East Singhbhum",
    "University": "Manipal Academy of Higher Education Deemed Manipal",
    "Management": "Trust",
    "ParentOrganization": "Manipal Academy of Higher Education (MAHE Deemed University) & Tata Steel Consortium",
    "KeyPeople": [
      {"Name": "Dr. Ramdas M. Pai", "Role": "Chancellor", "Details": "MAHE"},
      {"Name": "N. Chandrasekaran", "Role": "Chairman", "Details": "Tata Sons / Tata Steel"}
    ],
    "PoliticalAffiliation": "None direct / Apex Public-Private Academic & Corporate Consortium (MAHE + Tata Steel).",
    "FundingSource": "Tata Steel institutional infrastructure support, MAHE tuition fees, Tata Main Hospital (TMH) clinical facilities.",
    "SummaryReport": "Established in 2020 at Baridih, Jamshedpur as a premier consortium between MAHE Deemed University and Tata Steel. Self-financed."
  },

  # --- NORTH EAST (MANIPUR, MEGHALAYA, NAGALAND, SIKKIM, TRIPURA) ---
  {
    "SlNo": "410",
    "CollegeName": "Shija Academy of Health Sciences Imphal",
    "State": "Manipur",
    "District": "Imphal West",
    "University": "Manipur University",
    "Management": "Private",
    "ParentOrganization": "Shija Hospitals & Research Institute Pvt Ltd (SHRI)",
    "KeyPeople": [{"Name": "Dr. Khundrakpam Palin", "Role": "Chairman & Managing Director", "Details": "Surgeon and founder of Shija Healthcare Group"}],
    "PoliticalAffiliation": "None direct / First homegrown private medical college in North East India.",
    "FundingSource": "Shija Hospitals Ltd corporate revenues, student tuition fees, clinical earnings.",
    "SummaryReport": "Established in 2021 at Langol, Imphal as Manipur's first private medical college by Dr. Kh. Palin. Self-financed corporate healthcare institution."
  },
  {
    "SlNo": "413",
    "CollegeName": "PA Sangama International Medical College and Hospital",
    "State": "Meghalaya",
    "District": "Ri-Bhoi",
    "University": "University of Science and Technology Meghalaya",
    "Management": "Trust",
    "ParentOrganization": "Education Research & Development Foundation (ERDF) / USTM",
    "KeyPeople": [
      {"Name": "Mahbubul Hoque", "Role": "Chancellor & Founder", "Details": "Educationist and Chairman of ERDF"},
      {"Name": "Late P. A. Sangma", "Role": "Namesake Visionary", "Details": "Former Speaker of Lok Sabha and Chief Minister of Meghalaya"}
    ],
    "PoliticalAffiliation": "Named in honor of former Lok Sabha Speaker P. A. Sangma; high political stature in North East.",
    "FundingSource": "ERDF Trust funds, USTM university tuition fees, super-specialty hospital earnings.",
    "SummaryReport": "Established at Techno City, Khanapara under USTM/ERDF Trust, named after legendary North East leader P. A. Sangma. Self-financed."
  },
  {
    "SlNo": "416",
    "CollegeName": "Nagaland Institute of Medical Sciences & Research Kohima",
    "State": "Nagaland",
    "District": "Kohima",
    "University": "Nagaland University",
    "Management": "Society",
    "ParentOrganization": "Nagaland Medical Education Society (Govt of Nagaland)",
    "KeyPeople": [{"Name": "Department of Health & Family Welfare", "Role": "Governing Body", "Details": "Government of Nagaland"}],
    "PoliticalAffiliation": "State Government Autonomous Society.",
    "FundingSource": "Government of Nagaland budgetary support, Ministry of DoNER, PMSSY central scheme funds.",
    "SummaryReport": "Inaugurated in 2023 at Phriebagei, Kohima as Nagaland's FIRST medical college, operated by Nagaland Govt Autonomous Society."
  },
  {
    "SlNo": "501",
    "CollegeName": "Sikkim Manipal Institute of Medical Sciences Gangtok",
    "State": "Sikkim",
    "District": "East Sikkim",
    "University": "Sikkim Manipal Univ. of Health Medical & Tech. Scs",
    "Management": "Trust",
    "ParentOrganization": "Sikkim Manipal University (Government of Sikkim + Manipal Education & Medical Group MEMG Consortium)",
    "KeyPeople": [
      {"Name": "Governor of Sikkim", "Role": "Ex-Officio Chancellor", "Details": "Government of Sikkim"},
      {"Name": "Dr. Ramdas M. Pai", "Role": "Pro-Chancellor", "Details": "MEMG / MAHE"}
    ],
    "PoliticalAffiliation": "State Government + Corporate PPP Consortium.",
    "FundingSource": "MEMG private capital investment, Govt of Sikkim state partnership, student tuition fees, Central Referral Hospital revenues.",
    "SummaryReport": "Established in 1997 at Tadong, Gangtok as India's pioneer Public-Private Partnership (PPP) medical university between Govt of Sikkim and Manipal Group. Self-funded."
  },
  {
    "SlNo": "644",
    "CollegeName": "Tripura Santiniketan Medical College West Tripura",
    "State": "Tripura",
    "District": "West Tripura",
    "University": "Tripura University",
    "Management": "Trust",
    "ParentOrganization": "Malay Peetha Trust / Santiniketan Society",
    "KeyPeople": [{"Name": "Chandreshwar Prasad Singh", "Role": "Chairman", "Details": "Santiniketan Group"}],
    "PoliticalAffiliation": "None direct / Educational trust.",
    "FundingSource": "Tuition fees, hospital earnings.",
    "SummaryReport": "Established at Ranirkhamar, Madhuban, West Tripura by Santiniketan Society. Self-financed."
  },
  {
    "SlNo": "646",
    "CollegeName": "Tripura Medical College and Dr. B R A M Teaching Hospital Agartala",
    "State": "Tripura",
    "District": "West Tripura",
    "University": "Tripura University",
    "Management": "Trust",
    "ParentOrganization": "Society for Tripura Medical College (STMC - Govt of Tripura Autonomous Society)",
    "KeyPeople": [{"Name": "Chief Secretary / Health Secretary", "Role": "Chairman", "Details": "Government of Tripura"}],
    "PoliticalAffiliation": "State Government Autonomous Society.",
    "FundingSource": "Government of Tripura subventions, student fees, BRAM teaching hospital service charges.",
    "SummaryReport": "Established in 2006 at Hapania, Agartala by Society for Tripura Medical College (STMC) under Govt of Tripura Health Dept. Public-Trust society."
  },

  # --- ODISHA / ORISSA ---
  {
    "SlNo": "418",
    "CollegeName": "Institute of Medical Sciences & SUM Hospital Campus Bhubaneswar II",
    "State": "Orissa",
    "District": "Khordha",
    "University": "Siksha O Anusandhan University Bhubaneswar",
    "Management": "Trust",
    "ParentOrganization": "Siksha 'O' Anusandhan (SOA Deemed University Trust)",
    "KeyPeople": [{"Name": "Prof. Dr. Manojranjan Nayak", "Role": "Founder & President", "Details": "Educationist and founder of SOA University"}],
    "PoliticalAffiliation": "Significant media & educational stature in Odisha (Prameya news group background).",
    "FundingSource": "SOA Deemed University tuition fees, SUM Hospital clinical earnings.",
    "SummaryReport": "Second medical college campus under SOA Deemed University in Bhubaneswar. Self-financed."
  },
  {
    "SlNo": "429",
    "CollegeName": "Hi-Tech Medical College & Hospital Rourkela",
    "State": "Orissa",
    "District": "Sundargarh",
    "University": "Sambalpur University",
    "Management": "Trust",
    "ParentOrganization": "Vigyan Bharati Educational Trust (VBET)",
    "KeyPeople": [{"Name": "Dr. Tirupati Panigrahi", "Role": "Founder Chairman", "Details": "Hi-Tech Group"}],
    "PoliticalAffiliation": "Prominent business & political connections in Odisha.",
    "FundingSource": "Hi-Tech Group reserves, tuition fees, hospital operational income.",
    "SummaryReport": "Established in 2012 in Rourkela by Vigyan Bharati Educational Trust. Self-financed."
  },
  {
    "SlNo": "430",
    "CollegeName": "Instt. Of Medical Sciences & SUM Hospital Bhubaneswar",
    "State": "Orissa",
    "District": "Khordha",
    "University": "Siksha O Anusandhan University Bhubaneswar",
    "Management": "Trust",
    "ParentOrganization": "Siksha 'O' Anusandhan (SOA Deemed University)",
    "KeyPeople": [{"Name": "Prof. Dr. Manojranjan Nayak", "Role": "Founder President", "Details": "SOA University"}],
    "PoliticalAffiliation": "Prominent media/educational group in Odisha.",
    "FundingSource": "SOA University fees, 1600-bed super-specialty SUM Hospital earnings.",
    "SummaryReport": "Established in 2007 in Kalinga Nagar, Bhubaneswar. Flagship constituent of SOA Deemed University. Self-financed."
  },
  {
    "SlNo": "433",
    "CollegeName": "Kalinga Institute of Medical Sciences Bhubaneswar",
    "State": "Orissa",
    "District": "Khordha",
    "University": "KIIT University Deemed Bhubaneswar",
    "Management": "Trust",
    "ParentOrganization": "KIIT Educational Trust / KIIT Deemed University",
    "KeyPeople": [{"Name": "Dr. Achyuta Samanta", "Role": "Founder", "Details": "Educationist, philanthropist, and former Member of Parliament (Lok Sabha, BJD, Kandhamal)"}],
    "PoliticalAffiliation": "BJD Leader. Founder Dr. Achyuta Samanta is a former BJD Member of Parliament.",
    "FundingSource": "KIIT Deemed University tuition fees, KIMS 2000-bed super-specialty hospital clinical income.",
    "SummaryReport": "Established in 2007 in Bhubaneswar by former BJD MP Dr. Achyuta Samanta. Flagship medical college of KIIT Deemed University. Self-financed."
  },
  {
    "SlNo": "434",
    "CollegeName": "Hi-Tech Medical College & Hospital Bhubaneswar",
    "State": "Orissa",
    "District": "Khordha",
    "University": "Utkal University",
    "Management": "Trust",
    "ParentOrganization": "Vigyan Bharati Educational Trust (VBET)",
    "KeyPeople": [{"Name": "Dr. Tirupati Panigrahi", "Role": "Founder Chairman", "Details": "Hi-Tech Group"}],
    "PoliticalAffiliation": "Significant political & business standing in Odisha.",
    "FundingSource": "Hi-Tech Group funds, tuition fees, hospital clinical income.",
    "SummaryReport": "Established in 2005 at Pandara, Bhubaneswar by Dr. Tirupati Panigrahi. Odisha's pioneer private medical college. Self-financed."
  },
  {
    "SlNo": "435",
    "CollegeName": "DRIEMS Institute of Health Sciences and Hospital Kairapari",
    "State": "Orissa",
    "District": "Cuttack",
    "University": "Utkal University",
    "Management": "Society",
    "ParentOrganization": "DRIEMS Society",
    "KeyPeople": [{"Name": "Pramod Chandra Rath", "Role": "Chairman", "Details": "DRIEMS Group"}],
    "PoliticalAffiliation": "None direct / Educational society.",
    "FundingSource": "Tuition fees, hospital earnings.",
    "SummaryReport": "Established in 2023 at Tangi, Cuttack by DRIEMS Society. Self-financed."
  },

  # --- PUNJAB ---
  {
    "SlNo": "445",
    "CollegeName": "RIMT Medical College and Hospital Fatehgarh Sahib",
    "State": "Punjab",
    "District": "Fatehgarh Sahib",
    "University": "RIMT University",
    "Management": "Trust",
    "ParentOrganization": "Om Parkash Bansal Educational & Social Welfare Trust / RIMT University",
    "KeyPeople": [{"Name": "Hukam Chand Bansal", "Role": "Chancellor", "Details": "RIMT University"}],
    "PoliticalAffiliation": "None direct / Private university group.",
    "FundingSource": "RIMT University tuition fees, hospital clinical income.",
    "SummaryReport": "Established in Mandi Gobindgarh, Fatehgarh Sahib as constituent medical college of RIMT University. Self-financed."
  },
  {
    "SlNo": "447",
    "CollegeName": "Christian Medical College Ludhiana",
    "State": "Punjab",
    "District": "Ludhiana",
    "University": "Baba Farid University of Health Sciences Faridkot",
    "Management": "Trust",
    "ParentOrganization": "Christian Medical College Ludhiana Society",
    "KeyPeople": [
      {"Name": "Dr. Dame Edith Brown", "Role": "Founder", "Details": "Pioneer medical missionary (est. 1894)"},
      {"Name": "Dr. William Bhatti", "Role": "Director", "Details": "CMC Ludhiana"}
    ],
    "PoliticalAffiliation": "None / Historic Christian Minority Institution.",
    "FundingSource": "Church society trust reserves, subsidized student tuition fees, 750-bed super-specialty hospital clinical income.",
    "SummaryReport": "Established in 1894 as North India's pioneer Christian minority medical institution. Governed by an inter-denominational council. Self-funded."
  },
  {
    "SlNo": "448",
    "CollegeName": "Dayanand Medical College & Hospital Ludhiana",
    "State": "Punjab",
    "District": "Ludhiana",
    "University": "Baba Farid University of Health Sciences Faridkot",
    "Management": "Trust",
    "ParentOrganization": "Dayanand Medical College Managing Society / Arya Samaj",
    "KeyPeople": [
      {"Name": "Sunil Kant Munjal", "Role": "President", "Details": "Industrialist, Hero Enterprise Chairman"},
      {"Name": "Late Dr. Banarsi Das Soni", "Role": "Founder", "Details": "Arya Samajist physician"}
    ],
    "PoliticalAffiliation": "None direct / Managed by premier industrial house (Hero Group family) & Arya Samaj leaders.",
    "FundingSource": "Hero Group CSR & industrial capital, trust endowments, student tuition fees, 1000-bed Hero DMC Heart Institute earnings.",
    "SummaryReport": "Established in 1934 in Ludhiana. Managed by Hero Group family (Sunil Kant Munjal) under Arya Samaj trust. Premier non-profit medical college. Self-funded."
  },
  {
    "SlNo": "449",
    "CollegeName": "Sri Guru Ram Das Institute of Medical Sciences and Research Sri Amritsar",
    "State": "Punjab",
    "District": "Amritsar",
    "University": "Sri Guru Ram Das University of Health Sciences Sri Amritsar",
    "Management": "Trust",
    "ParentOrganization": "Sri Guru Ram Das Charitable Hospital Trust / Shiromani Gurdwara Parbandhak Committee (SGPC)",
    "KeyPeople": [{"Name": "Harjinder Singh Dhami", "Role": "President", "Details": "President of SGPC (Apex Sikh Religious Body)"}],
    "PoliticalAffiliation": "SGPC / Akali Dal Stature. Governed by SGPC, the apex statutory Sikh religious body.",
    "FundingSource": "SGPC shrine trust endowments, university tuition fees, SGRD Hospital clinical revenues.",
    "SummaryReport": "Established in 1997 in Vallah, Amritsar by SGPC. Flagship Sikh religious minority medical university. Self-funded."
  },
  {
    "SlNo": "450",
    "CollegeName": "Gian Sagar Medical College & Hospital Patiala",
    "State": "Punjab",
    "District": "Patiala",
    "University": "Baba Farid University of Health Sciences Faridkot",
    "Management": "Trust",
    "ParentOrganization": "Gian Sagar Educational & Charitable Trust",
    "KeyPeople": [{"Name": "Nirmal Singh Bhangoo", "Role": "Founder / Promoter", "Details": "Pearls Group"}],
    "PoliticalAffiliation": "Complex political and corporate history in Punjab.",
    "FundingSource": "Trust funds, student tuition fees, hospital clinical income.",
    "SummaryReport": "Established in 2007 at Ramnagar, Banur, Patiala by Gian Sagar Trust. Self-financed."
  },
  {
    "SlNo": "454",
    "CollegeName": "Adesh Institute of Medical Sciences & Research Bhatinda",
    "State": "Punjab",
    "District": "Bathinda",
    "University": "Adesh University Bathinda",
    "Management": "Trust",
    "ParentOrganization": "Adesh Foundation / Adesh University",
    "KeyPeople": [{"Name": "Dr. Har S. Gill", "Role": "Founder & Chancellor", "Details": "Adesh Group of Institutions"}],
    "PoliticalAffiliation": "Prominent educational & political standing in Malwa region of Punjab.",
    "FundingSource": "Adesh University tuition fees, 750-bed super-specialty hospital clinical earnings.",
    "SummaryReport": "Established in 2006 in Bathinda. Flagship constituent of Adesh Private University led by Dr. H. S. Gill. Self-financed."
  },
  {
    "SlNo": "456",
    "CollegeName": "Chintpurni Medical College Pathankot Gurdaspur",
    "State": "Punjab",
    "District": "Gurdaspur",
    "University": "Baba Farid University of Health Sciences Faridkot",
    "Management": "Trust",
    "ParentOrganization": "Swarn Salaria Educational Trust",
    "KeyPeople": [{"Name": "Swaran Salaria", "Role": "Chairman & Founder", "Details": "Industrialist and senior BJP political leader in Punjab"}],
    "PoliticalAffiliation": "BJP Leader. Founder Swaran Salaria is a senior BJP political figure.",
    "FundingSource": "Promoter capital, tuition fees, hospital earnings.",
    "SummaryReport": "Established in 2011 in Pathankot by BJP leader Swaran Salaria under Swarn Salaria Educational Trust. Self-financed."
  },
  {
    "SlNo": "457",
    "CollegeName": "Punjab Institute of Medical Sciences Jalandhar",
    "State": "Punjab",
    "District": "Jalandhar",
    "University": "Baba Farid University of Health Sciences Faridkot",
    "Management": "Trust",
    "ParentOrganization": "PIMS Medical Education & Research Society (Punjab Govt PPP / Surjit Singh Rakhra Trust)",
    "KeyPeople": [{"Name": "Surjit Singh Rakhra", "Role": "Promoter / Trustee", "Details": "Former Cabinet Minister (Punjab, Shiromani Akali Dal)"}],
    "PoliticalAffiliation": "Akali Dal / Punjab Govt PPP. Promoted in PPP model connected to former SAD Minister Surjit Singh Rakhra.",
    "FundingSource": "PIMS Society trust funds, Punjab Govt PPP support, student tuition fees, hospital clinical income.",
    "SummaryReport": "Established in 1999 at Garha Road, Jalandhar under PPP model between Punjab Govt and PIMS Society. Self-financed PPP trust."
  },

  # --- UTTAR PRADESH (REMAINING 4) ---
  {
    "SlNo": "647",
    "CollegeName": "KMC Medical College & Hospital Maharajganj",
    "State": "Uttar Pradesh",
    "District": "Maharajganj",
    "University": "Atal Bihari Vajpayee Medical University Lucknow",
    "Management": "Trust",
    "ParentOrganization": "KMC Educational Trust",
    "KeyPeople": [{"Name": "Dr. Vinay Kumar Srivastava", "Role": "Chairman", "Details": "KMC Group Maharajganj"}],
    "PoliticalAffiliation": "None direct / Educational trust in Eastern UP.",
    "FundingSource": "Tuition fees, hospital operational income.",
    "SummaryReport": "Medical college in Maharajganj operated by KMC Educational Trust. Self-financed."
  },
  {
    "SlNo": "656",
    "CollegeName": "Shri Gorakshnath Medical College Hospital & Arogya Dham Gorakhpur",
    "State": "Uttar Pradesh",
    "District": "Gorakhpur",
    "University": "Mahayogi Gorakhnath University Gorakhpur",
    "Management": "Society",
    "ParentOrganization": "Maharana Pratap Shiksha Parishad / Gorakhnath Math Trust",
    "KeyPeople": [{"Name": "Yogi Adityanath", "Role": "Chancellor & Peethadhishwar", "Details": "Chief Minister of Uttar Pradesh and Head Seer of Gorakhnath Math"}],
    "PoliticalAffiliation": "Chief Minister of UP / Gorakhnath Math. Chaired by Yogi Adityanath, Chief Minister of Uttar Pradesh.",
    "FundingSource": "Gorakhnath Math trust endowments, Mahayogi Gorakhnath University tuition fees, Arogya Dham super-specialty hospital clinical income.",
    "SummaryReport": "Constituent medical college of Mahayogi Gorakhnath University, established under historic Maharana Pratap Shiksha Parishad (Gorakhnath Math) led by Chief Minister Yogi Adityanath. Self-funded religious/educational trust."
  },
  {
    "SlNo": "657",
    "CollegeName": "Shri Siddhi Vinayak Medical College & Hospital Sambhal",
    "State": "Uttar Pradesh",
    "District": "Sambhal",
    "University": "Atal Bihari Vajpayee Medical University Lucknow",
    "Management": "Private",
    "ParentOrganization": "Shri Siddhi Vinayak Trust",
    "KeyPeople": [{"Name": "Anupam Kapoor", "Role": "Chairman", "Details": "Shri Siddhi Vinayak Group"}],
    "PoliticalAffiliation": "None direct / Educational trust.",
    "FundingSource": "Tuition fees, hospital earnings.",
    "SummaryReport": "Established in Sambhal under Shri Siddhi Vinayak Trust. Self-financed."
  },
  {
    "SlNo": "658",
    "CollegeName": "Autonomous State Medical College and Hospital Auraiya",
    "State": "Uttar Pradesh",
    "District": "Auraiya",
    "University": "Atal Bihari Vajpayee Medical University Lucknow",
    "Management": "Society",
    "ParentOrganization": "Autonomous State Medical College Society Auraiya (Govt of Uttar Pradesh)",
    "KeyPeople": [{"Name": "Department of Medical Education", "Role": "Governing Body", "Details": "Government of Uttar Pradesh"}],
    "PoliticalAffiliation": "State Government Autonomous Society.",
    "FundingSource": "Government of Uttar Pradesh budget & central health scheme allocations.",
    "SummaryReport": "State government autonomous medical college society in Auraiya."
  },

  # --- UTTARAKHAND ---
  {
    "SlNo": "733",
    "CollegeName": "Graphic Era Institute of Medical Sciences Dehradun",
    "State": "Uttarakhand",
    "District": "Dehradun",
    "University": "Graphic Era Institute of Medical Sciences Dehradun",
    "Management": "Society",
    "ParentOrganization": "Graphic Era Educational Society",
    "KeyPeople": [{"Name": "Prof. Dr. Kamal Ghanshala", "Role": "Founder & President", "Details": "Graphic Era Group of Universities"}],
    "PoliticalAffiliation": "None direct / Leading educational conglomerate in Uttarakhand.",
    "FundingSource": "Graphic Era University tuition fees, super-specialty hospital clinical income.",
    "SummaryReport": "Established in Dehradun under Graphic Era Educational Society led by Dr. Kamal Ghanshala. Self-financed."
  },
  {
    "SlNo": "735",
    "CollegeName": "Himalayan Institute of Medical Sciences Dehradun",
    "State": "Uttarakhand",
    "District": "Dehradun",
    "University": "Swami Rama Himalayan University",
    "Management": "Trust",
    "ParentOrganization": "Himalayan Evangelical Trust / Swami Rama Himalayan University",
    "KeyPeople": [
      {"Name": "Late Swami Rama", "Role": "Founder & Spiritual Master", "Details": "Yogi, author, and founder of Himalayan Institute"},
      {"Name": "Dr. Vijay Dhasmana", "Role": "Chancellor", "Details": "SRHU Dehradun"}
    ],
    "PoliticalAffiliation": "Spiritual Philanthropic Trust.",
    "FundingSource": "SRHU University tuition fees, 1200-bed Himalayan Hospital clinical earnings.",
    "SummaryReport": "Established in 1995 at Jolly Grant, Dehradun by Swami Rama. Flagship medical university in Uttarakhand. Self-funded."
  },
  {
    "SlNo": "736",
    "CollegeName": "Shri Guru Ram Rai Institute of Medical & Health Sciences Dehradun",
    "State": "Uttarakhand",
    "District": "Dehradun",
    "University": "Shri Guru Ram Rai University",
    "Management": "Society",
    "ParentOrganization": "Shri Guru Ram Rai Education Mission / Darbar Shri Guru Ram Rai Ji Maharaj",
    "KeyPeople": [{"Name": "Mahant Devendra Dass Ji Maharaj", "Role": "Chancellor & Sajjada Nasheen", "Details": "Head of Darbar Sahib Dehradun"}],
    "PoliticalAffiliation": "Spiritual Shrine Board with immense political respect across Uttarakhand.",
    "FundingSource": "Darbar Sahib trust endowments, university tuition fees, Shri Mahant Indiresh Hospital earnings.",
    "SummaryReport": "Established in 2002 at Patel Nagar, Dehradun under SGRR Education Mission led by Mahant Devendra Dass. Self-funded spiritual trust."
  },
  {
    "SlNo": "739",
    "CollegeName": "Gautam Buddha Chikitsa Mahavidyalaya Dehradun",
    "State": "Uttarakhand",
    "District": "Dehradun",
    "University": "Ras Bihari Bose Subharti University Dehradun",
    "Management": "Trust",
    "ParentOrganization": "Ras Bihari Bose Subharti University Trust / Subharti Group",
    "KeyPeople": [{"Name": "Dr. Atul Krishna", "Role": "Founder", "Details": "Subharti Group"}],
    "PoliticalAffiliation": "None direct / Subharti Group.",
    "FundingSource": "University fees, Dr. K. K. B. Hospital clinical revenues.",
    "SummaryReport": "Established in 2022 at Jhajra, Dehradun under Ras Bihari Bose Subharti University. Self-financed."
  },

  # --- WEST BENGAL ---
  {
    "SlNo": "743",
    "CollegeName": "Krishnanagar Institute of Medical Sciences Nadia",
    "State": "West Bengal",
    "District": "Nadia",
    "University": "The West Bengal University of Health Sciences",
    "Management": "Private",
    "ParentOrganization": "Krishnanagar Educational Trust (PPP with WB Govt)",
    "KeyPeople": [{"Name": "Trustees", "Role": "Management Board", "Details": "KIMS Nadia"}],
    "PoliticalAffiliation": "State PPP Partnership.",
    "FundingSource": "Tuition fees, hospital earnings.",
    "SummaryReport": "Established in Krishnanagar, Nadia under PPP framework. Self-financed."
  },
  {
    "SlNo": "744",
    "CollegeName": "East West Institute of Medical Sciences and Research Burdwan",
    "State": "West Bengal",
    "District": "Purba Bardhaman",
    "University": "The West Bengal University of Health Sciences",
    "Management": "Private",
    "ParentOrganization": "East West Education Trust",
    "KeyPeople": [{"Name": "Trustees", "Role": "Management", "Details": "East West Group"}],
    "PoliticalAffiliation": "None direct / Educational trust.",
    "FundingSource": "Tuition fees, hospital earnings.",
    "SummaryReport": "Established in Talit, Burdwan by East West Education Trust. Self-financed."
  },
  {
    "SlNo": "745",
    "CollegeName": "Jakir Hossain Medical College Burdwan",
    "State": "West Bengal",
    "District": "Murshidabad",
    "University": "The West Bengal University of Health Sciences",
    "Management": "Trust",
    "ParentOrganization": "Shivam Educational Trust",
    "KeyPeople": [{"Name": "Jakir Hossain", "Role": "Founder Chairman", "Details": "Member of Legislative Assembly (Trinamool Congress, Jangipur) and former Minister of State for Labour"}],
    "PoliticalAffiliation": "TMC Leader. Founder Jakir Hossain is a sitting Trinamool Congress MLA and former Minister.",
    "FundingSource": "Industrial business capital, student tuition fees, hospital clinical income.",
    "SummaryReport": "Established in 2023 at Raghunathganj, Murshidabad by TMC MLA and former Minister Jakir Hossain. Self-financed Muslim minority trust."
  },
  {
    "SlNo": "747",
    "CollegeName": "JMN Medical College Nadia",
    "State": "West Bengal",
    "District": "Nadia",
    "University": "West Bengal University of Health Sciences Kolkata",
    "Management": "Trust",
    "ParentOrganization": "JMN Educational Trust",
    "KeyPeople": [{"Name": "Trustees", "Role": "Management", "Details": "JMN Group"}],
    "PoliticalAffiliation": "None direct / Educational trust.",
    "FundingSource": "Tuition fees, hospital clinical income.",
    "SummaryReport": "Established in 2023 at Chakdaha, Nadia by JMN Educational Trust. Self-financed."
  },
  {
    "SlNo": "748",
    "CollegeName": "JIS School of Medical Science & Research Howrah",
    "State": "West Bengal",
    "District": "Howrah",
    "University": "JIS University Kolkata",
    "Management": "Society",
    "ParentOrganization": "JIS Group Educational Trust / JIS University",
    "KeyPeople": [
      {"Name": "Sardar Jodh Singh", "Role": "Founder", "Details": "Industrialist and founder of JIS Group"},
      {"Name": "Taranjit Singh", "Role": "Managing Director", "Details": "JIS Group"}
    ],
    "PoliticalAffiliation": "Sikh Minority Educational Group (Largest private educational group in Eastern India).",
    "FundingSource": "JIS Group corporate revenues, university tuition fees, hospital clinical earnings.",
    "SummaryReport": "Established in 2023 at Santragachi, Howrah as constituent medical college of JIS Private University. Self-financed."
  },
  {
    "SlNo": "757",
    "CollegeName": "Santiniketan Medical College Bolpur",
    "State": "West Bengal",
    "District": "Birbhum",
    "University": "The West Bengal University of Health Sciences",
    "Management": "Trust",
    "ParentOrganization": "Swadhin Trust / Santiniketan Society",
    "KeyPeople": [{"Name": "Chandreshwar Prasad Singh", "Role": "Chairman", "Details": "Santiniketan Group"}],
    "PoliticalAffiliation": "None direct / Educational trust.",
    "FundingSource": "Tuition fees, hospital earnings.",
    "SummaryReport": "Established in 2021 at Bolpur, Birbhum as India's first PPP medical college in West Bengal. Self-financed."
  },
  {
    "SlNo": "763",
    "CollegeName": "Shri Ramkrishna Institute of Medical Sciences & Sanaka Hospitals Durgapur",
    "State": "West Bengal",
    "District": "Paschim Bardhaman",
    "University": "West Bengal University of Health Sciences Kolkata",
    "Management": "Trust",
    "ParentOrganization": "Sanaka Educational Trust",
    "KeyPeople": [{"Name": "Tapan Kumar Pobi", "Role": "Chairman", "Details": "Sanaka Group Durgapur"}],
    "PoliticalAffiliation": "Local political connections in Durgapur industrial belt.",
    "FundingSource": "Sanaka Group reserves, tuition fees, hospital clinical income.",
    "SummaryReport": "Established in 2019 at Malandighi, Durgapur by Sanaka Educational Trust. Self-financed."
  },
  {
    "SlNo": "764",
    "CollegeName": "Jagannath Gupta Institute of Medical Sciences & Hospital Kolkata",
    "State": "West Bengal",
    "District": "South 24 Parganas",
    "University": "West Bengal University of Health Sciences Kolkata",
    "Management": "Trust",
    "ParentOrganization": "UIMS Trust / Jagannath Gupta Family Trust",
    "KeyPeople": [{"Name": "K. K. Gupta", "Role": "Chairman", "Details": "JIMSH Kolkata"}],
    "PoliticalAffiliation": "None direct / Educational trust.",
    "FundingSource": "Tuition fees, hospital clinical earnings.",
    "SummaryReport": "Established in 2018 at Budge Budge, Kolkata by UIMS Trust. Self-financed."
  },
  {
    "SlNo": "765",
    "CollegeName": "Gouri Devi Institute of Medical Sciences and Hospital Durgapur",
    "State": "West Bengal",
    "District": "Paschim Bardhaman",
    "University": "West Bengal University of Health Sciences Kolkata",
    "Management": "Society",
    "ParentOrganization": "Rahul Foundation",
    "KeyPeople": [{"Name": "RN Majumder", "Role": "Chairman", "Details": "Rahul Foundation Durgapur"}],
    "PoliticalAffiliation": "None direct / Educational society.",
    "FundingSource": "Group reserves, tuition fees, hospital earnings.",
    "SummaryReport": "Established in 2016 at Rajbandh, Durgapur by Rahul Foundation. Self-financed."
  },
  {
    "SlNo": "766",
    "CollegeName": "IQ-City Medical College Burdwan",
    "State": "West Bengal",
    "District": "Paschim Bardhaman",
    "University": "West Bengal University of Health Sciences Kolkata",
    "Management": "Trust",
    "ParentOrganization": "Mani Group / IQ City Knowledge Campus",
    "KeyPeople": [{"Name": "Sanjay Jhunjhunwala", "Role": "CEO & MD", "Details": "Mani Group Real Estate & Infrastructure"}],
    "PoliticalAffiliation": "None direct / Corporate infrastructure group.",
    "FundingSource": "Mani Group corporate capital, tuition fees, 800-bed hospital clinical income.",
    "SummaryReport": "Established in 2013 in Durgapur by Mani Group. Self-financed corporate medical campus."
  },
  {
    "SlNo": "771",
    "CollegeName": "ICARE Institute of Medical Sciences & Research Haldia Purba Midnapore",
    "State": "West Bengal",
    "District": "Purba Medinipur",
    "University": "West Bengal University of Health Sciences Kolkata",
    "Management": "Trust",
    "ParentOrganization": "Indian Centre for Advancement of Research and Education (ICARE)",
    "KeyPeople": [{"Name": "Lakshman Chandra Seth", "Role": "Chairman & Founder", "Details": "Former Member of Parliament (CPI-M/TMC, Tamluk) and veteran political figure in Haldia"}],
    "PoliticalAffiliation": "CPI-M / TMC Leader. Founded by former MP Lakshman Seth.",
    "FundingSource": "ICARE Society reserves, tuition fees, Bidhan Chandra Roy Hospital earnings.",
    "SummaryReport": "Established in 2011 in Haldia by former MP Lakshman Seth under ICARE Society. Self-financed."
  },
  {
    "SlNo": "779",
    "CollegeName": "KPC Medical College Jadavpur Kolkata",
    "State": "West Bengal",
    "District": "Kolkata",
    "University": "West Bengal University of Health Sciences Kolkata",
    "Management": "Private",
    "ParentOrganization": "KPC Group / Shashi Sekhar Trust",
    "KeyPeople": [{"Name": "Dr. Kali Pradip Chaudhuri", "Role": "Founder & Chairman", "Details": "NRI orthopedic surgeon, industrialist, and founder of KPC Group (USA/India)"}],
    "PoliticalAffiliation": "High-Stature NRI Business Leader (First private medical college in West Bengal established in 2006).",
    "FundingSource": "KPC Group USA corporate capital, student tuition fees, 800-bed hospital clinical income.",
    "SummaryReport": "Established in 2006 at Jadavpur, Kolkata by NRI surgeon Dr. Kali Pradip Chaudhuri as West Bengal's FIRST private medical college. Self-funded."
  }
]

final_sources = [
  {"SlNo": "60", "CollegeName": "Katihar Medical College Katihar", "Sources": ["https://kmc.alkarimuniversity.edu.in/", "https://en.wikipedia.org/wiki/Ahmad_Ashfaque_Karim"]},
  {"SlNo": "61", "CollegeName": "Mata Gujri Memorial Medical College Kishanganj", "Sources": ["https://mgmmc.org/"]},
  {"SlNo": "66", "CollegeName": "Radha Devi Jageshwari Memorial Medical College and Hospital Turki", "Sources": ["https://rdjmmch.org/"]},
  {"SlNo": "67", "CollegeName": "Shree Narayan Medical Institute and Hospital Rohtas", "Sources": ["https://snmih.in/"]},
  {"SlNo": "70", "CollegeName": "Netaji Subhas Medical College & Hospital Amhara Bihta Patna", "Sources": ["https://nsmch.com/"]},
  {"SlNo": "71", "CollegeName": "Lord Buddha Koshi Medical College and Hospital Saharsa", "Sources": ["https://lbkmch.org/"]},
  {"SlNo": "72", "CollegeName": "Madhubani Medical College Madhubani", "Sources": ["https://mmc.edu.in/", "https://myneta.info/"]},
  {"SlNo": "76", "CollegeName": "Narayan Medical College & Hospital Sasaram", "Sources": ["https://nmch.ac.in/", "https://en.wikipedia.org/wiki/Gopal_Narayan_Singh"]},

  {"SlNo": "78", "CollegeName": "Abhishek Mishra Memorial Medical College & RC Bhilai", "Sources": ["https://ammrc.in/"]},
  {"SlNo": "79", "CollegeName": "Shri Rawatpura Sarkar Institute of Medical Sciences and Research Atal Nagar Raipur", "Sources": ["https://srimsr.org/"]},
  {"SlNo": "85", "CollegeName": "Shri Balaji Institute of Medical Science Mowa", "Sources": ["https://sbims.in/"]},
  {"SlNo": "86", "CollegeName": "Raipur Institute of Medical Sciences (RIMS) Raipur", "Sources": ["https://rimsindia.ac.in/"]},
  {"SlNo": "87", "CollegeName": "Shri Shankaracharya Institute of Medical Sciences Bhilai", "Sources": ["https://ssims.ac.in/"]},

  {"SlNo": "96", "CollegeName": "Army College of Medical Sciences New Delhi", "Sources": ["https://theacms.in/", "https://en.wikipedia.org/wiki/Army_College_of_Medical_Sciences"]},
  {"SlNo": "104", "CollegeName": "Hamdard Institute of Medical Sciences & Research New Delhi", "Sources": ["https://himsr.co.in/", "https://en.wikipedia.org/wiki/Jamia_Hamdard"]},

  {"SlNo": "147", "CollegeName": "Maharishi Markandeshwar College of Medical Sciences & Research Sadopur", "Sources": ["https://mmusadopur.ac.in/"]},
  {"SlNo": "148", "CollegeName": "Amrita School of Medicine Faridabad", "Sources": ["https://amrita.edu/school/medicine/faridabad/"]},
  {"SlNo": "149", "CollegeName": "Maharaja Agrasen Medical College Agroha", "Sources": ["https://mamc.edu.in/", "https://en.wikipedia.org/wiki/Savitri_Jindal"]},
  {"SlNo": "150", "CollegeName": "Faculty of Medicine and Health Sciences Gurgaon", "Sources": ["https://sgtuniversity.ac.in/fmhs/"]},
  {"SlNo": "152", "CollegeName": "Maharishi Markandeshwar Institute Of Medical Sciences & Research Mullana Ambala", "Sources": ["https://mmimsr.mmumullana.org/"]},
  {"SlNo": "153", "CollegeName": "Al Falah School of Medical Sciences & Research Centre Faridabad", "Sources": ["https://alfalahuniversity.edu.in/"]},
  {"SlNo": "155", "CollegeName": "Adesh Medical College and Hospital Shahabad Kurukshetra", "Sources": ["https://amch.ac.in/"]},
  {"SlNo": "156", "CollegeName": "N.C. Medical College & Hospital Panipat", "Sources": ["https://ncmedicalcollege.com/"]},
  {"SlNo": "157", "CollegeName": "World College of Medical Sciences & Research Jhajjar", "Sources": ["https://wcmrs.com/"]},

  {"SlNo": "168", "CollegeName": "Maharishi Markandeshwar Medical College & Hospital Solan", "Sources": ["https://mmusolan.org/"]},

  {"SlNo": "181", "CollegeName": "Acharya Shri Chander College of Medical Sciences Jammu", "Sources": ["https://ascomsonline.in/"]},

  {"SlNo": "186", "CollegeName": "Laxmi Chandravansi Medical College and Hospital Bishrampur", "Sources": ["https://lcmch.org/", "https://myneta.info/"]},
  {"SlNo": "187", "CollegeName": "Manipal Tata Medical College Baridih Jameshedpur", "Sources": ["https://manipal.edu/mtmc-jamshedpur.html"]},

  {"SlNo": "410", "CollegeName": "Shija Academy of Health Sciences Imphal", "Sources": ["https://shijaacademy.com/"]},
  {"SlNo": "413", "CollegeName": "PA Sangama International Medical College and Hospital", "Sources": ["https://ustm.ac.in/"]},
  {"SlNo": "416", "CollegeName": "Nagaland Institute of Medical Sciences & Research Kohima", "Sources": ["https://nimsr.nagaland.gov.in/"]},
  {"SlNo": "501", "CollegeName": "Sikkim Manipal Institute of Medical Sciences Gangtok", "Sources": ["https://smu.edu.in/smims/"]},
  {"SlNo": "644", "CollegeName": "Tripura Santiniketan Medical College West Tripura", "Sources": ["https://tsmc.in/"]},
  {"SlNo": "646", "CollegeName": "Tripura Medical College and Dr. B R A M Teaching Hospital Agartala", "Sources": ["https://tmc.nic.in/"]},

  {"SlNo": "418", "CollegeName": "Institute of Medical Sciences & SUM Hospital Campus Bhubaneswar II", "Sources": ["https://soa.ac.in/ims/"]},
  {"SlNo": "429", "CollegeName": "Hi-Tech Medical College & Hospital Rourkela", "Sources": ["https://hi-techmedicalrkl.org/"]},
  {"SlNo": "430", "CollegeName": "Instt. Of Medical Sciences & SUM Hospital Bhubaneswar", "Sources": ["https://soa.ac.in/ims/"]},
  {"SlNo": "433", "CollegeName": "Kalinga Institute of Medical Sciences Bhubaneswar", "Sources": ["https://kims.kiit.ac.in/", "https://en.wikipedia.org/wiki/Achyuta_Samanta"]},
  {"SlNo": "434", "CollegeName": "Hi-Tech Medical College & Hospital Bhubaneswar", "Sources": ["https://hi-techmedical.org/"]},
  {"SlNo": "435", "CollegeName": "DRIEMS Institute of Health Sciences and Hospital Kairapari", "Sources": ["https://driems.ac.in/"]},

  {"SlNo": "445", "CollegeName": "RIMT Medical College and Hospital Fatehgarh Sahib", "Sources": ["https://rimt.ac.in/medical/"]},
  {"SlNo": "447", "CollegeName": "Christian Medical College Ludhiana", "Sources": ["https://cmcludhiana.in/"]},
  {"SlNo": "448", "CollegeName": "Dayanand Medical College & Hospital Ludhiana", "Sources": ["https://dmch.edu/"]},
  {"SlNo": "449", "CollegeName": "Sri Guru Ram Das Institute of Medical Sciences and Research Sri Amritsar", "Sources": ["https://sgrdimsr.in/"]},
  {"SlNo": "450", "CollegeName": "Gian Sagar Medical College & Hospital Patiala", "Sources": ["https://giansagar.com/"]},
  {"SlNo": "454", "CollegeName": "Adesh Institute of Medical Sciences & Research Bhatinda", "Sources": ["https://adeshuniversity.ac.in/"]},
  {"SlNo": "456", "CollegeName": "Chintpurni Medical College Pathankot Gurdaspur", "Sources": ["http://cmcpathankot.com/"]},
  {"SlNo": "457", "CollegeName": "Punjab Institute of Medical Sciences Jalandhar", "Sources": ["https://pimsj.com/"]},

  {"SlNo": "647", "CollegeName": "KMC Medical College & Hospital Maharajganj", "Sources": ["https://kmcmedicalcollege.com/"]},
  {"SlNo": "656", "CollegeName": "Shri Gorakshnath Medical College Hospital & Arogya Dham Gorakhpur", "Sources": ["https://mgug.ac.in/", "https://en.wikipedia.org/wiki/Yogi_Adityanath"]},
  {"SlNo": "657", "CollegeName": "Shri Siddhi Vinayak Medical College & Hospital Sambhal", "Sources": ["https://ssvtrust.org/"]},
  {"SlNo": "658", "CollegeName": "Autonomous State Medical College and Hospital Auraiya", "Sources": ["https://asmcauraiya.edu.in/"]},

  {"SlNo": "733", "CollegeName": "Graphic Era Institute of Medical Sciences Dehradun", "Sources": ["https://geims.ac.in/"]},
  {"SlNo": "735", "CollegeName": "Himalayan Institute of Medical Sciences Dehradun", "Sources": ["https://srhu.edu.in/himalayan-institute-of-medical-sciences/"]},
  {"SlNo": "736", "CollegeName": "Shri Guru Ram Rai Institute of Medical & Health Sciences Dehradun", "Sources": ["https://sgrrmc.com/"]},
  {"SlNo": "739", "CollegeName": "Gautam Buddha Chikitsa Mahavidyalaya Dehradun", "Sources": ["https://gbcm.org.in/"]},

  {"SlNo": "743", "CollegeName": "Krishnanagar Institute of Medical Sciences Nadia", "Sources": ["https://kimsnadia.org/"]},
  {"SlNo": "744", "CollegeName": "East West Institute of Medical Sciences and Research Burdwan", "Sources": ["https://ewimsr.org/"]},
  {"SlNo": "745", "CollegeName": "Jakir Hossain Medical College Burdwan", "Sources": ["https://jhmc.in/", "https://myneta.info/"]},
  {"SlNo": "747", "CollegeName": "JMN Medical College Nadia", "Sources": ["https://jmnmedicalcollege.org/"]},
  {"SlNo": "748", "CollegeName": "JIS School of Medical Science & Research Howrah", "Sources": ["https://jismedicalcollege.ac.in/"]},
  {"SlNo": "757", "CollegeName": "Santiniketan Medical College Bolpur", "Sources": ["https://smc.edu.in/"]},
  {"SlNo": "763", "CollegeName": "Shri Ramkrishna Institute of Medical Sciences & Sanaka Hospitals Durgapur", "Sources": ["https://srims.sanakaeducationaltrust.com/"]},
  {"SlNo": "764", "CollegeName": "Jagannath Gupta Institute of Medical Sciences & Hospital Kolkata", "Sources": ["https://jimsh.org/"]},
  {"SlNo": "765", "CollegeName": "Gouri Devi Institute of Medical Sciences and Hospital Durgapur", "Sources": ["https://gimsh.in/"]},
  {"SlNo": "766", "CollegeName": "IQ-City Medical College Burdwan", "Sources": ["https://iqcitymedicalcollege.in/"]},
  {"SlNo": "771", "CollegeName": "ICARE Institute of Medical Sciences & Research Haldia Purba Midnapore", "Sources": ["https://icare-haldia.org/imsr/"]},
  {"SlNo": "779", "CollegeName": "KPC Medical College Jadavpur Kolkata", "Sources": ["https://kpcmedicalcollege.org/"]}
]

own.extend(final_records)
src.extend(final_sources)

save_db(own, src)
