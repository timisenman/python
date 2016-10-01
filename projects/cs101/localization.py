#!/usr/local/bin/python
import os
import sys
import json
import gspread
import traceback
from oauth2client.client import SignedJwtAssertionCredentials

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def printc(color, string):
	print color + string + ENDC

def main():
	options = {}
	args = []

	for arg in sys.argv:
		if arg[0] == '-':
			options[arg] = True
		else:
			args.append(arg)

	argc = len(args)

	if argc <= 1:
		printc(OKGREEN, '\nLocalization Spreadsheet import/export tool')
		printc(HEADER,
'''
Usage: ./localization.py command [args] [options]
	You can also provide the --help option to a specific command to get help for it.
	Please note that export will overwrite the current contents of the worksheet
	and if the new data is smaller than the existing data, it will only partially overwrite it.
Commands:
	import spreadsheet_name strings_path [opts]\timports data from a google spreadsheet.
	export spreadsheet_name strings_path [opts]\texports data from a collection of .json files to a google spreadsheet.
''')
	else:
		command = args[1]

		if command == 'import':
			importFrom(argc, args, options)
		elif command == 'export':
			exportTo(argc, args, options)
		else:
			printc(WARNING, 'Warning: invalid command `' + command +'` - doing nothing.')

###########################################################################################################
# Utils
###########################################################################################################

def append(table, key, value):
	if not key in table:
			table[key] = value
	else:
		existing = table[key]
		if isinstance(existing, list):
			existing.append(value)
		else:
			table[key] = [existing, value]


def parseTable(data):
	output = {}
	row = 1
	propertyCount = 1

	if len(data) < 1 or len(data[0]) < 1:
		return output

	for col in range(1,len(data[0])):
		languageCode = data[0][col]
		if languageCode:
			output[languageCode] = {}
			propertyCount += 1
		else:
			break

	for row in range(1,len(data)):
		tag = data[row][0]

		if tag:
			for col in range(1,propertyCount):
				languageCode = data[0][col]
				entry = unicode(data[row][col])
				if not tag in output[languageCode]:
					output[languageCode][tag] = entry
				else:
					printc(FAIL, 'Import failed, duplicate key in spreadsheet: ' + tag)
					raise Exception('Import failed, duplicate key in spreadsheet: ' + tag)
		else:
			break

	return output

def makeDirAsNeeded(filename):
	if not os.path.exists(os.path.dirname(filename)):
	    try:
	        os.makedirs(os.path.dirname(filename))
	    except OSError as exc: # Guard against race condition
	        if exc.errno != errno.EEXIST:
	            raise

def getScriptPath():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

def loginToGSpread(isVerbose):
	try:
		scope = ['https://spreadsheets.google.com/feeds']
		path = os.path.join(getScriptPath(), 'credentials.json')
		json_key = json.load(open(path))
		credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
		gc = gspread.authorize(credentials)
	except Exception as err:
		printc(FAIL, 'Error: Invalid credentials, make sure a valid credentials.json exists in the same directory as this script.')
		traceback.print_exc()
		sys.exit()

	if isVerbose:
		printc(OKGREEN, 'Authenticated as ' + json_key['client_email'] );

	return gc

def openSpreadsheet(gc,sheetName):
	try:
		spreadsheet = gc.open(sheetName)
		return spreadsheet
	except gspread.exceptions.SpreadsheetNotFound as err:
		printc(FAIL, 'Error: spreadsheet not found, make sure the spreadsheet is shared with the account whose credentials you are using.\nProbably "weeby-1288@appspot.gserviceaccount.com"')
		sys.exit()


def unique(seq):
   set = {}
   map(set.__setitem__, seq, [])
   return set.keys()

def checkArguments(argc,errorMessages):
	i = 3
	for message in errorMessages:
		if argc < i:
			printc(FAIL, message);
			sys.exit()
		i += 1

def checkPath(path):
	if not os.path.exists(os.path.dirname(path)):
		printc(FAIL, 'ERROR: path does not exist: ' + path)
		sys.exit()

###########################################################################################################
# Commands
###########################################################################################################

def importFrom(argc, args, options):
	if '-h' in options or '--help' in options:
		printc(OKGREEN, 'Help for import')
		printc(HEADER,
'''
Usage: ./localization.py import spreadsheet_name strings_path [options]
	spreadsheet_name is the name of the spreadsheet in google docs.
	strings_path is the export path.
Options:
	-v --verbose\tprint more information.
	-h --help\tshow this meassage.
''')
		return

	checkArguments(argc,[
		'ERROR: please specify a spreadsheet name.',
		'ERROR: please specify a strings path.'
	])

	sheetName = args[2]
	stringsPath = args[3]
	isVerbose = '-v' in options or '--verbose' in options

	printc(OKGREEN, '\nImporting from: ' + sheetName)
	if isVerbose:
		printc(OKGREEN, 'Export path: ' + stringsPath)

	gc = loginToGSpread(isVerbose)
	spreadsheet = openSpreadsheet(gc,sheetName)
	worksheet = spreadsheet.get_worksheet(0)

	categories = {}
	languageData = {}

	data = worksheet.get_all_values()
	output = parseTable(data)

	if len(output) < 1:
		printc(WARNING, 'Warning: worksheet 0 was empty, or was parsed incorrectly.')

	for languageCode in output:
		if not languageCode in languageData:
			languageData[languageCode] = {}

		for key in output[languageCode]:
			pair = key.split('.',1)

			if len(pair) > 1:
				category = pair[0]
				tag = pair[1]
			else:
				tag = pair[0]
				category = 'default'
				printc(WARNING, 'Warning: loading a tag into the default categort `default`')

			if not category in languageData[languageCode]:
				languageData[languageCode][category] = {}
			languageData[languageCode][category][tag] = output[languageCode][key]

	for languageCode in languageData:
		outputData = json.dumps(languageData[languageCode], indent=2)
		filename = os.path.join(stringsPath, languageCode+'.json')
		makeDirAsNeeded(filename)
		outputFile = open(filename, 'w')
		outputFile.write(outputData)
		outputFile.close()

		missingCount = 0
		missingTags = []

		for category in languageData[languageCode]:
			for entry in languageData[languageCode][category]:
				if not languageData[languageCode][category][entry]:
					missingTags.append(entry)
					missingCount += 1

		if isVerbose:
			if missingCount > 0:
				printc(WARNING, languageCode + ': total: ' + str(len(languageData[languageCode])) + ', missing: ' + str(missingCount))
				printc(WARNING, 'missing tags:' + str(missingTags))
				print ''
			else:
				printc(OKGREEN, languageCode + ': total: ' + str(len(languageData[languageCode])) )

	printc(OKGREEN, 'Import Complete')


def exportTo(argc, args, options):
	if '-h' in options or '--help' in options:
		printc(OKGREEN, 'Help for export')
		printc(HEADER,
'''
Usage: ./localization.py export spreadsheet_name strings_path  [options]
	spreadsheet_name is the name of the spreadsheet in google docs.
	strings_path is the path to a folder full of .json localization strings.
Options:
	-v --verbose\tprint more information.
	-h --help\tshow this meassage.
''')
		return

	checkArguments(argc,[
		'ERROR: please specify a spreadsheet name.',
		'ERROR: please specify a strings path.'
	])

	sheetName = args[2]
	stringsPath = args[3]
	isVerbose = '-v' in options or '--verbose' in options

	checkPath(stringsPath)

	languageData = {}
	languageCodes = []
	categories = []

	for filename in os.listdir(stringsPath):
		if filename.endswith('.json'):
			languageCode = filename[:-5]

			try:
				data = json.load(open( os.path.join(stringsPath, filename)) )
			except Exception as err:
				printc(WARNING,'Warning: failed to load: ' + filename)
				continue;

			for category in data:
				categories.append(category)

			languageCodes.append(languageCode)
			append(languageData,languageCode,data)

	if len(languageData) <= 0:
		printc(WARNING, 'Warning: no data to export.')
		return

	languageCodes.sort()
	languageCodes.insert(0,'tag')

	categories = unique(categories)
	categories.sort()

	exportData = [languageCodes]

	letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'; #TODO: Only supports 25 languages ... fix this if you need more.

	printc(OKGREEN, '\nExporting to: ' + sheetName)

	if isVerbose:
		printc(OKGREEN, 'From directory: ' + stringsPath)

	gc = loginToGSpread(isVerbose)
	spreadsheet = openSpreadsheet(gc,sheetName)
	worksheet = spreadsheet.get_worksheet(0)

	for category in categories:

		tags = []

		for languageCode in languageData:
			if category in languageData[languageCode]:
				for tag in languageData[languageCode][category]:
					tags.append(tag)

		tags = unique(tags)
		tags.sort()

		missingCount = 0

		for tag in tags:
			row = [category + '.' + tag]
			for codeIndex in range(1,len(languageCodes)):
				languageCode = languageCodes[codeIndex]
				if category in languageData[languageCode] and tag in languageData[languageCode][category]:
					row.append(languageData[languageCode][category][tag])
				else:
					row.append('')
					missingCount += 1
			exportData.append(row)


	rowCount = len(exportData)
	colCount = len(exportData[0]) - 1

	alphanum = 'A1:' + letters[colCount] + str(rowCount);

	worksheet.resize(rowCount,colCount+1)
	data = worksheet.range(alphanum)

	for cell in data:
		row = cell.row - 1
		col = cell.col - 1
		cell.value = exportData[row][col]

	if isVerbose:
		printc(OKGREEN, 'Exporting languages: ' + str(languageCodes[1:]) )
		printc(OKGREEN, 'Exporting ' + str(len(tags)) + ' tags')
		if missingCount > 0:
			printc(WARNING, str(missingCount) + ' missing translation(s) were detected')
		printc(OKGREEN, 'Exporting in range: ' + alphanum)

	worksheet.update_cells(data)

	printc(OKGREEN, 'Export Complete')

main();