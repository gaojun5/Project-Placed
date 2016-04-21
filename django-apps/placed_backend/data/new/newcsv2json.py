# csv2json.py
#
# Copyright 2009 Brian Gershon -- briang at webcollective.coop
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import getopt
import csv
from os.path import dirname
import simplejson
import argparse

class InputConverter(object):

    def __init__(self):
        self.impl_map = {
            'short' : int,
            'int' : int,
            'integer' : int,
            'long' : long,
            'float' : float,
            'double' : float,
            'string' : self.convert_string,
            'timestamp' : long,
            'array' : self.convert_array,
            'bool':bool,
            }

    def get_impl(self, name):
        impl = self.impl_map.get(name)
        if not impl:
            raise NotSupportedError('"{}" is not a supported type'.format(name))
        return impl

    def convert_string(self, value):
        return value.decode('utf-8')

    def convert_array(self, value):
        """return self.dequote(self.convert_string(value).split(u','))"""
        #return self.convert_string(value).split(u',')
        return map(int, self.convert_string(value).split(u','))

    def dequote(self,s):
        """
        If a string has single or double quotes around it, remove them.
        Make sure the pair of quotes match.
        If a matching pair of quotes is not found, return the string unchanged.
        """
        if (s[0] == s[-1]) and s.startswith(("'", '"')):
            return s[1:-1]
        return s

parser = argparse.ArgumentParser(description='Convert csv to JSON')
parser.add_argument('--infile', nargs='?',
                    help='path to csv file')
parser.add_argument('--model_name', nargs='?',
                    help='model name')
parser.add_argument('--columns', nargs='*',
                    help="""column definition formatted as col_name:col_type [...]
                    column types are: short, int, integer, long, float, double, string, timestamp, array""")

args = parser.parse_args()
columns = args.columns
model_name = args.model_name
input_file_name = args.infile

#print "Converting From %s " % input_file_name
#print "Converting to model %s" % model_name

try:
    #script, input_file_name, model_name = sys.argv
    input_file_name, model_name, columns
except ValueError:
    print "\nRun via:\n\n%s input_file_name model_name" % sys.argv[0]
    print "\ne.g. %s airport.csv app_airport.Airport" % sys.argv[0]
    print "\nNote: input_file_name should be a path relative to where this script is."
    sys.exit()

in_file = dirname(__file__) + input_file_name
out_file = dirname(__file__) + input_file_name + ".json"

converter = InputConverter()
cols = [col.split(':') for col in columns]
function_seq = [(c[0], converter.get_impl(c[1])) for c in cols]

print "Converting %s from CSV to JSON as %s" % (in_file, out_file)

f = open(in_file, 'r' )
fo = open(out_file, 'w')

#reader = csv.reader( f )
reader = csv.reader( f)

header_row = []
entries = []

# debugging
# if model_name == 'app_airport.Airport':
#     import pdb ; pdb.set_trace( )

for row in reader:
    if not header_row:
        header_row = row
        continue

    pk = row[0]
    model = model_name
    fields = {}
    for i in range(len(row)-1):
        active_field = row[i+1]
        print "active_field %s" % active_field
        # convert numeric strings into actual numbers by converting to either int or float
        if active_field.isdigit():
            try:
                new_number = int(active_field)
            except ValueError:
                new_number = float(active_field)
            fields[header_row[i+1]] = new_number
        else:
            #fields[header_row[i+1]] = active_field.strip()

            #if active_field == '\\N':
            if active_field == '':
            #if active_field is None:
                print "cols[i+1][1]%s" % cols[i+1][1]
                if cols[i+1][1] == 'array':
                    fields[header_row[i+1]] = []
                else:
                    #if cols[i+1][1] == 'string':
                    #    fields[header_row[i+1]] = ''
                    #else:
                        if cols[i+1][1] == 'integer' or cols[i+1][1] == 'int':
                            fields[header_row[i+1]] = 0
                        else:
                            if cols[i+1][1] == 'bool':
                                fields[header_row[i+1]] = False
                            else:
                                fields[header_row[i+1]] = None # NULL -> None
            else:
                print "header_row[i] %s" % header_row[i]
                print "function_seq[i+1][0] %s" % function_seq[i+1][0]
                print "function_seq[i+1][1] %s" % function_seq[i+1][1]
                print "function_seq[i+1][1](active_field) %s" % function_seq[i+1][1](active_field)
                fields[header_row[i+1]] = function_seq[i+1][1](active_field)

    row_dict = {}
    print "pk=%s" % pk
    row_dict["pk"] = int(pk)
    row_dict["model"] = model_name

    row_dict["fields"] = fields
    entries.append(row_dict)

fo.write("%s" % simplejson.dumps(entries, indent=4))

f.close()
fo.close()
