def first_function():
    print("Keep it logically awesome.")

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    print(quotes)

if __name__== "__main__":
  first_function()
