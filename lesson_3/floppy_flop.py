#!/usr/bin/python -tt
"""Floppy Flop
Program that tries to help the grandmother of the people from ITC.
Given the backup, it takes all the customers saved there and fill the table with the missing information.
"""
import os.path
import sys
import csv
from geopy.geocoders import Nominatim
import pycountry

NUMBER_OF_ARGS = 2
FILE_NAME = 1
LOCATION_INFORMATION = ["Address", "City", "Country", "Latitude", "Longitude", "State", "Zip Code"]


class CountryTranslator:
    @staticmethod
    def iso_code_by_name(country_name):
        country = pycountry.countries.get(name=country_name)
        return country.alpha_2


class Geocoder:
    """Adapter for handling geolocation searches."""

    def __init__(self):
        """Initializes the adapter with the true geocoder module."""
        self.geocoder = Nominatim(user_agent="Floppy Flop")

    def find_location(self, customer):
        """Given a customer, it gets the location from the coordinates or from the full address."""
        if customer["Latitude"] and customer["Longitude"]:
            return self.location_by_coordinates(customer["Latitude"], customer["Longitude"])
        else:
            address_query = self.address_query(customer)
            location = self.geocoder.geocode(address_query).raw
            if self.information_still_missing(location):
                return self.location_by_coordinates(location['lat'], location['lon'])
        return location

    def location_by_coordinates(self, latitude, longitude):
        """Given the coordinates, use geocoder to retrieve the location information"""
        return self.geocoder.reverse(f'{latitude}, {longitude}').raw

    def address_query(self, customer):
        """
        Given a customer, takes only the location info of his/her, builds the query dict that Geopy needs,
        and returns it.
        """
        address_query = {key.lower().replace(" ", ""): value for key, value in customer.items() if
                         value and key in LOCATION_INFORMATION}
        country_name = address_query.get('country')
        return {**address_query, 'country': CountryTranslator.iso_code_by_name(country_name)}

    def information_still_missing(self, location):
        """Given the location information retrieved until the moment, checks if still miss information."""
        return 'address' not in location


    def full_address(self, address_info):
        """Given the address info, takes all but the city, postcode, state and country, and returns the full address."""
        avoidable_fields = ['city', 'state', 'country', 'country_code', 'post_code']
        return ', '.join([value for key, value in address_info.items() if key not in avoidable_fields and value])


def recover_missing_information(filename):
    """
    Given a filename, opens the file, read each customer row,
    and tries to fill the missing information of each one.
    """
    updated_filename = os.path.join(os.path.dirname(filename), 'updated_' + os.path.basename(filename))

    for i, customer in enumerate(get_rows(filename)):
        if i == 0:
            csv_file = open(updated_filename, mode='w')
            writer = csv.DictWriter(csv_file, fieldnames=customer.keys())
            writer.writeheader()

        updated_customer = filled_customer(customer)
        writer.writerow(updated_customer)

    csv_file.close()


def filled_customer(customer):
    """Given a customer, checks what information is missing, fills those fields, and returns the updated customer."""
    geocoder = Geocoder()
    location = geocoder.find_location(customer)
    address_info = location['address']
    return {**customer, 'Country': address_info.get('country'), 'State': address_info.get('state'),
            'Zip Code': address_info.get('postcode'), 'City': address_info.get('city'),
            'Address': geocoder.full_address(address_info), "Latitude": location.get('lat'), "Longitude": location.get('lon')}


def get_rows(filename):
    """Given a csv filename, tries to read all the rows, appends them to a list and returns a list of dicts."""
    try:
        csv_file = open(filename, encoding='latin1')
        csv_reader = csv.DictReader(csv_file)
        customers = [customer for customer in csv_reader]
        csv_file.close()
        return customers
    except FileNotFoundError as e:
        print(f"The provided filename '{filename}' doesn't exist", e)
        sys.exit(1)


def main():
    """ Provided main(), calls recover_missing_information(). """
    if len(sys.argv) != NUMBER_OF_ARGS:
        print("usage: ./floppy_flop.py file-to-read")
        sys.exit(1)

    recover_missing_information(sys.argv[FILE_NAME])


if __name__ == "__main__":
    main()
