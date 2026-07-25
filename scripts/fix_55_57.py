import json

with open('data/private_colleges_ownership.json', 'r') as f:
    own = json.load(f)
with open('data/private_college_sources.json', 'r') as f:
    src = json.load(f)

# Filter out erroneous SlNo 61 if present
own = [x for x in own if str(x['SlNo']) != "61"]
src = [x for x in src if str(x['SlNo']) != "61"]

record_55 = {
  "SlNo": "55",
  "CollegeName": "Himalaya Medical College and Hospital Patna",
  "State": "Bihar",
  "District": "Patna",
  "University": "Bihar University of Health Sciences",
  "Management": "Trust",
  "ParentOrganization": "Himalaya Educational Trust",
  "KeyPeople": [{"Name": "Dr. R. K. Sharma", "Role": "Chairman", "Details": "Himalaya Educational Group"}],
  "PoliticalAffiliation": "None direct / Private educational trust.",
  "FundingSource": "Tuition fees, hospital operational income.",
  "SummaryReport": "Established at Chhitori, Chhata, Patna by Himalaya Educational Trust. Self-financed."
}

source_55 = {
  "SlNo": "55",
  "CollegeName": "Himalaya Medical College and Hospital Patna",
  "Sources": ["https://hmchpatna.org/"]
}

record_57 = {
  "SlNo": "57",
  "CollegeName": "Mata Gujri Memorial Medical College Kishanganj",
  "State": "Bihar",
  "District": "Kishanganj",
  "University": "B.N. Mandal University",
  "Management": "Trust",
  "ParentOrganization": "Mata Gujri Memorial Medical College Trust / Takht Sri Harimandir Ji Patna Sahib",
  "KeyPeople": [{"Name": "Takht Sri Harimandir Ji Prabandhak Committee", "Role": "Managing Body", "Details": "Sikh Religious Shrine Board"}],
  "PoliticalAffiliation": "None direct / Sikh Religious Minority Institution.",
  "FundingSource": "Sikh shrine trust endowments, student tuition fees, Lions Seva Kendra hospital earnings.",
  "SummaryReport": "Established in 1990 in Kishanganj as Bihar's premier Sikh religious minority medical college. Managed under Sikh shrine board trust. Self-funded."
}

source_57 = {
  "SlNo": "57",
  "CollegeName": "Mata Gujri Memorial Medical College Kishanganj",
  "Sources": ["https://mgmmc.org/"]
}

own_dict = {str(x['SlNo']): x for x in own}
src_dict = {str(x['SlNo']): x for x in src}

own_dict["55"] = record_55
src_dict["55"] = source_55
own_dict["57"] = record_57
src_dict["57"] = source_57

sorted_own = sorted(own_dict.values(), key=lambda x: int(x['SlNo']))
sorted_src = sorted(src_dict.values(), key=lambda x: int(x['SlNo']))

with open('data/private_colleges_ownership.json', 'w') as f:
    json.dump(sorted_own, f, indent=2)
with open('data/private_college_sources.json', 'w') as f:
    json.dump(sorted_src, f, indent=2)

print(f"Updated total records: {len(sorted_own)}")
