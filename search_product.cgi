#!/usr/local/bin/python3
import jinja2
import cgi
import mysql.connector
import cgitb
import json


def main():
    # cgitb.enable(display=1, logdir="/logs", context=5, format="html")
    connectionToDatabase = ""
    form = cgi.FieldStorage()
    # searchTerm = form['search_term'].value
    searchTerm = "gene"
    uniqueNameResults = []
    valueResults = []
    # This line tells the template loader where to search for template files
    # templateLoader = jinja2.FileSystemLoader(searchpath="./templates")

    try:
        conn = mysql.connector.connect(
            user='mmorro14', password='DT2112', host='localhost', database='mmorro14_chado')
        curs = conn.cursor()

    except:
        connectionToDatabase = "Connection and Query Failed"
        print("Content-Type: text/html\n\n")
        print(connectionToDatabase)
        # WHERE THE RETURN/GOES NEEDS TO BE

    try:
        submit = form['submit'].value

        try:
            select_stmt = "SELECT f.uniquename, product.value FROM feature f JOIN featureprop product ON f.feature_id=product.feature_id JOIN cvterm productprop ON product.type_id=productprop.cvterm_id WHERE productprop.name = %(product_name)s AND product.value LIKE %(product_value)s "
            curs.execute(select_stmt, {
                'product_name': 'gene_product_name', 'product_value': '%' + searchTerm + '%'})

            for uniquename, value in curs:
                uniqueNameResults.append(bytearray.decode(uniquename))
                valueResults.append(bytearray.decode(value))

            connectionToDatabase = "Connection and Query Succeded"
            searchZip = zip(uniqueNameResults, valueResults)

            # if not uniqueNameResults:
            #     env = jinja2.Environment(loader=templateLoader)
            #     template = env.get_template('results_failed.html')
            #     print("Content-Type: text/html\n\n")
            #     print(template.render(placeholder=searchTerm))
            # else:
            #     env = jinja2.Environment(loader=templateLoader)
            #     template = env.get_template('results.html')
            #     print("Content-Type: text/html\n\n")
            #     print(template.render(placeholder=searchTerm,
            #                           number=len(uniqueNameResults), results=searchZip))

            if not uniqueNameResults:
                print("Content-Type: text/html\n\n")
                print(connectionToDatabase)
                # WHERE THE RETURN/GOES NEEDS TO BE

            else:
                return json.dumps(searchZip[:5])

        except:
            connectionToDatabase = "Connection Succeded but Query Failed"
            print("Content-Type: text/html\n\n")
            print(connectionToDatabase)
            # WHERE THE RETURN/GOES NEEDS TO BE
    except KeyError:
        try:
            select_stmt = "SELECT f.uniquename, product.value FROM feature f JOIN featureprop product ON f.feature_id=product.feature_id JOIN cvterm productprop ON product.type_id=productprop.cvterm_id WHERE productprop.name = %(product_name)s AND product.value LIKE %(product_value)s LIMIT 5"
            curs.execute(select_stmt, {
                'product_name': 'gene_product_name', 'product_value': '%' + searchTerm + '%'})

            for _, value in curs:
                valueResult = bytearray.decode(value)
                valueResults.append(
                    {'value': valueResult, 'label': valueResult})

            connectionToDatabase = "Connection and Query Succeded"

            # if not uniqueNameResults:
            #     env = jinja2.Environment(loader=templateLoader)
            #     template = env.get_template('results_failed.html')
            #     print("Content-Type: text/html\n\n")
            #     print(template.render(placeholder=searchTerm))
            # else:
            #     env = jinja2.Environment(loader=templateLoader)
            #     template = env.get_template('results.html')
            #     print("Content-Type: text/html\n\n")
            #     print(template.render(placeholder=searchTerm,
            #                           number=len(uniqueNameResults), results=searchZip))

            if not valueResults:
                print("Content-Type: text/html\n\n")
                print(connectionToDatabase)
                # WHERE THE RETURN/GOES NEEDS TO BE

            else:
                return json.dumps(valueResults)

    except:
        connectionToDatabase = "Connection Succeded but Query Failed"
        print("Content-Type: text/html\n\n")
        print(connectionToDatabase)
        # WHERE THE RETURN/GOES NEEDS TO BE

    curs.close()
    conn.close()


if __name__ == '__main__':
    main()
