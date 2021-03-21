#!/usr/local/bin/python3
import cgi
import mysql.connector
import git
import json


def main():

    connectionToDatabase = ""
    cgitb.enable()
    form = cgi.FieldStorage()
    searchTerm = form['searchTerm'].value
    uniqueNameResults = []
    valueResults = []

    # This line tells the template loader where to search for template files
    # templateLoader = jinja2.FileSystemLoader(searchpath="./templates")

    try:
        conn = mysql.connector.connect(
            user='mmorro14', password='DT2112', host='localhost', database='mmorro14_chado')
        curs = conn.cursor()

        try:
            select_stmt = "SELECT f.uniquename, product.value FROM feature f JOIN featureprop product ON f.feature_id=product.feature_id JOIN cvterm productprop ON product.type_id=productprop.cvterm_id WHERE productprop.name = %(product_name)s AND product.value LIKE %(product_value)s "
            curs.execute(select_stmt, {
                         'product_name': 'gene_product_name', 'product_value': '%' + searchTerm + '%'})

            for uniquename, value in curs:
                uniqueNameResults.append(bytearray.decode(uniquename))
                valueResults.append(bytearray.decode(value))

            connectionToDatabase = "Connection and Query Succeded"
            searchZip = zip(uniqueNameResults, valueResults)

            if not uniqueNameResults:

                print("Content-Type: text/html\n\n")
                print(template.render(placeholder=searchTerm))
            else:

                print("Content-Type: text/html\n\n")
                print(template.render(placeholder=searchTerm,
                                      number=len(uniqueNameResults), results=searchZip))

        except:
            connectionToDatabase = "Connection Succeded but Query Failed"

            print("Content-Type: text/html\n\n")
            print(template.render(placeholder=connectionToDatabase))

        curs.close()
        conn.close()

    except:
        connectionToDatabase = "Connection and Query Failed"

        print("Content-Type: text/html\n\n")
        print(template.render(placeholder=connectionToDatabase))


if __name__ == '__main__':
    main()
