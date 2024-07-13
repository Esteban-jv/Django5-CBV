from django.shortcuts import render
from django.views.generic import ListView
import csv

# Create your views here.
def csv_read(request):
    filename="documents\Libro1.csv"
    try:
        with open(filename) as file:
            csv_reader = csv.reader(file, delimiter=";")
            response = render(request, 'csv.html', {'objects': csv_reader})
        # file.close()
            return response
    except (IOError) as error:
        print("Error {}".format(error))

def csv_read_dic(request):
    filename="documents\Libro1.csv"
    try:
        file = open(filename)
        csv_reader = csv.DictReader(file, delimiter=";")
        response = render(request, 'csv.html', {'objects': csv_reader})
        file.close()
        return response
    except (IOError) as error:
        print("Error {}".format(error))

def csv_write(request):
    filename="documents\Libro2.csv"
    try:
        file = open(filename, 'w', newline='')
        csv_writer = csv.writer(file, delimiter=",")
        print(type(csv_writer))
        csv_writer.writerow(['Movie 1', 'Movie 2', 'Movie 3'])
        csv_writer.writerow(['Avengers', 'EndGame', 'Toy Story 3'])
        return render(request, 'csv.html', {'objects': []})
    except (IOError) as error:
        print("Error {}".format(error))

def csv_write_dic(request):
    filename="documents\Libro2.csv"
    try:
        file = open(filename, 'w', newline='')
        csv_writer = csv.DictWriter(file, delimiter=",", fieldnames=['name','surname'])
        print(type(csv_writer))
        csv_writer.writeheader()
        csv_writer.writerow({ 'name': 'Andres', 'surname': 'Cruz'})
        return render(request, 'csv.html', {'objects': []})
    except (IOError) as error:
        print("Error {}".format(error))