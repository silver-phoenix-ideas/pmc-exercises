import webbrowser

user_query = input("Enter search query: ")
formatted_query = user_query.replace(" ", "+")

webbrowser.open("https://google.com/search?q=" + formatted_query)
