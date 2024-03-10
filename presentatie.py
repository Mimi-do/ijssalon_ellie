from helper import onderstreep

def presenteer(mijn_dict, totaal):
    for k,v in mijn_dict.items():
        print(f"{k} : {v}")
    print("=========================")
    print(f"totaal : {totaal}")
