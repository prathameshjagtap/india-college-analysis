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

tg_records = [
  {
    "SlNo": "587",
    "CollegeName": "Nova Institute of Medical Sciences and Research Centre Ranga Reddy",
    "State": "Telangana",
    "District": "Ranga Reddy",
    "University": "Kaloji Narayana Rao University of Health Sciences Warangal",
    "Management": "Trust",
    "ParentOrganization": "Nova Educational Society",
    "KeyPeople": [{"Name": "Er. M. V. Koteswara Rao", "Role": "Chairman", "Details": "Nova Educational Group"}],
    "PoliticalAffiliation": "None identified / Private educational society.",
    "FundingSource": "Student tuition fees, hospital clinical income.",
    "SummaryReport": "Established under Nova Educational Society in Ranga Reddy district. Self-financed through student tuition fees."
  },
  {
    "SlNo": "594",
    "CollegeName": "Neelima Institute of Medical Sciences Medchal",
    "State": "Telangana",
    "District": "Medchal",
    "University": "Kaloji Narayana Rao University of Health Sciences Warangal",
    "Management": "Trust",
    "ParentOrganization": "Anurag Educational Trust / Gayatri Educational Society",
    "KeyPeople": [
      {"Name": "Dr. P. Neelima", "Role": "Chairperson / Managing Director", "Details": "Neelima Hospitals"},
      {"Name": "Dr. P. Rajeshwar Reddy", "Role": "Promoter Associate", "Details": "MLA (BRS, Jangaon) and Chairman of Anurag University"}
    ],
    "PoliticalAffiliation": "BRS Affiliation. Associated with Dr. P. Rajeshwar Reddy, BRS MLA (Jangaon) and former MLC.",
    "FundingSource": "Anurag Educational Trust endowment, tuition fees, hospital revenue.",
    "SummaryReport": "Medical college established in Medchal under Anurag Educational Trust/Gayatri Educational Society, connected to BRS MLA Dr. P. Rajeshwar Reddy. Self-financed."
  },
  {
    "SlNo": "598",
    "CollegeName": "Chalmeda Anand Rao Insttitute Of Medical Sciences Karimnagar",
    "State": "Telangana",
    "District": "Karimnagar",
    "University": "Kaloji Narayana Rao University of Health Sciences Warangal",
    "Management": "Trust",
    "ParentOrganization": "Arihant Educational Society",
    "KeyPeople": [{"Name": "Chalmeda Laxminarsimha Rao", "Role": "Chairman & Founder", "Details": "Prominent political figure and industrialist in Telangana"}],
    "PoliticalAffiliation": "Political Leader. Founder Chalmeda Laxminarsimha Rao is a prominent political leader in Karimnagar (contested elections under Congress / BRS).",
    "FundingSource": "Tuition fees, super-specialty hospital revenue, promoter capital.",
    "SummaryReport": "Established in 2002 by Chalmeda Laxminarsimha Rao under Arihant Educational Society in Karimnagar. Financed via student fees and hospital operations."
  },
  {
    "SlNo": "600",
    "CollegeName": "Arundathi Institute of Medical Sciences Medchal",
    "State": "Telangana",
    "District": "Medchal",
    "University": "Kaloji Narayana Rao University of Health Sciences Warangal",
    "Management": "Society",
    "ParentOrganization": "Arundathi Educational Society",
    "KeyPeople": [{"Name": "Ch. Mahender Reddy", "Role": "Chairman", "Details": "Arundathi Group"}],
    "PoliticalAffiliation": "Associated with Malla Reddy educational group ecosystem (BRS political connections).",
    "FundingSource": "Student tuition fees, hospital fees.",
    "SummaryReport": "Medical college in Medchal district managed by Arundathi Educational Society. Self-financed."
  },
  {
    "SlNo": "601",
    "CollegeName": "CMR Institute of Medical Science Medchal Malkajgiri",
    "State": "Telangana",
    "District": "Medchal Malkajgiri",
    "University": "Kaloji Narayana Rao University of Health Sciences Warangal",
    "Management": "Society",
    "ParentOrganization": "CMR Educational Society / Malla Reddy Group",
    "KeyPeople": [
      {"Name": "Ch. Gopal Reddy", "Role": "Chairman", "Details": "CMR Group"},
      {"Name": "Ch. Malla Reddy", "Role": "Founder Promoter", "Details": "Former Cabinet Minister (BRS) & MLA (Medchal)"}
    ],
    "PoliticalAffiliation": "BRS Affiliation. Promoter Ch. Malla Reddy is a former Minister for Labour & Employment (BRS) and sitting MLA.",
    "FundingSource": "CMR Educational Group reserves, student tuition fees, hospital revenue.",
    "SummaryReport": "Established under CMR Educational Society, part of the CMR/Malla Reddy group headed by BRS MLA & former Minister Ch. Malla Reddy. Self-financing."
  },
  {
    "SlNo": "602",
    "CollegeName": "Father Colombo Institute of Medical Sciences Warangal",
    "State": "Telangana",
    "District": "Warangal",
    "University": "Kaloji Narayana Rao University of Health Sciences Warangal",
    "Management": "Trust",
    "ParentOrganization": "Colombo Educational Society / Catholic Diocese of Warangal",
    "KeyPeople": [{"Name": "Most Rev. Dr. Udumala Bala", "Role": "Chairman / Bishop", "Details": "Bishop of Warangal Catholic Diocese"}],
    "PoliticalAffiliation": "None identified / Christian Minority Trust.",
    "FundingSource": "Christian missionary trust funds, student fees, charitable hospital revenue.",
    "SummaryReport": "Christian minority medical college in Warangal managed by Colombo Educational Society under the Catholic Diocese of Warangal. Funded through church trust reserves and self-financing fee structure."
  },
  {
    "SlNo": "603",
    "CollegeName": "S V S Medical College Mehboobnagar",
    "State": "Telangana",
    "District": "Mehboobnagar",
    "University": "Kaloji Narayana Rao University of Health Sciences Warangal",
    "Management": "Trust",
    "ParentOrganization": "SVS Educational Society",
    "KeyPeople": [{"Name": "Dr. S. Venkata Ramana Reddy", "Role": "Founder Chairman", "Details": "Physician and educationist"}],
    "PoliticalAffiliation": "None direct / Private educational trust with local administrative ties.",
    "FundingSource": "Tuition fees, hospital operational revenues.",
    "SummaryReport": "Established in 1999 in Mahabubnagar by Dr. S. Venkata Ramana Reddy under SVS Educational Society. Funded via self-financing tuition fees and hospital operations."
  },
  {
    "SlNo": "606",
    "CollegeName": "Deccan College of Medical Sciences Hyderabad",
    "State": "Telangana",
    "District": "Hyderabad",
    "University": "Kaloji Narayana Rao University of Health Sciences Warangal",
    "Management": "Trust",
    "ParentOrganization": "Darussalam Educational Trust (DET)",
    "KeyPeople": [
      {"Name": "Asaduddin Owaisi", "Role": "Chairman", "Details": "Member of Parliament (Hyderabad) and President of AIMIM"},
      {"Name": "Akbaruddin Owaisi", "Role": "Managing Trustee", "Details": "MLA (Chandrayangutta, AIMIM)"}
    ],
    "PoliticalAffiliation": "AIMIM Affiliation. Managed by Darussalam Educational Trust chaired by AIMIM MP Asaduddin Owaisi and MLA Akbaruddin Owaisi.",
    "FundingSource": "DET trust reserves, student tuition fees, Owaisi Hospital clinical revenues.",
    "SummaryReport": "Premier Muslim minority medical college established in 1984 by Sultan Salahuddin Owaisi, managed by Darussalam Educational Trust led by AIMIM President & MP Asaduddin Owaisi."
  },
  {
    "SlNo": "607",
    "CollegeName": "MNR Medical College & Hospital Sangareddy",
    "State": "Telangana",
    "District": "Sangareddy",
    "University": "Kaloji Narayana Rao University of Health Sciences Warangal",
    "Management": "Trust",
    "ParentOrganization": "MNR Educational Trust",
    "KeyPeople": [{"Name": "M. N. Raju", "Role": "Founder Chairman", "Details": "MNR Educational Group"}],
    "PoliticalAffiliation": "None direct / Academic trust with wide presence in Telangana & UAE.",
    "FundingSource": "MNR Group institutional revenues, student fees, hospital revenue.",
    "SummaryReport": "Established in 2002 in Sangareddy by M.N. Raju under MNR Educational Trust. Self-funded private trust medical college."
  },
  {
    "SlNo": "608",
    "CollegeName": "Kamineni Institute of Medical Sciences Narketpally",
    "State": "Telangana",
    "District": "Nalgonda",
    "University": "Kaloji Narayana Rao University of Health Sciences Warangal",
    "Management": "Trust",
    "ParentOrganization": "Kamineni Education Society",
    "KeyPeople": [
      {"Name": "Kamineni Suryanarayana", "Role": "Founder & Chairman", "Details": "Industrialist and founder of Kamineni Group"},
      {"Name": "Dr. Kamineni Srinivas", "Role": "Promoter Associate", "Details": "Former Health Minister of Andhra Pradesh (BJP)"}
    ],
    "PoliticalAffiliation": "BJP Connections. Promoters associated with former Health Minister Dr. Kamineni Srinivas (BJP).",
    "FundingSource": "Kamineni Group healthcare capital, tuition fees, hospital clinical earnings.",
    "SummaryReport": "Founded in 1999 at Narketpally by Kamineni Group under Kamineni Education Society. Self-funded medical college and super-specialty hospital."
  },
  {
    "SlNo": "610",
    "CollegeName": "Bhaskar Medical College Yenkapally",
    "State": "Telangana",
    "District": "Ranga Reddy",
    "University": "Kaloji Narayana Rao University of Health Sciences Warangal",
    "Management": "Trust",
    "ParentOrganization": "J.B. Educational Society",
    "KeyPeople": [{"Name": "J. Bhaskar Rao", "Role": "Founder Chairman", "Details": "J.B. Group of Educational Institutions"}],
    "PoliticalAffiliation": "None direct / Educational conglomerate.",
    "FundingSource": "J.B. Educational Society funds, student tuition fees, hospital income.",
    "SummaryReport": "Established in 2005 at Moinabad, Ranga Reddy district by J. Bhaskar Rao under J.B. Educational Society. Self-financed."
  },
  {
    "SlNo": "611",
    "CollegeName": "TRR Institute of Medical Sciences Patancheru",
    "State": "Telangana",
    "District": "Sangareddy",
    "University": "Kaloji Narayana Rao University of Health Sciences Warangal",
    "Management": "Trust",
    "ParentOrganization": "TRR Educational Society",
    "KeyPeople": [{"Name": "T. Ram Reddy", "Role": "Chairman", "Details": "TRR Educational Group"}],
    "PoliticalAffiliation": "Local political leadership connections in Sangareddy/Medak region.",
    "FundingSource": "Student tuition fees, hospital charges.",
    "SummaryReport": "Medical college at Patancheru operated by TRR Educational Society. Self-financed."
  },
  {
    "SlNo": "615",
    "CollegeName": "Surabhi Institute of Medical Sciences Siddipet",
    "State": "Telangana",
    "District": "Siddipet",
    "University": "Kaloji Narayana Rao University of Health Sciences Warangal",
    "Management": "Trust",
    "ParentOrganization": "Surabhi Educational Society",
    "KeyPeople": [{"Name": "Dr. V. Surabhi Reddy", "Role": "Chairman", "Details": "Surabhi Educational Society"}],
    "PoliticalAffiliation": "None identified / Private educational society.",
    "FundingSource": "Student fees, hospital clinical income.",
    "SummaryReport": "Established in Siddipet under Surabhi Educational Society. Self-financed medical institution."
  },
  {
    "SlNo": "616",
    "CollegeName": "Mamata Academy of Medical Sciences Bachupally",
    "State": "Telangana",
    "District": "Medchal Malkajgiri",
    "University": "Kaloji Narayana Rao University of Health Sciences Warangal",
    "Management": "Society",
    "ParentOrganization": "Mamata Educational Society",
    "KeyPeople": [
      {"Name": "Puvvada Ajay Kumar", "Role": "Chairman", "Details": "Former Cabinet Minister for Transport (Telangana, BRS) and former MLA (Khammam)"},
      {"Name": "Puvvada Nageswara Rao", "Role": "Founder", "Details": "Veteran CPI political leader and former MLA"}
    ],
    "PoliticalAffiliation": "BRS / Political Family. Founded by family of former BRS Cabinet Minister Puvvada Ajay Kumar and CPI veteran Puvvada Nageswara Rao.",
    "FundingSource": "Mamata Group reserves, tuition fees, Bachupally hospital operational income.",
    "SummaryReport": "Established at Bachupally, Hyderabad by Mamata Educational Society, headed by former BRS Minister Puvvada Ajay Kumar. Self-financed."
  },
  {
    "SlNo": "617",
    "CollegeName": "Dr. Patnam Mahender Reddy Institute of Medical Sciences Chevella Rangareddy",
    "State": "Telangana",
    "District": "Ranga Reddy",
    "University": "Kaloji Narayana Rao University of Health Sciences Warangal",
    "Management": "Society",
    "ParentOrganization": "Patnam Mahender Reddy Educational Society",
    "KeyPeople": [{"Name": "Dr. Patnam Mahender Reddy", "Role": "Founder & Chairman", "Details": "Member of Legislative Council (MLC) and former Cabinet Minister for IT & Transport (Telangana, BRS)"}],
    "PoliticalAffiliation": "BRS Leader. Founded by Dr. Patnam Mahender Reddy, senior BRS political leader, former Minister and MLC.",
    "FundingSource": "Promoter capital, student tuition fees, hospital revenue.",
    "SummaryReport": "Established in Chevella by BRS leader & former Cabinet Minister Dr. Patnam Mahender Reddy. Funded via self-financing medical college fee model."
  },
  {
    "SlNo": "619",
    "CollegeName": "Ayaan Institute of Medical Sciences Teaching Hospital & Research Centre Kanaka Mamidi",
    "State": "Telangana",
    "District": "Ranga Reddy",
    "University": "Kaloji Narayana Rao University of Health Sciences Warangal",
    "Management": "Trust",
    "ParentOrganization": "Ayaan Educational Society",
    "KeyPeople": [{"Name": "Dr. M. A. Bari", "Role": "Chairman", "Details": "Ayaan Educational Society"}],
    "PoliticalAffiliation": "None identified / Muslim Minority Institution.",
    "FundingSource": "Minority trust funds, student tuition fees, hospital receipts.",
    "SummaryReport": "Muslim minority medical college at Kanaka Mamidi, Ranga Reddy district, operated by Ayaan Educational Society. Self-financed."
  },
  {
    "SlNo": "620",
    "CollegeName": "Maheshwara Medical College Chitkul Patancheru Medak",
    "State": "Telangana",
    "District": "Medak",
    "University": "Kaloji Narayana Rao University of Health Sciences Warangal",
    "Management": "Trust",
    "ParentOrganization": "Maheshwara Educational Trust / TG Group",
    "KeyPeople": [
      {"Name": "T. G. Venkatesh", "Role": "Promoter / Patriarch", "Details": "Former Member of Parliament (Rajya Sabha, BJP) and former AP Minister"},
      {"Name": "T. G. Bharat", "Role": "Trustee", "Details": "Cabinet Minister for Industries & Commerce (Andhra Pradesh, TDP) and MLA (Kurnool)"}
    ],
    "PoliticalAffiliation": "BJP & TDP Affiliation. Promoted by TG Group family of former MP T.G. Venkatesh and current AP Cabinet Minister T.G. Bharat.",
    "FundingSource": "TG Group industrial capital, tuition fees, hospital service revenues.",
    "SummaryReport": "Established at Chitkul, Patancheru by TG Group, associated with former BJP MP T.G. Venkatesh and AP Minister T.G. Bharat. Self-financed."
  },
  {
    "SlNo": "621",
    "CollegeName": "Mahavir Institute of Medical Sciences Vikarabad",
    "State": "Telangana",
    "District": "Vikarabad",
    "University": "Kaloji Narayana Rao University of Health Sciences Warangal",
    "Management": "Society",
    "ParentOrganization": "Mahavir Educational Society",
    "KeyPeople": [{"Name": "V. Mahipal Reddy", "Role": "Chairman & Founder", "Details": "Former Member of Legislative Assembly (BRS, Patancheru)"}],
    "PoliticalAffiliation": "BRS Affiliation. Founder V. Mahipal Reddy is a former BRS MLA for Patancheru.",
    "FundingSource": "Promoter capital, student tuition fees, hospital revenue.",
    "SummaryReport": "Founded in Vikarabad by former BRS MLA V. Mahipal Reddy under Mahavir Educational Society. Self-financed medical institution."
  },
  {
    "SlNo": "622",
    "CollegeName": "R.V.M. Institute of Medical Sciences and Research Centre Siddipet",
    "State": "Telangana",
    "District": "Siddipet",
    "University": "Kaloji Narayana Rao University of Health Sciences Warangal",
    "Management": "Trust",
    "ParentOrganization": "RVM Educational Society",
    "KeyPeople": [{"Name": "Dr. Y. V. R. Maha Varma", "Role": "Chairman", "Details": "RVM Educational Group"}],
    "PoliticalAffiliation": "None direct / Educational trust.",
    "FundingSource": "Tuition fees, hospital clinical income.",
    "SummaryReport": "Established at Laxmakkapally, Siddipet by RVM Educational Society. Self-financed."
  },
  {
    "SlNo": "625",
    "CollegeName": "Mallareddy Medical College for Women Hyderabad",
    "State": "Telangana",
    "District": "Hyderabad",
    "University": "Kaloji Narayana Rao University of Health Sciences Warangal",
    "Management": "Society",
    "ParentOrganization": "Malla Reddy Educational Society",
    "KeyPeople": [
      {"Name": "Ch. Malla Reddy", "Role": "Founder Chairman", "Details": "Former Cabinet Minister (BRS) and sitting MLA (Medchal)"},
      {"Name": "Ch. Bhadra Reddy", "Role": "President", "Details": "Malla Reddy Health City"}
    ],
    "PoliticalAffiliation": "BRS Leader. Founder Ch. Malla Reddy is a prominent BRS MLA and former Cabinet Minister.",
    "FundingSource": "Malla Reddy Educational Group revenue, tuition fees, hospital earnings.",
    "SummaryReport": "Women's medical college established at Suraram, Hyderabad by BRS leader Ch. Malla Reddy. Self-financed through group revenues."
  },
  {
    "SlNo": "627",
    "CollegeName": "Kamineni Academy of Medical Sciences & Research Center Hyderabad",
    "State": "Telangana",
    "District": "Hyderabad",
    "University": "Kaloji Narayana Rao University of Health Sciences Warangal",
    "Management": "Trust",
    "ParentOrganization": "Kamineni Education Society",
    "KeyPeople": [
      {"Name": "Kamineni Shashidhar", "Role": "Managing Director", "Details": "Kamineni Hospitals"},
      {"Name": "Dr. Kamineni Srinivas", "Role": "Promoter Associate", "Details": "Former Health Minister of AP (BJP)"}
    ],
    "PoliticalAffiliation": "BJP Connections. Associated with Kamineni Group and former AP BJP Health Minister Dr. Kamineni Srinivas.",
    "FundingSource": "Kamineni Hospitals operational income, tuition fees.",
    "SummaryReport": "Located at L.B. Nagar, Hyderabad, operated by Kamineni Education Society. Funded by hospital revenues and tuition fees."
  },
  {
    "SlNo": "628",
    "CollegeName": "Apollo Institute of Medical Sciences and Research Hyderabad",
    "State": "Telangana",
    "District": "Hyderabad",
    "University": "Kaloji Narayana Rao University of Health Sciences Warangal",
    "Management": "Society",
    "ParentOrganization": "Apollo Hospitals Educational Trust",
    "KeyPeople": [
      {"Name": "Dr. Prathap C. Reddy", "Role": "Founder Chairman", "Details": "Apollo Hospitals Group"},
      {"Name": "Ms. Upasana Kamineni Konidela", "Role": "Vice Chairperson", "Details": "Apollo Charity / AIMSR Hyderabad"}
    ],
    "PoliticalAffiliation": "None direct / Major healthcare corporate group.",
    "FundingSource": "Apollo Hospitals Enterprise Ltd backing, tuition fees, hospital operations.",
    "SummaryReport": "Established at Jubilee Hills, Hyderabad by Apollo Hospitals Educational Trust. Self-funded corporate healthcare medical institute."
  },
  {
    "SlNo": "629",
    "CollegeName": "Malla Reddy Institute of Medical Sciences Hyderabad",
    "State": "Telangana",
    "District": "Hyderabad",
    "University": "Kaloji Narayana Rao University of Health Sciences Warangal",
    "Management": "Society",
    "ParentOrganization": "Malla Reddy Educational Society",
    "KeyPeople": [
      {"Name": "Ch. Malla Reddy", "Role": "Founder Chairman", "Details": "Former Cabinet Minister (BRS) & MLA"}
    ],
    "PoliticalAffiliation": "BRS Leader. Founded by Ch. Malla Reddy, former Minister and BRS MLA.",
    "FundingSource": "Malla Reddy Group revenues, tuition fees, hospital operational income.",
    "SummaryReport": "Established in 2012 at Suraram, Hyderabad by BRS MLA Ch. Malla Reddy. Self-financed."
  },
  {
    "SlNo": "630",
    "CollegeName": "Dr. VRK Womens Medical College Aziznagar",
    "State": "Telangana",
    "District": "Ranga Reddy",
    "University": "Kaloji Narayana Rao University of Health Sciences Warangal",
    "Management": "Trust",
    "ParentOrganization": "Darussalam Educational Trust / Dr. VRK Society",
    "KeyPeople": [{"Name": "Asaduddin Owaisi", "Role": "Management Head", "Details": "MP (Hyderabad) and President of AIMIM"}],
    "PoliticalAffiliation": "AIMIM Affiliation. Managed under the umbrella of Darussalam Educational Trust (Owaisi family).",
    "FundingSource": "DET trust funds, tuition fees, hospital clinical income.",
    "SummaryReport": "Muslim minority women's medical college at Aziznagar, Ranga Reddy, managed under Darussalam Educational Trust ecosystem. Self-funded."
  },
  {
    "SlNo": "632",
    "CollegeName": "Shadan Institute of Medical Sciences Research Centre and Teaching Hospital Peerancheru",
    "State": "Telangana",
    "District": "Ranga Reddy",
    "University": "Kaloji Narayana Rao University of Health Sciences Warangal",
    "Management": "Society",
    "ParentOrganization": "Shadan Educational Society",
    "KeyPeople": [
      {"Name": "Dr. Shah Alam Rasool Khan", "Role": "Chairman", "Details": "Shadan Educational Society"},
      {"Name": "Late Dr. Vizarat Rasool Khan", "Role": "Founder Chairman", "Details": "Former MLA (AIMIM / TDP) and eminent minority educationist"}
    ],
    "PoliticalAffiliation": "Political Family. Founded by late Dr. Vizarat Rasool Khan, former Member of Legislative Assembly (MLA).",
    "FundingSource": "Shadan Group trust reserves, tuition fees, teaching hospital revenue.",
    "SummaryReport": "Established in 2005 as a premier Muslim minority medical college near Peerancheru, Hyderabad by late MLA Dr. Vizarat Rasool Khan. Self-financed."
  },
  {
    "SlNo": "633",
    "CollegeName": "Prathima Institute Of Medical Sciences Karimnagar",
    "State": "Telangana",
    "District": "Karimnagar",
    "University": "Kaloji Narayana Rao University of Health Sciences Warangal",
    "Management": "Trust",
    "ParentOrganization": "Prathima Educational Society / Prathima Group",
    "KeyPeople": [{"Name": "B. Srinivas Rao", "Role": "Chairman", "Details": "Industrialist, Prathima Group"}],
    "PoliticalAffiliation": "Strong political ties in Telangana (Prathima Group promoters have familial/business links to major political leaders in AP & Telangana).",
    "FundingSource": "Prathima Group infrastructure & healthcare earnings, tuition fees, hospital revenue.",
    "SummaryReport": "Established in 2001 in Karimnagar by B. Srinivas Rao under Prathima Educational Society. Financed through Prathima Group corporate revenues and college fees."
  },
  {
    "SlNo": "634",
    "CollegeName": "Prathima Relief Institute of Medical Sciences Warangal",
    "State": "Telangana",
    "District": "Warangal",
    "University": "Kaloji Narayana Rao University of Health Sciences Warangal",
    "Management": "Trust",
    "ParentOrganization": "Prathima Educational Society",
    "KeyPeople": [{"Name": "B. Srinivas Rao", "Role": "Chairman", "Details": "Prathima Group"}],
    "PoliticalAffiliation": "Political links through Prathima Group promoters.",
    "FundingSource": "Prathima Group capital, tuition fees, hospital operational income.",
    "SummaryReport": "Medical college established in Warangal by Prathima Educational Society. Self-financed."
  },
  {
    "SlNo": "642",
    "CollegeName": "Mediciti Institute Of Medical Sciences Ghanpur",
    "State": "Telangana",
    "District": "Medchal",
    "University": "Kaloji Narayana Rao University of Health Sciences Warangal",
    "Management": "Trust",
    "ParentOrganization": "Share Medical Care (NGO Trust) / MediCiti Healthcare",
    "KeyPeople": [{"Name": "Dr. P. S. Maharaju", "Role": "Founder Chairman", "Details": "Cardiothoracic surgeon and NRI philanthropist"}],
    "PoliticalAffiliation": "None identified / NRI philanthropic medical foundation.",
    "FundingSource": "Share Medical Care trust funds, tuition fees, hospital clinical earnings.",
    "SummaryReport": "Established in 2002 at Ghanpur, Medchal by Share Medical Care foundation founded by NRI cardiothoracic surgeon Dr. P.S. Maharaju. Self-funded."
  },
  {
    "SlNo": "643",
    "CollegeName": "Mamata Medical College Khammam",
    "State": "Telangana",
    "District": "Khammam",
    "University": "Kaloji Narayana Rao University of Health Sciences Warangal",
    "Management": "Trust",
    "ParentOrganization": "Mamata Educational Society",
    "KeyPeople": [
      {"Name": "Puvvada Ajay Kumar", "Role": "Chairman", "Details": "Former Cabinet Minister (BRS) & MLA (Khammam)"},
      {"Name": "Puvvada Nageswara Rao", "Role": "Founder Chairman", "Details": "Former CPI MLA"}
    ],
    "PoliticalAffiliation": "BRS / CPI Leader Family. Founded by family of former BRS Cabinet Minister Puvvada Ajay Kumar and veteran politician Puvvada Nageswara Rao.",
    "FundingSource": "Mamata Educational Society reserves, tuition fees, 1000+ bed hospital revenues.",
    "SummaryReport": "Established in 1998 in Khammam as one of Telangana's oldest private medical colleges, founded by Puvvada family (BRS/CPI leaders). Self-financed."
  }
]

tg_sources = [
  {"SlNo": "587", "CollegeName": "Nova Institute of Medical Sciences and Research Centre Ranga Reddy", "Sources": ["http://novamedicalcollege.org/"]},
  {"SlNo": "594", "CollegeName": "Neelima Institute of Medical Sciences Medchal", "Sources": ["https://nims.edu.in/", "https://anurag.edu.in/"]},
  {"SlNo": "598", "CollegeName": "Chalmeda Anand Rao Insttitute Of Medical Sciences Karimnagar", "Sources": ["https://caims.in/", "https://myneta.info/"]},
  {"SlNo": "600", "CollegeName": "Arundathi Institute of Medical Sciences Medchal", "Sources": ["https://aims.edu.in/"]},
  {"SlNo": "601", "CollegeName": "CMR Institute of Medical Science Medchal Malkajgiri", "Sources": ["https://cmrims.edu.in/", "https://en.wikipedia.org/wiki/Chama_Kura_Malla_Reddy"]},
  {"SlNo": "602", "CollegeName": "Father Colombo Institute of Medical Sciences Warangal", "Sources": ["https://fathercolomboims.com/"]},
  {"SlNo": "603", "CollegeName": "S V S Medical College Mehboobnagar", "Sources": ["https://svsmedcol.com/"]},
  {"SlNo": "606", "CollegeName": "Deccan College of Medical Sciences Hyderabad", "Sources": ["https://deccancollegeofmedicalsciences.edu.in/", "https://en.wikipedia.org/wiki/Asaduddin_Owaisi", "https://en.wikipedia.org/wiki/Deccan_College_of_Medical_Sciences"]},
  {"SlNo": "607", "CollegeName": "MNR Medical College & Hospital Sangareddy", "Sources": ["https://mnrindia.org/mnrmc/"]},
  {"SlNo": "608", "CollegeName": "Kamineni Institute of Medical Sciences Narketpally", "Sources": ["https://kaminenimedical.org/", "https://kaminenihospitals.com/"]},
  {"SlNo": "610", "CollegeName": "Bhaskar Medical College Yenkapally", "Sources": ["http://bhascarmedicalcollege.edu.in/"]},
  {"SlNo": "611", "CollegeName": "TRR Institute of Medical Sciences Patancheru", "Sources": ["https://trrims.in/"]},
  {"SlNo": "615", "CollegeName": "Surabhi Institute of Medical Sciences Siddipet", "Sources": ["https://surabhimedicalcollege.com/"]},
  {"SlNo": "616", "CollegeName": "Mamata Academy of Medical Sciences Bachupally", "Sources": ["https://mams.org.in/", "https://en.wikipedia.org/wiki/Puvvada_Ajay_Kumar"]},
  {"SlNo": "617", "CollegeName": "Dr. Patnam Mahender Reddy Institute of Medical Sciences Chevella Rangareddy", "Sources": ["https://pmrims.in/", "https://en.wikipedia.org/wiki/Patnam_Mahender_Reddy"]},
  {"SlNo": "619", "CollegeName": "Ayaan Institute of Medical Sciences Teaching Hospital & Research Centre Kanaka Mamidi", "Sources": ["http://ayaanmedicalcollege.com/"]},
  {"SlNo": "620", "CollegeName": "Maheshwara Medical College Chitkul Patancheru Medak", "Sources": ["https://maheshwaramedical.com/", "https://en.wikipedia.org/wiki/T._G._Venkatesh"]},
  {"SlNo": "621", "CollegeName": "Mahavir Institute of Medical Sciences Vikarabad", "Sources": ["https://mims.edu.in/", "https://myneta.info/"]},
  {"SlNo": "622", "CollegeName": "R.V.M. Institute of Medical Sciences and Research Centre Siddipet", "Sources": ["https://rvmims.org/"]},
  {"SlNo": "625", "CollegeName": "Mallareddy Medical College for Women Hyderabad", "Sources": ["https://mrmcw.edu.in/", "https://en.wikipedia.org/wiki/Chama_Kura_Malla_Reddy"]},
  {"SlNo": "627", "CollegeName": "Kamineni Academy of Medical Sciences & Research Center Hyderabad", "Sources": ["https://kamsrc.com/"]},
  {"SlNo": "628", "CollegeName": "Apollo Institute of Medical Sciences and Research Hyderabad", "Sources": ["https://apolloimsr.edu.in/"]},
  {"SlNo": "629", "CollegeName": "Malla Reddy Institute of Medical Sciences Hyderabad", "Sources": ["https://mrims.edu.in/", "https://en.wikipedia.org/wiki/Chama_Kura_Malla_Reddy"]},
  {"SlNo": "630", "CollegeName": "Dr. VRK Womens Medical College Aziznagar", "Sources": ["http://drvrkwmc.com/"]},
  {"SlNo": "632", "CollegeName": "Shadan Institute of Medical Sciences Research Centre and Teaching Hospital Peerancheru", "Sources": ["https://shadan.in/", "https://en.wikipedia.org/wiki/Vizarat_Rasool_Khan"]},
  {"SlNo": "633", "CollegeName": "Prathima Institute Of Medical Sciences Karimnagar", "Sources": ["https://prathima.in/"]},
  {"SlNo": "634", "CollegeName": "Prathima Relief Institute of Medical Sciences Warangal", "Sources": ["https://prathimarelief.in/"]},
  {"SlNo": "642", "CollegeName": "Mediciti Institute Of Medical Sciences Ghanpur", "Sources": ["https://mims.edu.in/"]},
  {"SlNo": "643", "CollegeName": "Mamata Medical College Khammam", "Sources": ["https://mamatamc.edu.in/", "https://en.wikipedia.org/wiki/Puvvada_Ajay_Kumar"]}
]

own.extend(tg_records)
src.extend(tg_sources)

save_db(own, src)
