import json

center_timeline = {
    1942: "British India", 1943: "British India", 1944: "British India", 1945: "British India", 1946: "British India",
    1947: "INC", 1948: "INC", 1949: "INC", 1950: "INC", 1951: "INC", 1952: "INC", 1953: "INC", 1954: "INC",
    1955: "INC", 1956: "INC", 1957: "INC", 1958: "INC", 1959: "INC", 1960: "INC", 1961: "INC", 1962: "INC",
    1963: "INC", 1964: "INC", 1965: "INC", 1966: "INC", 1967: "INC", 1968: "INC", 1969: "INC", 1970: "INC",
    1971: "INC", 1972: "INC", 1973: "INC", 1974: "INC", 1975: "INC", 1976: "INC",
    1977: "Janata Party", 1978: "Janata Party", 1979: "Janata Party",
    1980: "INC", 1981: "INC", 1982: "INC", 1983: "INC", 1984: "INC", 1985: "INC", 1986: "INC", 1987: "INC", 1988: "INC", 1989: "Janata Dal",
    1990: "Janata Dal / Samajwadi Janata Party", 1991: "INC", 1992: "INC", 1993: "INC", 1994: "INC", 1995: "INC",
    1996: "United Front", 1997: "United Front", 1998: "BJP (NDA)", 1999: "BJP (NDA)", 2000: "BJP (NDA)",
    2001: "BJP (NDA)", 2002: "BJP (NDA)", 2003: "BJP (NDA)",
    2004: "INC (UPA)", 2005: "INC (UPA)", 2006: "INC (UPA)", 2007: "INC (UPA)", 2008: "INC (UPA)", 2009: "INC (UPA)",
    2010: "INC (UPA)", 2011: "INC (UPA)", 2012: "INC (UPA)", 2013: "INC (UPA)",
    2014: "BJP (NDA)", 2015: "BJP (NDA)", 2016: "BJP (NDA)", 2017: "BJP (NDA)", 2018: "BJP (NDA)", 2019: "BJP (NDA)",
    2020: "BJP (NDA)", 2021: "BJP (NDA)", 2022: "BJP (NDA)", 2023: "BJP (NDA)", 2024: "BJP (NDA)"
}

def get_state_party(state, year):
    try:
        y = int(year)
    except:
        return "Unknown"
    
    if y <= 1946:
        return "British India / Princely State"
        
    s = state.lower()
    
    if "andhra" in s:
        if y in [2000, 2001, 2002, 2003]: return "TDP"
        if y in [2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013]: return "INC"
        if y in [2014, 2015, 2016, 2017, 2018]: return "TDP"
        if y in [2019, 2020, 2021, 2022, 2023]: return "YSRCP"
        if y == 2024: return "TDP (NDA)"
        
    if "bihar" in s:
        if y == 1987: return "INC"
        if y == 1990: return "Janata Dal"
        if y >= 2005: return "JDU (NDA/Mahagathbandhan)"
        
    if "chattisgarh" in s or "chhattisgarh" in s:
        if 2003 <= y <= 2018: return "BJP"
        if 2019 <= y <= 2023: return "INC"
        if y == 2024: return "BJP"
        
    if "delhi" in s:
        if 1998 <= y <= 2013: return "INC"
        if y >= 2015: return "AAP"
        
    if "gujarat" in s:
        if y == 1987: return "INC"
        if y >= 1998: return "BJP"
        
    if "haryana" in s:
        if y in [2002, 2003]: return "INLD"
        if 2005 <= y <= 2014: return "INC"
        if y >= 2014: return "BJP"
        
    if "himachal" in s:
        if y == 2013: return "INC"
        
    if "jammu" in s:
        if y == 1995: return "President's Rule"
        
    if "jharkhand" in s:
        if y in [2020, 2021]: return "JMM (UPA)"
        
    if "karnataka" in s:
        if y in [1953, 1955, 1963, 1965]: return "INC"
        if y == 1979: return "President's Rule / INC"
        if y == 1980: return "INC"
        if y in [1984, 1985, 1986, 1988]: return "Janata Party"
        if y in [1997, 1999]: return "Janata Dal"
        if y in [2000, 2002, 2003, 2005]: return "INC"
        if y == 2006: return "JD(S) - BJP"
        if y in [2008, 2009, 2010, 2011, 2012]: return "BJP"
        if y in [2013, 2014, 2015, 2016, 2017]: return "INC"
        if y == 2019: return "INC-JD(S) / BJP"
        if y in [2020, 2021, 2022, 2023]: return "BJP"
        if y == 2024: return "INC"
        
    if "kerala" in s:
        if y in [2001, 2002, 2003, 2004, 2005, 2011, 2012, 2013, 2014, 2015]: return "INC (UDF)"
        if y in [2000, 2006, 2007, 2008, 2009, 2010] or y >= 2016: return "CPI(M) (LDF)"
        
    if "madhya" in s:
        if y in [2001, 2002, 2003]: return "INC"
        if y >= 2004: return "BJP"
        
    if "maharashtra" in s:
        if y in [1969, 1984, 1989, 1990, 1991, 1994]: return "INC"
        if y == 1995: return "Shiv Sena - BJP"
        if 1999 <= y <= 2014: return "INC - NCP"
        if 2015 <= y <= 2019: return "BJP - Shiv Sena"
        if y in [2020, 2021]: return "MVA (Shiv Sena - NCP - INC)"
        if y >= 2022: return "Mahayuti (BJP - Shiv Sena - NCP)"
        
    if "manipur" in s:
        if y == 2021: return "BJP"
        
    if "meghalaya" in s:
        if y == 2024: return "NPP (MDA)"
        
    if "nagaland" in s:
        if y == 2023: return "NDPP"
        
    if "orissa" in s or "odisha" in s:
        if 2000 <= y <= 2023: return "BJD"
        if y == 2024: return "BJP"
        
    if "pondicherry" in s or "puducherry" in s:
        if y == 1997: return "DMK/TMC"
        if y in [1999, 2000, 2002, 2006, 2007]: return "INC"
        
    if "punjab" in s:
        if y in [1953, 1963]: return "INC"
        if y in [1997, 2007, 2008, 2009, 2010, 2011, 2012]: return "SAD - BJP"
        if y in [2002, 2003, 2004, 2005, 2006]: return "INC"
        if y in [2017, 2018, 2019, 2020, 2021]: return "INC"
        if y >= 2022: return "AAP"
        
    if "rajasthan" in s:
        if y in [1998, 1999, 2000, 2001, 2002, 2003, 2008, 2009, 2010, 2011, 2012, 2013, 2018, 2019, 2020, 2021, 2022, 2023]: return "INC"
        if y in [2004, 2005, 2006, 2007, 2014, 2015, 2016, 2017, 2024]: return "BJP"
        
    if "sikkim" in s:
        if y == 2000: return "SDF"
        
    if "tamil" in s:
        if y == 1985: return "AIADMK"
        if y == 1996: return "DMK"
        if y in [2001, 2002, 2003, 2004, 2005]: return "AIADMK"
        if y in [2006, 2007, 2008, 2009, 2010]: return "DMK"
        if 2011 <= y <= 2020: return "AIADMK"
        if y >= 2021: return "DMK"
        
    if "telangana" in s:
        # Before 2014, it was Andhra Pradesh
        if y <= 2014:
            if y in [1985, 1998, 1999, 2001, 2002, 2003]: return "TDP (Andhra Pradesh)"
            if y in [2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013]: return "INC (Andhra Pradesh)"
        if 2014 <= y <= 2023: return "BRS (TRS)"
        if y == 2024: return "INC"
        
    if "tripura" in s:
        if y == 2006: return "CPI(M)"
        if y == 2024: return "BJP"
        
    if "uttar pradesh" in s:
        if y == 1996: return "President's Rule"
        if y == 1997: return "BSP / BJP"
        if y in [2003, 2004, 2005, 2006]: return "SP"
        if y in [2007, 2008, 2009, 2010, 2011]: return "BSP"
        if 2012 <= y <= 2016: return "SP"
        if y >= 2017: return "BJP"
        
    if "uttarakhand" in s:
        if y == 1995: return "SP / President's Rule (Uttar Pradesh)"
        if y in [2002, 2003, 2004, 2005, 2006]: return "INC"
        if y in [2007, 2008, 2009, 2010, 2011]: return "BJP"
        if y in [2012, 2013, 2014, 2015, 2016]: return "INC"
        if y >= 2017: return "BJP"
        
    if "bengal" in s:
        if y in [2008, 2010, 2011]: return "CPI(M) (Left Front)"
        if y >= 2012: return "AITC (Trinamool Congress)"
        if y == 2011: return "AITC (Trinamool Congress)" # May 2011 onwards

    return "Unknown"

def main():
    input_file = 'data/private_colleges_ownership.json'
    output_file = 'data/private_colleges_ownership.json'
    
    with open(input_file, 'r') as f:
        colleges = json.load(f)
        
    for college in colleges:
        year_str = college.get("YearEstablished")
        if year_str:
            try:
                y = int(year_str)
                college["CenterRulingPartyAtEstablishment"] = center_timeline.get(y, "Unknown")
                college["StateRulingPartyAtEstablishment"] = get_state_party(college.get("State", ""), y)
            except ValueError:
                college["CenterRulingPartyAtEstablishment"] = "Unknown"
                college["StateRulingPartyAtEstablishment"] = "Unknown"
        else:
            college["CenterRulingPartyAtEstablishment"] = "Unknown"
            college["StateRulingPartyAtEstablishment"] = "Unknown"
            
    with open(output_file, 'w') as f:
        json.dump(colleges, f, indent=2)
        
    print(f"Successfully enriched {len(colleges)} records with ruling party fields.")

if __name__ == '__main__':
    main()
