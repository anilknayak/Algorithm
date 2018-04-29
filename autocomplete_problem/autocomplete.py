def extract(query):
    """Implement this method using the `query` API call, for example:
    query("abracadar") #=> ["abracadara"] using the default query method in main()
    """

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    all = []
    for letter in alphabet:
        fetch = query(letter)
        if len(fetch) == 5:
            for o in fetch:
                all.append(o)
            last = fetch[-1]
            last_fetch_2 = last[0:2]
            flag = True
            len_reached = 2
            while flag:
                temp_fetch = query(last_fetch_2)
                not_match_let = []
                for a in temp_fetch:
                    if not a in all:
                        not_match_let.append(a)

                if len(not_match_let) == 0:
                    flag = False
                else:
                    for o in not_match_let:
                        all.append(o)
                    len_reached = len_reached + 1
                    last_fetch_2 = not_match_let[-1][0:len_reached]
                not_match_let = []

        else:
            for o in fetch:
                all.append(o)

    return all

def main():
    """Runs your solution -- no need to update (except to maybe change the database)."""
    # Simple implementation of the autocomplete API
    database = ["abracadara", "al", "alice", "alicia", "allen", "alter", "altercation", "bob", "eve", "evening", "event", "eventually", "mallory"]
    # database = ["aa","ab","ac","ad","ae","aea", "aed", "aee","aeea","aeeb"]
    # print(" database length ", len(database))
    query = lambda prefix: [d for d in database if d.startswith(prefix)][:5]
    assert extract(query) == database

main()