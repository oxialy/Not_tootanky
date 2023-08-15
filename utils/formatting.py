from pprint import pprint 

def pretty_print_note(notes: dict):
    out_dict = dict()
    for note, value in notes.items():
        out_dict[note] = value["value"]
    pprint(out_dict)
