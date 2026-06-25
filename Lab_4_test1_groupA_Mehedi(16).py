class Books():

    def __init__(self, Book_ID, Book_Title, Author_Name, Number_of_Available_Copies,Year_of_Publication):
        self.Book_ID = Book_ID
        self.Book_Title = Book_Title
        self.Author_Name = Author_Name
        self.Number_of_Available_Copies = Number_of_Available_Copies
    
catalog = [
    {"id": 1245, "title": "Artificial Intelligence", "author": "Sophia White", "copies": 3, "year": 2021},
    {"id": 1001, "title": "Python Basics", "author": "John Smith", "copies": 4, "year": 2018},
    {"id": 1450, "title": "Cyber Security", "author": "Daniel Clark", "copies": 2, "year": 2022},
    {"id": 1078, "title": "Algorithms Made Easy", "author": "David Lee", "copies": 0, "year": 2019},
    {"id": 1525, "title": "Cloud Computing", "author": "Olivia Martin", "copies": 4, "year": 2023},
    {"id": 1120, "title": "Database Systems", "author": "Maria Green", "copies": 5, "year": 2017},
    {"id": 1300, "title": "Machine Learning", "author": "James Wilson", "copies": 0, "year": 2020},
    {"id": 1035, "title": "Data Structures", "author": "Alice Brown", "copies": 2, "year": 2016},
    {"id": 1375, "title": "Operating Systems", "author": "Emma Davis", "copies": 6, "year": 2015},
    {"id": 1189, "title": "Computer Networks", "author": "Robert King", "copies": 1, "year": 2014}
]




user_input={}
while user_input!="no":
    print("Choose Sorting Option:\n1.Sort by Book ID\n2.Sort by Year of Publication\n3.Sort by Availabe Copies\n" )
    user_input=input("Enter your option:")
    if user_input=="1":
        print("Sorting Catalog by Books ID:")
        print()
        Number_of_Comparison=0
        Number_of_Swaps=0
        for i in range(10):
            for j in range(10-i-1):
                Number_of_Comparison+=1
                if catalog[j]["id"]>catalog[j+1]["id"]:
                    catalog[j]["id"],catalog[j+1]["id"]=catalog[j+1]["id"],catalog[j]["id"]
                    Number_of_Swaps+=1
                    
            books = catalog[i]
            print(f"Book ID:{books['id']}")
            print(f"Book Title:{books['title']}")
            print(f"Author Name:{books['author']}")
            print(f"Number of Available Copies:{books['copies']}")
            print(f"Year of Publication:{books['year']}")
            print()
            print()
            print(".....")
        print("Number of Comparison",Number_of_Comparison)
        print("Number of Swaps",Number_of_Swaps)


    elif user_input=="2":
        print("Sorting Catalog by Years of Publication:")
        print()
        Number_of_Comparison=0
        Number_of_Swaps=0
        for i in range (9):
            min_index=i
            for j in range(i+1,n=9):
                if catalog[j]["year"]<catalog[min_index]["year"]:
                    min_index=j
            catalog[j]["year"],catalog[min_index]["year"]=catalog[min_index]["year"],catalog[j]["year"]
        # for i in range(10):
        #     for j in range(10-i-1):
        #         Number_of_Comparison+=1
        #         if catalog[j]["year"]>catalog[j+1]["year"]:
        #             catalog[j]["year"],catalog[j+1]["year"]=catalog[j+1]["year"],catalog[j]["year"]
        #             Number_of_Swaps+=1
                    
            books = catalog[i]
            print(f"Book ID:{books['id']}")
            print(f"Book Title:{books['title']}")
            print(f"Author Name:{books['author']}")
            print(f"Number of Available Copies:{books['copies']}")
            print(f"Year of Publication:{books['year']}")
            print()
            print()
            print(".....")
        print("Number of Comparison",Number_of_Comparison)
        print("Number of Swaps",Number_of_Swaps)

    else:
        print("Sorting Catalog by Available Copies:")
        print()
        Number_of_Comparison=0
        Number_of_Swaps=0
        for i in range(10):
            for j in range(10-i-1):
                Number_of_Comparison+=1
                if catalog[j]["copies"]>catalog[j+1]["copies"]:
                    catalog[j]["copies"],catalog[j+1]["copies"]=catalog[j+1]["copies"],catalog[j]["copies"]
                    Number_of_Swaps+=1
                    
            books = catalog[i]
            print(f"Book ID:{books['id']}")
            print(f"Book Title:{books['title']}")
            print(f"Author Name:{books['author']}")
            print(f"Number of Available Copies:{books['copies']}")
            print(f"Year of Publication:{books['year']}")
            print()
            print()
            print(".....")
        print("Number of Comparison",Number_of_Comparison)
        print("Number of Swaps",Number_of_Swaps)