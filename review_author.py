import sys

def check_alphabetical_ordering(author_file):
    last_author_key = None
    ordering_error_found = False
    for line_no, line in enumerate(author_file):
        if not line.strip().startswith("%") and not line.strip().startswith("@comment") and line.strip():  # ignore comments and empty lines
            line = line.strip()
            # print(line)
            # get the author key
            author_key = line.split("=")[0].split("{")[1].strip()
            # print(author_key)
            if last_author_key and last_author_key.lower() > author_key.lower():
                # print(f"Ordering error between {last_author_key} and {author_key}")
                print(f"::error file=author.bib,line={line_no}::Ordering error between {last_author_key} and {author_key}")
                ordering_error_found = True
            last_author_key = author_key
    return ordering_error_found


def review_author_file():
    with open("author.bib", "r") as author_file:
        ordering_error = check_alphabetical_ordering(author_file)
    return ordering_error

if __name__ == "__main__":
    found_error = review_author_file()
    if found_error:
        sys.exit(1)
        # print("::error file=author.bib::message=There was an error") 

