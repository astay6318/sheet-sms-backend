# code
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Response
from twilio.rest import Client
import os
from dotenv import load_dotenv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv()

sheet_id = os.environ.get("sheet_id")
api_key = os.environ.get("api_key")

# define the scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

@receiver(post_save,sender=Response) 
def create_profile( sender,instance, created, **kwargs):
	if created:
		account_sid = os.environ.get("twilio_account_sid")
		auth_token = os.environ.get("twilio_auth_token")
		client = Client(account_sid, auth_token)
		available_phone_number_country = client.available_phone_numbers('US').fetch()
		print(instance.user_id)
		print(instance.question.question_text)
		print(instance.answers)
		body={
			"user_id": instance.user_id,
			"question":instance.question.question_text,
			"answer":instance.answers
		}
		# Update the path to the JSON file
		json_file_path = 'sheets/abc.json'

		try:
			# Add exception handling for file-related errors
			creds = ServiceAccountCredentials.from_json_keyfile_name(json_file_path, scope)
			gspread_client = gspread.authorize(creds)
			# print("Akshat" * 100)
			# get the instance of the Spreadsheet
			sheet = gspread_client.open('commentary data')

			# get the first sheet of the Spreadsheet
			sheet_instance = sheet.get_worksheet(0)
			# print(sheet_instance/)
			# get the total number of columns
			sheet_instance.col_count
			## >> 26

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

