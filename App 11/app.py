import pandas as pd
from pdf_code import print_receipt

df = pd.read_csv("articles.csv", dtype={"id": str})

class Article():
    def __init__(self, article_id):
        self.id = article_id
        self.name = df.loc[df["id"] == article_id, 'name'].values[0]
        self.price = df.loc[df["id"] == article_id, 'price'].values[0]


    def available(self):
        number = df[df["id"] == self.id]['in stock'].values[0]
        if number > 0:
            return True
        else:
            return False


class Receipt():
    def __init__(self, article_object):
        self.article = article_object

    def print(self):
        print_receipt(article.id, article.name, article.price)

print(df)
article_id = input("Enter an article ID: ")
article = Article(article_id)
if article.available():
    receipt = Receipt(article_object=article)
    receipt.print()
    in_stock = df.loc[df["id"] == article_id]['in stock'].values[0]
    new_stock = in_stock -1
    df.loc[df["id"] == article_id, 'in stock'] = new_stock
    df.to_csv("articles.csv", index=False)  # Save the updated DataFrame back to the CSV file

else:
    print("The article is not available.")