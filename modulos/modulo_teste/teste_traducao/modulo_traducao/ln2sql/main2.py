from thesaurus import Thesaurus

def main():
    t = Thesaurus()
    t.load("thesaurus_store/th_english.dat")
    t.add_synonym_to_a_word("company","business")
    print (t.get_synonyms_of_a_word("company"))
    t.print_me()

if __name__ == '__main__':
    main()