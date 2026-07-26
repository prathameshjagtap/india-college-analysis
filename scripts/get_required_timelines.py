import json

def main():
    with open('data/private_colleges_ownership.json', 'r') as f:
        data = json.load(f)
    
    required = set()
    for college in data:
        state = college.get('State')
        year = college.get('YearEstablished')
        if state and year:
            required.add((state, year))
    
    # group by state
    by_state = {}
    for state, year in required:
        by_state.setdefault(state, []).append(year)
        
    for state in sorted(by_state.keys()):
        years = sorted(list(set(by_state[state])))
        print(f"{state}: {years}")

if __name__ == '__main__':
    main()
