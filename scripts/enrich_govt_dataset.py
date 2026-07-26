import csv
import json

from enrich_dataset import center_timeline, get_state_party


def main():
    with open('data/nmc_mbbs_colleges.csv', 'r') as f:
        csv_rows = {row['SlNo']: row for row in csv.DictReader(f)}

    with open('data/sources_and_funding.json', 'r') as f:
        colleges = json.load(f)

    for college in colleges:
        row = csv_rows.get(str(college['SlNo']))
        year_str = row.get('YearOfInception') if row else None
        college['YearOfInception'] = year_str
        college['AnnualIntake'] = row.get('AnnualIntake') if row else None
        try:
            y = int(year_str)
            college['CenterRulingPartyAtEstablishment'] = center_timeline.get(y, 'Unknown')
            college['StateRulingPartyAtEstablishment'] = get_state_party(row.get('State', ''), y)
        except (TypeError, ValueError):
            college['CenterRulingPartyAtEstablishment'] = 'Unknown'
            college['StateRulingPartyAtEstablishment'] = 'Unknown'

    with open('data/sources_and_funding.json', 'w') as f:
        json.dump(colleges, f, indent=2)

    print(f"Successfully enriched {len(colleges)} government college records with ruling party fields.")


if __name__ == '__main__':
    main()
