#signals used to perform particular action on the modification/creation of a particular entry in the Database

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Response
from twilio.rest import Client
import os
from dotenv import load_dotenv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#load the env variables
load_dotenv()

sheet_id = os.environ.get("sheet_id")
api_key = os.environ.get("api_key")

# define the scope,i.e., the level of access the application is requesting. Here google sheetsdata and google drive data is required
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']


#Send the message and update to google sheets after a response has been saved
@receiver(post_save,sender=Response) 
def create_profile( sender,instance, created, **kwargs):
	if created:
		account_sid = os.environ.get("twilio_account_sid")
		auth_token = os.environ.get("twilio_auth_token")
		client = Client(account_sid, auth_token)

		#define the body of the message to be sent to the client (dictionary)
		body={
			"user_id": instance.user_id,
			"question":instance.question.question_text,
			"answer":instance.answers
		}

		# Update the path to the JSON file
		json_file_path = 'sheets/abc.json'
		#first update in the sheets
		try:
			# get the credentials of the service account using the oauth2client library and authorize the credentials
			creds = ServiceAccountCredentials.from_json_keyfile_name(json_file_path, scope)
			gspread_client = gspread.authorize(creds)

			# get the instance of the Spreadsheet with the sheet_id
			sheet = gspread_client.open_by_key(sheet_id)

			# get the first sheet of the Spreadsheet (assuming only 1 form)
			sheet_instance = sheet.get_worksheet(0)

			# Find the first empty row
			next_row = len(sheet_instance.get_all_values()) + 1

			# Add the question in the first column
			sheet_instance.update_cell(next_row, 1, body["question"])

			# Join the characters of the answer into a single string with no separator
			joined_answer = ''.join(body["answer"])

			# Add the joined answer in the second column
			sheet_instance.update_cell(next_row, 2, joined_answer)
		except Exception as e:
			print(f"Error loading credentials from {json_file_path}: {e}")
			return
		#send an sms to the client
		try:
			message = client.messages.create(
			from_='+19528563009',
			body=f"User ID: {body['user_id']}\nQuestion: {body['question']}\nAnswer: {body['answer']}",
			to='+917587236895'
			)
		except Exception as e:
			print(e)
			return
		print(message.sid)

